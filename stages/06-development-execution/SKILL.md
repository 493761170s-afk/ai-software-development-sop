---
name: development-execution
description: Stage 6传统开发实施。有效Pre-Coding独立审查和真实任务授权后，人工/AI按同一边界编码、自测、Review、集成和提测；无权改变上游合同。
---

# Stage 6 — Development Execution

## 0. 入口

核验母SOP的PACKAGE_READY、真实有效独立REVIEW_PASS、Owner确认的GATE_PASSED和当前工作授权。缺任一项停止。质量下限见 [矩阵](../../references/adoption-level-matrix.md)，批准权见 [decision-rights](../../references/decision-rights.md)。

## 1. 正常开发周期

Iteration Planning → Task Ready Check → Assignment / Authorization → Development → Local Verification → Code Review → Merge / Integration → Ready for QA。

人工、AI、PAIR没有不同的快捷路径；允许在明确授权的工作集合内连续执行，不必一Issue一停。

## 2. Task Ready Check

读取当前任务的Requirement/Design/Contract/AC、相关模块、依赖、代码base和测试要求；检查工作项READY、前置依赖完成、Scope/Out of Scope、允许/禁止路径及操作、环境/外发数据/预算、真实批准记录。核对有效Review覆盖当前合同基线，没有未审实质变更。

合同基线与代码HEAD按 [review-validity](../../references/review-validity.md) 区分：普通实现提交不会仅因SHA变化导致重新全审。代码base仍须满足授权的分支/提交范围；出现漂移先核验，不盲续写。

## 3. 所有执行模式的共同边界

HUMAN、AI、HUMAN_AI_PAIR均使用 [WORK_ITEM](../../templates/WORK_ITEM.md) 和 [AUTHORIZATION](../../templates/AUTHORIZATION.md) 的等价字段，可在同一Tracker卡内完成，不增加双账本。HUMAN不能只有一个Assignee就忽略路径、合同或付费/私密数据边界。

PAIR指定Primary、Reviewer、交接点；幕后由人驱动AI仍受同一限制。换人/换模型不清零Fix Chain，不扩大权限。

只做工作项所需代码/测试/文档。不得顺手重构无关模块、修改共享基础设施或API/DB/业务规则、做邻接功能、改全局Tracker设置、未经授权触碰生产/付费Provider/私密数据。发现必要越界，立即BOUNDARY_EXCEEDED → 影响分析 → Owner批准；涉及合同变化必须走CR和独立重审后恢复。

实验来源代码先核查 [转入记录](../../references/experiment-promotion.md)，没有审查和转入授权不得复制/引用为正式实现。

## 4. Ownership、并行和交接

项目登记Module Owner；跨模块改动需相关Owner审查和许可，不以通知代替必要批准。并行基于冻结数据/API/交互合同，不允许多个分支自行定义同一个接口。人工↔AI使用 [HANDOFF](../../templates/HANDOFF.md)，记录Work ID、branch/SHA、已做/未做、阻塞、验证、边界和下一步；禁止只说“继续上次”。

## 5. 自测与代码审查

按影响与Profile执行build/compile、lint/format/type、unit、针对性integration、smoke、migration dry run及权限/租户负向测试。Mock联调可以验证合同，但不能替代明确要求的真实路径。

Review两轴：工程正确性/安全/架构/可维护性/异常/测试/边界，以及Specification是否完整且没有多做。STRICT高风险变更需独立实现审查；它不能替代Pre-Coding审查。纠正错误测试时遵守Stage 7，不能借自测“修绿”。

合并前核对exact PR head、当前Review/测试/工作授权、变更文件及Ownership，取得MERGE_AUTH；实际保护/CI不可用须如实阻塞或按已批准替代证据处理，不能伪报CI通过。集成后的新候选重新执行受影响测试。

## 6. 正式提测

提测包：候选SHA/Build、完成Work IDs、做/未做范围、需求/设计/技术引用、自测记录、测试账号与数据/状态、Migration/Config步骤、已知问题/延期项、新权限/flag/Provider配置、审查和授权记录。

核心链路打不开、关键接口5xx、权限/环境不可用、文档与实现冲突直接打回；QA接收提测不表示实现被验收。只有满足本阶段与质量矩阵才为STAGE_6_IMPLEMENTED。
