# Detailed Contrastive Reviewer Taste Profile for Federated Learning

## Anonymization Boundary

This profile is an aggregate child-skill reference derived from 61 anonymized high/general FL paper comparisons. It intentionally does not contain paper titles, author names, source file names, source-locator metadata, publication identifiers, individual sample identifiers, or pair identifiers.

Use this file as a reviewer-taste guide, not as a source index. The detailed reading reports and pairwise analyses remain external build artifacts and must not be copied into a packaged child skill unless explicitly re-anonymized.

## Evidence Base

- Evidence mode: contrastive deep reading over matched FL paper pairs.
- Corpus structure: 61 strong-paper deep readings, 61 general-paper deep readings, and 61 one-to-one subfield-related comparisons.
- Pairing policy: each strong paper was matched with one general paper in a related FL subfield; papers were not reused.
- Main recurring subfields observed:
  - Communication and systems efficiency: 60 comparisons.
  - Heterogeneity and non-IID optimization: 54 comparisons.
  - Federated large models and representation learning: 47 comparisons.
  - Privacy, security, and robustness: 44 comparisons.
  - Graph, multimodal, and domain-specific FL: 17 comparisons.
  - Personalized FL: 12 comparisons.
  - Fairness, unlearning, and governance: 6 comparisons.
  - Federated semi-supervised learning and domain adaptation: 3 comparisons.

The strongest global signal is that FL reviewers do not reward generic empirical improvement alone. They reward papers that make the federated regime inspectable, justify why the method is needed under that regime, compare against fair FL baselines, isolate the mechanism, and keep claims aligned with assumptions, privacy/system constraints, and realistic heterogeneity.

## Reviewer Taste Summary

An FL reviewer tends to ask a different question from a generic machine learning reviewer. The generic question is often "does the method improve performance?" The FL-specific question is "does the method still make sense when clients, communication, privacy, heterogeneity, local computation, participation, and deployment constraints are all part of the scientific object?"

Strong FL papers usually make the full experimental regime auditable: client counts, partition rule, non-IID severity, client participation, local epochs, optimizer, aggregation rule, tuning budget, communication rounds, payload size, seeds, and compute assumptions are clear enough that the reviewer can tell whether the reported gain is a real FL contribution or an artifact of simplified conditions.

General-level papers often fail for a subtler reason than "the idea is bad." They can have a plausible method but weak reviewer fit because they do not isolate the mechanism, under-specify the federated setting, compare against unfair or undertuned baselines, claim broad FL relevance from narrow experiments, or leave privacy/system/theory assumptions disconnected from the actual evaluation.

## Axis 1: Subfield-Specific FL Validity Checks

**Strength and coverage:** Strongest axis; supported across all 61 comparisons. The evidence indicates that reviewer expectations change materially by FL subfield.

### Reviewer Taste

The reviewer does not apply a single generic FL checklist. They first infer the paper's FL subtype and then ask whether the evidence controls the specific risks of that subtype. A communication-efficient method is judged by communication budget and transmitted payload. A privacy/security paper is judged by threat model, attacker capability, privacy budget, and utility tradeoff. A personalization paper is judged by separation of global, local, and client-specific gains. A large-model FL paper is judged by tuning budget, adapter or prompt design, model-size constraints, and deployment realism.

The hidden taste is: "show me that you know what kind of FL paper this is, and that your evidence targets the right failure modes for that kind."

### Strong Paper Pattern

Strong papers define the subfield-specific contract early. They make clear whether the main scientific object is communication efficiency, non-IID optimization, personalization, privacy, robustness, large-model adaptation, graph/multimodal learning, cross-silo deployment, cross-device deployment, fairness, unlearning, or semi-supervised/domain-shift FL. They then choose baselines, metrics, ablations, and assumptions that match that object.

Typical strong behavior includes:

- Communication/system papers report rounds, payload, local computation, compression/adapter overhead, and accuracy-efficiency tradeoffs.
- Privacy/security papers specify the threat model, attack surface, privacy leakage channel, defense assumptions, and utility cost.
- Personalization papers separate global model improvement from client-specific improvement and evaluate heterogeneous clients rather than only average accuracy.
- Large-model FL papers clarify which parameters are trained, frozen, adapted, or transmitted, and whether savings come from the method rather than from an undertuned alternative.
- Domain-specific FL papers justify why the domain setting is genuinely federated instead of a centralized benchmark with artificial partitions.

