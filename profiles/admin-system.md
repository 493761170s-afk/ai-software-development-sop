# Profile — Admin / Backoffice System

适用于内部运营后台、中后台、管理控制台。此 Profile 吸收了传统管理后台 SOP 中可复用的专项规则，但不替代母 SOP。

## Stage 2 追加

- 核心对象字典
- 状态机
- 角色/权限矩阵
- 数据范围（全部/部门/本人/自定义等）
- 校验/异常/审计规则
- 导入导出、审核、敏感操作规则

## Stage 3 追加

- 登录/无权限/404/空数据
- 布局/菜单/导航
- 列表/筛选/分页
- 新增编辑/抽屉/详情
- 权限点可见性
- 删除/冻结/拒绝等危险确认
- Loading/No Result/Partial Failure

## Stage 4 追加

- RBAC / Data Scope 双端一致
- 列表分页与索引
- 操作日志/登录日志
- 字典/枚举归属
- 导入导出与文件策略
- 管理后台脚手架/组件库许可评估

## Stage 5 典型任务

DB → List Query → Detail → Create/Update → Special Action → Permission/Scope → Audit → Frontend List/Form/Detail → Integration → Tests。

## Stage 7 必测

- 页面权限 + 接口权限
- 垂直越权、水平越权、数据权限
- 状态机
- 引用删除、重复提交、并发审核
- 导入/导出/日志（适用）

管理后台的 CRUD/RBAC 规则仅在加载本 Profile 时启用，不能上提为所有软件的硬规则。
