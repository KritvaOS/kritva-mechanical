# CALC-QR04-01 — QR-04 Leg Torque Sensitivity Screen

| Property | Value |
|---|---|
| Calculation ID | CALC-QR04-01 |
| Concept | QR-04 Agile Long-Leg Quadruped |
| Status | PROPOSED / ESTIMATE |
| Date | 2026-11-27 |
| Evidence type | C — paper calculation only |
| Related | `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md` |

**HOLD D-003 remains active.** This is a static, assumption-based sensitivity screen; no dynamic gait, impact, simulation, bench or physical evidence is claimed.

## 1. Inputs and method

`F_single = 6.5 kg × 9.81 m/s² = 63.77 N ≈ 64 N` (6.5 kg ASSUMED). Leg length is 0.280 m with 0.140/0.140 m segments (ASSUMED, not released dimensions). `τ = F × d⊥`.

The prior static estimates imply effective moment arms `d⊥ = τ/F`: hip yaw `1.5/63.77 = 23.5 mm`; hip flexion `5.5/63.77 = 86.2 mm`; knee `3.0/63.77 = 47.0 mm`. These are back-solved from the previous estimates, not independently derived from a pose. A ±20% sensitivity is an explicit planning assumption, not a statistical confidence interval. The 1.5× multiplier is a static-only planning screen, not a validated safety factor.

## 2. One-leg static sensitivity

| Joint | Implied d⊥ (mm) | ±20% d⊥ band (mm) | Static band (N·m) | 1.5× static-only screen (N·m) |
|---|---:|---:|---:|---:|
| Hip abduction / yaw | 23.5 | 18.8–28.1 | 1.20–1.80 | 1.80–2.70 |
| Hip flexion | 86.2 | 68.9–103.4 | 4.40–6.60 | 6.60–9.90 |
| Knee flexion | 47.0 | 37.6–56.4 | 2.40–3.60 | 3.60–5.40 |

The 1.5× column multiplies the static sensitivity only. It must not be called a peak or dynamic gait requirement. Replace the back-solved moment arms with an approved pose/coordinate model when available.

## 3. Limits

Load sharing, stance geometry, joint axes, ROM, speed, gait, impact, friction, sensor mass/location, mounting interface allowables and duty are UNKNOWN/OWNER_DECISION. No S/M/L assignment, hardware selection or safety conclusion follows from this calculation.
