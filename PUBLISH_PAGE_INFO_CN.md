# ClawHub 发布页信息：research-field-reviewer-openreview v1.0.0

| Field | Value |
| --- | --- |
| Name / Slug | `research-field-reviewer-openreview` |
| Display name | Research Field Reviewer OpenReview |
| Version | `1.0.0` |
| License | `MIT-0` |
| Emoji | 🧑‍⚖️ |
| Category | Research / Peer Review / OpenReview / Computer Science |
| Primary metadata source | `SKILL.md` YAML frontmatter + `_meta.json` |

## 一句话简介

根据论文研究领域，结合计算机顶会通用审稿标准、近三年 ICLR OpenReview 公开审稿意见、录用论文作者回复、细粒度逻辑漏洞清单，生成可溯源、可执行的专业审稿意见和分层修改建议。

## Short Description

Build evidence-grounded ICLR-style reviews by field.

## 适用场景

- 为计算机领域论文生成严谨审稿意见；
- 根据研究方向总结 ICLR 近三年 OpenReview 中常见 reviewer 质疑；
- 对比录用、拒稿、撤稿论文中的审稿关注点；
- 判断论文是否只是 A+B 组合、增量创新，或是否真正推动科学边界；
- 为论文修改提供 light / moderate / major 三档建议；
- 为 rebuttal 准备 reviewer concern map 和 accepted-paper response patterns。

## 核心功能

1. 自动检查当前日期并确定近三年 ICLR 检索窗口。
2. 使用 OpenReview API 抓取相关论文的公开 review、meta-review、decision、official comments。
3. 默认只保留录用论文中的作者回复，用于分析哪些答复能缓解审稿人疑虑。
4. 输出一般性顶会审稿意见和研究领域相关审稿意见两部分。
5. 对每条 field-specific 审稿模式保留 evidence ID、年份、状态、标题和 forum URL。
6. 内置 subtle logic flaws 检查，覆盖因果、消融、proxy metric、setting mismatch、baseline、公平性、隐私、communication cost 等隐藏漏洞。
7. 对 A+B 组合和增量创新做边界突破审计。
8. 最后给出轻量、中等、重大三档论文修改方案。

## 用户触发示例

```text
使用 $research-field-reviewer-openreview，审这篇联邦学习论文，并结合近三年 ICLR OpenReview 总结领域相关 reviewer 质疑。
```

```text
Use $research-field-reviewer-openreview to build a field-specific review checklist for graph neural networks and oversmoothing.
```

```text
使用 $research-field-reviewer-openreview，判断这篇文章是不是 A+B 增量创新，并给出能把它改得更像科学边界突破的建议。
```

## Tags

`paper-review`, `openreview`, `iclr`, `peer-review`, `computer-science`, `reviewer`, `rebuttal`, `novelty`, `soundness`, `research-field`, `subtle-logic-flaws`, `clawhub`, `mit-0`

## Release Notes

v1.0.0 初版：封装通用顶会审稿标准、OpenReview 领域证据抓取脚本、细粒度逻辑漏洞清单、A+B/增量创新审计和分层论文修改建议。
