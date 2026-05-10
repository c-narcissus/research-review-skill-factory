# Research Area Profile

## Area Name

Federated Learning

## One-Sentence Scope

Review federated learning papers across optimization, personalization, privacy/security, communication efficiency, semi-supervision, domain adaptation, large-model FL, and domain-specific FL settings.

## Target Venues

- NeurIPS
- ICLR
- ICML
- AAAI
- IJCAI
- KDD
- CVPR
- ACL
- TMLR

## Evidence Strategy

contrastive_61_deep_read_pairs_plus_runtime_literature_context

## Year Window

- not reported

## Minimum Reviewed Papers Per Area

20

## Research Fields

Narrow:
- federated learning
- personalized FL
- privacy-preserving FL
- communication-efficient FL

Parent:
- distributed machine learning
- privacy-preserving machine learning
- collaborative learning

Broad:
- machine learning

## Problem Families

- heterogeneity and non-iid optimization
- personalized federated learning
- privacy security and robustness
- communication and systems efficiency
- federated large models and representation learning
- federated semi-supervised domain adaptation
- graph multimodal and domain-specific fl
- fairness unlearning and governance

## Method Families

- aggregation and optimization
- personalization and adaptation
- privacy/security/robustness
- communication-efficient training
- semi-supervised/domain-adaptive FL
- federated large-model adaptation

## Theory Objects

- not reported

## Datasets And Settings

- mnist
- femnist
- cifar
- imagenet
- celeba
- reddit
- stackoverflow
- shakespeare
- ag news
- sst
- glue
- alpaca
- mimic
- isic
- brats
- camelyon
- movielens
- amazon
- yelp
- synthetic
- cross-device
- cross-silo
- non-IID partitions

## Baseline Families

- fedavg
- fedprox
- scaffold
- fednova
- fedbn
- moon
- fedrep
- per-fedavg
- ditto
- local training
- centralized
- fine-tuning
- oracle
- state-of-the-art
- sota
- baseline

## Metrics

- accuracy
- macro-F1
- AUC
- communication rounds
- bytes transmitted
- privacy budget
- client fairness
- robustness

## OpenReview Queries

- not reported

## OpenReview Sufficiency

- not reported

## Contrastive Sample Sources

High Level:
- not reported

General Level:
- not reported

## Contrastive Minimum Pair Reviews Per Area

61

## Contrastive Pair Review Summary

```json
{
  "deep_read_high_level_reports": 61,
  "deep_read_general_level_reports": 61,
  "matched_deep_read_comparisons": 61,
  "pairing_policy": "subfield-related one-to-one matching; no paper reused"
}
```

## Contrastive Taste Axes

- {'axis': 'subfield-specific FL validity checks', 'strength': 'strong', 'support': '61/61', 'coverage': 1.0}
- {'axis': 'baseline fairness and benchmark coverage', 'strength': 'strong', 'support': '48/61', 'coverage': 0.787}
- {'axis': 'scope control and overclaim discipline', 'strength': 'strong', 'support': '42/61', 'coverage': 0.689}
- {'axis': 'mechanism evidence and ablation completeness', 'strength': 'strong', 'support': '39/61', 'coverage': 0.639}
- {'axis': 'theory-to-method alignment and assumption clarity', 'strength': 'strong', 'support': '38/61', 'coverage': 0.623}
- {'axis': 'reproducibility and hyperparameter transparency', 'strength': 'strong', 'support': '34/61', 'coverage': 0.557}
- {'axis': 'FL setting realism and client heterogeneity validity', 'strength': 'strong', 'support': '22/61', 'coverage': 0.361}

## Runtime Literature Context Module

```json
{
  "enabled": true,
  "recent_years": 5,
  "max_context_papers": 20,
  "preferred_sources": [
    "official venue proceedings",
    "journal publisher pages",
    "OpenReview",
    "DBLP",
    "Semantic Scholar",
    "OpenAlex",
    "Crossref",
    "Papers with Code",
    "preprint servers as supplemental fallback"
  ],
  "venue_hints": [
    "NeurIPS",
    "ICML",
    "ICLR",
    "TMLR",
    "JMLR",
    "MLSys",
    "KDD",
    "AAAI",
    "IJCAI",
    "CVPR",
    "ACL",
    "EMNLP",
    "USENIX Security",
    "IEEE S&P",
    "ACM CCS",
    "PETS",
    "TPAMI",
    "IEEE TNNLS"
  ],
  "source_priority": [
    "top conferences",
    "top journals",
    "official proceedings",
    "canonical high-impact work",
    "preprints as supplemental fallback"
  ],
  "query_layers": [
    "target anchors",
    "same problem",
    "parent problem",
    "method lineage",
    "baseline and benchmark expectations",
    "recent top-conference/top-journal sweep",
    "contradictory or limitation-seeking pass"
  ]
}
```

## Expected Review Categories

- area placement
- FL setting validity
- baseline fairness
- mechanism and ablation evidence
- theory-assumption alignment
- reproducibility
- scope and overclaim control
- subfield-specific validity

## Subtle Logic Checks

- Does the claimed FL regime match the actual client/data/system setup?
- Are baseline and tuning budgets comparable under non-IID partitions?
- Could gains come from extra computation, larger models, or easier data splits?
- Are privacy/security/personalization/communication claims supported by matching evidence?

## Evidence Limitations

- Taste profile is learned from user-provided high/general sample folders, not public OpenReview review text.
- External deep reading reports and pair analyses are not included in the child skill to preserve privacy.
