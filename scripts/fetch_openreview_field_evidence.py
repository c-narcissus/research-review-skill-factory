#!/usr/bin/env python3
"""Fetch public ICLR OpenReview evidence for field-specific review synthesis.

This script uses only the Python standard library. It queries OpenReview API v2
for recent ICLR submissions, filters them by a field query, and extracts public
review, meta-review, decision, and comment notes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API = "https://api2.openreview.net"


def get_json(path: str, params: dict[str, Any], retries: int = 3) -> dict[str, Any]:
    query = urllib.parse.urlencode(params, doseq=True)
    url = f"{API}{path}?{query}" if query else f"{API}{path}"
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "field-reviewer-skill/1.0"})
            with urllib.request.urlopen(req, timeout=45) as response:
                return json.load(response)
        except Exception as exc:  # noqa: BLE001 - preserve stdlib-only script.
            last_error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"OpenReview request failed after {retries} attempts: {url}\n{last_error}")


def value_of(item: Any) -> Any:
    if isinstance(item, dict) and "value" in item:
        return item["value"]
    return item


def flatten_content(content: dict[str, Any]) -> dict[str, Any]:
    return {key: value_of(value) for key, value in (content or {}).items()}


def text_blob(note: dict[str, Any]) -> str:
    content = flatten_content(note.get("content", {}))
    parts: list[str] = []
    for key in ["title", "abstract", "keywords", "primary_area", "venue", "decision"]:
        value = content.get(key)
        if isinstance(value, list):
            parts.extend(str(v) for v in value)
        elif value is not None:
            parts.append(str(value))
    return "\n".join(parts)


def tokens(text: str) -> set[str]:
    return {tok for tok in re.findall(r"[a-z0-9][a-z0-9_+-]{1,}", text.lower()) if len(tok) > 1}


def relevance_score(note: dict[str, Any], query_tokens: set[str]) -> int:
    blob_tokens = tokens(text_blob(note))
    return len(query_tokens & blob_tokens)


def get_venue_status_ids(year: int) -> dict[str, str]:
    venue_id = f"ICLR.cc/{year}/Conference"
    data = get_json("/groups", {"id": venue_id})
    groups = data.get("groups", [])
    if not groups:
        raise RuntimeError(f"Venue group not found: {venue_id}")
    content = flatten_content(groups[0].get("content", {}))
    status_ids = {"accepted": venue_id}
    mapping = {
        "under_review": "submission_venue_id",
        "rejected": "rejected_venue_id",
        "withdrawn": "withdrawn_venue_id",
        "desk_rejected": "desk_rejected_venue_id",
    }
    for status, key in mapping.items():
        value = content.get(key)
        if value:
            status_ids[status] = str(value)
    return status_ids


def fetch_submission_page(venueid: str, limit: int, offset: int, include_replies: bool) -> list[dict[str, Any]]:
    params: dict[str, Any] = {"content.venueid": venueid, "limit": limit, "offset": offset}
    if include_replies:
        params["details"] = "replies"
    data = get_json("/notes", params)
    return data.get("notes", [])


def fetch_replies_for_forum(forum: str) -> list[dict[str, Any]]:
    data = get_json("/notes", {"forum": forum})
    return data.get("notes", [])


def invitation_kind(note: dict[str, Any]) -> str:
    invitations = note.get("invitations", []) or []
    suffixes = [
        "Official_Review",
        "Meta_Review",
        "Decision",
        "Rebuttal",
        "Official_Comment",
        "Public_Comment",
        "Revision",
    ]
    for invitation in invitations:
        for suffix in suffixes:
            if str(invitation).endswith(suffix):
                return suffix
    return "Other"


def note_text_fields(note: dict[str, Any]) -> dict[str, str]:
    content = flatten_content(note.get("content", {}))
    fields: dict[str, str] = {}
    for key, value in content.items():
        if isinstance(value, (int, float, bool)):
            fields[key] = str(value)
        elif isinstance(value, list):
            fields[key] = "; ".join(str(v) for v in value)
        elif value is not None:
            fields[key] = str(value)
    return fields


def likely_author_response(note: dict[str, Any]) -> bool:
    text = "\n".join(note_text_fields(note).values()).lower()
    signatures = " ".join(str(s) for s in note.get("signatures", [])).lower()
    if "author" in signatures:
        return True
    author_markers = [
        "dear reviewer",
        "we thank the reviewer",
        "we thank reviewers",
        "we appreciate the reviewer",
        "our rebuttal",
        "our response",
        "we have updated",
        "we will revise",
        "the authors",
        "best regards",
    ]
    reviewer_markers = [
        "i appreciate the response",
        "thank you for the response",
        "my concerns",
        "i have raised",
        "i have lowered",
    ]
    return any(marker in text for marker in author_markers) and not any(marker in text for marker in reviewer_markers)


def compact_note(note: dict[str, Any]) -> dict[str, Any]:
    fields = note_text_fields(note)
    return {
        "id": note.get("id"),
        "forum": note.get("forum"),
        "replyto": note.get("replyto"),
        "kind": invitation_kind(note),
        "invitations": note.get("invitations", []),
        "signatures": note.get("signatures", []),
        "content": fields,
        "likely_author_response": likely_author_response(note),
    }


def collect_relevant_papers(
    field: str,
    years: list[int],
    per_status: int,
    max_scanned_per_status: int,
    page_size: int,
) -> tuple[list[dict[str, Any]], list[str]]:
    query_tokens = tokens(field)
    warnings: list[str] = []
    collected: list[dict[str, Any]] = []

    for year in years:
        try:
            status_ids = get_venue_status_ids(year)
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"{year}: could not load venue group: {exc}")
            continue

        for status in ["accepted", "rejected", "withdrawn", "desk_rejected"]:
            venueid = status_ids.get(status)
            if not venueid:
                continue
            matches: list[tuple[int, dict[str, Any]]] = []
            scanned = 0
            offset = 0
            while scanned < max_scanned_per_status and len(matches) < per_status:
                try:
                    notes = fetch_submission_page(venueid, min(page_size, max_scanned_per_status - scanned), offset, True)
                except Exception as exc:  # noqa: BLE001
                    warnings.append(f"{year} {status}: fetch failed at offset {offset}: {exc}")
                    break
                if not notes:
                    break
                for note in notes:
                    scanned += 1
                    score = relevance_score(note, query_tokens)
                    if score > 0:
                        matches.append((score, note))
                offset += len(notes)
                if len(notes) < page_size:
                    break

            matches.sort(key=lambda item: (-item[0], str(flatten_content(item[1].get("content", {})).get("title", ""))))
            for score, note in matches[:per_status]:
                content = flatten_content(note.get("content", {}))
                replies = note.get("details", {}).get("replies")
                if replies is None:
                    replies = fetch_replies_for_forum(note.get("forum") or note.get("id"))
                compact_replies = [compact_note(reply) for reply in replies]
                collected.append(
                    {
                        "year": year,
                        "status": status,
                        "relevance_score": score,
                        "forum": note.get("forum") or note.get("id"),
                        "forum_url": f"https://openreview.net/forum?id={note.get('forum') or note.get('id')}",
                        "title": content.get("title"),
                        "abstract": content.get("abstract"),
                        "keywords": content.get("keywords"),
                        "primary_area": content.get("primary_area"),
                        "venue": content.get("venue"),
                        "venueid": content.get("venueid"),
                        "decision": content.get("decision"),
                        "number": note.get("number"),
                        "reviews": [r for r in compact_replies if r["kind"] == "Official_Review"],
                        "meta_reviews": [r for r in compact_replies if r["kind"] == "Meta_Review"],
                        "decisions": [r for r in compact_replies if r["kind"] == "Decision"],
                        "reviewer_comments": [
                            r
                            for r in compact_replies
                            if r["kind"] in {"Official_Comment", "Public_Comment"} and not r["likely_author_response"]
                        ],
                        "author_responses": [
                            r
                            for r in compact_replies
                            if status == "accepted" and (r["kind"] == "Rebuttal" or r["likely_author_response"])
                        ],
                    }
                )

    return collected, warnings


def truncate(text: Any, limit: int = 420) -> str:
    value = "" if text is None else str(text).replace("\n", " ").strip()
    value = re.sub(r"\s+", " ", value)
    return value if len(value) <= limit else value[: limit - 3] + "..."


def note_summary(note: dict[str, Any]) -> str:
    fields = note.get("content", {})
    preferred = [
        "questions",
        "questions_for_the_authors",
        "weaknesses",
        "strengths_and_weaknesses",
        "limitations",
        "comment",
        "review",
        "summary",
        "metareview",
    ]
    for key in preferred:
        if key in fields and fields[key]:
            return f"{key}: {truncate(fields[key])}"
    if fields:
        key = next(iter(fields))
        return f"{key}: {truncate(fields[key])}"
    return "(no text fields)"


def write_outputs(output: Path, field: str, years: list[int], papers: list[dict[str, Any]], warnings: list[str]) -> None:
    output.mkdir(parents=True, exist_ok=True)
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat()
    payload = {
        "field": field,
        "years": years,
        "generated_at_utc": generated_at,
        "warnings": warnings,
        "papers": papers,
    }
    (output / "field_evidence.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# OpenReview Field Evidence: {field}",
        "",
        f"- Generated UTC: `{generated_at}`",
        f"- ICLR years: `{', '.join(str(y) for y in years)}`",
        f"- Papers matched: `{len(papers)}`",
        "",
    ]
    if warnings:
        lines.append("## Warnings")
        lines.extend(f"- {warning}" for warning in warnings)
        lines.append("")

    for paper in papers:
        lines.extend(
            [
                f"## ICLR {paper['year']} / {paper['status']}: {paper.get('title')}",
                "",
                f"- Forum: {paper.get('forum_url')}",
                f"- Primary area: {paper.get('primary_area')}",
                f"- Keywords: {paper.get('keywords')}",
                f"- Venue/decision: {paper.get('venue') or paper.get('decision')}",
                f"- Reviews: {len(paper['reviews'])}; reviewer comments: {len(paper['reviewer_comments'])}; author responses retained: {len(paper['author_responses'])}",
                "",
            ]
        )
        for idx, review in enumerate(paper["reviews"][:4], 1):
            lines.append(f"- Review {idx}: {note_summary(review)}")
        for idx, comment in enumerate(paper["reviewer_comments"][:4], 1):
            lines.append(f"- Reviewer comment {idx}: {note_summary(comment)}")
        for idx, response in enumerate(paper["author_responses"][:4], 1):
            lines.append(f"- Accepted-paper author response {idx}: {note_summary(response)}")
        lines.append("")

    (output / "field_evidence.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    current_year = dt.datetime.now().year
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--field", required=True, help="Field query, e.g. 'graph neural networks oversmoothing'.")
    parser.add_argument("--years", nargs="*", type=int, default=[current_year, current_year - 1, current_year - 2])
    parser.add_argument("--per-status", type=int, default=3, help="Maximum matched papers per year/status.")
    parser.add_argument("--max-scanned-per-status", type=int, default=800, help="Maximum submissions scanned for each year/status.")
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--output", required=True, help="Output directory.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    papers, warnings = collect_relevant_papers(
        field=args.field,
        years=args.years,
        per_status=args.per_status,
        max_scanned_per_status=args.max_scanned_per_status,
        page_size=args.page_size,
    )
    write_outputs(Path(args.output), args.field, args.years, papers, warnings)
    print(f"Wrote {len(papers)} matched papers to {Path(args.output).resolve()}")
    if warnings:
        print("Warnings:", file=sys.stderr)
        for warning in warnings:
            print(f"- {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
