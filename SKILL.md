---
name: research-field-reviewer-openreview
description: Generate rigorous, evidence-grounded computer-science paper reviews by combining general top-conference review criteria with research-field-specific reviewer concerns mined from recent ICLR OpenReview forums. Use when Codex needs to review a paper, build a reviewer checklist for a specific research area, audit novelty or A+B incremental contributions, synthesize OpenReview reviewer questions and accepted-paper author responses, or advise how to revise a paper at light, moderate, and major revision levels.
license: MIT-0
metadata:
  openclaw:
    emoji: "review"
    requires:
      anyBins:
        - python3
        - python
---

# Research Field Reviewer OpenReview

Use this skill to produce a professional review plan or full review for a paper in a specific research field. The output must be source-grounded: separate paper evidence, public OpenReview evidence, and your own reviewer inference.

## Quick Start

1. Check the current date first. For ICLR evidence, define the default recent window as the current year and two previous years if those venues are public; otherwise use the three most recent public ICLR years.
2. Identify the paper's field from the user request, title/abstract, keywords, task, method family, datasets, and closest related work. Preserve the narrow field before broadening to ML/AI.
3. If OpenReview field evidence is needed, run:

```bash
python scripts/fetch_openreview_field_evidence.py --field "<research field>" --output "<workdir>/openreview_field_evidence"
```

Use `python3` if `python` is unavailable. Read the generated `field_evidence.md` and `field_evidence.json`.

4. Load only the references needed for the task:
   - `references/general_review_lenses.md` for general top-conference review criteria.
   - `references/openreview_field_protocol.md` for ICLR/OpenReview retrieval, evidence labels, and synthesis rules.
   - `references/subtle_logic_flaws.md` when auditing hidden logic weaknesses.

## Required Output Structure

For a full review, produce these sections:

1. **Paper Thesis And Scope**
   - State the paper's claimed contribution in one sentence.
   - Identify the exact field, task, assumptions, evidence type, and claimed novelty.
   - Mark missing source material as `not provided` or `not reported`; do not invent it.

2. **General Top-Conference Review**
   - Cover soundness, novelty/originality, significance, methodology, experiments, reproducibility, clarity, related work, limitations, and ethics/societal risk when relevant.
   - Convert vague criticism into actionable evidence requests.
   - Include 3-5 author questions only when answers could change the review or clarify a critical weakness.

3. **Field-Specific OpenReview Review**
   - Use recent ICLR evidence from accepted, rejected, withdrawn, and desk-rejected papers when available.
   - Use reviewer questions and concerns from all public statuses.
   - Use author responses only from accepted papers.
   - Summarize concerns by category, not paper-by-paper unless the user asks for a case list.
   - Attach evidence IDs or forum URLs for every field-specific pattern.

4. **Subtle Logic Flaws**
   - Apply `references/subtle_logic_flaws.md`.
   - Report each flaw as: flaw type, paper location, why it matters, evidence needed, and review wording.

5. **A+B / Incremental-Innovation Audit**
   - Decide whether the paper is mainly: new problem, new method, new theory, new evaluation, A+B combination, transfer to a new setting, engineering consolidation, or boundary-pushing scientific contribution.
   - For A+B or incremental work, test whether the paper makes the combination scientifically necessary or merely convenient.
   - Ask whether it identifies a broken assumption, unavailable mechanism, new constraint, or empty cell that changes the field's understanding.

6. **Revision Advice**
   - Provide three revision levels:
     - Light revision: wording, scope, related-work positioning, missing details, clearer figures/tables.
     - Moderate revision: extra baselines, ablations, diagnostics, sensitivity, statistical tests, threat/scope clarification.
     - Major revision: new experimental setting, stronger theory, direct mechanism test, benchmark redesign, dataset/resource release, or reframed contribution.
   - Tie each suggestion to a reviewer concern and likely impact on acceptability.

7. **Evidence Appendix**
   - List paper evidence, OpenReview evidence, and external reviewer-guideline evidence separately.
   - For OpenReview, include year, status, title, forum URL, note type, short quoted or paraphrased concern, and how it informs the current review.
   - Keep direct quotes short and use paraphrase for synthesis.

## Evidence Discipline

- Treat public OpenReview text as precedent evidence, not as a universal truth.
- Do not cite rejected-paper author responses unless they are public and the user explicitly asks; the default rule is accepted-paper author responses only.
- Do not overfit to ICLR if the target venue is different; use ICLR as a high-quality ML review prior, then adapt to the user's venue.
- If retrieval is incomplete, state exactly what was attempted, what was missing, and whether the field-specific synthesis is representative or only illustrative.
- Never fabricate reviewer scores, decisions, replies, OpenReview IDs, or paper titles.

## Review Tone

Write as a skeptical but constructive expert reviewer. Lead with the strongest decision-relevant issues, avoid generic praise, and frame weaknesses as evidence gaps, causal gaps, scope gaps, or interpretation gaps.
