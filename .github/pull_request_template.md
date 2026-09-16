## Problem

What concrete workflow problem or reusable gap does this change address?

## Change

Summarize the files and control semantics changed.

## Version impact

- [ ] Patch — wording/template correction without changing gates
- [ ] Minor — compatible capability/profile/adapter/template addition
- [ ] Major — authorization, testing, release, or pre-coding gate semantics change

## Boundary check

- [ ] No private project facts, credentials, customer data, or private repository references are included.
- [ ] Existing lifecycle authority is reused rather than duplicated.
- [ ] Platform/project adapters do not weaken the mother SOP.
- [ ] Any migration impact for existing adopters is documented.

## Validation

- [ ] `python scripts/validate.py`
- [ ] Relevant failure scenarios/regression cases were checked.
- [ ] Documentation links affected by this change were reviewed.

## Notes for reviewers

Call out any change to Stage gates, reviewer independence, authorization, test integrity, incident/hotfix handling, or release governance explicitly.
