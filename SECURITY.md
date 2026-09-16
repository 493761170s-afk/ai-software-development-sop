# Security Policy

## Reporting a vulnerability

Please do not publish credentials, private repository links, customer data, exploit details, or other sensitive material in a public issue.

For a suspected security problem in this repository, use GitHub's private vulnerability reporting feature if it is available for the repository. If private reporting is unavailable, open a minimal public issue that states only that a security-sensitive report is needed, without including exploit or secret details.

## Scope

This repository primarily contains workflow rules, templates, validators, and platform adapters. Security issues may still include:

- instructions that can cause agents to leak secrets or private evidence;
- unsafe examples that encourage committing credentials;
- governance rules that permit unauthorized production changes;
- validators or CI scripts that execute untrusted input unsafely;
- platform adapter guidance that can cause destructive or duplicate mutations.

## Project-specific security

Adopting this SOP does not create technical access control by itself. Each project must still implement and verify its own authentication, authorization, tenant isolation, secret management, branch protection, CI controls, environment separation, backup/rollback, observability, and incident response as applicable.

Markdown rules are governance constraints, not a substitute for technical enforcement.
