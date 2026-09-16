# Platform Adapters

Platform adapters map the core SOP onto a specific issue tracker or collaboration system without changing the lifecycle, review gates, authorization model, or project source-of-truth rules.

The core workflow is tracker-neutral. Use an adapter only when the target project actually uses that platform, and always discover the project's real issue types, fields, workflows, permissions, hierarchy, and linking capabilities before writing data.

Current public adapter:

- [`jira/`](jira/) — Jira issue modeling, readable issue templates, and safe migration/audit rules.

Additional adapters may be contributed as long as they remain optional and do not redefine the mother SOP.
