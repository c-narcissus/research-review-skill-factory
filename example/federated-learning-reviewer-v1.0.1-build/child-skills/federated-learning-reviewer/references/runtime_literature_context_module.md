# Runtime Literature Context Module

Use this replaceable module inside generated reviewer skills so each review can retrieve and reason over literature related to the target paper, rather than relying only on a static profile.

The module is domain-neutral. Area-specific child skills should configure the area vocabulary, venues, databases, and ranking preferences through the research area profile.

## Goal

Before writing a review, build a target-paper-specific literature context pack:

- what problem the target paper is solving;
- which parent problem and neighboring subproblems it belongs to;
- which related works, methods, baselines, datasets, and claims it cites or implies;
- which recent, high-impact, top-conference, or top-journal works are most relevant;
- how those works affect novelty, baseline expectations, evidence requirements, and reviewer questions.

The result is not a bibliography dump. It is a compact review context that helps the agent review like a field-aware reviewer who has read the recent and canonical literature. A search-result page, title list, or abstract-only lookup is not enough for literature-grounded review claims.

## Replaceable Components

Each implementation may replace these components independently:

- `target_paper_parser`: extracts title, abstract, introduction, related work, method, experiments, claims, references, and citation anchors.
- `problem_lifter`: maps the target contribution to parent problems, sibling problems, method families, benchmark families, and broader research questions.
- `query_planner`: creates exact, parent-problem, method-lineage, baseline, benchmark, and recent-top-venue queries.
- `source_retriever`: queries public scholarly sources or local corpora.
- `graph_builder`: builds a paper/problem/method/baseline/dataset/claim graph.
- `hybrid_ranker`: combines lexical match, semantic similarity, citation/venue signals, recency, and target-paper anchor proximity.
- `full_text_reader`: obtains accessible full text, extracts the problem, method, assumptions, experiments, limitations, and reviewer-relevant details, and marks inaccessible works as `metadata-only`.
- `evidence_summarizer`: summarizes retrieved works with citations, full-text coverage, and uncertainty.
- `review_context_mapper`: maps retrieved works to novelty, baseline, experimental design, assumption, and rebuttal implications.
- `privacy_and_source_filter`: avoids copying raw PDFs or private paths into the child skill; stores runtime retrieval traces outside the skill package.

## Runtime Retrieval Principles

- Do not write literature-grounded claims without retrieval or a provided local corpus.
- Do not write strong novelty, baseline, or missing-comparison claims from metadata-only records. Use metadata-only records only as leads or as weak context, and state the access limit.
- Do not invent paper titles, authors, venues, years, URLs, citation counts, or claims.
- Cite retrieved papers when using them as evidence.
- If retrieval fails or no relevant works are found, state that limitation and continue with target-paper-only review.
- When a publicly accessible PDF, publisher full text, proceedings page with full paper, OpenReview PDF, or user-provided local copy is available, open or download it for the nearest related works before judging novelty or baseline sufficiency.
- For each full-text-read related work, inspect at minimum the abstract, introduction/problem framing, method, experimental setup/baselines, main results, and limitations or discussion when present.
- Prefer top-conference, top-journal, and official proceedings sources. Public review sources such as OpenReview are strong evidence when available.
- Treat preprints as secondary evidence: use them for recency, missing metadata, or emerging work, but do not let them replace venue-published or top-venue evidence when that evidence exists.
- Prefer primary scholarly sources when available: official conference proceedings, journal publisher pages, OpenReview, ACL Anthology, DBLP, Semantic Scholar, OpenAlex, Crossref, and Papers with Code. Preprint servers are fallback or supplemental sources.
- Balance recent and canonical works. Recent work normally means the runtime current year and the previous four years unless the user or area profile specifies a different window.
- For rapidly moving areas, include a recency-biased pass and a canonical/high-citation pass.
- For niche areas, include parent-problem and method-lineage expansion instead of overfitting to a narrow keyword.

## Multi-Hop Query Planning

Build queries in layers:

1. **Target anchors**
   - exact title terms, cited related-work anchors, key baselines, datasets, and claimed method names.
2. **Same problem**
   - the target task, setting, objective, or benchmark with area terms.
3. **Parent problem**
   - the broader problem that reviewers would use to judge novelty and relevance.
4. **Method lineage**
   - borrowed ideas, model families, losses, optimization strategies, architectures, theory tools, or evaluation protocols.
5. **Baseline and benchmark expectations**
   - methods or datasets a reviewer would expect to see.
6. **Recent top-conference/top-journal sweep**
   - recent papers in the area/problem from likely top venues, top journals, official proceedings, or public review sources.
7. **Contradictory or limitation-seeking pass**
   - papers that expose failure modes, negative results, assumptions, or limits of the target method family.

The problem lifter should preserve the target paper's narrow problem while also asking what higher-level problem a reviewer will compare it against.

## Full-Text Reading Gate

Before producing the final review, select a compact critical reading set:

