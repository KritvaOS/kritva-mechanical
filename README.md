# kritva-mechanical

> Robot-level mechanical design, planning and verification for KritvaOS: frame, torso, arms, hands, legs, feet and the assemblies that join them to the existing Kritva actuators.

| Property | Value |
|---|---|
| Project | KritvaOS |
| Repository | `KritvaOS/kritva-mechanical` |
| Repository Type | Mechanical |
| Visibility Class | Not yet decided (no visibility decision recorded for this repository) |
| GitHub Setting | UNVERIFIED (not read; agents cannot read GitHub settings) |
| Lifecycle Status | PLANNING |
| Repository Owner | Dinesh (program owner) |
| Security Owner | Dinesh (program Security Owner, kritva-program D-032); hardware safety gates apply, see section 13 |
| Architecture | Not yet defined |
| Milestones | [planning/MILESTONE.md](planning/MILESTONE.md) (PROPOSED, working planning baseline) |
| Tasks | [planning/TASKS.md](planning/TASKS.md) (PROPOSED, `ROB-MECH` prefix unregistered) |
| Acceptance Criteria | [planning/ACCEPTANCE_CRITERIA.md](planning/ACCEPTANCE_CRITERIA.md) (PROPOSED, version 0.1.0) |
| Status Reporting | Not yet defined (no `status/status.json`; workstream not registered in kritva-program) |
| License | [LICENSE](LICENSE) (Apache License 2.0) |

**Current state in one line:** this repository contains planning documents only. No CAD, drawing, BOM, calculation, fixture, firmware or physical hardware exists here, and nothing in it authorises procurement, fabrication, assembly or physical testing.

## 1. Purpose and Scope

`kritva-mechanical` owns the mechanical design of the complete Kritva robot above the actuator level:

- the robot frame and structural assemblies, torso, arms, hands, legs and feet;
- robot-level CAD, drawings, bill of materials, mass properties and load cases;
- the robot-side mounting interfaces for actuators, including clearances, routing and service access;
- assembly, inspection and mechanical verification procedures for robot-level hardware;
- the mechanical planning set: milestones, tasks, acceptance criteria, sanity and regression plans, review checklist and commit procedure.

It does **not** own:

- actuator designs. Those stay in `kritva-actuator` (shared requirements, interfaces, integration), `kritva-actuator-s`, `kritva-actuator-m` and `kritva-actuator-l` (variant mechanics) and `kritva-actuator-embedded` (electronics and firmware);
- program governance: decisions, the approved task baseline, task weights, the approval ledger, gates and consolidated status. Those belong to `kritva-program`;
- electrical power distribution, compute, sensing or software. No separate repository exists for them yet, and this repository does not absorb them.

Responsibilities may be split into further repositories later if independent teams, release cycles or access rules justify it. Until then the aim is the smallest number of repositories that keeps ownership clear.

## 2. Position in the KritvaOS Ecosystem

```text
kritva-program            governance, baseline, gates, consolidated status
      ^   status facts (schema 2.0)            | approvals, task IDs, weights
      |                                         v
kritva-mechanical  <--- interface contracts --->  kritva-actuator (parent)
 (robot structure)                                  |- kritva-actuator-s / -m / -l  (variant mechanics)
                                                    '- kritva-actuator-embedded     (electronics, firmware)
```

