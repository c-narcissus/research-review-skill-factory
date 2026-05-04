# Research Field Reviewer OpenReview

## 中文简介

`research-field-reviewer-openreview` 是一个面向计算机科学论文审稿的领域化审稿 skill。它的目标不是只给通用审稿模板，而是根据论文所属研究领域，结合顶会通用审稿标准和 OpenReview 上相近领域论文的公开 reviewer concerns，生成更贴近该领域的专业审稿意见。

设计思想包括三层：

1. **通用顶会审稿层**：检查 novelty、soundness、significance、methodology、experiments、reproducibility、clarity、limitations 等核心维度。
2. **领域证据层**：根据论文研究方向检索近年 ICLR/OpenReview 公开审稿意见，区分 accepted、rejected、withdrawn、desk-rejected 等不同状态，并默认只使用 accepted papers 的作者回复来总结可行 rebuttal patterns。
3. **逻辑漏洞与修改建议层**：检查 A+B / 增量创新、claim-support gap、theory-implementation gap、baseline fairness、proxy metric、scope inflation 等细粒度问题，并给出 light / moderate / major 三档修改建议。

## 如何使用

假设你已经安装了这个 skill，可以直接在对话中调用：

```text
使用 $research-field-reviewer-openreview，审稿这篇关于 graph neural networks and oversmoothing 的论文。请结合近三年 ICLR OpenReview 中相关论文的审稿意见，总结领域相关 reviewer 质疑，并给出 light / moderate / major 三档修改建议。
```

也可以只让它生成某个领域的审稿 checklist：

```text
Use $research-field-reviewer-openreview to build a field-specific review checklist for graph neural networks and oversmoothing, grounded in recent ICLR OpenReview reviewer concerns.
```

---

## English Overview

`research-field-reviewer-openreview` is a field-aware peer-review skill for computer-science papers. Its purpose is to move beyond a generic review template by combining general top-conference review criteria with public OpenReview reviewer concerns from related research areas.

The design has three layers:

1. **General top-conference review layer**: checks novelty, soundness, significance, methodology, experiments, reproducibility, clarity, and limitations.
2. **Field evidence layer**: retrieves recent ICLR/OpenReview evidence for related papers, separates accepted, rejected, withdrawn, and desk-rejected cases, and uses accepted-paper author responses by default to summarize useful rebuttal patterns.
3. **Logic-gap and revision layer**: audits A+B or incremental novelty, claim-support gaps, theory-implementation gaps, baseline fairness, proxy metrics, and scope inflation, then provides light / moderate / major revision advice.

## Usage

Assuming the skill is already installed, invoke it directly:

```text
Use $research-field-reviewer-openreview to review this paper on graph neural networks and oversmoothing. Ground the review in recent ICLR OpenReview reviewer concerns, summarize field-specific risks, and provide light / moderate / major revision advice.
```

You can also use it to build a field-specific checklist:

```text
Use $research-field-reviewer-openreview to build a field-specific review checklist for graph neural networks and oversmoothing, grounded in recent ICLR OpenReview reviewer concerns.
```


## License

MIT-0.
