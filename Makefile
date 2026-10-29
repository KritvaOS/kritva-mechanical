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

help:
> @echo "Standard gates (all NOT_IMPLEMENTED today, each fails):"
> @echo "  make check  make lint  make test-unit  make test-integration"
> @echo "  make test-regression  make test  make docs-check  make acceptance"
> @echo "Implemented helper:"
> @echo "  make test-tools   unit tests for the vendored commit-format checker and these gates"

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
