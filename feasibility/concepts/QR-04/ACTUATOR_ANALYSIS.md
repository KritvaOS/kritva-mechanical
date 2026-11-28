# QR-04 — Joint and Actuator Requirements (Week 3/4 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-QR-04 |
| Status | PROPOSED — paper estimate; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.5.0 |
| Last Updated | 2026-11-28 |
| Evidence type | C — paper calculation only |

HOLD D-003 remains active. No gait, impact, simulation, bench or physical evidence is claimed; all results are estimates, not requirements or actuator selections.

## 1. Inputs and method

The updated load uses the 7.5 kg nominal QR-04 mass budget: F_single = 7.5 × 9.81 = 73.58 N. Assigning all robot weight to one leg is a conservative static load-sharing case, not a validated gait or stance requirement. Leg length 280 mm and 140/140 mm segment split are ASSUMED. Use τ = F × d⊥. Prior joint torque estimates were based on 6.5 kg; those implied moment arms are retained while load is scaled to 7.5 kg. A ±20% moment-arm sensitivity is conservative planning only, not a validated worst-case bound. The 1.5× multiplier is static-only and not a validated safety factor.

## 2. Static torque and sensitivity screen, one leg

| Joint | Implied d⊥ (mm) | ±20% d⊥ band (mm) | Static torque band (N·m) | 1.5× static-only screen (N·m) |
|---|---:|---:|---:|---:|
| Hip abduction / yaw | 23.5 | 18.8–28.2 | 1.38–2.08 | 2.08–3.12 |
| Hip flexion | 86.2 | 68.9–103.4 | 5.08–7.62 | 7.62–11.42 |
| Knee flexion | 47.0 | 37.6–56.4 | 2.77–4.15 | 4.15–6.23 |

See calculations/CALC-QR04-01_leg_torque_screen.md. Moment-arm values use a consistent 1-decimal-mm rule; torques use two decimals. Values are demand-versus-family-range observations, not compatibility conclusions. The parent family spec labels S/L figures as placeholders and the M reference is not frozen; exact speed-under-load, thermal, packaging and duty data remain unavailable.

## 3. Proposed family-band screen (not assignment)

| Family band | Proposed continuous torque | Proposed peak torque | Source headline speed | Maturity caveat |
|---|---:|---:|---:|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to ~60 rpm | S values are placeholders |
| Kritva-M | 10 N·m | 20–25 N·m | 45 rpm | M reference is not frozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | ~20–40 rpm | L values are placeholders |

No S/M/L compatibility, model selection, speed, thermal, packaging or duty conclusion is claimed; see references/SOURCE_REGISTER.md SRC-11.

## 4. Open inputs

Leg joint axes, exact link lengths/pose, load sharing, gait, impact, ROM, speed, duty, contact friction, body CoM and sensor configuration remain UNKNOWN or ASSUMED. The indicated mounting interface and adjustable sensor module remain OWNER_DECISION. HOLD D-003 remains active.
