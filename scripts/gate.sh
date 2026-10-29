#!/bin/sh
# Gate runner for the standard make targets (ROB-MECH-004).
#
# Usage: sh scripts/gate.sh <target>
#
# Every standard gate is NOT_IMPLEMENTED today: this prints that fact and exits 3.
# An unimplemented gate is never a pass (program acceptance standard, make targets).
# When a gate is implemented, replace its entry below with the real check in a
# separate task, and record it in planning/CHANGELOG.md.
#
# Exit codes: 0 all checks pass; 1 a check failed; 2 usage error; 3 NOT_IMPLEMENTED.

target="${1:-}"

case "$target" in
  check)            scope="structure, registers, evidence, hold guard, status (SAN-001 to SAN-004, SAN-009 to SAN-016)" ;;
  lint)             scope="static style checks for scripts and documents" ;;
  test-unit)        scope="known-answer and other unit tests for the repository's checks and calculations" ;;
  test-integration) scope="cross-document and cross-repository checks, status generation end to end" ;;
  test-regression)  scope="regression suites REG-001 onward (verification/REGRESSION_PLAN.md)" ;;
  test)             scope="all test tiers T0 to T5 that apply" ;;
  docs-check)       scope="document headers, local links, README structure, placeholders (SAN-005 to SAN-008)" ;;
  acceptance)       scope="acceptance criteria evidence for the task or milestone under review" ;;
  *)
    echo "usage: scripts/gate.sh {check|lint|test-unit|test-integration|test-regression|test|docs-check|acceptance}" >&2
    exit 2
    ;;
esac

echo "NOT_IMPLEMENTED: make ${target} is not implemented yet. Scope: ${scope}." >&2
echo "This is not a pass. See verification/SANITY_PLAN.md and planning/TASKS.md." >&2
exit 3
