# AI Software Development SOP

一套面向 AI Coding Agent、人工开发者和人机协作团队的**阶段化软件开发生命周期与工程治理体系**。

它不是“让 AI 自己决定怎么开发”的 Vibe Coding 流程，而是保留传统软件工程中的需求、产品/体验设计、技术设计、详细任务拆分、测试、验收、发布和运维职责，用已经确认的上游产物约束下游 AI 的行为。

> 当前版本线：**4.1.x**  
> 唯一生命周期权威：[`SKILL.md`](SKILL.md)

## 核心规则

正式产品 Coding 之前必须完成：

```text
Stage 1 项目定义
Stage 2 需求工程
Stage 3 产品 / 体验设计
Stage 4 技术设计
Stage 5 开发计划与详细 WBS

→ 另一个非编制模型做独立 Pre-Coding Review
→ BLOCKER / MAJOR 清零并取得真实 PASS
→ Owner 核验 Gate
→ 明确的任务分配 / CODING_AUTH

Stage 6 开发实施
Stage 7 集成与验证
Stage 8 验收 / 发布 / 运维
```

独立审查位于 Stage 5 与 Stage 6 之间，不是 Stage 9，也不能代替人类 Owner 的最终授权。

## 设计原则

- 传统 SDLC 为主，AI 是执行资源。
- Product / Design / Technical Contract / Tracker / Code & Test Evidence 各有唯一权威，禁止 Shadow SOT。
- 一个 Live Tracker 维护实时状态，规划文档不重复维护进度。
- Requirement / Work Item / Test 使用稳定 ID，不依赖 Jira、GitHub Issues 等平台编号。
- Scope、需求、AC、NFR、交互行为、API/DB/Event/File/AI/Provider 合同、工作边界和必测标准发生实质变化时，必须走 Change Control，并使受影响的旧 Review PASS 失效。
- Bug 和 Change Request 分离。
- 不允许通过删测试、降断言、skip、错误 snapshot、Mock 真实必测路径等方式“做绿”。
- 测试证据必须绑定精确候选、环境、配置和范围。
- Merge、Verified、Accepted、Released 是不同状态。
- `EXPERIMENTAL`、`HOTFIX`、`HUMAN`、`TEST_CORRECTION` 都不能成为绕过 Gate 的标签。

完整不可覆盖规则见 [`SKILL.md`](SKILL.md)。

## 仓库内容

- [`stages/`](stages/)：Stage 1–8
- [`profiles/`](profiles/)：SaaS、Web、Admin、Mobile、Desktop、Backend、AI、Game、Data、Media、Automation、Shared Platform
- [`utilities/`](utilities/)：独立审查、变更控制、事故/Hotfix、需求追溯、根因调试
- [`templates/`](templates/)：Project Profile、Baseline Audit、Work Item、Authorization、Test、Defect、Review、Release 等模板
- [`references/`](references/)：决策权、采用级别、审查有效性、多 Profile 叠加、Tracker 治理等
- [`adapters/`](adapters/)：可选平台适配器；当前公开提供 Jira Adapter

## 快速接入

1. 先读 [`SKILL.md`](SKILL.md)。
2. 将本套件放到目标 Coding Agent 实际会读取的位置，并固定版本/提交。
3. 用 [`templates/PROJECT_PROFILE.md`](templates/PROJECT_PROFILE.md) 建立项目自己的 Profile。
4. EXISTING / MIGRATION 项目先执行 [`templates/PRE_CODING_BASELINE_AUDIT.md`](templates/PRE_CODING_BASELINE_AUDIT.md)。
5. 对明确本期范围完成 Stage 1 → 5。
6. 用 [`utilities/independent-pre-coding-review/SKILL.md`](utilities/independent-pre-coding-review/SKILL.md) 做首次 FULL 独立审查。
7. Owner 核验 Review 与当前基线一致后记录 Gate，再对具体工作项授予 Coding 权限。
8. Stage 6–8 按工作项、测试、变更控制和精确证据推进。

详细步骤见 [`docs/QUICK_START.md`](docs/QUICK_START.md)。

## Jira 与其他 Tracker

核心 SOP 不绑定具体任务管理平台。使用 Jira 时按 [`adapters/jira/`](adapters/jira/) 先发现实际 Issue Type、字段、Workflow、层级、依赖和 Sprint/Release 配置，再做分类、创建或迁移。GitHub Issues 或其他 Tracker 则按 [`references/tracker-governance.md`](references/tracker-governance.md) 的能力映射和降级规则执行。

## 关于这个公开仓库

本仓库是公开 OSS 版本，不导入任何私有业务项目的 Git 历史、内部项目 Adapter、凭据或业务事实。公开版只保留通用工程方法和可复用平台能力。

## License

Apache License 2.0，见 [`LICENSE`](LICENSE)。
