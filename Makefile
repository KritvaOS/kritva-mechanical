# Makefile for kritva-mechanical (ROB-MECH-004).
#
# The program's standard gate targets are exposed here. Each one that is not
# implemented runs scripts/gate.sh, prints NOT_IMPLEMENTED and fails. It is never
# a pass. Today all eight are unimplemented.
#
# Exit status: scripts/gate.sh exits 3 for NOT_IMPLEMENTED. GNU make reports any
# failed recipe as exit status 2 and prints "Error 3". Run scripts/gate.sh
# directly when the exact code 3 is needed.
#
# Recipes start with ">" instead of a tab (.RECIPEPREFIX), so the file survives
# copy and paste. Requires GNU make 3.82 or later.

.RECIPEPREFIX = >

.PHONY: help check lint test-unit test-integration test-regression test docs-check acceptance test-tools
.PHONY: preflight preflight-commits hooks-install preflight-hook-on preflight-hook-off

help:
> @echo "Standard gates (all NOT_IMPLEMENTED today, each fails):"
> @echo "  make check  make lint  make test-unit  make test-integration"
> @echo "  make test-regression  make test  make docs-check  make acceptance"
> @echo "Implemented helper:"
> @echo "  make test-tools         unit tests for the vendored commit-format checker and these gates"
> @echo "  make preflight          run before a push: commit-format check of this branch, then the unit tests"
> @echo "  make hooks-install      git hooks for this clone: a bad commit message is rejected at commit time"

check:
> @sh scripts/gate.sh check

lint:
> @sh scripts/gate.sh lint

test-unit:
> @sh scripts/gate.sh test-unit

test-integration:
> @sh scripts/gate.sh test-integration

test-regression:
> @sh scripts/gate.sh test-regression

test:
> @sh scripts/gate.sh test

docs-check:
> @sh scripts/gate.sh docs-check

acceptance:
> @sh scripts/gate.sh acceptance

# Not a standard gate: it tests this repository's own tooling only and says so.
test-tools:
> python3 -m unittest discover -s tests

# Preflight (same idea as kritva-sense): "make preflight" is the one command to run before pushing.
# It runs the checks CI runs on a pull request, keeps going after a failure, prints a summary,
# fixes nothing and never fetches or installs anything. Not mirrored: secret-scan (gitleaks, CI),
# a local link check, check_readme.py and the manual checks in AGENTS.md; say so in the pull request.
# These are helpers, not standard gates. PREFLIGHT_BASE is the branch the commits are compared
# with; run "git fetch origin" first.
PREFLIGHT_BASE ?= origin/main
PREFLIGHT_STEPS := preflight-commits test-tools

preflight:
> @fail=""; \
> for step in $(PREFLIGHT_STEPS); do \
>   echo ""; echo "[preflight] >>> $$step"; \
>   if $(MAKE) --no-print-directory $$step; then :; else fail="$$fail $$step"; fi; \
> done; \
> echo ""; \
> if [ -n "$$fail" ]; then \
>   echo "[preflight] FAILED:$$fail"; \
>   echo "[preflight] Fix these, then run make preflight again. CI would reject this push."; \
>   exit 1; \
> fi; \
> echo "[preflight] Passed: commit format, unit tests. Not run: secret-scan (CI), link check, check_readme.py, manual checks in AGENTS.md."

preflight-commits:
> @git rev-parse --verify --quiet "$(PREFLIGHT_BASE)^{commit}" >/dev/null || { echo "[preflight-commits] $(PREFLIGHT_BASE) not found. Run: git fetch origin"; exit 2; }
> @ids=$$(mktemp); \
> grep -o 'ROB-MECH-[0-9]\{3\}' planning/TASKS.md | sort -u > "$$ids"; \
> if [ ! -s "$$ids" ]; then echo "[preflight-commits] no task IDs found in planning/TASKS.md"; rm -f "$$ids"; exit 2; fi; \
> python3 scripts/security/check_commit_format.py --range "$(PREFLIGHT_BASE)..HEAD" --registry "$$ids"; rc=$$?; \
> rm -f "$$ids"; exit $$rc

hooks-install:
> @chmod +x .githooks/commit-msg .githooks/pre-push
> git config core.hooksPath .githooks
> @echo "[hooks] core.hooksPath set to .githooks."
> @echo "[hooks] commit-msg rejects a commit message that breaks the commit format; pre-push runs make preflight."
> @echo "[hooks] Skip once with --no-verify. Turn the pre-push check off with: make preflight-hook-off"

preflight-hook-on:
> git config kritva.preflightOnPush true
> @echo "[hooks] pre-push preflight is ON for this clone. It needs core.hooksPath (make hooks-install)."

preflight-hook-off:
> git config kritva.preflightOnPush false
> @echo "[hooks] pre-push preflight is OFF for this clone. The commit-msg hook and CI still check messages."
