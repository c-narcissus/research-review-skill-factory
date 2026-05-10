# Review Output Contract

Produce:

1. Summary and area placement.
2. Strengths tied to area-specific scientific goals.
3. Weaknesses ranked by decision impact.
4. Area precedent mapping from OpenReview, contrastive samples, or both.
5. Runtime related-literature context mapping, separating full-text-read works from metadata-only works.
6. Full-text reading coverage statement for nearest related work and expected baselines.
7. Claim-support matrix.
8. A+B / incremental novelty audit.
9. Standalone subtle logic flaw audit.
10. Reviewer questions.
11. Rebuttal plan.
12. Light, moderate, and major revision advice.
13. Evidence appendix.

For each weakness:

| Weakness | Target-paper evidence | Area precedent | Why it matters | Required fix | Response class |
| --- | --- | --- | --- | --- | --- |

Response class: `text clarification`, `minor revision`, `new experiment`, `major revision`, or `insufficient`.

For the standalone subtle logic flaw audit, use:

| Flaw type | Where it appears | Why it matters | Evidence needed | Review wording | Revision path |
| --- | --- | --- | --- | --- | --- |

If a checklist item does not apply, mark it `not applicable` with a short reason. Do not omit the section.
