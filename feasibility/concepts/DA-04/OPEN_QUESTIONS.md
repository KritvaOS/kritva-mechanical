# DA-04 — Open Questions and Evidence Needed

**Status:** PROPOSED | 2026-11-28 | HOLD D-003 active

| Open input / owner decision | Current status | Why it matters / evidence needed |
|---|---|---|
| Confirm the current 4-DOF-per-arm and 2-drive-channel baseline against the decision record | Source README records a decision claim; decision log not located in tracked tree | Do not restate approval as verified until the record is found |
| Wheel radius, track, wheel loading, tyre/friction and operating case | UNKNOWN | Required for traction and drive torque calculation |
| Arm link lengths, joint offsets, payload centre and representative pose | UNKNOWN | Required for per-joint arm torque and workspace |
| Battery, sensor and optional gripper baseline | OWNER_DECISION / UNKNOWN | Changes mass, CoM, power and cost scope |
| Component masses and CoM | UNKNOWN | Source-controlled parts or released geometry required |
| Material/process, interfaces, tolerances and structural allowables | UNKNOWN | Required before stress/deflection or manufacturing claims |
| Component prices, taxes, shipping, labour and test scope | UNKNOWN | Priced BOM and explicit budget scope required |

No numeric mass, cost, drive-load or stability result is retained without source inputs. See README.md, ARCHITECTURE.md, ACTUATOR_ANALYSIS.md, MASS_BUDGET.md and COST_MODEL.md.
