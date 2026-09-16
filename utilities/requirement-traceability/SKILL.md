---
name: requirement-traceability
description: 建立并审计从需求到设计、技术合同、开发任务、代码/PR、测试证据和发布版本的双向可追溯关系。用于 Pre-Coding Audit、Release Gate、缺陷影响分析和已有项目重基线。
---

# Requirement Traceability

## 核心链

```text
Requirement / Rule / AC
        ↓
Design / Interaction / Flow
        ↓
Technical Contract / ADR
        ↓
Stable Work ID / Tracker Key
        ↓
Commit / PR / Migration
        ↓
Test Case / Evidence
        ↓
Release Candidate / Release
```

要求双向可追溯：既能从 REQ 找实现，也能从一段实现找到其授权来源。

## 最小矩阵

| Requirement | Design | Contract | Work ID | Tracker | PR/SHA | Test | Evidence | Release |
|---|---|---|---|---|---|---|---|---|

## 审计问题

- 是否有 Requirement 没有 Work Item？
- 是否有 Work Item 没有 Requirement/Tech Debt/Defect 来源？
- 是否有 Figma/设计行为没有 Product Scope 支撑？
- 是否有 API/DB 字段只存在 Tracker 描述里？
- 是否有代码修改没有对应 Work ID？
- 是否有 AC 没有测试或证据？
- 是否有测试证据不是当前 Candidate SHA？

发现缺口不自动补“合理内容”，按拥有该事实的上游 Stage 回填。
