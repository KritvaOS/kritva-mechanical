# QR-02 — Joint and Actuator Requirements (Week 3/4 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-QR-02 |
| Status | PROPOSED — paper estimate; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.5.0 |
| Last Updated | 2026-11-28 |
| Evidence type | C — paper calculation only |

HOLD D-003 remains active. No gait, impact, simulation, bench or physical evidence is claimed; no actuator is selected.

## 1. Configuration and assumptions

Standard quadruped: four legs × three DOF per leg = 12 baseline channels (CONCEPT_TARGET). The static screen uses the 6.3 kg sensor-inclusive nominal planning mass from MASS_BUDGET.md, with the entire weight assigned to one leg: F = 6.3 × 9.81 = 61.80 N. This one-leg whole-weight case is intentionally conservative relative to multi-leg static sharing; it is not a validated gait or stance requirement. The sensor-excluded nominal mass is 6.1 kg. Leg length is 220 mm with 110/110 mm segment split, representative speed is 2 rad/s (19.1 rpm), and the planning multiplier is 1.5×; these are ASSUMED, not approved requirements.

## 2. Per-joint static screen, one leg

| Joint | Static torque (N·m) | 1.5× static-only screen (N·m) | Speed input | Torque-only family screen |
|---|---:|---:|---|---|
| Hip abduction / yaw | 1.10–1.65 (back-solved moment-arm sensitivity) | 1.65–2.47 | 2 rad/s ASSUMED | S is the smallest proposed band to examine; not assigned |
| Hip flexion | 4.33–5.56; nominal 4.94 | 6.49–8.34 | 2 rad/s ASSUMED | Static high end exceeds proposed S continuous max 5; 1.5× static-only screen is higher; M is not assigned |
| Knee flexion | 1.92–2.89 (back-solved moment-arm sensitivity) | 2.89–4.33 | 2 rad/s ASSUMED | S torque band is a screening candidate only; not assigned |

See calculations/CALC-QR02-01_leg_torque.md for formulas, scaled budget mass and the limitations on back-solved moment arms. The hip-yaw +20% moment-arm case is a conservative sensitivity only, not a validated worst case. The 1.5× column is not a dynamic peak.

## 3. Proposed family-band screen (not assignment)

| Family band | Proposed continuous torque | Proposed peak torque | Source headline speed | Maturity caveat |
|---|---:|---:|---:|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to ~60 rpm | S values are placeholders |
| Kritva-M | 10 N·m | 20–25 N·m | 45 rpm | M reference is not frozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | ~20–40 rpm | L values are placeholders |

The parent family specification is proposal-level only. Headline speed is not demonstrated at required joint load; dynamic gait, thermal duty, packaging and exact variant output curves remain unavailable. See references/SOURCE_REGISTER.md SRC-11. No exact S/M/L compatibility or model selection is claimed.

## 4. Open inputs

Exact joint axes, pose, ROM, trajectory, duty, support polygon, ground reaction and impact, payload, battery and S/M/L variant-specific output data remain UNKNOWN/TBD. Optional sensors and force feet remain OWNER_DECISION. HOLD D-003 remains active.
