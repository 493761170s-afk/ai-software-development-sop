# Incident / Hotfix Record

状态：OPEN / CONTAINED / FIX_PENDING / VERIFIED / CLOSED（未填默认OPEN）

Incident ID / 生产环境与目标身份：
严重度、准入证据、影响用户/数据/外部系统：
Incident Owner / Technical / QA / Release Owner：
开始时间 / 下一检查时间 / 授权到期 / 收尾截止：

## 真实授权

HOTFIX_AUTH原文/记录、批准人、时间、允许与禁止动作：
工作授权 / MERGE_AUTH / RELEASE_AUTH（分别列出，不互相推断）：
Runbook、回滚兼容检查、凭据/外发/预算限制：

## 修复分流

止损操作 / 基线内实现缺陷 / 必须先CR+重审：
REQ/AC/Contract / 合同基线 / 有效独立PASS / Work ID / CR：
实质变更？新审查报告和批准后才可Coding：
实验代码来源及转正记录（如适用）：
Fix Chain ID / 累计尝试 / 停止或升级条件：

## 证据与动作

| 时间 | 操作者 | 目标/动作 | 候选SHA/产物/配置 | 授权依据 | 结果/恢复证据 |
|---|---|---|---|---|---|

独立复核/复测人或模型来源 / 测试与回归 / QA结论：
实际发布候选 / 生产验证 / 恢复或回退决定：

## 事故收尾

时间线 / 根因 / 数据与权限核查 / 残留风险：
预防任务（唯一Tracker）/文档与合同同步：
Incident与Release Owner确认 / 关闭时间：
