---
name: integration-verification
description: Stage 7。执行联调、冒烟、系统/集成/回归/安全/专项测试，并严格控制测试期间修改边界；区分 Bug、Test Defect、Environment Issue 与 Change Request，使用 Fix Chain、Loop Guard、Regression Impact 和 Exact Candidate SHA 防止无限反复修改。
---

# Stage 7 — Integration & Verification

## 1. 测试目标

测试用于证明实现符合冻结 Baseline，不用于继续设计产品。

每个失败首先问：

> 它违反了哪一条已批准的 Requirement / AC / Interaction / Design / API / DB / Security / NFR Contract？

能指出 → 可能是 Defect。  
指出不了 → 先分类 Requirement/Design Gap 或 Enhancement，不能直接改代码。

## 2. Verification Baseline

开始正式测试时冻结：

- Release / Scope
- Requirement / AC versions
- Design version
- Technical Contract version
- Candidate SHA / Build ID
- Environment / Config
- Required Test Set

证据必须绑定 Candidate。候选发生变化，按影响范围作废并重跑相关证据。

## 3. 缺陷分类

- `IMPLEMENTATION_DEFECT` — 实现违反冻结 Baseline，可直接进入修复。
- `REGRESSION` — 已正确行为被当前变更破坏，修复并增加回归测试。
- `TEST_DEFECT` — 测试本身错误；修测试必须记录依据 `TEST_CORRECTION`。
- `ENVIRONMENT_INFRA` — 配置/数据/环境问题，不能通过改业务逻辑掩盖。
- `REQUIREMENT_GAP` — 产品规则缺失/矛盾，回 Stage 2。
- `DESIGN_GAP` — 交互/页面/调用流程缺失/冲突，回 Stage 3。
- `PLAN_CONTRACT_GAP` — 技术合同/架构不够或错误，回 Stage 4。
- `ENHANCEMENT` — 新想法/体验优化，进入 Backlog/Change Request，不作为当前缺陷。

## 4. Modification Levels

- `L0 NO_CODE_CHANGE`：数据、环境、测试配置问题。
- `L1 LOCAL_FIX`：单功能/单组件/单 Service 的局部实现缺陷。
- `L2 MODULE_FIX`：一个模块多文件，要求模块回归。
- `L3 CROSS_CUTTING_FIX`：Auth、Tenant、Shared Core、DB Schema、API Contract、Provider、Billing、AI Pipeline 等；必须 Impact Analysis + 扩展回归。
- `L4 BASELINE_CHANGE`：需求、设计、合同、业务语义改变；停止普通测试修复，走 Change Control 并回正确上游阶段。

## 5. Fix Boundary

Bug 修复卡必须声明：

- Origin Work ID / Feature
- Defect ID
- Allowed change paths/modules
- Forbidden areas
- Affected tests
- Fix Chain ID

发现必须碰 Forbidden Area：`BOUNDARY_EXCEEDED`，不能继续扩散。

## 6. Loop Guard

- 第一次修复失败：正常重新分析。
- 同一 Defect 第一次 Reopen：强制 Root Cause Analysis。
- 同一 Defect 或同一 Fix Chain 连续 3 次修复仍失败：`STOP_FOR_ENGINEERING_REVIEW`。
- 修 A 不断产生 B/C/D 且属于同一因果链：按 Fix Chain 计数，不能通过换 Bug ID 绕过停止条件。

## 7. Test Integrity

禁止为了 Green：

- 删除失败测试；
- 降低 assertion；
- 把 strict 改为 loose；
- skip/ignore；
- 更新 snapshot 接受错误 UI；
- mock 掉必须真实验证的依赖；
- 改 Expected Result 迎合当前代码；
- 关闭 lint/type/security rule。

确为测试错误时必须给出：错误依据、正确期望来源、影响用例，并标记 `TEST_CORRECTION`。

## 8. Regression Impact Matrix

测试范围由影响分析决定，不是每次修改都无脑全量跑：

