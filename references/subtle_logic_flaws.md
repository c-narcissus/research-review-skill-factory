# Subtle Logic Flaws Checklist

Use this reference for rigorous reviews and hidden-weakness scans. These flaws are easy to miss because the paper may have strong main results, plausible motivation, and ordinary ablations.

## Reporting Format

For each flaw, report:

| Flaw type | Where it appears | Why it matters | Evidence needed | Review wording |
| --- | --- | --- | --- | --- |

Phrase issues as evidence gaps, causal gaps, scope gaps, or interpretation gaps. Do not accuse authors of bad faith.

## Flaw Types

1. **Problem-Module Causality Gap**: The paper says problem `A` exists, designs module `X` for `A`, and shows removing `X` hurts final performance, but does not show `X` mitigates `A`. Ask for a direct diagnostic of `A`, before/after evidence, severity sweep, negative control, and cost-matched alternative.
2. **Ablation Necessity vs Sufficiency Gap**: Removing `X` hurts, so authors imply `X` is necessary and sufficient. Ask for X-only, Y-only, X+Y, interaction ablation, and capacity/cost-matched alternatives.
3. **Proxy Metric Substitution Gap**: The paper claims to solve `A` but evaluates proxy `B`. Ask for the target metric, proxy justification, and divergence cases.
4. **Setting-Mismatch Gap**: Motivation describes one regime while experiments or theory use another. Ask for scoped claims or experiments in the motivated regime.
5. **Hidden Extra Resource Gap**: Improvement comes from extra data, labels, compute, tuning, communication, model capacity, augmentation, or statistics not given to baselines. Ask for equal-resource baselines and cost accounting.
6. **Baseline Degradation Explanation Gap**: Baselines are unexpectedly weak, unstable, or below known performance. Ask for implementation provenance, tuning budget, baseline-specific settings, and sanity checks.
7. **Theory-Implementation Gap**: The theorem is correct for a simplified object but the implementation differs. Ask for an assumption-to-implementation table and empirical checks of theorem-relevant quantities.
8. **Scope Inflation Gap**: Local evidence is stated as a general claim. Ask for broader evidence, narrowed wording, or limitations.
9. **Correlation-As-Mechanism Gap**: Diagnostic `D` correlates with performance and is treated as the mechanism. Ask for intervention, mediation, or counterexamples.
10. **Visualization-As-Evidence Gap**: t-SNE, heatmaps, attention maps, or examples are used as mechanism evidence. Ask for quantitative diagnostics, repeated seeds, and failure cases.
11. **Hyperparameter-as-Mechanism Gap**: The module works only because of thresholds, weights, or schedules. Ask for sensitivity, default justification, tuning budget comparison, and robustness.
12. **Fairness/Personalization Aggregation Gap**: Claims about fairness or personalization use only mean performance. Ask for per-client / group / worst-case distributions.
13. **Privacy-Preserving Language Gap**: The paper says privacy-preserving because raw data are not shared. Ask for threat model, leakage tests, and DP/secure aggregation/encryption if claimed.
14. **Communication-Efficiency Accounting Gap**: Fewer rounds are reported but true bytes, payloads, compute, memory, or wall-clock cost are omitted.
15. **Negative Result Avoidance Gap**: The paper shows successes but not failure boundaries while making broad claims.
16. **First-Claim Fragility**: "First" or "novel" depends on narrow wording. Ask for closest settings and meaningful differences.
17. **Component Naming Overreach**: Module names imply causal, robust, private, adaptive, optimal, or fair properties not shown.
18. **Rebuttal Fragility Gap**: Authors can explain a concern, but explanation is not evidence. Distinguish text-only fixes from empirical fixes.