### Weak Paper Gaps

Weak papers often say "federated" but evaluate as if FL were only a data-splitting wrapper. They may report accuracy without showing how communication, participation, privacy, local computation, or heterogeneity shaped the method. They may import a generic ML method into FL without explaining the federated failure mode it solves.

Common gaps:

- Missing communication or system-budget controls in an efficiency claim.
- Missing threat model in privacy/security claims.
- Missing client-level analysis in personalization claims.
- Missing non-IID severity and partition details in heterogeneity claims.
- Missing parameter/update accounting in large-model or adapter-based FL.
- Domain-specific data split is not convincingly tied to real client boundaries.

### How To Ask During Review

- What exact FL subtype does this paper belong to, and what failure mode is the method designed to solve?
- Are the baselines, metrics, and ablations specific to that subtype?
- Does the evaluation include the FL constraints that the paper claims to address?
- If the method is removed from FL and tested as centralized learning, what scientific claim remains?
- Are client-level effects hidden by averaged metrics?

### Rebuttal and Revision Advice

- State the FL subtype and its reviewer contract explicitly in the introduction and experiment section.
- Add a compact table mapping claims to required evidence: communication, privacy, heterogeneity, personalization, large-model budget, or domain deployment.
- If a full new experiment is impossible, add at least one diagnostic ablation that directly tests the claimed FL constraint.
- Replace broad claims such as "effective in FL" with subtype-grounded claims such as "effective under partial participation with heterogeneous client distributions and fixed communication budget."

### Subfield Exceptions and Scope

This axis applies to every FL paper, but the expected evidence differs. A theory paper may not need extensive system measurements if the contribution is a clean convergence result; however, its assumptions must match realistic FL regimes. A domain application paper may not need to beat every optimization baseline, but it must justify the federated data boundary and client heterogeneity. A privacy paper can trade utility for privacy, but only if the tradeoff and threat model are explicit.

## Axis 2: Baseline Fairness and Benchmark Coverage

**Strength and coverage:** Strong; supported in 48 of 61 comparisons.

### Reviewer Taste

FL reviewers are unusually sensitive to unfair baselines because small implementation choices can dominate reported gains. They expect comparisons to control for aggregation rule, local epochs, client sampling, optimizer, partition severity, communication budget, and tuning budget. A method that beats a weak or mismatched baseline does not yet earn trust.

The hidden taste is: "your improvement must survive the strongest reasonable FL alternative under the same federated regime."

### Strong Paper Pattern

Strong papers compare against multiple relevant baseline families instead of a single canonical algorithm. They include classical aggregation baselines, local training or centralized references where appropriate, personalization baselines for personalized claims, communication-efficient baselines for system claims, privacy/security baselines for robustness claims, and strong modern methods in the same subfield.

They also make benchmark coverage meaningful rather than merely large. The datasets, tasks, partition rules, client counts, and metrics are chosen to stress the claimed FL difficulty. When a paper uses multiple datasets, it explains why they represent different heterogeneity, modality, scale, privacy, or deployment conditions.

### Weak Paper Gaps

Weak papers often include many baselines but do not make them fair. They may compare against untuned defaults, omit the nearest subfield competitor, change budgets across methods, use unrealistic partitions, or report only favorable metrics. Sometimes the baseline list appears broad, but the actual comparison fails to control for communication rounds, local epochs, model capacity, or tuning effort.

Common gaps:

- Baselines are present but not matched to the paper's FL subtype.
- Centralized or local baselines are missing when they are necessary to contextualize FL benefit.
- Communication or computation budgets are not equalized.
- Strong recent subfield baselines are absent.
- Non-IID settings are too narrow to justify broad claims.
- Hyperparameter tuning effort differs across methods.

### How To Ask During Review

- What is the nearest strong baseline for this exact FL problem, and is it included?
- Were all methods given comparable tuning, computation, local epochs, and communication rounds?
- Does the benchmark cover the claimed client heterogeneity and deployment scenario?
- Are reported gains robust across datasets, seeds, client partitions, and participation rates?
- Would the conclusion change if a stronger baseline were tuned under the same budget?

### Rebuttal and Revision Advice

- Add a baseline fairness table with method family, tuning budget, local epochs, rounds, communication budget, and partition rule.
- Add the most relevant missing baseline, even if only on the primary benchmark.
- If full baseline expansion is infeasible, rerun a smaller but fair comparison on the most diagnostic setting.
- Report effect sizes, variance, and failure cases rather than only best-case averages.
- Explain why omitted baselines are not comparable if they truly are out of scope.

