---
name: product-experience-design
description: Stage 3。把已批准需求变成用户/调用方可执行的流程、信息架构、页面/交互/状态或无 UI 系统的行为设计；定义 Figma、Interaction Spec、文案和异常态，并禁止设计自行扩大 Scope。
---

# Stage 3 — Product & Experience Design

## 目标

回答“用户/调用方具体怎么完成任务，以及系统在每个状态下怎么响应”。

有 UI 的项目需要界面/交互设计；无 UI 的 API/服务也必须有调用流程、状态、错误和操作语义设计，不能把 Stage 3 简化为 `N/A` 后什么都不做。

## UI 项目必需

- Information Architecture / Navigation
- User Flow / Task Flow
- Page / Screen Inventory
- Interaction Specification
- Forms / Validation / Confirmation
- Loading / Empty / No Result / Error / Permission / Offline 等状态
- Success / Failure Feedback
- Copy / Terminology
- Responsive / Device / Accessibility（按 Profile）
- Figma 或等价 Design Source（项目需要时）

### Interaction Spec 是需求与 Figma 的桥梁

对每个关键操作说明：

```text
入口 → 用户动作 → 校验 → 系统状态 → API/命令 → 成功反馈 → 失败反馈 → 下一步
```

## 无 UI 项目必需

至少定义：

- Caller journey / sequence
- command/API semantics
- state/lifecycle
- errors/retry/idempotency behavior
- observability feedback
- operational UX（CLI output / logs / job status 等）

## 设计权威规则

- Figma/原型用于表达已批准行为，**画出来不等于进入 Scope**。
- Product SOT 与 Figma 冲突时，不允许开发者自行选择；回 Stage 2/3 解决。
- 历史页、废弃 frame、静态截图不能覆盖当前 Design Source。
- 新交互需要重新评估开发和测试成本。

## Gate

`STAGE_3_DESIGN_READY`：

- 关键用户/调用流程从头到尾可解释；
- 正常态、错误态、空态、权限/不可用态都有定义；
- 产品术语一致；
- 开发能够列出所需 Contract；
- 测试能够据此列出行为用例。

## 统一准出补充

除本阶段原有Gate，还须逐项引用 [采用质量矩阵](../../references/adoption-level-matrix.md) 和 [Profile组合规则](../../references/profile-overlay.md) 的适用证据；空模板/未知值不是完成。批准责任按 [decision-rights](../../references/decision-rights.md)。
