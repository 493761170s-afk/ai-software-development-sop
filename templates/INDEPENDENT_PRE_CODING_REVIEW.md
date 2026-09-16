# Independent Pre-Coding Review Record

状态：DRAFT / EVIDENCE_BLOCKED / COMPLETE（非Verdict）
Review ID / Project / 本期Release与范围 / 日期与轮次：
模式：FULL | DELTA
父完整审查与上次报告 / 所有未决Finding清单：

## 1. 身份、独立性和真实来源

主要人工Owner：
主要编制模型及其他实质编制模型（provider、模型标识/显示名、可获得版本、来源）：
Reviewer（provider、标识/显示名、可获得版本、调用或平台可见证据）：
别名归一与编制参与排除结果 / 同provider allowlist及批准依据：
独立上下文、只读工具或操作证据 / 被审基线前后核对：
原始报告URL/评论ID/导出文件、内容hash、来源时间：
若人工转载：原始来源、未改写声明和模型证据：
STRICT人工来源核验人及说明：
版本未知写NOT_EXPOSED；身份不可确定写IDENTITY_UNVERIFIED，不能填有效PASS。规则：[reviewer-provenance](../references/reviewer-provenance.md)。

## 2. 合同基线和审查范围

源Repo / 分支 / exact源SHA：
合同内容清单ID/hash（资料路径、版本、REQ/Work ID；排除审查记录自身）：
Product/Requirement / Design-Figma / Technical / WBS / Test Plan / Traceability / Risks引用：
外部设计及Tracker结构快照的版本/导出时间/hash：
质量矩阵覆盖 / Profile组合检查引用：

DELTA必填：旧/新清单、语义diff、完整影响闭包、消费者、排除集合与依据、未知范围、Technical/QA及消费者Owner确认、Reviewer范围确认。
规则：[review-validity](../references/review-validity.md)。

## 3. 已读取资料与覆盖

| Stage/交叉维度 | 已读取来源及版本 | 本轮覆盖ID/范围 | PASS/FAIL或继承父报告依据 | Findings |
|---|---|---|---|---|
| Stage 1 | | | | |
| Stage 2 | | | | |
| Stage 3 | | | | |
| Stage 4 | | | | |
| Stage 5 | | | | |
| 双向追溯/边界/Profile交叉 | | | | |

首次FULL所有行必须实际覆盖。DELTA不得用N/A替代未读但受影响材料，也不得宣称全项目重新通过。

## 4. Findings与修订

| Finding ID | BLOCKER/MAJOR/MINOR/NOTE | 文件/版本/证据 | 风险/失败场景 | 影响ID | Owning Stage | 建议 | 状态/关闭证据 |
|---|---|---|---|---|---|---|---|

| 轮次 | 旧/新基线 | 处理与未决Findings | Reviewer与原始报告 | 结论 |
|---|---|---|---|---|

## 5. 最终审查（空白不是PASS）

BLOCKER数 / MAJOR数 / MINOR-NOTE处置：
跨阶段矛盾/Shadow SOT/未知影响/不可读关键资料是否清除：
Reviewer原文Verdict：PRE_CODING_REVIEW_PASS | PRE_CODING_REVIEW_FAIL
适用基线与覆盖ID / 审查时间 / 原始报告定位：

## 6. Owner核验与准入（不是模型自授）

身份/来源、覆盖、基线有效性核验 / Technical Owner / 真实批准记录：
PRE_CODING_GATE_PASSED 或 BLOCKED：
工作授权另行引用，不由PASS自动生成。

## 7. 失效与继承日志

| 时间 | 变更/CR | 失效范围/原因 | 保留范围和证据 | FULL/DELTA | 新报告 |
|---|---|---|---|---|---|