### Subfield Exceptions and Scope

For theory-heavy papers, baseline coverage may be lighter, but empirical claims still need fair comparison. For application papers with constrained data access, reviewers may accept fewer baselines if the paper clearly explains deployment constraints and includes strong internal controls. For large-model FL, baseline fairness must include parameter count, trainable parameter fraction, prompt/adapter budget, and communication payload; raw accuracy alone is not enough.

## Axis 3: Scope Control and Overclaim Discipline

**Strength and coverage:** Strong; supported in 42 of 61 comparisons.

### Reviewer Taste

FL reviewers prefer a narrow, defensible claim over a broad but under-supported claim. Because FL combines optimization, systems, privacy, client heterogeneity, and deployment assumptions, broad claims are easy to overstate. A reviewer is more likely to trust a paper that says exactly where the method works, where it may fail, and which assumptions are necessary.

The hidden taste is: "do not sell a simplified setting as general FL."

### Strong Paper Pattern

Strong papers connect claims to assumptions. They state whether the setting is cross-device or cross-silo, whether clients are many or few, whether participation is partial or full, whether labels are balanced, whether privacy is formal or informal, whether communication is a constraint, and whether the method requires server-side data, public data, trusted clients, or extra metadata.

Strong papers also use limitations strategically. They do not bury limitations as a formality; they use them to define the valid scope of contribution. This makes the contribution more credible because the reviewer can see the boundary between demonstrated result and speculation.

### Weak Paper Gaps

Weak papers often claim general FL effectiveness while testing one simplified benchmark, one partition rule, or one client regime. They may imply privacy, robustness, personalization, or communication benefit without measuring the relevant dimension. They may use language that suggests deployment readiness while relying on assumptions unlikely to hold in deployment.

Common gaps:

- Claims about "real-world FL" without realistic participation, heterogeneity, or communication constraints.
- Claims about privacy/security without a concrete adversary or leakage analysis.
- Claims about personalization without client-level metrics.
- Claims about communication efficiency without payload or round accounting.
- Claims about robustness without stress tests.
- Claims about generality from a single benchmark family.

### How To Ask During Review

- Which claims are directly supported by experiments or theory, and which are speculative?
- What assumptions must hold for the method to work?
- Does the paper distinguish cross-silo, cross-device, simulated, and deployment settings?
- Are privacy, security, communication, or personalization terms used as evidence-backed claims or as broad framing?
- What is the strongest limitation that should change the paper's conclusion?

### Rebuttal and Revision Advice

- Rewrite claims to match the exact evaluated regime.
- Add a "claim-to-evidence" paragraph or table.
- Convert unsupported broad claims into future-work or limitation statements.
- Add one stress test that directly challenges the broadest claim.
- Use limitations to increase credibility rather than treating them as a weakness.

### Subfield Exceptions and Scope

Position, benchmark, and theory papers may legitimately make broader conceptual claims, but they still need to separate conceptual insight from empirically validated performance. In privacy and security FL, cautious scope is especially important: reviewers will penalize vague safety language more strongly than a narrow but honest threat model.

## Axis 4: Mechanism Evidence and Ablation Completeness

**Strength and coverage:** Strong; supported in 39 of 61 comparisons.

### Reviewer Taste

FL methods often combine many moving parts: local objectives, server aggregation, regularization, client sampling, personalization heads, compression modules, privacy mechanisms, pseudo-labeling, adapters, or domain-specific encoders. Reviewers therefore ask whether the reported gain comes from the proposed mechanism or from incidental tuning and additional complexity.

The hidden taste is: "show which component causes the improvement, and show it under the FL condition where it is supposed to matter."

### Strong Paper Pattern

Strong papers include ablations that isolate the claimed mechanism. They remove or vary key components, test sensitivity to non-IID severity, client participation, local epoch count, communication rounds, privacy budget, or model scale, and explain why the trend supports the mechanism. They often include diagnostic experiments, not just leaderboard comparisons.

Strong papers also connect ablations to the method narrative. If the method claims to reduce client drift, the ablation measures drift or a proxy under heterogeneous clients. If it claims communication efficiency, the ablation varies payload or rounds. If it claims personalization, it separates client-specific gains from global accuracy.

### Weak Paper Gaps