- the nearest prior work named by the target paper as most related;
- the strongest expected baseline family or benchmark paper;
- the most relevant recent top-venue/top-journal work for the same problem;
- one canonical or high-impact work that defines the parent problem, when needed;
- any work used to claim that a baseline is missing, outdated, or unfair.

Read the accessible full text for this set whenever possible. A normal review should full-text read at least three works when three relevant accessible works exist. If fewer than three accessible works exist, state that limit.

For each candidate work, assign one coverage status:

- `full-text-read`: full text was opened or downloaded and the required sections were inspected.
- `partial-full-text`: only some sections were accessible; state which sections were read.
- `metadata-only`: only title, abstract, citation metadata, or search-result snippets were available; do not use this work as decisive evidence.
- `inaccessible`: retrieval failed; do not use this work as evidence except to explain the search limit.

Do not let the context pack pass the gate unless it includes a full-text coverage statement and reading notes for every work used in novelty, expected-baseline, or missing-comparison judgments.

## Knowledge Graph Schema

The runtime graph can be implemented as JSON, a graph database, or a simple table, but should use these node and edge types.

### Nodes

- `target_paper`
- `retrieved_paper`
- `problem`
- `parent_problem`
- `method_family`
- `baseline`
- `dataset_or_setting`
- `metric`
- `claim`
- `limitation`
- `venue_or_source`

### Edges

- `cites`
- `solves_same_problem`
- `belongs_to_parent_problem`
- `uses_method_family`
- `extends_or_combines`
- `compares_to_baseline`
- `evaluates_on`
- `supports_claim`
- `challenges_claim`
- `reveals_limitation`
- `expected_by_reviewers`

## Ranking Policy

Rank papers with a hybrid score:

- relevance to target problem and contribution;
- proximity to target references or cited baselines;
- top-conference, top-journal, official-proceedings, or public-review source signal;
- recency within the configured recent window;
- citation or influence signal when available;
- coverage diversity across parent problem, same problem, method lineage, and baselines;
- source reliability and metadata completeness.

Do not let citation count alone dominate; a very recent top-conference or top-journal paper may be more reviewer-relevant than an older high-citation paper.

## Source Priority

Use this priority order unless the user or area profile overrides it:

1. Top conferences, top journals, and official proceedings in the target area.
2. Public-review versions of top-venue papers, such as OpenReview records.
3. Canonical or high-citation papers that define the problem, baseline, benchmark, or method lineage.
4. Strong workshop papers only when the target area is emerging and no top-venue equivalent exists.
5. Preprints only as supplemental evidence for the latest developments or as pointers to later published versions.

When a preprint and a peer-reviewed/top-venue version both exist, cite and rely on the peer-reviewed/top-venue version.

## Required Runtime Artifacts

These are generated per target-paper review and should remain outside the child skill package:

- `runtime_literature_query_plan.md/json`
- `retrieved_literature_metadata.json`
- `full_text_reading_notes.md/json`
- `runtime_literature_graph.json`
- `runtime_literature_context_pack.md/json`
- `retrieval_trace.md/json`

## Context Pack Format

```markdown
# Runtime Literature Context Pack

## Target Paper Placement

- Narrow problem:
- Parent problem:
- Method lineage:
- Claimed novelty:
- Key cited anchors:

## Retrieved Works

| Work | Year | Venue/Source | Source tier | Coverage status | Why relevant | Review use |
| --- | ---: | --- | --- | --- | --- | --- |

## Full-Text Reading Notes

| Work | Sections read | Key method/evidence | Baseline or novelty implication | Limits |
| --- | --- | --- | --- | --- |

## Reviewer-Relevant Literature Map

### Novelty Context

### Expected Baselines

### Experiment And Benchmark Expectations

### Theory Or Assumption Expectations

### Known Limitations Or Failure Modes

## Review Implications

- Strength implications:
- Weakness implications:
- Questions for authors:
- Rebuttal or revision suggestions:

## Retrieval Limits

- Missing sources:
- Search failures:
- Unverified metadata:
```

## Child Skill Use

Generated child skills should read this module before reviewing a target paper. At review time:

1. Inspect the target paper and extract anchors.
2. Build a multi-hop query plan.
3. Retrieve and rank related literature from public or user-provided sources.
4. Apply the full-text reading gate to the critical reading set.
5. Build the runtime context pack with full-text coverage status and reading notes.
6. Use only full-text-read or explicitly partial-full-text works for strong novelty, baseline, evidence-sufficiency, and missing-comparison judgments.
7. Cite retrieved works or state retrieval and full-text access limits.

If the user explicitly disables internet access or asks for no retrieval, the skill should state that it is using only bundled/static context and the target paper.

## Privacy And Packaging

Do not package runtime retrieval outputs into the skill. Do not store user PDFs, private local paths, private notes, raw crawled pages, or API keys in child skill references. Keep runtime retrieval traces in the current review workspace.
