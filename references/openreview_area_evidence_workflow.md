# OpenReview Area Evidence Workflow

Use this workflow to create a compact review-response bank for a research area or problem family.

## Year Selection

Check the current date. Default to the current ICLR year and two previous public ICLR years. If the current year is not public, use the three most recent public ICLR years.

Record:

- date checked;
- years used;
- queries used;
- retrieval limitations.

## Retrieval Command

```bash
python scripts/fetch_openreview_field_evidence.py --field "<query>" --years <Y1> <Y2> <Y3> --per-status 3 --output "<evidence-dir>/<query-slug>"
```

For smoke tests:

```bash
python scripts/fetch_openreview_field_evidence.py --field "<query>" --years <Y1> <Y2> <Y3> --per-status 1 --max-scanned-per-status 80 --output "<evidence-dir>/<query-slug>"
```

## Evidence Rules

- Include reviewer concerns from accepted, rejected, withdrawn, and desk-rejected public submissions when available.
- Include author responses only from accepted papers by default.
- Keep a representative sample across subareas rather than overfitting to one keyword.
- Mark weak or analogical evidence explicitly.

## Bank Entry Format

Use this format in the generated child skill:

```markdown
## Category: <concern category>

- Trigger terms: <keywords>
- Reviewer precedent: <paraphrased concern pattern>
- Accepted-paper response pattern: <how successful authors handled it>
- Future-paper review use: <what reviewers should check in papers in this area>
- Rebuttal/revision use: <text-only, minor revision, new experiment, major revision, or insufficient>
- Evidence:
  - [ICLRYYYY status] Title. Note type. Forum: URL.
```

## Recommended Categories

- novelty and A+B positioning;
- theory-to-method alignment;
- mechanism evidence;
- baseline fairness and tuning;
- benchmark and metric validity;
- ablation completeness;
- reproducibility and implementation detail;
- hidden resources;
- communication/compute/privacy/safety/fairness;
- overclaim and scope control.
