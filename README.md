# Research Review Skill Factory

## 中文简介

`research-review-skill-factory` 是一个用于**生成领域级审稿 skill 的元 skill**。它不是直接审某一篇论文，而是面向一个特定研究领域、问题族或方法组合，构建一个可复用的个性化审稿 skill。

它的设计目的：

1. **定义研究领域画像**：明确研究方向、核心问题、方法家族、理论对象、实验设置、baseline 家族和评价指标。
2. **检索 OpenReview 证据**：根据领域关键词收集近年 ICLR/OpenReview 公开审稿意见和录用论文作者回复。
3. **归纳审稿模式**：把历史 reviewer concerns 和 accepted-paper response patterns 整理成领域专属 review-response bank。
4. **生成子审稿 skill**：输出一个可安装、可复用的领域审稿 skill，用于审该方向后续论文。

## 使用方法（假设已安装）

建议在 **Codex** 中使用这个元 skill 来生成领域审稿 skill。

安装后，可以直接在对话中调用：

```text
使用 $research-review-skill-factory，为“半监督联邦学习 + 表征学习理论”这个研究方向生成一个专属审稿 skill。请结合近三年 ICLR OpenReview 的相关审稿意见和录用论文作者回复，整理 reviewer 关注点、常见 rebuttal 策略、细粒度逻辑漏洞检查项，以及 light / moderate / major 三档修改建议。
```

一个更短的例子：

```text
使用 $research-review-skill-factory，为 graph neural networks and oversmoothing 这个方向生成一个 OpenReview-grounded 审稿 skill。
```

生成流程通常包括：

1. 生成研究领域 profile；
2. 规划 OpenReview 检索关键词；
3. 下载或读取相关 OpenReview 证据；
4. 归纳领域 review-response bank；
5. 生成并验证新的领域审稿 skill。

生成的领域审稿 skill 建议在 **ChatGPT 网页版**中使用，并开启 **extended thinking** 模式。使用时，将生成的领域审稿 skill ZIP 文件放入 ChatGPT 网页版项目的 **Sources** 里，然后在对话框中明确说明：请按照这个 ZIP 文件里的 skill 对目标论文进行审稿。

---

## English Overview

`research-review-skill-factory` is a **meta-skill for building research-area-specific review skills**. It does not review one paper directly. Instead, it creates a reusable reviewer skill for a specific research area, problem family, or method combination.

Its design goals are:

1. **Define the research-area profile**: fields, problems, method families, theory objects, experimental settings, baseline families, and metrics.
2. **Retrieve OpenReview evidence**: collect public reviewer concerns and accepted-paper author response patterns from recent ICLR/OpenReview forums.
3. **Synthesize review patterns**: turn historical reviewer concerns into a reusable area-specific review-response bank.
4. **Generate a child review skill**: package the area profile, evidence bank, subtle logic flaw checks, and review output contract into a reusable skill.

## Usage (Assuming Installed)

This meta-skill is intended to be used in **Codex** to generate research-area-specific reviewer skills.

After installing the skill, invoke it directly:

```text
Use $research-review-skill-factory to build a custom review skill for the research area “semi-supervised federated learning + representation learning theory”. Ground it in recent ICLR OpenReview reviewer concerns and accepted-paper author responses, and include reviewer focus areas, rebuttal strategies, subtle logic flaw checks, and light / moderate / major revision advice.
```

A shorter example:

```text
Use $research-review-skill-factory to generate an OpenReview-grounded review skill for graph neural networks and oversmoothing.
```

The usual workflow is:

1. build a research-area profile;
2. plan OpenReview search queries;
3. retrieve or read relevant OpenReview evidence;
4. synthesize an area-specific review-response bank;
5. generate and validate a new review skill for that area.

The generated research-area-specific reviewer skill is best used in **ChatGPT web** with **extended thinking** enabled. Put the generated reviewer skill ZIP file into the ChatGPT project **Sources**, then ask ChatGPT to review the target paper according to the skill in that ZIP file.

## License

MIT-0.
