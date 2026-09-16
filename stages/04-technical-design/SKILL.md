---
name: technical-design
description: Stage 4。把产品和体验需求转成可实现的架构、数据、API/事件、权限、安全、并发、第三方、迁移、部署、可观测性和测试策略；区分 EXISTING/APPROVED/PROPOSED/BLOCKED，避免提案被当成合同。
---

# Stage 4 — Technical Design

## 核心规则

Technical Design 的任务是定义 HOW，但不能重新定义 WHAT。

所有技术项必须有状态：

- `EXISTING` — 已实现且被当前基线确认
- `APPROVED` — 已批准、可作为开发合同
- `PROPOSED` — 候选方案，不能据此正式实现
- `BLOCKED` — 等待决策/证据
- `DEPRECATED` — 禁止作为新开发依据

## 通用设计面

按项目适用性覆盖：

- System Context / Architecture
- Module / Component boundaries
- Data model / schema / storage
- API / Event / Command Contract
- State / concurrency / transaction / idempotency
- AuthN / AuthZ / tenant/data isolation
- Security / privacy / secrets
- External Providers / rate limits / error mapping / cost
- Caching / queue / background jobs
- File/media/object storage
- Migration / compatibility / rollback
- Observability / logging / metrics / tracing
- Configuration / environments
- Performance / scale / capacity
- Failure modes / recovery
- Testability / fixtures / test seams
- Deployment topology / release constraints

## Contract 冻结

进入 Stage 5 前，目标 Release 的关键合同必须 `APPROVED`：

- 数据模型中的业务不变量；
- API / message / file format；
- 权限/租户边界；
- 外部 Provider 能力边界；
- 迁移和兼容策略；
- AI/数据/媒体等 Profile 要求的专项合同。

不要求一次把未来所有接口全部设计完，但目标 Work Items 的依赖合同不得处于 `PROPOSED`。

## ADR

对会影响多模块、难以逆转或代价明显的决策写 ADR。不要把每个实现细节都变成 ADR。

## Gate

`STAGE_4_TECH_READY`：

- 架构和模块边界足够支持任务拆分；
- 关键 Contract 已批准；
- NFR 有对应技术策略；
- 高风险项有验证计划；
- 未决技术项与受影响 Stable IDs 已显式记录。

## 统一准出补充

除本阶段原有Gate，还须逐项引用 [采用质量矩阵](../../references/adoption-level-matrix.md) 和 [Profile组合规则](../../references/profile-overlay.md) 的适用证据；空模板/未知值不是完成。批准责任按 [decision-rights](../../references/decision-rights.md)。

对EXISTING代码核验来源、当前合同及批准关系；实验代码不因已存在而获准复用。采用前遵守 [实验转入规则](../../references/experiment-promotion.md)，识别共享消费者并纳入影响闭包。
