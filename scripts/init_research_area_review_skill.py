#!/usr/bin/env python3
"""Create a research-area-specific review skill from an area profile JSON spec."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any


MIT0 = """MIT No Attribution

Copyright 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


def slugify(text: str, fallback: str = "research-area") -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized[:48].strip("-") or fallback


def read_spec(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Spec must be a JSON object")
    return data


def list_md(values: Any) -> str:
    if not values:
        return "- not reported"
    if isinstance(values, str):
        values = [values]
    return "\n".join(f"- {value}" for value in values)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_skill_md(skill_name: str, spec: dict[str, Any]) -> str:
    area_name = spec.get("area_name") or skill_name
    scope = spec.get("one_sentence_scope") or "not reported"
    description = (
        f"Review papers in the research area '{area_name}' using a custom area profile, "
        "OpenReview-derived reviewer concern patterns, subtle logic flaw checks, "
        "and rebuttal/revision planning. Use for papers in this field/problem family."
    )
    return f"""---
name: {skill_name}
description: {description}
license: MIT-0
---

# {area_name} Reviewer OpenReview

Use this area-specific skill to review papers in this research field or problem family.

Scope: {scope}

## Required Reading Order

1. Read `references/research_area_profile.md`.
2. Read `references/openreview_review_response_bank.md`.
3. Read `references/review_output_contract.md`.
4. Read `references/subtle_logic_flaws.md`.
5. Then inspect the target paper.

## Review Workflow

1. Place the target paper inside the area map.
2. Match the paper's claims and modules to the local review-response bank.
3. Generate area-specific review concerns and questions.
4. Audit novelty, A+B incrementality, baselines, reproducibility, and subtle logic flaws.
5. Produce rebuttal strategy and light/moderate/major revision advice.

## Evidence Discipline

- Separate target-paper evidence, OpenReview precedent, and reviewer inference.
- Cite OpenReview precedent by year, status, title, forum URL, and note type.
- Mark missing paper details as `not reported`.
- Do not paste raw reviews.
"""


def build_profile_md(spec: dict[str, Any]) -> str:
    fields = spec.get("research_fields", {})
    return f"""# Research Area Profile

## Area Name

{spec.get('area_name', 'not reported')}

## One-Sentence Scope

{spec.get('one_sentence_scope', 'not reported')}

## Target Venues

{list_md(spec.get('target_venues'))}

## Research Fields

Narrow:
{list_md(fields.get('narrow'))}

Parent:
{list_md(fields.get('parent'))}

Broad:
{list_md(fields.get('broad'))}

## Problem Families

{list_md(spec.get('problem_families'))}

## Method Families

{list_md(spec.get('method_families'))}

## Theory Objects

{list_md(spec.get('theory_objects'))}

## Datasets And Settings

{list_md(spec.get('datasets_and_settings'))}

## Baseline Families

{list_md(spec.get('baseline_families'))}

## Metrics

{list_md(spec.get('metrics'))}

## OpenReview Queries

{list_md(spec.get('openreview_queries'))}

## Expected Review Categories

{list_md(spec.get('expected_review_categories'))}

## Subtle Logic Checks

{list_md(spec.get('subtle_logic_checks'))}

## Evidence Limitations

{list_md(spec.get('evidence_limitations'))}
"""


REVIEW_CONTRACT = """# Review Output Contract

Produce:

1. Summary and area placement.
2. Strengths tied to area-specific scientific goals.
3. Weaknesses ranked by decision impact.
4. OpenReview precedent mapping.
5. Claim-support matrix.
6. A+B / incremental novelty audit.
7. Subtle logic flaw audit.
8. Reviewer questions.
9. Rebuttal plan.
10. Light, moderate, and major revision advice.
11. Evidence appendix.

For each weakness:

| Weakness | Target-paper evidence | Area precedent | Why it matters | Required fix | Response class |
| --- | --- | --- | --- | --- | --- |

Response class: `text clarification`, `minor revision`, `new experiment`, `major revision`, or `insufficient`.
"""


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, help="Research area profile JSON spec.")
    parser.add_argument("--output-dir", required=True, help="Directory where the child skill folder will be created.")
    parser.add_argument("--skill-name", help="Override generated child skill name.")
    parser.add_argument("--bank", help="Path to curated OpenReview review-response bank markdown.")
    parser.add_argument("--subtle-logic", help="Path to subtle logic flaws markdown.")
    args = parser.parse_args(argv)

    spec = read_spec(Path(args.spec))
    base_slug = spec.get("area_slug") or slugify(spec.get("area_name", "research-area"))
    skill_name = args.skill_name or f"{slugify(base_slug)}-reviewer-openreview"
    if len(skill_name) > 64:
        skill_name = skill_name[:64].strip("-")

    skill_dir = Path(args.output_dir) / skill_name
    if skill_dir.exists():
        raise FileExistsError(f"Refusing to overwrite existing skill directory: {skill_dir}")

    write(skill_dir / "SKILL.md", build_skill_md(skill_name, spec))
    write(skill_dir / "references" / "research_area_profile.md", build_profile_md(spec))
    write(skill_dir / "references" / "review_output_contract.md", REVIEW_CONTRACT)
    write(
        skill_dir / "agents" / "openai.yaml",
        "interface:\n"
        f"  display_name: \"{spec.get('area_name', skill_name)} Reviewer\"\n"
        "  short_description: \"Custom OpenReview-grounded area review skill.\"\n"
        f"  default_prompt: \"Use ${skill_name} to review this paper in the target research area.\"\n",
    )
    write(skill_dir / "LICENSE.txt", MIT0)
    write(
        skill_dir / "_meta.json",
        json.dumps(
            {
                "name": skill_name,
                "version": "1.0.0",
                "license": "MIT-0",
                "source_meta_skill": "research-review-skill-factory",
                "area_name": spec.get("area_name", ""),
            },
            ensure_ascii=False,
            indent=2,
        ),
    )

    root = Path(__file__).resolve().parents[1]
    bank = Path(args.bank) if args.bank else root / "references" / "generated_area_review_skill_contract.md"
    subtle = Path(args.subtle_logic) if args.subtle_logic else root / "references" / "subtle_logic_flaws.md"
    shutil.copyfile(bank, skill_dir / "references" / "openreview_review_response_bank.md")
    shutil.copyfile(subtle, skill_dir / "references" / "subtle_logic_flaws.md")

    print(skill_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
