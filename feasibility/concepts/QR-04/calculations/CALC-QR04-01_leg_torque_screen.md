# CALC-QR04-01 — QR-04 Leg Torque Sensitivity Screen

| Property | Value |
|---|---|
| Calculation ID | CALC-QR04-01 |
| Concept | QR-04 Agile Long-Leg Quadruped |
| Status | PROPOSED / ESTIMATE |
| Date | 2026-11-28 |
| Evidence type | C — paper calculation only |
| Related | ACTUATOR_ANALYSIS.md, MASS_BUDGET.md |

HOLD D-003 remains active. This is a static, assumption-based sensitivity screen; no dynamic gait, impact, simulation, bench or physical evidence is claimed.

## 1. Inputs and method

F_single = 7.5 kg × 9.81 m/s² ÷ 1 leg = 73.58 N. The 7.5 kg value is the QR-04 nominal mass budget. Assigning full robot weight to one leg is a conservative static load-sharing case, not a validated gait or stance requirement. Leg length is 0.280 m with 0.140/0.140 m segments (ASSUMED, not released dimensions). Use τ = F × d⊥.

The prior static estimates at 6.5 kg imply effective moment arms of hip yaw 23.5 mm, hip flexion 86.2 mm and knee 47.0 mm. The same moment arms are retained while force is scaled to 7.5 kg. A ±20% sensitivity is an explicit conservative screening assumption around those back-solved values, not a statistically supported or validated worst-case bound. The 1.5× multiplier is static-only and is not a validated safety factor.

## 2. One-leg static sensitivity

| Joint | Implied d⊥ (mm) | ±20% d⊥ band (mm) | Static band (N·m) | 1.5× static-only screen (N·m) |
|---|---:|---:|---:|---:|
| Hip abduction / yaw | 23.5 | 18.8–28.2 | 1.38–2.08 | 2.08–3.12 |
| Hip flexion | 86.2 | 68.9–103.4 | 5.08–7.62 | 7.62–11.42 |
| Knee flexion | 47.0 | 37.6–56.4 | 2.77–4.15 | 4.15–6.23 |

Moment-arm values are rounded consistently to one decimal millimetre; torque values are rounded to two decimals. The 1.5× column multiplies static sensitivity only and must not be called a dynamic peak. Replace back-solved moment arms with an approved pose/coordinate model when available.

## 3. Limits

Load sharing, stance geometry, joint axes, ROM, speed, gait, impact, friction, sensor mass/location, mounting interface allowables and duty are UNKNOWN/OWNER_DECISION. No S/M/L assignment, hardware selection or safety conclusion follows from this calculation.
