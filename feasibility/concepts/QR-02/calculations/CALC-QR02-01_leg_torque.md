# CALC-QR02-01 — QR-02 Leg Joint Torque Screening

| Property | Value |
|---|---|
| Calculation ID | CALC-QR02-01 |
| Concept | QR-02 Standard Quadruped |
| Status | PROPOSED / ESTIMATE |
| Date | 2026-11-28 |
| Evidence type | C — paper calculation only |
| Related | ACTUATOR_ANALYSIS.md, MASS_BUDGET.md |

HOLD D-003 remains active. No gait, impact, simulation, bench or physical result is claimed.

## 1. Inputs and method

τ = F × d⊥, where F is the vertical load carried by the representative leg and d⊥ is the perpendicular moment arm for a stated pose. F_single = 6.3 kg × 9.81 m/s² ÷ 1 leg = 61.80 N. The 6.3 kg mass is the QR-02 sensor-inclusive nominal planning total; assigning the entire robot weight to one leg is an intentionally conservative static screen, not a validated gait case or required support condition. The sensor-excluded subtotal is 6.1 kg.

The leg length is 0.220 m and segment split 0.110/0.110 m (ASSUMED). A 1.5× multiplier is an ASSUMED planning screen, not a validated safety factor. Representative speed 2 rad/s = 19.1 rpm is ASSUMED; no speed, trajectory or duty requirement exists.

## 2. Static load and sensitivity

| Joint | Effective moment-arm basis | Static estimate (N·m) | 1.5× static-only screen (N·m) | Status |
|---|---|---:|---:|---|
| Hip flexion | ASSUMED pose band 0.070–0.090 m; nominal 0.080 m | 4.33–5.56; nominal 4.94 | 6.49–8.34 | ESTIMATE; pose not sourced from geometry |
| Hip abduction / yaw | Earlier 1.2 N·m estimate back-solves to ≈0.02224 m at 5.5 kg; ±20% moment-arm sensitivity | 1.10–1.65; nominal 1.37 | 1.65–2.47 | Conservative planning sensitivity only; not independent geometry evidence |
| Knee flexion | Earlier 2.1 N·m estimate back-solves to ≈0.03892 m at 5.5 kg; ±20% moment-arm sensitivity | 1.92–2.89; nominal 2.41 | 2.89–4.33 | Sensitivity only; back-solved, not independent evidence |

The yaw and knee moment arms are retained from the prior estimate and scaled to 6.3 kg; they are not measured or pose-derived. The +20% moment-arm case is used as a conservative screening sensitivity, not a validated worst-case bound. Replace it when joint axes, pose and coordinates are defined. Values are rounded to 0.01 N·m.

## 3. Dynamic loads and limits

Dynamic gait, acceleration, ground reaction, impact, contact friction, lateral loading, actual load-sharing between legs and single-leg support duration are UNKNOWN. The 1.5× column is static-only and must not be called a peak or gait requirement. Current speed is an ASSUMED 2 rad/s, not a capability target. No S/M/L assignment is made from this calculation.
