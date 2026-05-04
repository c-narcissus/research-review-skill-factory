# Subtle Logic Flaws Checklist

Include this checklist in generated area reviewer skills.

| Flaw type | Review action |
| --- | --- |
| Problem-module causality gap | If problem A motivates module X, require evidence that X mitigates A, not only final metric gains. |
| Ablation necessity vs sufficiency gap | Removing X hurts does not prove X is uniquely responsible. Ask for X-only, Y-only, X+Y, interactions, and cost-matched alternatives. |
| Proxy metric substitution gap | Match metrics to claims such as privacy, fairness, robustness, personalization, representation quality, communication, or theory. |
| Setting mismatch gap | Motivation, method, theory, and experiments must share compatible assumptions. |
| Hidden extra resource gap | Account for public data, server labels, compute, tuning, model size, communication, auxiliary statistics, or generated data. |
| Baseline degradation gap | Weak baselines need provenance, tuning budget, and sanity checks against published results. |
| Theory-implementation gap | Map theorem assumptions to actual training, sampling, architecture, hyperparameters, and evaluation. |
| Scope inflation gap | Do not turn local evidence into broad field claims. |
| Correlation-as-mechanism gap | A correlated diagnostic is not causal mechanism evidence. |
| Visualization-as-evidence gap | Qualitative examples and plots need quantitative support and failure cases. |
| Hyperparameter-as-mechanism gap | Require sensitivity and fair tuning when thresholds, temperatures, weights, schedules, or steps drive results. |
| Privacy-preserving language gap | No raw data sharing is not enough; require a threat model and leakage tests when privacy is claimed. |
| Communication-efficiency accounting gap | Report bytes, payloads, local compute, memory, and wall-clock costs, not only rounds. |
| Rebuttal fragility gap | Distinguish text-only clarifications from concerns requiring new evidence. |

Report as:

| Flaw type | Where it appears | Why it matters | Evidence needed | Review wording | Revision path |
| --- | --- | --- | --- | --- | --- |
