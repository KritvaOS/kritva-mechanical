# QR-02 — Joint and Actuator Requirements (Week 3/4 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-QR-02 |
| Status | PROPOSED — paper estimate; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.4.0 |
| Last Updated | 2026-11-27 |
| Evidence type | C — paper calculation only |

**HOLD D-003 remains active.** No gait, impact, simulation, bench or physical evidence is claimed; no actuator is selected.

## 1. Configuration and assumptions

Standard quadruped: four legs × three DOF per leg = 12 baseline channels (CONCEPT_TARGET). For the static screen, robot mass is 5.5 kg, single-leg support is `5.5 × 9.81 = 53.96 N ≈ 54 N`, hip-to-foot length is 220 mm with 110/110 mm segment split, representative speed is 2 rad/s (19.1 rpm), and the planning multiplier is 1.5×. These are ASSUMED inputs, not approved requirements. The multiplier is not a validated safety factor.

## 2. Per-joint static screen, one leg

| Joint | Static torque (N·m) | 1.5× static-only screen (N·m) | Speed input | Torque-only family screen |
|---|---:|---:|---|---|
| Hip abduction / yaw | 0.96–1.44 (back-solved moment-arm sensitivity) | 1.44–2.16 | 2 rad/s ASSUMED | S is the smallest proposed band to examine; not assigned |
| Hip flexion | 3.78–4.86; nominal 4.32 | 5.67–7.29 | 2 rad/s ASSUMED | Static high end nears S continuous max 5; 1.5× screen exceeds it. M is only a proposed torque band, not an assignment; dynamic loads unknown |
| Knee flexion | 1.68–2.52 (back-solved moment-arm sensitivity) | 2.52–3.78 | 2 rad/s ASSUMED | S torque band is a screening candidate only |

See `calculations/CALC-QR02-01_leg_torque.md` for formulas, moment-arm assumptions and the explicit limitation that two moment-arm bands are back-solved from the previous estimates. These are static-only calculations; the 1.5× column is not a dynamic peak.

## 3. Proposed family-band screen (not assignment)

| Family band | Proposed continuous torque | Proposed peak torque | Source headline speed | Maturity caveat |
|---|---:|---:|---:|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to ~60 rpm | S data are placeholders |
| Kritva-M | 10 N·m | 20–25 N·m | 45 rpm | M reference is not frozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | ~20–40 rpm | L data are placeholders |

These are parent-repository family-level proposal bands, not verified variant output curves. Headline speed is not demonstrated at the required joint load; thermal, duty, packaging and exact model data remain unavailable.

`KritvaOS/kritva-actuator/docs/architecture/ACTUATOR_FAMILY_SPEC.md` at commit `31bfc20aed0479a3bce64cf8945e86b1fa6f2fa6` contains proposed family bands. S/L values are placeholders and the M reference is not frozen. A torque-only band comparison does not establish compatibility; speed under load, dynamic gait, thermal duty, packaging and mass remain unverified. See `references/SOURCE_REGISTER.md` SRC-11.

## 4. Open inputs

Exact joint axes, pose, ROM, trajectory, duty, support polygon, ground reaction and impact, payload, battery and S/M/L variant-specific output data remain UNKNOWN/TBD. Optional sensors and force feet remain OWNER_DECISION. HOLD D-003 remains active.