- UI 局部 → component/unit + 对应 E2E + visual/interaction（适用）
- Backend Service → unit + integration + 相关 E2E
- API Contract → consumer/contract + integration + affected E2E
- DB/Migration → migration + DB integration + affected flows
- Auth/Permission → auth/security/negative suite
- Tenant Isolation → cross-tenant negative suite
- Shared Core → broad/full regression
- Release Candidate → Canonical Full Verify（按 Profile）

## 9. 系统测试层

按项目适用：

1. Smoke
2. Functional
3. Integration/Contract
4. Error/Boundary/Concurrency
5. Security/Permission/Data isolation
6. UX/Compatibility/Performance
7. Project-Type Profile tests
8. Regression

## 10. Exit Criteria

至少：

- 0 Open Blocker / P0
- P1 按 Release Policy 清零或书面接受
- Required AC passed
- Required regression passed
- No unauthorized change
- No unresolved Requirement/Design/Contract gap for target Release
- No active `BOUNDARY_EXCEEDED`
- Exact Candidate SHA recorded
- Evidence complete

满足下列QA收尾要求并由QA Owner签核后才能标记 `STAGE_7_VERIFIED`；不等于产品验收或发布批准。

## 11. 提测接收、分诊与缺陷生命周期

QA先核验候选/环境/配置/账号/数据版本、状态/权限样本、种子数据安全与测试计划；冒烟不通过或环境不稳定先BLOCKED，不能继续把结果算通过。质量与Profile标准见 [矩阵](../../references/adoption-level-matrix.md) 和 [组合规则](../../references/profile-overlay.md)。

缺陷生命周期：NEW → TRIAGED → ASSIGNED → IN_FIX → READY_FOR_RETEST → RETEST → VERIFIED → CLOSED；复测失败→REOPENED并触发原RCA/Fix Chain规则。BLOCKED单列；DUPLICATE/REJECTED/DEFERRED必须有依据、原问题链接和有权Owner决定，不抹掉风险。

QA分诊确认类型、严重度(P0–P3)、业务优先级（与严重度分开）、修复Owner/独立复测者、响应和复测目标时间、影响/边界、Fix Chain和验收来源。具体响应时限由项目设置，不在母SOP凭空定统一SLA。修复者不能为了关闭问题自行降级、标延期或更换Defect ID重置尝试。

## 12. 独立复测与测试纠错

开发自测不等于复测。P0/P1修复必须由非修复者重新按原复现步骤、原AC和相关回归验证当前候选；AI修复需另一可辨认模型或独立人工，单人兼任Owner不免除此条。复测依据和模型原始来源按 [reviewer-provenance](../../references/reviewer-provenance.md)留存。

STRICT的全部TEST_CORRECTION，以及任何级别涉及P0/P1的TEST_CORRECTION，必须由非纠错编制者的独立审查者先核验原测试错误、正确期望的批准来源及覆盖未降低，再采用修正并复测。不能用TEST_CORRECTION名义改变产品验收标准。确实改变标准时走 [change-control](../../utilities/change-control/SKILL.md) 和独立Pre-Coding重审。低风险常规纠错仍须同行Review和证据，不可自贴标签修绿。

同一因果Fix Chain计数跨分支/执行者/新Bug保留；根因未明、连续3次失败或修复扩散即停止盲修。第三次后只有Engineering Review记录新根因/新方案、明确边界和重新授权才可再尝试，不能清零历史；无证据不续跑。

## 13. 探索、回归与Test Closure

在已批准范围内安排探索性测试，记测试章程/覆盖/发现；新想法进Backlog，必要的产品/测试标准变化走CR。回归由影响闭包决定；代码、模型/Prompt、数据、配置或环境变化时核验失效证据，真实路径和离线/Mock证据分开。

使用 [TEST_CLOSURE](../../templates/TEST_CLOSURE.md)汇总计划/通过/失败/阻塞/未执行/N/A，关联AC、缺陷/复测/回归、TEST_CORRECTION、专项风险与候选。所有必测项通过；P0=0；P1按批准政策处理，但安全/租户隔离或关键AC失败不得带病放行。

QA Owner根据证据明确签核。修复者不能独自关闭P0/P1或用自测取代QA；模型输出STAGE_7_VERIFIED字符串不构成签核。责任与单人团队安排见 [decision-rights](../../references/decision-rights.md)。
