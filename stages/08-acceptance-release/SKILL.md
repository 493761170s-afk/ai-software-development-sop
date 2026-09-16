---
name: acceptance-release
description: Stage 8。执行产品验收、UAT/业务验收、预发、Go/No-Go、发布、回滚准备、生产观察和 Closeout；严格区分 Verified、Accepted、Merge/Deploy 和 Released，确保发布基于 Exact Candidate 及完整证据。
---

# Stage 8 — Acceptance, Release & Operations

## 1. 验收层次

按项目适用区分：

- Product Acceptance：做出来的是冻结范围里定义的产品。
- UAT / Business Acceptance：真实角色/调用方能完成工作。
- Pre-Production Acceptance：生产近似配置下可运行。
- Release Go/No-Go：风险、回滚、监控、值守都准备好。
- Production Verification：真实发布后的 smoke/health/critical journey。

测试通过不能替代业务/产品验收；UAT 也不能替代预发验证。

## 2. Acceptance

验收关注：

- Scope 是否偷换；
- Requirement / Design / Contract 是否一致；
- 主路径是否可用；
- 关键 NFR 是否达到门槛；
- Deferred / Known Issues 是否透明。

结论：`PASS | CONDITIONAL_PASS | FAIL`。Conditional 必须记录遗留、Owner、目标版本和风险接受者。

## 3. Release Candidate

每个 RC 必须记录：

- RC ID
- Exact Git SHA / Build artifact digest
- Config version
- Migration set
- Environment
- Required verification evidence
- Known Issues

Candidate 代码、migration 或关键配置变化后，创建新 RC 或更新版本，旧证据不能无条件继承。

## 4. Go / No-Go

至少检查：

- P0/Blocker = 0
- P1 policy satisfied
- Critical journeys = 100%
- Security/permission/tenant/profile-critical tests passed
- Backup / migration / rollback ready
- Observability / alerts ready
- Secrets/config correct
- Release notes / runbook / owner/on-call ready
- Acceptance conclusion recorded
- Stage 7 TEST_CLOSURE / QA Owner sign-off recorded

## 5. Release

`MERGE_AUTH`、`ACCEPTANCE`、`RELEASE_AUTH` 分离。任何一个不能由 CI/AI 自行推断。

发布动作涉及生产、付费 Provider、破坏性迁移或真实通知时，按 Project Profile 的授权策略执行。

## 6. Rollback

必须定义触发条件、操作步骤、数据兼容和责任人。不能只有一句“可回滚”。

数据库或数据格式不可逆时，必须有 forward-fix / backup restore / compatibility window 方案。

## 7. Observation

上线观察期按风险设定。观察期：

- 只修事故/已确认缺陷；
- 不混入新功能；
- 监控错误率、关键任务、性能、权限/数据、Provider/AI/媒体等专项指标；
- 已确认生产P0进入 [incident-hotfix](../../utilities/incident-hotfix/SKILL.md)；其他缺陷/新需求走常规缺陷/CR。

## 8. Closeout

完成：

- Tracker 状态收口
- Release evidence 索引
- Deferred / debt 入 Backlog
- 文档与实际版本一致
- Retrospective：记录这次流程暴露的通用问题 vs 项目特例

只有 Production Verification 和 Closeout 完成后，才可标记 `RELEASED`。

## 9. 发布和事故责任补充

准出同时满足 [质量矩阵](../../references/adoption-level-matrix.md) 及 [Profile组合](../../references/profile-overlay.md)。按 [decision-rights](../../references/decision-rights.md) 指定具名验收/Release Owner，真实批准绑定RC/产物/配置/环境，不从AI报告推断授权。单人可兼任，独立技术/QA证据仍必须存在。

没有可用恢复方案、P0、安全/租户/关键AC失败或缺QA收尾即NO-GO。部署与已验候选不同，必须更新RC和受影响证据。运营中的止损不等于新代码许可；没有有效基线或需改合同先CR+独立审查，再正式Coding，禁止事后补审。事故只按独立utility执行，不由Project Profile自由写豁免。

共享平台发布须验证消费者兼容、迁移/回滚组合及必要消费者Owner确认；供应方批准不能替代其他项目批准。生产验证与事故收尾分别留存，关闭发布不自动关闭事故遗留。
