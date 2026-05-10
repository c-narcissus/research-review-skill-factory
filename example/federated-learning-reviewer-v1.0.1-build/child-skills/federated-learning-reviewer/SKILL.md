---
name: federated-learning-reviewer
description: Review papers in the research area 'Federated Learning' using a custom area profile, contrastive high-level-vs-general sample taste patterns, subtle logic flaw checks, and rebuttal/revision planning. Use for papers in this field/problem family.
license: MIT-0
---

# Federated Learning Reviewer Contrastive

Use this area-specific skill to review papers in this research field or problem family.

Scope: Review federated learning papers across optimization, personalization, privacy/security, communication efficiency, semi-supervision, domain adaptation, large-model FL, and domain-specific FL settings.

Evidence mode: `contrastive`

## Required Reading Order

1. Read `references/research_area_profile.md`.
2. Read `references/contrastive_taste_profile.md`.
3. Read `references/paper_review_rubric_for_contrastive.md`.
4. Read `references/privacy_and_anonymization_rules.md`.
5. Read `references/runtime_literature_context_module.md` and follow its full-text reading gate.
6. Read `references/review_output_contract.md`.
7. Read `references/subtle_logic_flaws.md`.
8. Then inspect the target paper.

## Review Workflow

1. Place the target paper inside the area map.
2. Match the paper's claims and modules to the local precedent artifacts.
3. Build a runtime literature context pack from the target paper's related work, problem, methods, baselines, and claims unless the user disables retrieval.
4. For the nearest related works that affect novelty, baseline expectations, or missing comparisons, obtain and read the accessible full text whenever possible; record full-text reading notes, or mark the work `metadata-only` when access fails.
5. Generate area-specific review concerns and questions using static precedent plus runtime literature context.
6. Audit novelty, A+B incrementality, baselines, reproducibility, and subtle logic flaws.
7. Produce a standalone subtle logic flaw audit table; do not bury these checks only inside the weakness list.
8. Produce rebuttal strategy and light/moderate/major revision advice.

## Evidence Discipline

- Separate target-paper evidence, OpenReview precedent, and reviewer inference.
- Separate runtime retrieved literature from bundled/static precedent.
- Separate full-text-read literature from metadata-only literature; do not use metadata-only records for strong novelty, baseline, or missing-comparison claims.
- Cite OpenReview precedent by year, status, title, forum URL, and note type.
- Cite runtime retrieved papers when using them to judge novelty, baseline expectations, or missing comparisons.
- Cite contrastive precedent through the final taste profile axes, aggregate support, and stated limitations.
- State retrieval and full-text access limits explicitly when the review relies on target-paper evidence only.
- Mark missing paper details as `not reported`.
- Do not paste raw reviews.
- Do not include private source maps, paper titles, authors, URLs, paths, publication identifiers, preprint registry IDs, or filenames in contrastive references.