Weak papers may include ablations, but the ablations do not test the core mechanism. They remove arbitrary modules, report only small performance drops, or omit sensitivity to the FL variable that motivates the method. Sometimes the method has several components but the experiments cannot tell whether any one component is necessary.

Common gaps:

- Ablations do not correspond to the main claim.
- No sensitivity to heterogeneity, participation, communication, or privacy budget.
- No component-level analysis for multi-module methods.
- No diagnostic metric for the claimed mechanism.
- Improvements could be explained by increased model capacity or tuning.
- Negative or unstable cases are omitted.

### How To Ask During Review

- What is the one mechanism the paper claims is responsible for the gain?
- Which ablation would falsify that mechanism?
- Are improvements still visible when the FL stressor is varied?
- Does the method add capacity, computation, communication, or data access that baselines do not receive?
- Are the ablation metrics aligned with the mechanism or only with final accuracy?

### Rebuttal and Revision Advice

- Add a minimal mechanism ablation, even on the main dataset only.
- Report sensitivity to the FL variable central to the claim: non-IID severity, participation rate, local epochs, communication rounds, privacy budget, client count, or model scale.
- Include a diagnostic metric tied to the proposed mechanism.
- Clarify which component is essential and which is an engineering convenience.
- If the mechanism cannot be isolated, weaken causal language and present the result as an empirical recipe.

### Subfield Exceptions and Scope

For systems papers, ablations should include latency, payload, memory, or compute overhead. For theory papers, ablations may be less central, but empirical validation should still check whether theoretical conditions correspond to observed trends. For domain application papers, mechanistic evidence can be qualitative or diagnostic if full ablation is costly, but the paper should still explain why the domain-specific component matters.

## Axis 5: Theory-to-Method Alignment and Assumption Clarity

**Strength and coverage:** Strong; supported in 38 of 61 comparisons.

### Reviewer Taste

FL reviewers are skeptical of theory that is detached from the actual method or evaluation. They do not require every FL paper to have theory, but if the paper uses convergence, privacy, robustness, fairness, or efficiency theory to support its contribution, the assumptions must match the federated regime under test.

The hidden taste is: "the theorem should explain the method's behavior under the same FL constraints that appear in the experiments."

### Strong Paper Pattern

Strong papers define assumptions clearly and connect them to design choices. They explain how client heterogeneity, smoothness, bounded gradients, participation, local update steps, privacy noise, compression, or personalization terms enter the analysis. They then evaluate settings where those assumptions are at least plausibly relevant.

Even when theory is partial, strong papers are honest about what it proves. They distinguish convergence guarantees, intuition, approximation, and empirical evidence. They do not use a theorem as decoration.

### Weak Paper Gaps

Weak papers may include formalism without reviewer value. The assumptions may be unrealistic, hidden, or disconnected from experiments. The theorem may analyze a simplified method while the experiment uses a more complex algorithm. Privacy or robustness claims may rely on informal arguments rather than defined guarantees.

Common gaps:

- The analyzed algorithm differs from the implemented algorithm.
- Assumptions exclude the heterogeneity that motivates the paper.
- Theory ignores partial participation, local steps, compression, privacy noise, or client drift.
- Convergence claims are not tied to empirical settings.
- Privacy/security claims are not formalized enough for the claimed strength.
- The paper uses theory vocabulary to imply more than it proves.

### How To Ask During Review

- What exactly is proven, and for which algorithm?
- Which assumptions are essential, and are they plausible under the evaluated FL setting?
- Does the theory explain the empirical trend or merely coexist with it?
- Are convergence, privacy, robustness, or fairness claims stronger than the analysis supports?
- If the assumptions fail under realistic non-IID clients, what conclusion remains?

### Rebuttal and Revision Advice

- Add a concise assumption-to-experiment mapping.
- Clarify whether theory is a proof, intuition, or sufficient-condition analysis.
- State which implementation details are not covered by the theorem.
- Add one empirical test that varies the assumption most important to the theory.
- Weaken theorem-driven claims when the proof applies only to a simplified setting.

### Subfield Exceptions and Scope

Pure empirical systems or application papers may not need formal theory, but they should avoid theory-like claims. Privacy, robustness, and fairness papers face a higher bar because claims can have safety implications. Optimization papers should align convergence analysis with realistic local updates and heterogeneous clients.

## Axis 6: Reproducibility and Hyperparameter Transparency

