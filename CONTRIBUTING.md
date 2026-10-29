# Contributing to kritva-mechanical

Thank you for helping. This repository is planning-first: the robot mechanical hold in `kritva-program` is still in force, so work here today is planning, documents and tooling, not CAD, procurement or fabrication.

## Before you start

1. Read [README.md](README.md), [AGENTS.md](AGENTS.md) and [planning/TASKS.md](planning/TASKS.md).
2. Pick a task by its stable ID (`ROB-MECH-NNN`). Work that matches no task needs one added first; ask the owner. Tasks marked BLOCKED must not be started.
3. Check the task's acceptance criteria in [planning/ACCEPTANCE_CRITERIA.md](planning/ACCEPTANCE_CRITERIA.md) so you know what evidence is expected.

## Making a change

1. Branch from `main`. Do not push to `main`.
2. Make one focused change. Never renumber or reuse task, criterion or check IDs.
3. If the change alters a milestone, task, criterion, check, review rule or the README's scope, add a [planning/CHANGELOG.md](planning/CHANGELOG.md) entry in the same pull request. The changelog is append only.
4. Run the checks listed in [AGENTS.md](AGENTS.md) and state what you ran in the pull request. Do not claim a check you did not run.
5. Commit with the format in [planning/GIT_COMMIT_STEP.md](planning/GIT_COMMIT_STEP.md): `type(scope): summary` and one `Task:` footer, for example:

```
docs(mechanical): add interface control document outline

Task: ROB-MECH-010
```

   `Tasks: None (reason)` is allowed only on docs or chore commits.
6. Open a pull request using the template. The owner reviews and merges with a merge commit.

## Rules that always apply

- No secrets, credentials, personal data or production data.
- No values from another repository without its owner, revision and maturity.
- No acceptance claims: a merge records a change, it does not accept a task.
- Report vulnerabilities and safety concerns privately, as described in [SECURITY.md](SECURITY.md).

## Licence

By contributing you agree your contribution is licensed under the Apache License 2.0 in [LICENSE](LICENSE).
