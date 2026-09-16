---
name: requirements-engineering
description: Stage 2。把项目范围转成可开发、可测试的产品需求、功能需求、用户故事/用例、业务规则、状态、权限/访问控制、异常和验收标准。默认借用 Spec Kit 方法论但不创建第二套 SOT。
---

# Stage 2 — Requirements Engineering

## 原则

需求必须描述 **WHAT / WHY / WHO / EXPECTED RESULT**，不要提前把实现方案伪装成需求。

Spec Kit 默认只作为方法论：Specify → Clarify → Analyze。所有结果写入项目已声明的 Product SOT。

## 需求结构

每个正式功能至少明确：

- Stable Requirement ID
- Actor / Caller
- Trigger / Preconditions
- Happy Path
- Business Rules / State Transition
- Inputs / Outputs
- Permission / Access / Data Scope（适用时）
- Validation
- Empty / Error / Retry / Partial Success（适用时）
- Audit / Notification / Side Effect（适用时）
- Acceptance Criteria
- Out of Scope / Deferred

项目还必须定义 NFR 最低集：安全、性能、可靠性、可用性、审计、运维、隐私/数据、兼容性中与该项目相关的项。

## 映射到项目协作工具

采用云效 Projex 时，在需求落卡前读取[云效建模规则](../../adapters/yunxiao/MODELING_RULES.md)。保留产品/系统能力和可验收 NFR 的需求身份；实现步骤与纯验收执行清单交给 Stage 5 作为工程/测试任务映射。不要把每个规格小节、里程碑或功能编号机械新建为需求，不以其他项目的需求数量作为目标。中文卡片应保留 WHAT/WHY/WHO 和可观察 AC，而不是只翻译标题。

## Stable IDs

推荐分层：

```text
REQ-xxx       Requirement
US-xxx        User Story / Use Case
RULE-xxx      Business Rule
AC-xxx        Acceptance Criterion
```

Stable ID 不能等于 Jira Key。

## Requirement Gap

发现未决问题时必须记录：

- 问题
- 影响 Stable IDs
- Owner
- Options / Tradeoff
- Deadline / Decision point
- 是否阻塞当前 Release / Module

未决问题只阻塞受影响工作，禁止为“完整”而猜答案。

## Gate

`STAGE_2_REQUIREMENTS_READY` 至少满足：

- Scope 内功能都有可追溯需求；
- 核心业务规则/状态/权限已定义或明确 N/A；
- AC 足以让测试人员/AI 写出测试；
- NFR 已定义到当前 Release 所需深度；
- 不存在会让目标功能含义发生根本变化的未决问题。

禁止：只写“做用户管理 / 做内容分析 / 做首页”这类不可验收标题。

## 统一准出补充

除本阶段原有Gate，还须逐项引用 [采用质量矩阵](../../references/adoption-level-matrix.md) 和 [Profile组合规则](../../references/profile-overlay.md) 的适用证据；空模板/未知值不是完成。批准责任按 [decision-rights](../../references/decision-rights.md)。
