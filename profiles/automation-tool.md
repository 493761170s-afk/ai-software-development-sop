# Profile — Automation / Tooling / CLI

核心风险是副作用而不是页面。

必须定义：

- dry-run / preview
- permissions
- side-effect allowlist
- idempotency
- retry/resume
- destructive action confirmation
- logs/audit
- input/output contract
- failure rollback or safe partial state
- secrets handling

AI 执行真实外部操作、付费调用、生产修改或 Private 数据传播必须有显式授权。
