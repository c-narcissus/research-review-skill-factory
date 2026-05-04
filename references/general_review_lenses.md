# General Top-Conference Review Lenses

Use these lenses for the general review section before adding field-specific OpenReview evidence.

## Core Review Dimensions

| Lens | What To Check | Good Reviewer Question |
| --- | --- | --- |
| Soundness | Are claims supported by correct theory, appropriate methods, and convincing experiments? | What central claim would fail if one assumption, metric, or baseline changed? |
| Novelty / Originality | Is the contribution clearly distinguished from closest prior work? | Is this new knowledge, a new combination with articulated reasoning, or a known result in new packaging? |
| Significance | Does the work add value to the community beyond local metric gains? | Who would build on this, and what would they learn that was not already available? |
| Methodology | Are design choices justified and compared with credible alternatives? | Could a simpler, cost-matched, or established method explain the gain? |
| Experiment Design | Are datasets, splits, metrics, baselines, tuning, seeds, and statistical reliability adequate? | Does each experiment answer a reviewer doubt or only decorate the story? |
| Reproducibility | Are implementation details sufficient for an expert to rerun the main claim? | What exact details are missing: code, hyperparameters, compute, data preprocessing, splits, seeds? |
| Claim Scope | Are conclusions scoped to the tested setting? | Does the abstract or conclusion claim more than the evidence supports? |
| Related Work | Are closest works handled fairly and specifically? | Would a reader understand what prior assumption is being broken or reused? |
| Clarity | Is the paper readable enough to inspect the contribution? | Which figure, theorem, or module blocks understanding and needs rewriting? |
| Limitations / Ethics | Are failure cases, societal risks, privacy, fairness, and misuse issues handled when relevant? | Does the paper discuss the most likely failure mode rather than safe, generic limitations? |

## Review Writing Rules

- Summarize the paper's intended contribution, but do not let the summary become the critique.
- Use decision-relevant ordering: fatal soundness or evidence issues first, then novelty/significance, then clarity.
- Make every weakness actionable: ask for a diagnostic, baseline, ablation, proof detail, statistical test, scope change, or writing revision.
- Separate the dimensions. A paper can be technically sound but incremental, exciting but under-evidenced, or clear but weakly positioned.
- Ask 3-5 key questions only when answers could change the evaluation or clarify a critical limitation.
- Avoid "not SOTA" as a standalone rejection reason. Ask whether the paper contributes understanding, efficiency, robustness, new setting coverage, or conceptual clarity.
- Avoid "obvious in retrospect" as a standalone novelty objection. Require specific prior-work evidence.
- If using LLM assistance, keep responsibility for the content and check for fabricated facts or unsupported citations.

## Borrowed Review Priors

These public guidelines and agent descriptions motivate the checklist:

- ICLR 2026 Reviewer Guide: a review should assess whether the submission contributes sufficient value and new knowledge; reviewers should ask what problem is tackled, whether the approach is well motivated and placed in literature, whether claims are supported, and what the work's significance is. Source: https://iclr.cc/Conferences/2026/ReviewerGuide
- ICML 2026 Reviewer Instructions: review strengths and weaknesses across soundness, presentation, significance, and originality; originality can include creative combinations, real-world applications, or removing restrictive assumptions. Source: https://icml.cc/Conferences/2026/ReviewerInstructions
- ICLR 2025 Review Feedback Agent announcement: review feedback should make vague comments actionable, check whether the paper already addresses questions, and remove unprofessional remarks. Source: https://blog.iclr.cc/2024/10/09/iclr2025-assisting-reviewers/
- ACL Rolling Review guidelines: reviewers should assess evidence for soundness, proof validity, sound argumentation, novelty, statistical significance, reproducibility, professional tone, and whether score justifications match the text. Source: https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md
- Local `paper-deep-reading-teaching-explainer` priors: use claim-by-claim support, figure/table-to-claim mapping, experiment-as-question-answer units, reviewer-lens audit, missing-detail ledger, and scientific-frontier vs ordinary engineering distinction.
