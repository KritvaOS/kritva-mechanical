# Provenance of the vendored status schema

| File | Source | Source commit | SHA-256 of the copy | Modified |
|---|---|---|---|---|
| `status.schema.json` | `KritvaOS/kritva-program`, `schema/status.schema.json` (schema 2.0) | `ff6d33afe26d14ddd29a949f50a97f8ee16331c8` (local clone; may be behind GitHub) | `0c12f2a652936fd3c9db5a571e61491e1bacb8047087e5567c3c5e0fa1c1231d` | No, byte-for-byte copy |

The program schema is the authority. If it changes, copy it again, update this table in the same pull request, regenerate `status/status.json` and add a changelog entry. Do not edit the copy to make a report pass.

`gen_status.py` validates with a small built-in checker for the parts of JSON Schema that schema 2.0 uses, so CI needs no extra packages. The unit tests also compare it with the `jsonschema` package when that package is installed. The program's own validator (`tools/`, not vendored here) remains the final check before registration (ROB-MECH-006).
