# Research Area Profile Schema

Use this schema before generating a custom area reviewer skill.

```json
{
  "area_name": "",
  "area_slug": "",
  "target_venues": ["ICLR"],
  "one_sentence_scope": "",
  "research_fields": {
    "narrow": [],
    "parent": [],
    "broad": []
  },
  "problem_families": [],
  "method_families": [],
  "theory_objects": [],
  "datasets_and_settings": [],
  "baseline_families": [],
  "metrics": [],
  "openreview_queries": [],
  "expected_review_categories": [],
  "subtle_logic_checks": [],
  "evidence_limitations": []
}
```

## Query Planning

Create 8-20 queries that cover:

- exact research area phrase;
- each problem family;
- each method family;
- important theory objects;
- benchmark or setting keywords;
- closest baseline families;
- broader fallback fields.

Example for semi-supervised federated diffusion representation learning:

- `semi-supervised federated learning`
- `federated learning label scarcity`
- `federated diffusion model`
- `diffusion model representation learning`
- `federated self-supervised learning`
- `representation learning theory`
- `spectral methods representation learning`
- `contrastive learning federated`
- `non contrastive learning`
- `privacy preserving federated generative model`
