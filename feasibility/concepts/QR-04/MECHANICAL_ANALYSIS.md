# QR-04 — Mechanical Evidence Status (Week 3/4)

**Status:** INCOMPLETE — qualitative configuration review only. HOLD D-003 active.

## Source-backed configuration

The concept artwork/README describes four long-leg assemblies with three DOF per leg and a 450 × 280 × 320 mm body target. It prints a 5–7 kg (est.) mass target and a 0.5–1.0 kg (est.) payload target. These remain CONCEPT_TARGETs, not measured inputs. See README.md sections 2, 4, 6 and 9; ARCHITECTURE.md sections 2–3.

## Load and stability

For the same force and pose, torque changes with the perpendicular joint moment arm (τ = F d⊥). The concept source does not provide leg-segment lengths, joint offsets, a standing pose or a load-sharing model, so the longer-leg description alone does not support a numeric torque comparison with QR-02. CALC-QR04-01 reports only a conditional one-leg force scenario from the printed target range; no joint torque is calculated.

Body CoM, support polygon, ground contact, friction, gait, impact, actuator mass and mounting loads remain UNKNOWN. The cross-section-only 4 × M5 / 2 × Ø5 interface is an indicative owner decision, not a rated structural interface. No stability margin or fastener capacity is claimed.

## Structure and sensor module

Leg sections, material grade, joints, wall thickness and bearing/support details are not released. The adjustable sensor module is shown only on the cross-section; its inclusion, mass and location remain OWNER_DECISION. Deflection, strength, thermal and cable-flex checks are NOT COMPUTABLE from available inputs.

## Evidence status

| Topic | Status | Source / next input |
|---|---|---|
| Configuration and actuator count | Transcribed CONCEPT_TARGET | README.md / ARCHITECTURE.md |
| Joint loads and speed | TBD; no moment arms or motion case | ACTUATOR_ANALYSIS.md / CALC-QR04-01 |
| Mass and CoM | UNKNOWN | MASS_BUDGET.md; source-controlled masses and geometry required |
| Mounting interface | OWNER_DECISION; no allowables | Cross-section review and approved interface spec required |
| Cost | UNKNOWN | COST_MODEL.md; priced BOM required |

References: references/SOURCE_REGISTER.md SRC-01–SRC-06. No gait validation, simulation, bench or physical evidence is claimed.
