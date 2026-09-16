---
name: root-cause-debug
description: 对重复失败、复杂缺陷、测试反复 Reopen 或修复扩散执行证据驱动的根因分析。用于替代“看到报错就继续打补丁”，并与 Fix Chain / Loop Guard 联动。
---

# Root Cause Debug

## 原则

先证明问题，再解释问题；先找到最小故障机制，再修改。

## Red-Capable Loop

```text
Reproduce
→ collect evidence
→ narrow failing seam
→ form falsifiable hypothesis
→ test hypothesis
→ identify root cause
→ design smallest correct fix
→ targeted verification
→ regression
```

## 必须记录

- Defect / Fix Chain ID
- Candidate/base SHA
- Reproduction steps
- Expected vs Actual（引用 Baseline）
- Logs/trace/data/screenshot 等证据
- Root cause
- Why previous fix failed（若 Reopen）
- Affected surface
- Fix boundary
- Regression set

## Stop Conditions

以下任一发生就停止盲修：

- 同一 Defect 第一次 Reopen 后仍无根因；
- Fix Chain 第 3 次失败；
- 修复必须扩大到未授权 Foundation/Contract；
- 证据指向 Requirement/Design/Technical Gap；
- 环境无法稳定复现。

停止后路由到 Engineering Review / Change Control / 上游 Stage，而不是继续试错。
