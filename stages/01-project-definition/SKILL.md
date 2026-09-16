---
name: project-definition
description: Stage 1。对新项目或已有项目进行立项、目标、用户/调用方、范围、非范围、项目类型、依赖和成功指标定义；已有项目同时启动 Pre-Coding Baseline Audit。正式需求、设计和 Coding 前使用。
---

# Stage 1 — Project Definition

## 目标

把“想做一个东西”变成可治理的项目边界。这里定义的是**为什么做、给谁做、本期做什么/不做什么**，不是先写页面或技术方案。

## 必须回答

1. 项目服务谁：终端用户、内部岗位、开发者、API 调用方、运营、管理员或多租户客户？
2. 解决什么问题，当前替代方式是什么？
3. 核心业务/系统对象或能力是什么？
4. 本 Release / V1 的成功结果是什么？
5. 明确 Out of Scope 是什么？
6. 有哪些外部依赖、合规/付费/Secret/数据风险？
7. 项目属于哪些类型 Profile？
8. 是 NEW、EXISTING 还是 MIGRATION？

## 必须产物

- Project Charter / 一页项目定义
- Stakeholder / Actor / Caller 列表
- Scope / Out of Scope
- Success Metrics / Release Goal
- External Dependencies / Constraints
- Project-Type Profiles
- 初始 Risk Register
- EXISTING/MIGRATION：Baseline Inventory + 权威状态表

## Existing Project 规则

已有代码、已有 Figma、已有 Issue 都不自动等于完成 Stage 1。第一次接入：

- 找出当前真正运行的版本；
- 找出产品/技术/设计/任务/测试资料；
- 标记 Canonical / Reference / Deprecated；
- 不为了形式重写已经有效的资料；
- 把缺口留给 Stage 2–5 补齐。

## Gate

`STAGE_1_PROJECT_DEFINED` 只有在目标、用户/调用方、Scope、Out of Scope、项目类型和依赖得到明确记录后才能通过。

禁止：

- Scope 未定就大量画 UI 或 Coding；
- 把“AI 能做出来”当作产品目标；
- 用当前代码行为反推并偷偷定义产品规则；
- 把未验证的第三方能力写成已承诺功能。

## 统一准出补充

除本阶段原有Gate，还须逐项引用 [采用质量矩阵](../../references/adoption-level-matrix.md) 和 [Profile组合规则](../../references/profile-overlay.md) 的适用证据；空模板/未知值不是完成。批准责任按 [decision-rights](../../references/decision-rights.md)。

在项目Profile中指定具名Product/Design/Technical/QA/Release Owner（可同一人兼任）、SOP源版本、实际控制手段、组合Profiles及风险责任，不让AI代签批准。
