# Human / AI Executor Model

任务属于项目，不属于执行者。HUMAN、AI、HUMAN_AI_PAIR共用Work Item、Scope/Contract/路径/操作边界、真实授权、测试、Review和唯一Tracker；执行方式不同不改变批准权。

```text
有效Stage 1–5基线及独立Review
→ READY工作项 + 明确任务授权
→ HUMAN / AI / HUMAN_AI_PAIR
→ Local Verify → Review → Integration → QA
```

[decision-rights](decision-rights.md)定义共同授权字段，Stage 6执行。Tracker卡已包含等价字段时不重复抄表。支付/生产/数据权限按动作适用性判断，不按执行者是不是人决定。PAIR指定Primary/Reviewer/交接；换执行者不重置缺陷链或重新取得默认权限。
