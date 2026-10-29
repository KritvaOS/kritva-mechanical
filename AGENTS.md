# Kritva Mechanical Agent Instructions

These instructions apply to the `kritva-mechanical` repository: robot-level mechanical planning and, later, design for the Kritva robot. Actuator internals live in the actuator repositories; decisions, baseline, approvals and gates live in `kritva-program`. This file is PROPOSED until the owner adopts it, and it follows the kritva-program agent instructions where they overlap.

## Authority

- Dinesh (owner and Security Owner) decides. Advice from agents or other AI tools, including external reviews, is advisory only.
- `kritva-program` is the single authority for decisions, the baseline, approvals, gates and consolidated status. This repository reports facts; a report, a merge or a registration gives no credit.
- Planning documents here are working baselines. Material changes are recorded in `planning/CHANGELOG.md`, which is append only.

## What agents must not change without an owner decision

- Any file in `kritva-program`, including its baseline, approvals, gate records, workstream registry and source manifest. Proposals go in this repository (see `planning/REGISTRATION_PROPOSAL.md`); the owner makes the program change.
- The mechanical HOLD (program decision D-003). The actuator lift (D-052) covers the actuator workstreams only. Do not start or add CAD, BOM, quotes, procurement, fabrication, prototypes, physical tests or a design freeze for the robot. Tasks that need the hold lifted stay BLOCKED.
- Open safety gates, task IDs (never renumber or reuse), acceptance criteria IDs, and any recorded reference value or tolerance (a re-baseline needs a decision reference and a changelog entry).
- Governance files: `AGENTS.md`, `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE`, `.github/` (workflows, `CODEOWNERS`, the pull request template) and, once present, the `Makefile` and `scripts/`. Do not edit them to make a check pass.
- The generated `status/status.json`, once it exists. Regenerate it; never edit it by hand.

## Status semantics

- Execution, review, acceptance and git state are separate fields in `planning/TASKS.md`. IMPLEMENTED means a document or artefact exists and is not accepted. Do not mark a task COMPLETE without the review its acceptance criteria require.
- Mark values that come from another repository with their owner, revision and maturity. A preliminary value is never presented as verified.
- Claude and other agents cannot read GitHub rulesets or settings; do not record them as verified.

## Validation before a pull request

Today nothing is automated here. Until the `Makefile` exists (task ROB-MECH-004), check by hand and say so in the pull request:

- Every local link in the changed Markdown files resolves.
- Task IDs and acceptance criteria IDs are unique, and every task has criteria.
- `README.md` passes the program's `check_readme.py` when it changed.
- No secrets, credentials, personal data or production data are in the change.

When the `Makefile` is added, an unimplemented gate must exit with code 3 (`NOT_IMPLEMENTED`), never 0. Do not claim a check passed unless you ran it.

## Secrets and data

- Never commit credentials, tokens, private keys, production data or personal data. Use obviously fake values in examples and mark them as such.
- If a secret is committed by mistake, tell the Security Owner (Dinesh) at once. Removing it in a later commit does not make it safe; it must be revoked or rotated.
- The `secret-scan` workflow, once added, runs on every push and pull request. Do not add allowlist entries to silence it; propose them to the owner with the reason.

## Commits and pull requests

- Work on a branch and open a pull request. Do not push to `main`. Do not force-push shared branches or rewrite history without the owner's explicit approval.
- Commit format (program decision D-053): `type(scope): summary`, at most 90 characters, with exactly one `Task:` or `Tasks:` footer. `Tasks: None (reason)` is allowed only on docs or chore commits. See `planning/GIT_COMMIT_STEP.md`.
- Do not add `Claude-Session:` or session-URL trailers to commit messages or pull request descriptions. A `Co-Authored-By:` line is allowed.
- Merge method is a merge commit. With a single owner an author cannot self-approve; the owner merges.
- Pull requests use `.github/PULL_REQUEST_TEMPLATE.md`.

## When unsure

Say what you do not know and ask the owner. Do not invent evidence, test results, hardware behaviour, material or load values, or approvals.