This repository consumes actuator geometry, mass, load and operating-limit data from the actuator repositories and produces the robot-side mounting and structure that carries them. It reports implementation facts to [kritva-program](https://github.com/KritvaOS/kritva-program), which decides what counts as accepted progress. In kritva-program the relevant workstream is `MECHANICAL` (currently with no repository registered and `hold: true`); the five actuator workstreams `ACT_INT`, `ACT_EMB`, `ACT_S`, `ACT_M` and `ACT_L` roll up to it or to related workstreams.

Naming used in this repository, kept apart on purpose:

| Name | Owner | Meaning |
|---|---|---|
| P0 to P8 | kritva-program | Frozen program phases. This repository never redefines them. |
| A0, A1, A2 | kritva-actuator | The actuator family's own milestone lifecycle. Not robot hardware versions. |
| ROB-A0, ROB-A1 and so on | this repository (PROPOSED) | Robot hardware baselines: a named, frozen robot configuration. |
| ROB-M0 to ROB-M5 | this repository (PROPOSED) | Robot mechanical milestones, accepted as working planning baselines and adjustable as work proceeds. |

The `ROB-` namespace is PROPOSED. It needs registration with kritva-program before any task using it can earn program credit.

## 3. Architecture

Not yet defined. No robot-level architecture document exists. The first architecture work (frame, torso, limb and joint layout, interface definitions and mass budget) is planned under milestone ROB-M1 and is not started. A skeleton or sketch will be linked here with its status when it exists, and will not be described as an approved architecture.

## 4. Documents to Read First

| Document | Label, status | What it answers |
|---|---|---|
| [LICENSE](LICENSE) | AUTHORITATIVE for licensing; status: in place | Under what terms the content may be used |
| [planning/MILESTONE.md](planning/MILESTONE.md) | AUTHORITATIVE for milestone definitions (role); status: PROPOSED | What the robot mechanical milestones are and how they may change |
| [planning/TASKS.md](planning/TASKS.md) | AUTHORITATIVE for local task records (role); status: PROPOSED | Which tasks exist, in what order, with which dependencies |
| [planning/ACCEPTANCE_CRITERIA.md](planning/ACCEPTANCE_CRITERIA.md) | AUTHORITATIVE for acceptance criteria (role); status: PROPOSED | What measurable evidence makes a task or milestone acceptable |
| [verification/SANITY_PLAN.md](verification/SANITY_PLAN.md) | AUTHORITATIVE for fast checks (role); status: PROPOSED, nothing implemented | Which fast checks run on every pull request |
| [verification/REGRESSION_PLAN.md](verification/REGRESSION_PLAN.md) | AUTHORITATIVE for regression checks (role); status: PROPOSED, nothing implemented | Which checks protect accepted designs from regressions |
| [planning/REGISTRATION_PROPOSAL.md](planning/REGISTRATION_PROPOSAL.md) | PROPOSAL; status: PROPOSED, owner decision pending | How this repository would be registered in kritva-program |
| [planning/REVIEW_CHECKLIST.md](planning/REVIEW_CHECKLIST.md) | AUTHORITATIVE for review (role); status: PROPOSED | What a reviewer checks before approving |
| [planning/GIT_COMMIT_STEP.md](planning/GIT_COMMIT_STEP.md) | AUTHORITATIVE for branch and commit sequence once adopted; status: PROPOSED | The branch, commit and pull request sequence |
| [planning/CHANGELOG.md](planning/CHANGELOG.md) | EVIDENCE, append only; status: PROPOSED | How the plan itself has changed and why |
| [reviews/2026-10-28-external-review-chatgpt.md](reviews/2026-10-28-external-review-chatgpt.md) | EVIDENCE of an advisory external review; status: DRAFT, dispositions pending | What the external reviewer found and how each finding maps to the plan |
| [Program acceptance standard](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/ACCEPTANCE_STANDARD.md) | PROPOSED standard in kritva-program (current link; the program record controls) | Task definition of done, test gates, commit format, tags, required files |
| [Program agent instructions](https://github.com/KritvaOS/kritva-program/blob/main/AGENTS.md) | AUTHORITATIVE for kritva-program agents (current link) | What agents must not change without an owner decision |

All of these documents are drafts written on 2026-10-28 and none has been reviewed yet. The roles shown are intended roles, not approvals.

## 5. Repository Structure and File Responsibilities

The files named in the first four rows exist today (the planning and verification folders hold the drafts listed in section 4). Every other path is a target layout; a folder is created only when it holds a real file, so none is scaffolded in advance.

| Path | Responsibility | Label, status | Edit by hand? |
|---|---|---|---|
| `README.md` | Navigation page for this repository | REFERENCE; status: DRAFT | Yes |
| `LICENSE` | Apache License 2.0 text | AUTHORITATIVE; in place | No |
| [AGENTS.md](AGENTS.md) | Instructions for agents: authority, hold, what not to change, validation, commit rules | AUTHORITATIVE for agents once adopted; IMPLEMENTED as a draft (PROPOSED) | Yes, owner decision for changes |
| [SECURITY.md](SECURITY.md) | Private reporting route for vulnerabilities and safety concerns | AUTHORITATIVE once the owner confirms the route; IMPLEMENTED as a draft (PROPOSED) | Yes, owner decision |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to pick a task, change, check and submit | REFERENCE; IMPLEMENTED as a draft (PROPOSED) | Yes |
| [.github/CODEOWNERS](.github/CODEOWNERS) | Code owner for every path | AUTHORITATIVE once adopted (login confirmed by the owner); IMPLEMENTED as a draft (PROPOSED); not verified as enforced | Yes, owner decision |
| [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) | Pull request checklist | INPUT; IMPLEMENTED as a draft (PROPOSED) | Yes |
| [planning/](planning/) | Milestones, task register, acceptance criteria, review checklist, commit procedure, changelog. Layout follows the ChatGPT planning session; the program standard places `ACCEPTANCE_CRITERIA.md` at the repository root, a deviation the owner chose on 2026-10-28 and recorded in the changelog | MIXED; IMPLEMENTED as drafts (PROPOSED) | Yes |
| [verification/](verification/) | Sanity plan and regression plan (plans only; no check is implemented). Later test procedures | MIXED; plans IMPLEMENTED as drafts (PROPOSED), checks NOT YET IMPLEMENTED | Yes |
| [reviews/](reviews/) | Recorded external and independent reviews with finding dispositions | EVIDENCE; IMPLEMENTED (one advisory review recorded) | Append only |
| `requirements/` | Robot-level mechanical requirements and load cases | AUTHORITATIVE once approved; NOT YET IMPLEMENTED | Yes |
| `architecture/` | Frame, torso, limb and joint architecture, interface control | AUTHORITATIVE once approved; NOT YET IMPLEMENTED | Yes |
| `cad/` | Native CAD sources and neutral exports | INPUT; NOT YET IMPLEMENTED, on hold (section 13) | Via CAD tool |
| `drawings/` | Released drawings | EVIDENCE once released; NOT YET IMPLEMENTED | Append only |
| `bom/` | Bill of materials | INPUT; NOT YET IMPLEMENTED, on hold (section 13) | Yes |
| `assembly/` | Assembly and inspection procedures | AUTHORITATIVE once approved; NOT YET IMPLEMENTED | Yes |
| `results/` | Immutable, revision-specific verification evidence | EVIDENCE; NOT YET IMPLEMENTED | Append only |
| `status/` | `status.json` generated from the task register | GENERATED; NOT YET IMPLEMENTED | No |
| [scripts/security/](scripts/security/) | Vendored program commit-format checker with its [provenance](scripts/security/PROVENANCE.md) | INPUT; IMPLEMENTED as a draft (PROPOSED); not yet run in CI | Only by re-copying from kritva-program |
| [tests/](tests/) | Unit tests for the commit-format checker | INPUT; IMPLEMENTED as a draft (PROPOSED); run locally only | Yes |
| [.github/workflows/](.github/workflows/) | `secret-scan` and `commit-message-check` workflows | INPUT; IMPLEMENTED as drafts (PROPOSED); no CI run recorded yet | Yes, owner decision |
| [.gitleaks.toml](.gitleaks.toml) | Secret-scan configuration, no allowlist | INPUT; IMPLEMENTED as a draft (PROPOSED) | Yes, owner decision |
| `Makefile`, other `scripts/` | Gate targets and generators | INPUT; NOT YET IMPLEMENTED | Yes |
| `releases/` | Immutable released hardware configurations | EVIDENCE; NOT YET IMPLEMENTED | Append only |

Required program files not yet present: `Makefile`. The `secret-scan` and `commit-message-check` workflows exist as drafts that have not yet run. The governance files `AGENTS.md`, `SECURITY.md`, `CONTRIBUTING.md`, `.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md` exist as unreviewed drafts, and nothing shows that `CODEOWNERS` is enforced on GitHub (program acceptance standard section 7).

## 6. Toolchain, Getting Started and Development Workflow

No toolchain is defined and no command exists in this repository. There is no Makefile, script or CI workflow, so none is advertised here.

| Tool | Purpose | Version | Check |
|---|---|---|---|
| Git | Version control | Not yet defined | `git --version` |
| CAD system | Robot-level modelling | Not yet defined (to be chosen under ROB-M1) | Not yet defined |

| Command | Effect | Needs | Preview |
|---|---|---|---|
| `python3 ../kritva-program/scripts/docs/check_readme.py README.md` | check (read only); requires a sibling clone of kritva-program | Local clone only | Not needed |

The program's standard make targets (`make check`, `make lint`, `make test-unit`, `make test-integration`, `make test-regression`, `make test`, `make docs-check`, `make acceptance`) are not implemented here. When they are added, an unimplemented target must exit non-zero with `NOT_IMPLEMENTED`; it is never reported as a pass.

Working practice today: edit Markdown on a branch, run the README check above, and open a pull request. Do not commit CAD or binary design files until the hold in section 13 allows it and a storage and revision convention is approved.

## 7. Dependencies and Interfaces

| Dependency | Direction | Kind | Contract | State |
|---|---|---|---|---|
| `kritva-program` | upstream | governance | Status schema 2.0, task IDs, baseline, gates, commit standard | ESTABLISHED for the program; this repository is not yet registered, so UNVERIFIED here |
| `kritva-actuator` | upstream | design | Actuator mounting interface, dimensions, loads, mass properties, operating limits | PLANNED (no robot-side interface document exists) |
| `kritva-actuator-s`, `-m`, `-l` | upstream | design | Variant geometry, sizing results and mounting datums | PLANNED; sizing inputs in those repositories are reported by an external audit as still preliminary (not verified here) |
| `kritva-actuator-embedded` | upstream | design | Controller and board envelope, connectors, wiring routes | PLANNED |
| Electrical, power and compute design | upstream | design | Harness routing, battery and compute envelopes | UNVERIFIED (no owning repository identified) |

No interface here is versioned or approved. The first deliverable of the interface work is a robot-to-actuator interface control document, planned under ROB-M0 and ROB-M1.

## 8. Roadmap

| Item | Document | Status and meaning of dates |
|---|---|---|
| Roadmap | Not yet defined | No dates exist. Any date added later is labelled PROPOSED until the owner approves it. |
| Milestones | [planning/MILESTONE.md](planning/MILESTONE.md) (PROPOSED) | Working sequence ROB-M0 Requirements, ROB-M1 Architecture, ROB-M2 Detailed design, ROB-M3 Fabrication readiness, ROB-M4 Assembly and inspection, ROB-M5 Mechanical verification. Accepted as planning baselines by the owner (2026-10-28 working session); adjustable. Not program baseline entries. |

Accepting a milestone for planning does not mean its tasks are done, its evidence exists, or any gate has passed.

## 9. Tasks and Acceptance Criteria

Tasks live in a single canonical register, [planning/TASKS.md](planning/TASKS.md), with one stable ID each (`ROB-MECH-001` to `ROB-MECH-042` are drafted). The proposed ID family is `ROB-MECH-NNN`, which needs approval and registration in kritva-program before it earns credit. Existing actuator task IDs (`ACT-INT`, `ACT-EMB`, `ACT-S`, `ACT-M`, `ACT-L`) are preserved and are not renumbered or reused here.

Acceptance criteria live in [planning/ACCEPTANCE_CRITERIA.md](planning/ACCEPTANCE_CRITERIA.md), written to the program template. Work is not accepted because a file exists, a commit was made, a pull request merged or a local test passed. A task is done only when it meets the program definition of done: stable ID, testable criteria, merged through the required review, required checks passed on the exact closing commit, reviews recorded against that commit, documentation updated and evidence pointing at immutable references.

## 10. Status Reporting and Program Integration

Four things are kept apart and never merged into one flag or percentage:

- **Execution:** what this repository reports about its own implementation state.
- **Evidence:** the exact commit, result and scope behind each claim.
- **Acceptance:** decided by the program's acceptance authority, not by this repository's report.
- **Release readiness:** the result of the applicable gates.

Planned mechanism: `status/status.json` (schema 2.0), generated from the task register and validated in CI, registered as a source in kritva-program, then consolidated there. Today none of this exists: there is no status file, the repository is not registered, and the `MECHANICAL` workstream in kritva-program has no repository. Until registered, this repository's progress is UNVERIFIED in the program view, which is the accurate state.

This repository sends facts only. It never claims program approval or credit, never edits the program baseline or task weights, and does not add hardware-version or phase fields to the status file unless the approved schema allows them. Progress percentages and task counts are not written in this README; see the program's generated status view.

## 11. Build, Test, Regression and Validation

| Check | Command | Effect | Runs in CI? | Expected |
|---|---|---|---|---|
| README structure | `python3 ../kritva-program/scripts/docs/check_readme.py README.md` | check | no | PASS means structure only; not accuracy |
| Sanity checks | Not yet defined | n/a | no | NOT YET IMPLEMENTED |
| Regression checks | Not yet defined | n/a | no | NOT YET IMPLEMENTED |

Plans are drafted in [verification/SANITY_PLAN.md](verification/SANITY_PLAN.md) and [verification/REGRESSION_PLAN.md](verification/REGRESSION_PLAN.md) (PROPOSED). A check that is not implemented is listed as not implemented, never as passing. Software checks, calculations and simulation never stand in for physical verification.

## 12. Git Workflow and Review

No commit or pull request rule is verified as enforced in this repository yet: the `secret-scan` and `commit-message-check` workflows and `CODEOWNERS` exist as drafts with no recorded CI run, and nobody has verified branch protection or required checks.

Proposed convention, to be adopted formally through the owner and recorded in [planning/GIT_COMMIT_STEP.md](planning/GIT_COMMIT_STEP.md): the kritva-program commit standard (decision D-053; see section 4 of the program acceptance standard). In short, `type(scope): summary` with exactly one `Task:` or `Tasks:` footer, or `Tasks: None (reason)` on a docs or chore commit that implements no task; work on a branch and open a pull request; merge with a merge commit; never push to `main`; no AI-session trailers or links in commit messages or pull request text. Until adopted, this is advisory reference, not a second mandatory format.

## 13. Safety and Security

Software checks, analytical calculations and simulation validate only the stated model, inputs and software properties. They do not prove physical safety, component suitability, design acceptance or readiness for human use.

Open-gate summary (a summary of what this repository must respect, not the gate authority; the controlling records are in kritva-program):

| Gate | Controls | Authority and status | Evidence needed to close | Prohibited while open |
|---|---|---|---|---|
| Mechanical HOLD (D-003) | Mechanical CAD, actuators, BOM, quotes, procurement, fabrication, prototype, design freeze | kritva-program decision, Accepted. Lifted by D-052 only for `ACT_S`, `ACT_M`, `ACT_L`, `ACT_EMB`, `ACT_INT`; the `MECHANICAL` workstream still carries `hold: true` | An owner decision reopening robot mechanical work | CAD, BOM, quotes, procurement, fabrication, assembly and prototype work for the robot scope |
| P6 LAB & ROBOT entry | Entry to the lab and robot phase | kritva-program gate register; requires an explicit decision reopening mechanical work | The reopening decision and the P6 criteria, still pending | Treating any planning acceptance as entry to P6 |
| Actuator release gates (A, B, C) | Actuator design release, bench validation, safety and release acceptance | Owned by `kritva-actuator`; state not verified here (an external audit reports none passed) | Per the actuator repository's own records | Using actuator results as robot-level evidence |

Lifting a hold or passing one gate does not approve a design, waive another gate or authorise physical operation. Closing a child-repository input does not close a parent gate. Planning-document work in this repository is not CAD, BOM, procurement, fabrication or prototype work, and is treated as permitted under the hold; if the owner reads the hold differently, this section is corrected.

Evidence is stated by type: software test, calculation, simulation, bench measurement or independently accepted physical test. Each statement names the tested revision, procedure, result and scope. Software and model evidence is never offered as physical test evidence. Required human safety reviews stay mandatory for safety-gated work.

Security: [SECURITY.md](SECURITY.md) is a draft; the owner must confirm the vulnerability-reporting route. Never post details of an unfixed vulnerability in a public issue or pull request. Never commit credentials, tokens, keys, production or personal data.

## 14. Release and Versioning

Nothing is released. Planned: annotated SemVer tags (`vMAJOR.MINOR.PATCH`) created only after an approved merge and required checks, with the tag message naming the completion record and exact commit; a milestone closes only through an approved `COMPLETION_RECORD.md`, never through a merge, a passing run or a tag. Robot hardware baselines (`ROB-A0` and so on) are immutable configurations recorded under `releases/` once released. Document versions and release versions are separate. Known limitations: no release process, tag policy or completion record exists yet for this repository.

## 15. Ownership and Escalation

Repository and security owner: Dinesh. Code ownership is drafted in [.github/CODEOWNERS](.github/CODEOWNERS) (owner login confirmed by the owner; enforcement not verified). With a single owner, a pull request author cannot self-approve under the program's usual ruleset; the program's approach is that the owner merges using the bypass or a second reviewer is added. Raise a blocker by opening an issue or commenting on the pull request and naming the owner. Do not invent evidence, test results, hardware behaviour or approvals, and do not claim a check passed unless it was run.

## 16. Related Repositories and References

- [kritva-program](https://github.com/KritvaOS/kritva-program): plan, baseline, decisions, gates and consolidated status.
- [kritva-actuator](https://github.com/KritvaOS/kritva-actuator): parent actuator repository, with `kritva-actuator-s`, `kritva-actuator-m`, `kritva-actuator-l` and `kritva-actuator-embedded` as children.
- [kritva-core](https://github.com/KritvaOS/kritva-core) and [kritvaos-community](https://github.com/KritvaOS/kritvaos-community): software repositories this robot will eventually run.

## 17. License

Apache License 2.0. See [LICENSE](LICENSE).
