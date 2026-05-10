# Privacy And Anonymization Rules

These rules apply to contrastive sample manifests, pair plans, pair review banks, rationale reports, taste profiles, and generated child skill references.

## Allowed In Child Skill References

- `area_slug`;
- abstracted content features;
- reviewer-taste inferences;
- aggregate counts, coverage, and limitations.

## Forbidden In Child Skill References

Do not include:

- paper titles;
- author names;
- original filenames;
- URLs;
- absolute or relative local paths;
- publication identifiers;
- preprint registry IDs;
- forum IDs or source-specific identifiers for contrastive samples;
- raw paper text that would identify the paper.

## Private Source Map

The private source map may contain original paths, URLs, filenames, and source details for local work only. It must not be copied into generated child skills, uploaded packages, or zip files.

Before packaging, scan child skill `references/` for forbidden patterns such as web protocol strings, drive paths, home-directory paths, publication identifiers, preprint registry identifiers, and obvious title/author fields.

## Child Skill Boundary

Generated child skills should contain the final validated taste profile and review rules only. Keep detailed pair reviews, reading notes, training rationale reports, validation reports, sample manifests, and private maps as external build artifacts.
