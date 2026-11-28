# CALC-QR02-01 — QR-02 Leg Joint Torque Screening

| Property | Value |
|---|---|
| Calculation ID | CALC-QR02-01 |
| Concept | QR-02 Standard Quadruped |
| Status | PROPOSED / ESTIMATE |
| Date | 2026-11-27 |
| Evidence type | C — paper calculation only |
| Related | `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md` |

**HOLD D-003 remains active.** No gait, impact, simulation, bench or physical result is claimed.

## 1. Inputs and method

`τ = F × d⊥`, where `F` is the vertical load carried by the representative leg and `d⊥` is the perpendicular moment arm for a stated pose. `F_single = 5.5 kg × 9.81 m/s² ÷ 1 leg = 53.96 N ≈ 54 N` (5.5 kg is ASSUMED). The leg length is 0.220 m and segment split 0.110/0.110 m (ASSUMED). A 1.5× multiplier is an ASSUMED planning screen, not a validated safety factor. Representative speed 2 rad/s = 19.1 rpm is ASSUMED; no speed, trajectory or duty requirement exists.

## 2. Static load and sensitivity

| Joint | Effective moment arm basis | Static estimate (N·m) | 1.5× static-only screen (N·m) | Status |
|---|---|---:|---:|---|
| Hip flexion | ASSUMED pose band 0.070–0.090 m; nominal 0.080 m | 3.78–4.86; nominal 4.32 | 5.67–7.29 | ESTIMATE; pose not sourced from geometry |
| Hip abduction / yaw | Existing 1.2 N·m estimate implies 0.022 m at 54 N; ±20% moment-arm sensitivity | 0.96–1.44; nominal 1.20 | 1.44–2.16 | Sensitivity only; back-solved, not independent evidence |
| Knee flexion | Existing 2.1 N·m estimate implies 0.039 m at 54 N; ±20% moment-arm sensitivity | 1.68–2.52; nominal 2.10 | 2.52–3.78 | Sensitivity only; back-solved, not independent evidence |

The hip-flexion range uses `54 N × 0.070–0.090 m`; its nominal value is `54 N × 0.080 m = 4.32 N·m`. The yaw and knee moment arms above are algebraically inferred from the earlier estimates only to expose the assumption; they are not measured, geometry-derived or independent validation. Replace them when joint axes, pose and coordinates are defined.

## 3. Dynamic loads and limits

Dynamic gait, acceleration, ground reaction, impact, contact friction, lateral loading, load-sharing between legs and single-leg support duration are UNKNOWN. The 1.5× column is a static-only planning screen and must not be called a peak or gait requirement. Current speed is an ASSUMED 2 rad/s, not a capability target. No S/M/L assignment is made from this calculation.
