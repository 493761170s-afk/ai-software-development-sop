# Profile — AI Product / AI-Driven Feature

功能测试通过不等于 AI 质量通过。

## Stage 2

定义 AI 能力边界、允许/禁止行为、事实/证据要求、结构输出、失败/降级体验、质量和成本目标。

## Stage 4

至少记录：

- model/provider/version
- prompt/workflow/version
- temperature/config/tool policy
- input/output schema
- evidence/citation policy
- safety/privacy policy
- retry/fallback
- token/cost budget
- caching
- observability
- deterministic/non-deterministic expectations

## Eval Contract

建立 Golden/Calibration/Eval Set，定义：

- 数据集权威位置和版本
- 结构正确率
- factual/evidence quality
- task-specific quality rubric
- regression threshold
- human review sample strategy

## Stage 7

必须同时跑：传统功能/集成测试 + AI Eval。Prompt/model/config 变化视为会影响 Candidate Evidence 的变更。

## 安全、隐私与实际行为

设计和测试Prompt injection/不可信文档或网页指令、工具调用权限升级、PII/Secret进入Prompt/日志/Trace、跨租户上下文和缓存泄漏。模型输出不能授权自身执行高影响操作；按已批准政策保留人工确认和停止/恢复路径。

评测集/校准集的来源、租户边界、脱敏、留存/删除和外发权限必须明确；离线/Mock评测不能冒充真实运行验收。AI质量、安全/副作用和传统功能分别提供证据。多人/多系统组合按 [profile-overlay](../references/profile-overlay.md) 取并集并检查交叉风险。
