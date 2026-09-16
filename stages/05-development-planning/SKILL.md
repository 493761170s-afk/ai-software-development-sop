---
name: development-planning
description: Stage 5。把冻结的需求、设计和技术合同拆成传统研发可执行的 Milestone、Module、Feature 和详细 Work Item；支持按模块、页面、接口、数据库、测试、运维拆分，建立依赖、估算、负责人/AI执行者、验收和唯一 Live Tracker，形成待独立模型全面审查的 Pre-Coding Package。
---

# Stage 5 — Development Planning & Detailed Task Breakdown

这是Coding前最后一个编制阶段；完成后必须由另一个模型全面独立审查，通过且取得工作授权才进入Stage 6。

## 1. WBS 层级

默认：

```text
Project
└── Release / Milestone
    └── Module / System / Epic
        └── Feature / Capability / Story
            └── Work Item / Task
```

以上是规划分析维度，不是要求 Tracker 为每层都创建对象，也不是“迭代 → 需求 → 任务 → 缺陷”的固定树。采用云效时按[建模规则](../../adapters/yunxiao/MODELING_RULES.md)区分需求分解、依赖和交付归属；里程碑不自动成为迭代。

任务必须按**可独立开发、Review、验证**的边界拆分，不能只写“前端一周 / 后端一周 / 完成 XX 模块”。

## 2. Work Item 类型

根据项目组合使用：

- DB / Migration / Index / Seed
- Backend / Domain / Service
- API / Event / Command
- Frontend Page / Screen / Component
- Interaction / State handling
- Mobile / Native integration
- Game logic / Level / Asset / HUD / Save
- AI prompt/workflow/model adapter/eval
- Data pipeline / quality / backfill
- Media pipeline / codec / render / transform
- Provider / Integration
- Security / Permission / Tenant
- Test / Fixture / E2E / Performance
- DevOps / Config / Migration / Observability
- Documentation / Runbook

## 3. 页面/屏幕拆分

不要只建“完成监测模块前端”。按页面和独立行为拆，例如：

```text
Monitoring List Page
- page shell + route
- filters/search
- data table/list
- pagination
- row actions
- permission/availability state
- loading/empty/error/no-result
- API integration
- page/component tests
```

只有在各项可以独立开发/Review/验收且复杂度值得时才继续拆；不要把每个按钮拆成十分钟微任务。

## 4. 后端拆分

典型 Feature 可拆：

```text
Data contract / migration
List/query
Detail
Create/update/delete/action
Domain validation/state transition
Permission/tenant isolation
Audit/side effects
Provider integration
Unit/integration/security tests
```

复杂状态机、异步任务、导入导出、支付、权限、多租户、AI pipeline 等不得塞进“普通 CRUD”估时。

## 5. Work Item Contract — 必填

每张正式开发卡至少包含：

```text
Stable Work ID
Title
Module / Feature / Page
Requirement IDs / AC IDs
Design reference
Technical Contract reference
Scope
Out of Scope
Inputs
Expected Outputs
Dependencies / Blockers
Assignee
Execution Mode: HUMAN | AI | HUMAN_AI_PAIR
Acceptance Criteria
Required Tests
Review Requirements
Allowed Change Boundary
Risk / Special authorization
Estimate / Priority
Tracker status
Evidence links
```

### Ready for Development 六问

1. 做什么？
2. 为什么/依据哪条 Requirement？
3. 具体输入和输出是什么？
4. 什么明确不做？
5. 依赖和 Contract 是否 Ready？
6. 怎么证明完成？

任一项回答不清，任务不能进入 READY。

## 6. 并行开发

并行依赖冻结 Contract，而不是互相等代码：

```text
Requirement/Design ready
→ Data/API Contract approved
→ Backend implements real contract
→ Frontend/Client implements against contract/mock
→ Integration switches to real endpoint
```

前端等的是合同，不是后端代码；后端等的是规则和字段合同，不是页面切图。

## 7. Tracker Takeover

- 导入前：WBS/Planning Document 是拆分来源；
- 导入后：Live Tracker 是唯一执行状态账本；
- 规划文件停止维护“进行中/完成”实时状态；
- Stable Work ID ↔ Tracker Key 建立映射；
- 批量创建必须幂等；未知结果先查询，不重复创建。

云效项目在接管前必须执行[分类审查与安全整改](../../adapters/yunxiao/CLASSIFICATION_AUDIT.md)，证明所有批准需求/AC/NFR、工程工作和必需验证有完整去向，并采用[中文卡片模板](../../adapters/yunxiao/CARD_TEMPLATES.md)。不得机械为每个开发任务复制测试卡、为工程任务虚构产品需求，或为了填满迭代页面伪造排期。既有项目先复用、再按批准计划整改；实质拆分/合并和依赖变化仍走变更控制。

## 8. Stage 5准出：送审包准备完成

按 [质量矩阵](../../references/adoption-level-matrix.md) 检验Stage 1–5及 [Profile交叉要求](../../references/profile-overlay.md)，形成 `STAGE_5_PRE_CODING_PACKAGE_READY`。附：Stage 1–4批准证据、本期完整WBS、全部工作项及依赖、测试计划、Tracker映射/接管状态、未知项影响ID、授权位置、全部实质编制模型/人工责任人、合同清单与内容版本、设计快照、Tracker结构快照、仓库源SHA。

所有模式工作卡都有相同的允许/禁止路径、操作、环境、外部调用/数据/预算边界；按 [decision-rights](../../references/decision-rights.md) 指定批准人。为P0/P1安排独立复测，STRICT安排独立测试纠错复核及QA收尾责任。不把测试和集成藏进“开发完成”。

## 9. 独立审查与后续任务

调用 [independent-pre-coding-review](../../utilities/independent-pre-coding-review/SKILL.md)。PACKAGE_READY不是Coding许可。必须取得真实持久化PASS、Technical Owner核验的GATE_PASSED和具体工作授权。

FAIL回Finding所属Stage修复；实质更改按 [review-validity](../../references/review-validity.md) 重新确定影响并独立FULL/DELTA审查。新增缺陷子卡和负责人/状态更新不能成为重新定义合同的通道；满足该文档的非实质条件才不触发重审。
