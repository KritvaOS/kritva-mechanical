# Kritva Pro Skills

**Private repository. Confidential. Do not share, fork, or copy content into public repositories.**

This repository contains Kritva's premium Claude skills, plugins, and supporting material. It is the authoring workspace for premium knowledge and the private plugin marketplace that licensed customers install from.

> **Status:** Initial development. Structure, manifests, and release workflows may change.
> Claude plugin and marketplace manifest formats may change over time. Verify against
> the current official documentation (https://docs.claude.com) before building release tooling around them.

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How This Repo Relates to the Public Project](#2-how-this-repo-relates-to-the-public-project)
3. [Repository Structure](#3-repository-structure)
4. [Local Workspace Setup](#4-local-workspace-setup)
5. [Authoring Skills](#5-authoring-skills)
6. [Tracking Component Compatibility](#6-tracking-component-compatibility)
7. [Building Plugins](#7-building-plugins)
8. [Testing and Evals](#8-testing-and-evals)
9. [Workflow: Responding to Upstream Changes](#9-workflow-responding-to-upstream-changes)
10. [Branching, Commits, and Pull Requests](#10-branching-commits-and-pull-requests)
11. [Releases and Versioning](#11-releases-and-versioning)
12. [Customer Access and Distribution](#12-customer-access-and-distribution)
13. [Working with Claude Code](#13-working-with-claude-code)
14. [Security and Confidentiality](#14-security-and-confidentiality)
15. [Decision Records](#15-decision-records)

---

## 1. Purpose and Scope

### What lives here

- Premium skills that go beyond the free `kritva-dev` skill in the public repo
- Claude Code plugins bundling skills, slash commands, agents, and MCP configuration
- The private plugin marketplace manifest
- Evals that verify premium skill quality
- Build and release tooling
- Internal ADRs for the pro product

### What does NOT live here

| Content | Where it belongs |
|---|---|
| Public architecture, interfaces, free skill | `kritvaos-community` and component repos (public) |
| Hosted MCP server code, billing, license keys | `kritva-cloud` (private) |
| Hardware designs, FPGA work, tuned parameters | `kritva-hardware` (private) |
| Pricing, customers, contracts, partner details | `kritva-business` (private) |
| Secrets and credentials | Secrets manager only. Never in any repo |

### Value principle

Skills are text and can be copied once a customer has them. Skills here should **teach Claude how to use Kritva and the hosted Kritva services well**. The hardest-to-copy value stays in hosted services (`kritva-cloud`).

---

## 2. How This Repo Relates to the Public Project

This repo **mirrors** the public component structure but **does not contain** the public repositories.

```text
Public (open source)                 Private (this repo)
─────────────────────                ─────────────────────────────
kritvaos-community   ──────────────▶ cross-component/
kritva-core          ──────────────▶ components/kritva-core/
kritva-motion        ──────────────▶ components/kritva-motion/
kritva-sense         ──────────────▶ components/kritva-sense/
kritva-skill         ──────────────▶ components/kritva-skill/
kritva-mind          ──────────────▶ components/kritva-mind/
```

### Rules

1. **Public repos are read-only from this repo's perspective.** Read their source and docs; never modify them from a pro-skills session.
2. **This repo is never added as a submodule of any public repo.**
3. **No submodules here by default.** Public repos are cloned beside this one (see [Section 4](#4-local-workspace-setup)). If a future ADR introduces submodules, it must document the reasons.
4. **Private content never flows into public repos.** If something here should become public, it is moved deliberately through a reviewed pull request in the public repo, with an ADR noting the decision.

---

## 3. Repository Structure

```text
kritva-pro-skills/
├── README.md                          # This file
├── CLAUDE.md                          # Rules for Claude Code in this repo
├── CHANGELOG.md                       # Customer-facing version history
├── LICENSE-COMMERCIAL.md              # Commercial license terms
├── compatibility.json                 # Skill ↔ component version mapping
├── .gitignore
│
├── .claude-plugin/
│   └── marketplace.json               # Private marketplace manifest
│
├── components/                        # AUTHORING: premium knowledge per component
│   ├── kritva-core/
│   │   ├── COMPONENT.md               # Summary, public repo link, supported versions
│   │   ├── skills/
│   │   │   ├── core-scheduler-tuning/
│   │   │   │   ├── SKILL.md
│   │   │   │   ├── reference/
│   │   │   │   └── scripts/
│   │   │   └── core-runtime-debugging/
│   │   │       └── SKILL.md
│   │   └── reference/                 # Shared private notes on Core internals
│   ├── kritva-motion/
│   │   ├── COMPONENT.md
│   │   └── skills/
│   │       └── motion-controller-tuning/SKILL.md
│   ├── kritva-sense/
│   │   ├── COMPONENT.md
│   │   └── skills/
│   │       └── sense-pipeline-optimization/SKILL.md
│   ├── kritva-skill/
│   └── kritva-mind/
│
├── cross-component/                   # AUTHORING: skills spanning several components
│   ├── skills/
│   │   ├── kritva-safety-review/
│   │   │   ├── SKILL.md
│   │   │   └── checklists/
│   │   └── kritva-system-integration/
│   │       └── SKILL.md
│   ├── commands/                      # Slash command sources
│   └── agents/                        # Subagent sources
│
├── plugin-definitions/                # Which skills go into which plugin
│   ├── kritva-pro-dev.json
│   ├── kritva-hardware-profiles.json
│   └── kritva-enterprise.json
│
├── plugins/                           # BUILD OUTPUT: what customers install
│   ├── kritva-pro-dev/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── skills/
│   │   ├── commands/
│   │   ├── agents/
│   │   └── .mcp.json                  # Points to hosted Kritva MCP server
│   ├── kritva-hardware-profiles/
│   └── kritva-enterprise/
│
├── tests/
│   ├── evals/                         # Test prompts + expected behavior, per skill
│   │   ├── core-scheduler-tuning/
│   │   │   ├── cases.yaml
│   │   │   └── README.md
│   │   └── kritva-safety-review/
│   └── fixtures/                      # Sample configs, logs, code for evals
│
├── docs/
│   ├── authoring-guide.md             # Skill writing standards
│   ├── release-checklist.md
│   ├── tiers.md                       # Which plugin maps to which offering
│   └── decisions/                     # Internal ADRs for the pro product
│
└── scripts/
    ├── validate.sh                    # Validate manifests and SKILL.md frontmatter
    ├── build-plugins.sh               # Assemble plugins/ from sources
    ├── check-compatibility.sh         # Flag skills affected by upstream changes
    └── release.sh                     # Version bump, changelog, tag
```

### Authoring vs. build output

| Folder | Role | Edited by hand? |
|---|---|---|
| `components/`, `cross-component/` | Source of truth for all premium content | **Yes** |
| `plugin-definitions/` | Maps sources to plugins | **Yes** |
| `plugins/` | Assembled output customers install | **No.** Regenerated by `build-plugins.sh` |

Never edit files in `plugins/` directly. Changes will be overwritten on the next build.

---

## 4. Local Workspace Setup

Clone public and private repos **side by side** in one parent folder:

```text
~/kritva/
├── kritvaos-community/     (public, with submodules)
├── kritva-pro-skills/      (private, this repo)
├── kritva-cloud/           (private)
└── kritva-hardware/        (private)
```

```bash
mkdir -p ~/kritva && cd ~/kritva
git clone --recurse-submodules https://github.com/KritvaOS/kritvaos-community.git
git clone git@github.com:KritvaOS/kritva-pro-skills.git
```

Public component source is then available at:

```text
../kritvaos-community/kritva-core
../kritvaos-community/kritva-motion
...
```

Keep the public checkout up to date before authoring:

```bash
cd ~/kritva/kritvaos-community
git pull && git submodule update --init --recursive
```

---

## 5. Authoring Skills

### Where a new skill goes

| Skill is about… | Location |
|---|---|
| One component only | `components/<component>/skills/<skill-name>/` |
| Several components, safety, or system integration | `cross-component/skills/<skill-name>/` |

### Skill folder layout

```text
<skill-name>/
├── SKILL.md         # Short, focused instructions (required)
├── reference/       # Deep-dive docs Claude loads only when needed
├── templates/       # Starter files, config examples
├── scripts/         # Helper scripts the skill can run
└── checklists/      # Review checklists
```

### `SKILL.md` template

```markdown
---
name: core-scheduler-tuning
description: Use when tuning Kritva Core scheduling, diagnosing latency or
  jitter, configuring task priorities, or reviewing real-time performance
  of Kritva Core v0.3 and later.
---

# Kritva Core Scheduler Tuning

## When to use
...

## Workflow
1. ...
2. ...

## Safety boundaries
- Recommendations are for development and testing. Never suggest placing
  AI tooling inside the real-time control loop.
- Changes to timing parameters must be validated on target hardware.

## Reference files
- `reference/scheduler-internals.md` — read when diagnosing priority inversion
- `scripts/analyze_latency.py` — run on exported trace logs
```

### Authoring standards

1. **`description` drives activation.** Write it as "Use when…" with the words developers actually type.
2. **Keep `SKILL.md` short.** Move depth into `reference/` and point to it.
3. **State the component versions** the skill applies to.
4. **Include safety boundaries** in every skill touching Core, Motion, or hardware.
5. **Every skill has evals** in `tests/evals/<skill-name>/` before release.
6. **Register the skill** in `compatibility.json` and at least one `plugin-definitions/*.json`.

Full standards: [`docs/authoring-guide.md`](docs/authoring-guide.md).

### `COMPONENT.md` template

```markdown
# kritva-core (Pro)

- **Public repo:** https://github.com/KritvaOS/kritva-core
- **Local source:** ../kritvaos-community/kritva-core
- **Supported versions:** v0.3.x
- **Premium skills:** core-scheduler-tuning, core-runtime-debugging
- **Maintainer:** <name>

## Notes
Private context about this component that skills draw on.
```

---

## 6. Tracking Component Compatibility

`compatibility.json` links every premium skill to the public component versions it was written and tested against.

```json
{
  "kritva-core": {
    "repo": "https://github.com/KritvaOS/kritva-core",
    "tested_versions": ["v0.3.x"],
    "last_reviewed": "2026-10-05",
    "skills": ["core-scheduler-tuning", "core-runtime-debugging"]
  },
  "kritva-motion": {
    "repo": "https://github.com/KritvaOS/kritva-motion",
    "tested_versions": ["v0.2.x"],
    "last_reviewed": "2026-10-05",
    "skills": ["motion-controller-tuning"]
  },
  "cross-component": {
    "requires": {
      "kritva-core": "v0.3.x",
      "kritva-motion": "v0.2.x"
    },
    "skills": ["kritva-safety-review", "kritva-system-integration"]
  }
}
```

### Rules

- Every skill appears in exactly one entry.
- `tested_versions` is updated **only after evals pass** against that version.
- `scripts/check-compatibility.sh` compares `tested_versions` with the latest public release tags and lists skills needing review.

---

## 7. Building Plugins

### Plugin definitions

Each file in `plugin-definitions/` lists what goes into one plugin:

```json
{
  "name": "kritva-pro-dev",
  "version": "0.1.0",
  "description": "Advanced Kritva development, performance tuning, and safety review",
  "skills": [
    "components/kritva-core/skills/core-scheduler-tuning",
    "components/kritva-core/skills/core-runtime-debugging",
    "components/kritva-motion/skills/motion-controller-tuning",
    "cross-component/skills/kritva-safety-review"
  ],
  "commands": [
    "cross-component/commands/kritva-perf-audit.md",
    "cross-component/commands/kritva-safety-check.md"
  ],
  "agents": [
    "cross-component/agents/kritva-reviewer.md"
  ],
  "mcp": true
}
```

### Build

```bash
./scripts/validate.sh        # Check frontmatter, manifests, references
./scripts/build-plugins.sh   # Regenerate plugins/ from definitions
```

The build script:

1. Clears each `plugins/<name>/` folder.
2. Copies listed skills, commands, and agents.
3. Writes `.claude-plugin/plugin.json` with name, version, and description.
4. Adds `.mcp.json` when `"mcp": true`.
5. Updates `.claude-plugin/marketplace.json`.

### Marketplace manifest (generated)

```json
{
  "name": "kritva-pro",
  "owner": { "name": "KritvaOS" },
  "plugins": [
    {
      "name": "kritva-pro-dev",
      "source": "./plugins/kritva-pro-dev",
      "description": "Advanced Kritva development, performance tuning, and safety review"
    },
    {
      "name": "kritva-hardware-profiles",
      "source": "./plugins/kritva-hardware-profiles",
      "description": "Certified hardware and FPGA integration guidance"
    }
  ]
}
```

### MCP configuration

`.mcp.json` in a plugin points to the hosted Kritva MCP server. It must **never** contain an API key. Customers supply their own license key through an environment variable, for example `KRITVA_API_KEY`.

---

## 8. Testing and Evals

Customers pay for consistent results. Every skill has evals.

### Eval case format (`tests/evals/<skill>/cases.yaml`)

```yaml
skill: core-scheduler-tuning
component_version: v0.3.x
cases:
  - id: latency-spike-diagnosis
    prompt: >
      My Kritva Core control task shows periodic 4 ms latency spikes.
      Here is the trace log. What is causing it?
    fixtures:
      - fixtures/core/trace-latency-spike.log
    must_include:
      - identifies priority inversion or blocking as a likely cause
      - recommends validating changes on target hardware
    must_not_include:
      - suggests running an LLM inside the control loop
```

### When to run evals

- Before every release
- After editing any skill
- After a new public component release (see [Section 9](#9-workflow-responding-to-upstream-changes))
- After a new Claude model becomes available

Record results in the pull request description.

---

## 9. Workflow: Responding to Upstream Changes

When a public component releases a new version (for example, `kritva-core v0.4.0`):

```text
1. Update local public checkout
        │
        ▼
2. Run check-compatibility.sh → list affected skills
        │
        ▼
3. Review changelog and diff of the component
        │
        ▼
4. Update affected skills (branch: compat/kritva-core-v0.4)
        │
        ▼
5. Update evals and fixtures, run all affected evals
        │
        ▼
6. Update compatibility.json (tested_versions, last_reviewed)
        │
        ▼
7. Pull request → review → merge
        │
        ▼
8. Build plugins, update CHANGELOG.md, release
```

```bash
cd ~/kritva/kritvaos-community && git pull && git submodule update --init --recursive
cd ~/kritva/kritva-pro-skills
git checkout main && git pull
git checkout -b compat/kritva-core-v0.4
./scripts/check-compatibility.sh
```

---

## 10. Branching, Commits, and Pull Requests

### Branches

| Prefix | Use |
|---|---|
| `skill/` | New skill or major skill rewrite |
| `update/` | Improvements to existing skills |
| `compat/` | Upstream compatibility updates |
| `plugin/` | Plugin definition changes |
| `release/` | Release preparation |
| `chore/` | Tooling, scripts, docs |

`main` is protected. All changes go through pull requests with at least one reviewer.

### Commit messages

```text
Add core-scheduler-tuning skill
Update motion-controller-tuning for kritva-motion v0.3
Add kritva-safety-review to kritva-pro-dev plugin
Release kritva-pro-dev v0.2.0
```

### Pull request checklist

- [ ] `validate.sh` passes
- [ ] Evals added or updated, and passing (results in PR description)
- [ ] `compatibility.json` updated if versions changed
- [ ] Plugin definitions updated if skills were added or removed
- [ ] `plugins/` regenerated with `build-plugins.sh` (not hand-edited)
- [ ] No secrets, API keys, or customer data
- [ ] No private content copied into or referenced from public repos

---

## 11. Releases and Versioning

### Versioning

- Each **plugin** uses semantic versioning (`vMAJOR.MINOR.PATCH`).
  - **MAJOR:** removed skills, breaking changes, dropped component versions
  - **MINOR:** new skills, new supported component versions
  - **PATCH:** fixes and wording improvements
- Repository tags use the format `<plugin-name>-vX.Y.Z`, for example `kritva-pro-dev-v0.2.0`.

### Release steps

```bash
git checkout main && git pull
git checkout -b release/kritva-pro-dev-v0.2.0
./scripts/validate.sh
./scripts/build-plugins.sh
# Run all evals for skills in this plugin
./scripts/release.sh kritva-pro-dev 0.2.0   # bumps version, updates CHANGELOG, tags
git push -u origin release/kritva-pro-dev-v0.2.0
# Open PR → merge → push tag
```

### `CHANGELOG.md` entry format

```markdown
## kritva-pro-dev v0.2.0 — 2026-10-20

### Added
- core-runtime-debugging skill

### Changed
- core-scheduler-tuning now supports kritva-core v0.4.x

### Compatibility
- kritva-core v0.3.x, v0.4.x
- kritva-motion v0.2.x
```

Full checklist: [`docs/release-checklist.md`](docs/release-checklist.md).

---

## 12. Customer Access and Distribution

### Distribution model

Customers install plugins from this repository as a private marketplace. **Repository access is the access control.**

### Granting access

- Create one GitHub team per customer organization, for example `customer-acme`.
- Give the team **read-only** access to this repository.
- Record access changes in `kritva-business` (not here).

### Revoking access

- Remove the customer team's access when a subscription ends.
- Customers keep whatever they already installed. Ongoing value comes from updates and hosted services.

### Never

- Grant write access to customers
- Store customer names, contracts, or contact details in this repo
- Put customer-specific skills in shared plugins. Use a separate private repo per customer if needed

> Distribution details depend on how Claude handles private plugin marketplaces at the time of release.
> Check the current official documentation before onboarding customers.

---

## 13. Working with Claude Code

### Where to start a session

Open Claude Code in `~/kritva/kritva-pro-skills/`. Use a **separate session** for public repos so private files can't slip into public commits.

### Example requests

```text
Read the v0.4.0 changelog in ../kritvaos-community/kritva-core, run
scripts/check-compatibility.sh, and list which skills in
components/kritva-core/ need updates and why.
```

```text
Create a new skill components/kritva-motion/skills/motion-trajectory-debugging
using the template in this README. Add eval cases in tests/evals/, register
it in compatibility.json and plugin-definitions/kritva-pro-dev.json.
Show me the diff before committing.
```

```text
Prepare release kritva-pro-dev v0.2.0: validate, build plugins, update
CHANGELOG.md, and create a release branch. Do not push the tag yet.
```

### Rules for Claude Code (also in `CLAUDE.md`)

1. This is a **private** repository. Never copy its content into any public repo.
2. Public source at `../kritvaos-community/` is **read-only**. Never modify it from this session.
3. Author skills in `components/` or `cross-component/`. Never hand-edit `plugins/`.
4. Every new or changed skill needs evals and a `compatibility.json` update.
5. Always run `validate.sh` and show the diff before committing.
6. Never push directly to `main` or push release tags without explicit approval.
7. Never commit secrets, API keys, license keys, or customer information.
8. Skills must never recommend placing AI tooling inside the real-time control loop.

---

## 14. Security and Confidentiality

### Repository settings

- Visibility: **Private**
- Forking: **Disabled**
- Branch protection on `main`: required reviews, required status checks
- Secret scanning and push protection: **Enabled**
- Two-factor authentication required for all organization members

### `.gitignore` minimum

```gitignore
.env
.env.*
*.pem
*.key
secrets/
customer-data/
*.log
!tests/fixtures/**/*.log
```

### Test fixtures

- Use synthetic or fully anonymized data only.
- Never include real customer logs, robot data, or configurations.

### If something leaks

1. Rotate any exposed credentials immediately.
2. Remove the content and rewrite history if needed (coordinate before force-pushing).
3. Record the incident and follow-up actions in `kritva-business`.

---

## 15. Decision Records

Internal decisions about the pro product are recorded as ADRs in `docs/decisions/`, using the same format as the public project.

Suggested first ADRs:

| ADR | Topic |
|---|---|
| `0001-repo-structure.md` | Authoring vs. build output separation |
| `0002-no-submodules.md` | Public repos cloned side by side instead of as submodules |
| `0003-distribution-model.md` | Private marketplace with repo-based access control |
| `0004-hosted-value.md` | Core value delivered through hosted services, skills as guides |
| `0005-eval-requirements.md` | Eval coverage required before release |

---

*Confidential — KritvaOS. Internal use only.*
