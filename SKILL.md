---
name: research-review-skill-factory
description: Build custom peer-review skills for specific research areas, problem families, and method combinations using OpenReview evidence. Use when Codex needs a compact meta-review skill factory that takes a research field or topic cluster, retrieves and synthesizes recent ICLR/OpenReview reviewer concerns and accepted-paper author response patterns, then generates a ClawHub-ready reviewer skill tailored to that field/problem rather than to one specific manuscript.
license: MIT-0
metadata:
  openclaw:
    emoji: "review-factory"
    requires:
      anyBins:
        - python3
        - python
---

# Research Review Skill Factory

Use this meta-skill to build a custom review skill for a specific research area, problem family, or method combination. It is broader than a manuscript-specific builder: the generated child skill should help review future papers in the selected area.

## Core Idea

Create a field/problem-specific reviewer skill:

```text
research area + problem set -> area profile -> OpenReview queries -> reviewer concern patterns -> custom area reviewer skill
```

Examples:

- `ssfl-diffusion-representation-reviewer-openreview`
- `federated-ssl-privacy-reviewer-openreview`
- `spectral-representation-theory-reviewer-openreview`
- `llm-agent-benchmark-reviewer-openreview`

## Workflow

1. **Define the research area and problem set**
   - Ask for or infer the area scope: narrow field, parent fields, problem family, method families, theory objects, experiment settings, and target venues.
   - Use `references/research_area_profile_schema.md`.
   - Preserve narrow terms before broad terms.

2. **Generate OpenReview query plan**
   - Create 8-20 queries covering the exact area phrase, subproblems, method families, theory or benchmark keywords, closest baseline families, and broader fallback fields.
   - Check the current date and select the current ICLR year plus two previous public ICLR years unless the user specifies years.

3. **Retrieve public OpenReview evidence**
   - Use:

```bash
python scripts/fetch_openreview_field_evidence.py --field "<query>" --years <Y1> <Y2> <Y3> --output "<evidence-dir>/<query-slug>"
```

   - Collect reviewer concerns from accepted, rejected, withdrawn, and desk-rejected public submissions when available.
   - Use author responses only from accepted papers by default.

4. **Synthesize an area review-response bank**
   - Cluster reviewer concerns by category.
   - For each pattern, record trigger terms, reviewer concern, accepted-paper response pattern, what future papers in this area must show, and representative evidence.
   - Keep direct quotes short; paraphrase patterns and cite forum URLs.

5. **Generate the child area reviewer skill**
   - Use `scripts/init_research_area_review_skill.py` with a filled area profile JSON.
   - The generated child skill must include `SKILL.md`, `agents/openai.yaml`, `references/research_area_profile.md`, `references/openreview_review_response_bank.md`, `references/review_output_contract.md`, `references/subtle_logic_flaws.md`, `LICENSE.txt`, and `_meta.json`.

6. **Validate and package**
   - Run `quick_validate.py` on the child skill.
   - Run syntax checks on scripts.
   - Package the child skill only after confirming there are no raw evidence caches, PDFs, manuscripts, pycache, or private data.

## Generated Child Skill Requirements

The child skill must instruct future reviewers to:

- classify a submitted paper inside the target research area;
- retrieve the local area review-response bank before writing review comments;
- generate area-specific reviewer concerns and rebuttal/revision guidance;
- cite OpenReview precedent with year, status, title, forum URL, and note type;
- audit novelty, soundness, baselines, reproducibility, A+B incrementality, and subtle logic flaws;
- provide light, moderate, and major revision paths.

## Evidence Rules

- Never fabricate OpenReview titles, forum IDs, decisions, scores, or author responses.
- Treat OpenReview evidence as precedent, not as law.
- Do not include raw review dumps in the generated child skill.
- If evidence is sparse, label the bank as `limited evidence` and include a broader fallback area.

## References

- `references/research_area_profile_schema.md`: area/problem profile schema.
- `references/openreview_area_evidence_workflow.md`: retrieval and synthesis protocol.
- `references/generated_area_review_skill_contract.md`: generated child skill contract.
- `references/subtle_logic_flaws.md`: reusable hidden-weakness checklist.
