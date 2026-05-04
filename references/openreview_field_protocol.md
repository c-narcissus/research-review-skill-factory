# OpenReview Field Evidence Protocol

Use this protocol when the user asks for field-specific review concerns or when a paper's field needs empirical reviewer-precedent grounding.

## Date And Venue Window

1. Check the current date before selecting years.
2. Prefer ICLR current year plus two previous years if the current-year OpenReview venue is public.
3. If the current year is not public or lacks public reviews, use the three most recent public ICLR years.
4. Record the exact dates and years used in the evidence appendix.

As of 2026-05-04, the default window is ICLR 2026, 2025, and 2024 if each venue has public notes.

## What To Collect

For each relevant paper:

- submission metadata: year, status, title, authors if public, forum URL, abstract, keywords, primary area, venue / decision;
- reviewer concerns and questions: Official Reviews, Meta Reviews, review fields containing questions/weaknesses/limitations, reviewer Official Comments;
- author responses: only accepted papers by default, from Rebuttal notes or likely author Official Comments;
- decision context: decision and meta-review when public.

Statuses to attempt:

- accepted: `content.venueid = ICLR.cc/<YEAR>/Conference`;
- rejected: venue group's `rejected_venue_id`;
- withdrawn: venue group's `withdrawn_venue_id`;
- desk rejected: venue group's `desk_rejected_venue_id`;
- under review / public submissions: venue group's `submission_venue_id` only when final status is not available or the user asks.

## Tooling

Run the bundled script:

```bash
python scripts/fetch_openreview_field_evidence.py --field "<field query>" --output "<output-dir>"
```

Useful options:

```bash
python scripts/fetch_openreview_field_evidence.py --field "graph neural networks oversmoothing" --years 2026 2025 2024 --per-status 4 --max-scanned-per-status 1200 --output evidence/gnn
```

The script writes:

- `field_evidence.json`: structured evidence with notes and forum URLs;
- `field_evidence.md`: concise human-readable evidence digest.

OpenReview API facts:

- Notes are the main OpenReview containers for submissions, reviews, decisions, meta-reviews, and comments.
- API v2 note retrieval can filter by `forum`, `replyto`, `invitation`, and `content`, and `details='replies'` can include replies.
- Submission status is represented in `content.venueid`; accepted submissions use the original venue id while rejected/withdrawn/desk-rejected IDs come from the venue group.

Primary docs:

- https://docs.openreview.net/reference/api-v2/entities/note
- https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/how-to-get-all-notes-for-submissions-reviews-rebuttals-etc

## Synthesis Rules

Build field-specific categories by clustering reviewer concerns, not by copying all reviews. Common categories:

- problem motivation and setting validity;
- novelty against closest field-specific prior work;
- mechanism evidence and causal diagnostics;
- theory-to-implementation match;
- baseline fairness and tuning budget;
- benchmark / dataset / metric fit;
- ablation completeness and component necessity;
- robustness, distribution shift, and stress tests;
- compute, communication, privacy, safety, fairness, or data quality when field-relevant;
- clarity of figures, theorem statements, and algorithm description.

For each category, report:

| Category | Pattern In Reviews | Representative Evidence | How Authors Resolved It In Accepted Papers | Current Paper Risk | Suggested Fix |
| --- | --- | --- | --- | --- | --- |

Evidence format:

```text
[ICLR2025 accepted PwxYoMvmvy Official_Comment] Reviewer asked whether the theory is GNN-specific rather than an MLP-like dropout analysis; authors responded with graph-dependent concentration and extra experiments. Forum: https://openreview.net/forum?id=PwxYoMvmvy
```

## Handling Accepted vs Rejected Evidence

- Accepted-paper concerns show what weaknesses can be survivable when answered with evidence, revisions, or clear scoping.
- Rejected-paper concerns show what reviewers treat as decision-relevant when unresolved.
- Withdrawn and desk-rejected papers may have sparse public discussion; use them cautiously and mark incomplete evidence.
- Never imply that a concern guarantees rejection or acceptance.

## Author-Response Analysis

For accepted papers, classify author responses:

- text clarification;
- added experiment / ablation / diagnostic;
- added proof or theorem condition;
- related-work repositioning;
- scope narrowing;
- resource release / reproducibility detail;
- reviewer misunderstanding corrected with paper evidence.

For the current paper, state whether each suggested rebuttal is text-only sufficient or empirically insufficient.
