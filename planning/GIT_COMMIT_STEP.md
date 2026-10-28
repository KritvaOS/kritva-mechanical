# Git Commit Step

| Property | Value |
|---|---|
| Document ID | KOS-MECH-GIT |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Procedure |
| Status | PROPOSED (adoption of the kritva-program commit standard for this repository is not yet formally recorded) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-28 |
| Authority | AUTHORITATIVE for this repository's branch, commit and pull request sequence once adopted (role, not approval). The pinned engineering contract (program decision D-023) controls where it differs. |
| Related Tasks / Milestones | ROB-MECH-002, ROB-MECH-003 (enforcement); every task (consumers) |
| Related Documents | [TASKS.md](TASKS.md), [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md), [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md), [CHANGELOG.md](CHANGELOG.md), [README.md](../README.md); kritva-program [acceptance standard](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/ACCEPTANCE_STANDARD.md) section 4, [agent instructions](https://github.com/KritvaOS/kritva-program/blob/main/AGENTS.md) |

## Purpose

This document gives the required sequence for recording work in this repository: how to branch, how to write a commit message, how to open and land a pull request, and how to record the resulting commit on the task. Contributors follow it for every change, and reviewers use it to judge whether a change was made properly.

A commit is evidence of change, not of acceptance. A merge, a passing run or a tag does not make a task or milestone accepted.

## 1. Current state

No commit or pull request rule is enforced in this repository today. It has no workflows, no `CODEOWNERS` and no branch protection that anyone has verified. The rules below follow the kritva-program commit standard (decision D-053) and are PROPOSED for this repository. Until the owner adopts them formally and tasks ROB-MECH-002 and ROB-MECH-003 add enforcement, they are advisory reference, not a second mandatory format. Existing history is never checked or rewritten.

Where the pinned engineering contract (decision D-023) and this document differ, the contract wins and this file is corrected. The contract text is not yet committed to kritva-program, so the branch naming below is also PROPOSED.

## 2. Principles

1. **Everything goes through a pull request.** Never push to `main`.
2. **One logical change per commit, one task per commit.** Every commit names the task it implements.
3. **History is never rewritten on shared branches.** No force push and no rewriting of shared history without the owner's explicit approval.
4. **Checks are not silenced.** A failing check is fixed. No allowlist entry or ignore rule is added to make a change pass; propose it to the owner with the reason.
5. **No secrets, ever.** If one is committed by mistake, tell the Security Owner (Dinesh) at once. Removing it in a later commit does not make it safe; it must be revoked or rotated.
6. **The plan is not edited silently.** A change to tasks, criteria or milestones is recorded in the changelog in the same pull request.
7. **No invented evidence.** Do not claim a check passed unless it was run, and do not claim an approval that is not recorded.

## 3. Branches

| Rule | Value |
|---|---|
| Base | `main`, always up to date before opening a pull request |
| Name (PROPOSED) | `rob-mech/NNN-short-name`, where NNN is the task number and the short name is lower case with hyphens, for example `rob-mech/007-rob-a0-configuration` |
| One task per branch | Preferred; a branch that covers several closely tied tasks says so in the pull request |
| Lifetime | Short; delete the remote branch after the merge |
| Direct commits to `main` | Not allowed |

## 4. Commit message format

```text
type(scope): summary of at most 90 characters [TASK-ID]

Optional body explaining what and why.

Task: ROB-MECH-007
```

**Header.** `type(scope): summary`. The type is one of `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `ci`, `chore`, `perf`, `revert`, `security`. The scope is lower case and free-form. The summary is at most 90 characters, starts with a lower-case verb in the imperative and has no trailing full stop. The trailing `[TASK-ID]` is optional and not enforced; if present it must be one of the footer IDs and cannot be used with `Tasks: None`.

**Scopes in use here (PROPOSED):** `mechanical` is the default scope for a robot-level change that fits no narrower area. Narrower scopes are `planning`, `governance`, `docs`, `repo`, `security`, `requirements`, `architecture`, `interface`, `calc`, `status`, `verification`, `ci`, and, only after the hold is reopened, `cad`, `drawings`, `bom`, `assembly`, `manufacturing` and `results`. A scope that names an actuator area (`actuator-s`, `actuator-m`, `actuator-l`, `actuator-embedded`, `actuator`) is used only for interface work that consumes that repository's data, as in `feat(actuator-m): ...`; the task ID is still one from this repository's register.

**Footer.** Exactly one line, `Task:` or `Tasks:`, with one or more comma-separated IDs, each upper-case segments joined by hyphens (`Tasks: ROB-MECH-007, ROB-MECH-008`). The ID must exist in [TASKS.md](TASKS.md) before the commit.

**No task.** A change that implements no task (a record correction, a docs-only change) is a `docs` or `chore` commit with `Tasks: None (reason)`. The reason is mandatory and no other type may use it. If a change belongs to no existing task, create the task in the register first; do not reuse an unrelated ID and do not invent one.

**Other trailers.** Ordinary Git metadata, `Co-Authored-By` and `Signed-off-by` are allowed. Never add an AI-session trailer or link (`Claude-Session:` or a session URL); the program's `commit-message-check` rejects them.

### Valid examples

```text
docs(planning): define ROB-A0 configuration and numeric targets

Record segments, degrees of freedom per joint and the source of every
numeric target.

Task: ROB-MECH-007
```

```text
feat(requirements): add mechanical requirements with program traces

Task: ROB-MECH-008
```

```text
docs(interface): add robot-to-actuator interface control v0.1

Cites the actuator repository commit for every value; placeholder values
are labelled.

Tasks: ROB-MECH-010, ROB-MECH-011
```

```text
test(verification): add known-answer check for load-case calculation

Task: ROB-MECH-009
```

```text
ci(repo): add secret-scan and commit-message-check workflows

Task: ROB-MECH-003
```

```text
docs(planning): correct a link in the milestone register

Tasks: None (record correction, no task implemented)
```

```text
test(mechanical): add frame dimensional sanity checks

Check required datums and configured dimensional limits.

Task: ROB-MECH-004
```

The last example has the shape of the program's own illustration (`test(mechanical): add frame dimensional sanity checks` with a `Task:` footer). The task ID in any real commit must be the one in [TASKS.md](TASKS.md) that the commit implements. Dimensional checks themselves are stage 2 checks in [SANITY_PLAN.md](../verification/SANITY_PLAN.md) and wait for the hold to be reopened; the example shows the format, not permitted work today.

### Invalid examples

| Message | Why it fails |
|---|---|
| `update docs` | No type, no scope, no footer |
| `docs(planning): fix typo` with no footer | Missing `Task:` footer |
| `feat(cad): add frame skeleton` with `Tasks: None (cleanup)` | `Tasks: None` is only for docs or chore commits; also CAD is blocked by the hold |
| `docs: add plan` with two footer lines | More than one task footer |
| `docs: add plan [ROB-MECH-007]` with `Task: ROB-MECH-008` | The subject ID is not one of the footer IDs |
| A message ending in `Claude-Session: ...` | AI-session trailers are rejected |
| `Task: rob-mech-007` | IDs are upper case |

## 5. Required sequence

Follow these steps for every change. Today the checks in steps 4 and 5 are only partly available (section 11).

1. **Pick the task.** Confirm it exists in [TASKS.md](TASKS.md), is not BLOCKED, and its dependencies are done. If it is BLOCKED by the hold, stop: do not do the work.
2. **Confirm the criteria.** Read the task's criteria in [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) and know what evidence is needed and of which type.
3. **Branch.** Create a branch from an up-to-date `main` (section 3).
4. **Implement.** One logical change at a time. Keep unrelated changes out.
5. **Check locally.** Run the checks that exist (section 11). A check that is NOT_IMPLEMENTED is reported as such.
6. **Update the records.** Update the task status in [TASKS.md](TASKS.md) honestly (IMPLEMENTED is not accepted), the criteria results only where evidence exists, and add a [CHANGELOG.md](CHANGELOG.md) entry if the plan itself changed.
7. **Commit.** Use the format in section 4, with the task footer. One logical change per commit.
8. **Push** the branch. Do not force-push a branch that others use.
9. **Open a pull request** using the template and the title style in section 6. Say what is pending and which checks ran.
10. **Wait for the automated checks** and fix failures; do not skip or silence them.
11. **Review.** The reviewer works through [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md) against the exact head commit and records the result. A new push after review makes earlier approvals stale.
12. **Merge** only after the required checks and approvals pass. The merge method is a merge commit (program decision D-053), so the commits that were checked are the commits recorded.
13. **Record the result.** After the merge, record the 40-character merge or implementation commit SHA on the task (Git state NOT_COMMITTED to COMMITTED, then SYNCED once pushed and recorded), and cite the CI run ID.
14. **Report status.** Regenerate `status/status.json` once it exists, check it, and let the program consolidate it. Do not edit generated reports by hand.
15. **Delete the branch.** Fast-forward the local `main`.

A cross-repository change continues in step 16.

16. **Cross-repository follow-up.** Program registration, source refresh and any baseline change happen in kritva-program through its own pull request and its approval process, never from this repository. If this repository is later pinned as a submodule of a parent repository, the parent pointer is advanced in a separate parent pull request after the child's change is merged and reviewed.

## 6. Pull requests

### Acceptance sequence

Every pull request goes through these stages in order. The program's report-only `pr-acceptance-gate` reports REJECT, NEEDS_HUMAN or APPROVE and approves nothing; it never bypasses the human review in stage 5, and a planning-only task never becomes accepted progress merely because a pull request merged.

| Stage | Name | What happens |
|---|---|---|
| 1 | Task authorisation | The task ID already exists on the pull request's base branch and is open for work (not BLOCKED, not CANCELLED) |
| 2 | Commit validation | Every commit has the Conventional Commit header and exactly one `Task:` or `Tasks:` footer; no AI-session trailer |
| 3 | Scope validation | The pull request updates the acceptance criteria, the task register and other protected records where the change requires it, and touches no hold-controlled or program-owned record without the required decision |
| 4 | Automated checks | Secret scan, commit-message check, documentation and README checks, sanity checks and the regression checks the change-impact table requires |
| 5 | Human review | The required Code Owner, independent mechanical, safety or actuator-owner approval, recorded against the exact head commit using [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md) |
| 6 | Merge and evidence | Merge only after the required checks and approvals pass; record the resulting commit, the CI run ID and the review as evidence |
| 7 | Submodule update | Where a parent repository pins this repository, its pointer is advanced in a separate parent pull request after this change is merged and reviewed |

### Pull request details

| Item | Rule |
|---|---|
| Title | The same `type(scope): summary` style as the commits |
| Template | `.github/PULL_REQUEST_TEMPLATE.md` (to be added by task ROB-MECH-002): summary, scope and exclusions, commits, task and test table, validation, what is pending, plus the program's branching headings; a heading that does not apply says "Not applicable" |
| Size | Small enough to review against the checklist in one sitting; split larger work by task |
| Draft | Open as draft until the checks pass and the description is complete |
| Evidence | Link the CI run IDs and the evidence files; use commit SHAs, never branch names |
| Hold | A pull request that touches a hold-controlled path (`cad/`, `bom/`, `drawings/`, `assembly/`, `releases/`, procurement files) cites the recorded owner decision reopening robot mechanical work, or is closed |

## 7. Required checks and approvals

| Requirement | Applies to | Enforced today? |
|---|---|---|
| `secret-scan` | Every push and pull request | No (task 003) |
| `commit-message-check` | Every pull request | No (task 003) |
| Sanity checks ([SANITY_PLAN.md](../verification/SANITY_PLAN.md)) | Every pull request | No (task 004) |
| Regression checks ([REGRESSION_PLAN.md](../verification/REGRESSION_PLAN.md)) | Per the change-impact table | No (task 004) |
| Code Owner review | Every pull request | No (no `CODEOWNERS`, task 002) |
| Independent mechanical review | Requirements, interfaces, calculations, design, manufacturing, test results, milestone closure | Not available (reviewer role unfilled, PD-007) |
| Safety review | Hazards, assembly, powered or loaded operation, physical test | Not available (reviewer role unfilled, PD-007) |
| Report-only program PR gate | kritva-program pull requests | Program tool; reports REJECT, NEEDS_HUMAN or APPROVE and approves nothing |

Approvals made before the head commit changed are stale and are not accepted. With a single owner who is also the author, GitHub does not count the author's own approval; the owner asks a second reviewer or uses the owner's merge bypass, and the review record says so. A passing gate or a passing check never replaces the required human approval.

## 8. CAD and binary design artifacts

Mechanical CAD is blocked by the hold, and no CAD or binary file is committed until the hold allows it and the convention from task ROB-MECH-019 is decided. When that happens:

- the review evidence records the revision identifier or checksum of each file;
- a successful merge is not design approval: the approval is the recorded design review against the commit;
- neutral exports are committed only if the convention says so, and a stale export is a check failure;
- large files follow the approved storage method, never ad hoc.

## 9. Tags and releases

- Release tags are annotated SemVer tags, `vMAJOR.MINOR.PATCH`. No tag is created for a program phase or for a milestone when nothing versionable shipped, and no `v0.<phase>.<n>` scheme is used.
- A tag is created only after the approved merge and the required checks, and its message names the completion record and the exact commit.
- A tag is evidence, not closure authority. A milestone closes only through an approved `COMPLETION_RECORD.md`.
- Robot hardware baselines (`ROB-A0` and so on) are recorded under `releases/` after release and are never edited afterwards.
- Nothing has been released and no tag policy has been formally adopted for this repository yet.

## 10. Prohibited

| Do not | Why |
|---|---|
| Push to `main` | Everything goes through review |
| Force-push a shared branch or rewrite shared history | Evidence and approvals refer to commit SHAs |
| Edit kritva-program baseline, approvals, gate closures or task weights from this repository | The program owns them; credit comes only from approved baseline tasks with passing evidence |
| Add a commit with no task footer, or reuse or invent a task ID | Traceability |
| Add an AI-session trailer or link to a commit or pull request | The program check rejects it |
| Merge with a failing required check, or add an allowlist entry to silence one | Checks exist to block |
| Edit generated files by hand | They are rebuilt from their inputs |
| Commit secrets, credentials, production data or personal data | Cannot be made safe afterwards |
| Commit CAD, BOM, procurement or fabrication content while the hold is open | Mechanical hold, decision D-003 |
| Describe a commit, merge or tag as acceptance | Acceptance is decided separately |

## 11. Commands

Every command here is a Git command or a program check. None of them exists in this repository's own tooling, because it has none yet.

| Command | Effect | Needs | Preview |
|---|---|---|---|
| `git switch -c rob-mech/NNN-short-name` | modify (local branch) | Local clone | None needed |
| `git commit` | modify (local history) | Local clone | `git status`, `git diff --staged` |
| `git push -u origin rob-mech/NNN-short-name` | modify (remote branch) | Push permission | `git push --dry-run` |
| `python3 ../kritva-program/scripts/security/check_commit_format.py --range origin/main..HEAD` | check (read only); requires a sibling clone of kritva-program | Local clone | Not needed |
| `python3 ../kritva-program/scripts/docs/check_readme.py README.md` | check (read only); requires a sibling clone of kritva-program | Local clone | Not needed |

Warning: `git push`, a pull request merge and a tag publish change shared state. Do them only as the sequence in section 5 allows, with the required approvals. `make` targets for sanity and regression are not implemented yet and will be added under task ROB-MECH-004.

## 12. Common rejections

| Symptom | Cause | Fix |
|---|---|---|
| `missing Task: footer` | Footer absent | Add exactly one `Task:` or `Tasks:` line, or `Tasks: None (reason)` on a docs or chore commit |
| `header must be type(scope): summary` | Wrong type, no colon or space, or a summary over 90 characters | Reword to the format |
| `more than one Task: footer` | Two footer lines | Merge them into one `Tasks:` line |
| `'Tasks: None' is only for docs or chore commits` | Wrong type | Change the type, or name a real task |
| Unknown task ID | The ID is not in the register | Create the task in `TASKS.md` first |
| Session trailer rejected | AI-session trailer present | Remove it; `Co-Authored-By` is allowed |
| `secret-scan` fails | A secret pattern was found | Do not allowlist; remove it, tell the Security Owner and rotate it |
| Review marked stale | A push changed the head after review | Ask for a fresh review of the new head |

## 13. Recording Git state on a task

| State | Meaning | Recorded where |
|---|---|---|
| NOT_COMMITTED | No commit for the task exists | [TASKS.md](TASKS.md) |
| COMMITTED | A commit exists locally or on a branch | [TASKS.md](TASKS.md) |
| SYNCED | The commit is pushed and its 40-character SHA is recorded on the task | [TASKS.md](TASKS.md), and the status report once it exists |

The SHA recorded is the implementation or merge commit, not a branch name. Where a later commit changes the evidence, a new reference is added; the old one is not overwritten.

## 14. Maintenance

Change this document by a pull request that states the reason and is recorded in [CHANGELOG.md](CHANGELOG.md). When the owner formally adopts the commit standard for this repository, or when the engineering contract is committed to kritva-program, update the status, the branch rule and section 1 accordingly. Where the program commit standard changes, this document follows it.
