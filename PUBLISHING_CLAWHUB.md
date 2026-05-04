# Publishing To ClawHub

Skill slug: `research-field-reviewer-openreview`
Version: `1.0.0`
License: `MIT-0`
Primary metadata source: `SKILL.md` YAML frontmatter and `_meta.json`

## Package Contents

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `scripts/fetch_openreview_field_evidence.py`
- `LICENSE.txt`
- `_meta.json`
- `PUBLISH_PAGE_INFO_CN.md`

Do not include generated OpenReview evidence folders, paper PDFs, review outputs, cache files, or private manuscripts in the upload package.

## Recommended Publish Command

```bash
clawhub skill publish ./research-field-reviewer-openreview --version 1.0.0
```

## Pre-Publish Checklist

- `SKILL.md` starts with valid YAML frontmatter containing `name`, `description`, `license`, and optional `metadata`.
- Folder name is lowercase and URL-safe.
- License is declared as MIT-0 in `SKILL.md`, `_meta.json`, and `LICENSE.txt`.
- The OpenReview script uses public API data and writes generated evidence outside the skill package.
- No private paper text, reviewer assignments, or unpublished review data are included.
- `python scripts/fetch_openreview_field_evidence.py --help` works.
- Skill validation passes with `quick_validate.py`.