**Strength and coverage:** Strong; supported in 34 of 61 comparisons.

### Reviewer Taste

FL results are highly sensitive to details that are often treated as implementation trivia in ordinary ML papers. Client sampling, local epochs, optimizer choices, partition seeds, communication rounds, model initialization, tuning budget, and aggregation details can change conclusions. Reviewers reward papers that make these details inspectable.

The hidden taste is: "if I cannot reconstruct the federated experiment, I cannot trust the conclusion."

### Strong Paper Pattern

Strong papers report the experimental recipe clearly enough to audit fairness. They specify client construction, partition rule, non-IID parameter, client participation rate, number of rounds, local epochs, batch size, optimizer, learning rates, model architecture, seed handling, communication accounting, hardware or compute assumptions where relevant, and selection criteria for hyperparameters.

They also document appendix details or release plans in a way that supports the main text. Reproducibility is treated as evidence, not administrative overhead.

### Weak Paper Gaps

Weak papers may report final metrics but omit the experimental recipe. They may not specify partition seeds, client sampling, local update counts, tuning ranges, or communication accounting. In large-model FL, they may omit trainable parameter counts, adapter configurations, prompt settings, or memory/compute overhead. In privacy/security FL, they may omit privacy budget, attack settings, or defense hyperparameters.

Common gaps:

- Missing client partition details or non-IID severity.
- Missing local epoch, optimizer, learning rate, or tuning range.
- Missing seed and variance reporting.
- Missing communication payload or round accounting.
- Missing hyperparameter selection protocol.
- Missing implementation details for privacy, robustness, compression, personalization, or large-model adaptation.

### How To Ask During Review

- Could another group reconstruct the experiment from the paper and appendix?
- Are client construction, partition, local training, and aggregation fully specified?
- Are tuning budgets comparable across baselines?
- Are variance and seed sensitivity reported?
- Are communication, compute, and memory costs reproducible?

### Rebuttal and Revision Advice

- Add an experimental recipe table.
- Report tuning ranges and selection criteria.
- Add seeds, variance, and partition details.
- Add communication and compute accounting for methods that claim efficiency.
- If code cannot be released, provide enough pseudo-code, hyperparameters, and appendix details for independent reconstruction.

### Subfield Exceptions and Scope

Industrial or sensitive-data FL papers may be unable to release code or data, but they should compensate with transparent protocols, synthetic or public reproductions, and detailed configuration. Theory papers need less implementation detail, but any empirical support still needs enough specification to judge fairness.

## Axis 7: FL Setting Realism and Client Heterogeneity Validity

**Strength and coverage:** Strong but narrower; supported in 22 of 61 comparisons. It appears most clearly when the paper's claim depends on realistic client behavior.

### Reviewer Taste

FL reviewers ask whether the simulated setting actually represents the federated problem. A paper can perform well under a convenient partition but still fail as an FL contribution if the client regime is unrealistic, the heterogeneity is too easy, the participation pattern is simplified, or the client population does not match the claimed deployment scenario.

The hidden taste is: "the federated setting is not a wrapper around a dataset; it is part of the scientific claim."

### Strong Paper Pattern

Strong papers define client heterogeneity in a way that fits the target setting. They report client counts, client data sizes, label or feature skew, participation rate, cross-device or cross-silo assumptions, communication rounds, local epochs, and whether clients represent users, institutions, devices, domains, sensors, hospitals, organizations, or artificial shards.

They test whether performance survives changes in heterogeneity, participation, or client scale. When the setting is simulated, they explain what real FL scenario the simulation approximates.

### Weak Paper Gaps

Weak papers often rely on a single partition and treat it as representative. They may use artificial client splits without explaining why those clients correspond to real entities. They may report average accuracy while hiding client-level variance or minority-client failure. They may claim cross-device relevance with small client counts or claim cross-silo relevance without institutional heterogeneity.

Common gaps:

- Client construction is artificial and unjustified.
- Only one non-IID severity is tested.
- Client count or participation does not match the claimed regime.
- Average metrics hide worst-client or minority-client behavior.
- Cross-device and cross-silo assumptions are mixed.
- Communication and local computation constraints are not realistic.

### How To Ask During Review

- What real client population does the benchmark approximate?
- Is the setting cross-device, cross-silo, simulated, or domain-partitioned?
- Does performance survive stronger or different heterogeneity?
- Are client-level outcomes reported, not only global averages?
- Does the claimed deployment scenario match the evaluated client count and participation pattern?

