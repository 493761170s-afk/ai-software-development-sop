# Profile — SaaS

## Stage 1/2

明确 Tenant/Organization/Workspace 模型、客户边界、套餐/配额/计费（如适用）、数据归属和生命周期。

## Stage 4 必须评审

- Tenant identity source
- Tenant isolation invariant
- Membership / role / resource ownership
- Cross-tenant negative access
- Unique constraints 是否包含 tenant scope
- Data export/delete/retention
- Quota/rate limit/cost attribution
- Billing/subscription/webhook（如适用）
- Migration 对全部租户的影响
- Audit / admin impersonation（如存在）

## Stage 7 必测

- cross-tenant read/write negative tests
- role/data-scope tests
- quota/concurrency/idempotency
- subscription/billing boundary（适用）
- tenant migration / deletion / export（适用）
