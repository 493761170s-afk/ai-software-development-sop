# Test Plan

Release/Feature / 合同基线 / Profiles与交叉控制 / QA Owner：

## 环境与提测准入

候选SHA/Build/Config/环境/账号与各角色状态/种子数据版本：
数据来源、脱敏/留存/清理、目标身份、付费/外发/副作用权限：
Smoke条件、环境就绪检查、失败/不稳定时BLOCKED处置：

## 覆盖矩阵

| REQ/AC/风险控制 | Test IDs/层级 | 场景/负向边界 | Fixture/角色/环境 | Mock或真实路径 | 期望与阈值来源 | 证据 |
|---|---|---|---|---|---|---|

适用层级：Unit/Component、Integration/Contract、Functional、边界/错误/并发、安全/权限/租户、UX/兼容/可访问性、性能、AI/Game/Data/Media等专项、回归。不可用真实依赖不以Mock报告替代。

## 分诊、复测与探索

严重度和业务优先级规则、Owner、响应/复测时间目标：
P0/P1独立复测人/模型安排及来源证据：
STRICT及P0/P1 TEST_CORRECTION独立审查安排：
探索性测试章程/范围、发现如何登记：
Fix Chain/RCA/停止与升级入口：

## 回归与退出

影响分析及候选/环境变化后证据失效规则：
必需AC/测试集合全部通过，P0=0，安全/租户/关键AC失败不得豁免：
P1风险政策、遗留Owner/目标版本：
TEST_CLOSURE计划-执行对照、独立复测及QA Owner签核位置：