### Rebuttal and Revision Advice

- Add a short justification for client construction.
- Report sensitivity to heterogeneity severity or client participation.
- Add client-level variance, worst-client performance, or subgroup metrics when relevant.
- Clarify whether the result targets simulation, cross-silo deployment, or cross-device deployment.
- Narrow deployment claims if the setting is simplified.

### Subfield Exceptions and Scope

This axis is especially important for personalization, fairness, robustness, domain adaptation, medical FL, graph FL, and cross-device FL. It is less central for some algorithmic or theoretical papers if their contribution is explicitly scoped to a simplified regime, but even then reviewers expect the simplification to be named.

## Cross-Axis Review Heuristics

When using this profile to review an FL paper, do not score axes independently as a mechanical checklist. The axes interact:

- Baseline fairness is weak if the FL setting is unrealistic.
- Ablations are weak if they do not vary the FL stressor that motivates the method.
- Theory is weak if its assumptions exclude the evaluated heterogeneity.
- Reproducibility is weak if the paper omits the settings needed to judge baseline fairness.
- Scope control is weak if limitations do not acknowledge missing FL constraints.

The most review-relevant weaknesses are often cross-axis failures. For example, a paper may include many baselines and many datasets, but if client construction, tuning budgets, and communication accounting are unclear, reviewers may still see the evidence as insufficient.

## Practical Review Question Bank

Use these questions when drafting reviews:

1. What is the exact FL problem type, and are the experiments designed for that type?
2. Which FL constraint creates the need for the proposed method: heterogeneity, privacy, communication, personalization, robustness, domain shift, large-model cost, or governance?
3. Are the strongest relevant baselines included and tuned under the same budget?
4. Does the paper report client construction, non-IID severity, participation, local epochs, rounds, optimizer, seeds, and communication or compute accounting?
5. Does the core ablation isolate the claimed mechanism?
6. Are claims scoped to the evaluated client regime?
7. Are theory and assumptions aligned with the method actually implemented?
8. Does the result survive changes in heterogeneity, client participation, or system budget?
9. Are privacy, robustness, fairness, or security claims supported by the correct threat model and metrics?
10. Is the contribution still meaningful if viewed by a skeptical FL reviewer rather than a generic ML reviewer?

## Decision-Impact Weakness Patterns

The following patterns should usually have high decision impact:

- The paper claims broad FL relevance but evaluates only a narrow or artificial client split.
- The nearest FL baseline is missing or unfairly tuned.
- Communication, privacy, personalization, or robustness is claimed but not measured.
- The main mechanism is not isolated by ablation.
- The analysis proves a simplified algorithm while the empirical method is materially different.
- Client-level behavior is hidden when the contribution depends on heterogeneity or personalization.
- Reproducibility details are missing for partitioning, local updates, tuning, or communication.

The following weaknesses are usually moderate unless they affect the main claim:

- Limited dataset diversity when the paper is honestly scoped.
- Missing code release if configuration is otherwise detailed.
- Narrow theory when the paper presents it as intuition rather than proof of the full method.
- Missing deployment metrics for a primarily algorithmic contribution.

## Rebuttal Strategy Template

When helping authors respond to reviews using this taste profile:

1. First identify which axis drives the reviewer concern.
2. Do not answer with generic "we will clarify" language. Add a claim-evidence mapping.
3. If the concern is baseline fairness, provide tuning/budget details and, if possible, one new controlled baseline.
4. If the concern is mechanism, add or promise the smallest diagnostic ablation that directly tests the proposed component.
5. If the concern is setting realism, report or add heterogeneity, participation, client-count, or client-level analysis.
6. If the concern is scope, narrow the claim explicitly and explain why the remaining claim is still useful.
7. If the concern is reproducibility, provide the missing experimental recipe rather than arguing from final numbers.
8. If the concern is theory, state exactly what is proven, what is assumed, and how the empirical setting relates to it.

## How This Profile Should Be Used in a Child Skill

When reviewing a new FL paper, load this profile after the generic review rubric. First classify the paper's FL subtype, then select the most relevant axes. Use the axes to produce concrete review questions, evidence checks, decision-impact weaknesses, and revision advice.

Do not infer a paper's quality from whether it matches the source corpus distribution. Use the profile only as a learned reviewer-taste prior. The actual review must be grounded in the new paper's claims, experiments, assumptions, and evidence.
