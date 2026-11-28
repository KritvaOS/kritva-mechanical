# CALC-QR04-01 — QR-04 leg torque screen

| Property | Value |
|---|---|
| Concept | QR-04 Agile Long-Leg Quadruped |
| Status | PROPOSED / ESTIMATE; paper calculation only |
| Date | 2026-11-28 |
| Evidence type | C — formula-based scenario screen |
| Related | ACTUATOR_ANALYSIS.md, MASS_BUDGET.md, WEEK3_ESTIMATE_METHOD.md |

HOLD D-003 remains active. This is a static scenario screen, not gait, impact, simulation, bench or physical evidence. Sources: [WEEK3_SOURCE_REGISTER.md](../../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

## Load basis

The component model is 7.43 kg without the optional camera, producing F = 7.43 × 9.81 = 72.89 N. The separate camera scenario is 7.53 kg. For direct continuity with the prior reviewer’s rounded budget, the 7.50 kg case is also calculated: F = 73.58 N. The full robot weight is assigned to one leg; this is a deliberately conservative static load-share screen, not a normal gait or dynamic impact claim. Four-foot equal static sharing would be 18.22 N/foot at 7.43 kg, versus the 72.89 N one-leg screen.

Leg length is 0.280 m with a 0.140/0.140 m segment split. Moment arms are rounded consistently to 0.1 mm: hip yaw 23.5 mm, hip flexion 86.2 mm, knee 47.0 mm. The ±20% band is a sensitivity around back-solved geometry, not a measured range. Use τ = F × d⊥ and show 1.5× as an explicit headroom sensitivity, not a safety factor.

## Results

| Joint | d⊥ low–nominal–high mm | Static torque at 7.43 kg Nm | 1.5× screen at 7.43 kg Nm | 1.5× screen at 7.50 kg Nm |
|---|---|---:|---:|---:|
| Hip abduction / yaw | 18.8 / 23.5 / 28.2 | 1.37 / 1.71 / 2.06 | 2.06 / 2.57 / 3.08 | 2.07 / 2.59 / 3.11 |
| Hip flexion | 69.0 / 86.2 / 103.4 | 5.03 / 6.28 / 7.54 | 7.54 / 9.42 / 11.31 | 7.61 / 9.51 / 11.42 |
| Knee flexion | 37.6 / 47.0 / 56.4 | 2.74 / 3.43 / 4.11 | 4.11 / 5.14 / 6.17 | 4.15 / 5.19 / 6.22 |

All moment arms use one rounding rule and torque uses two decimal places. The hip-yaw bound deliberately places the full robot weight on one leg at the yaw offset; this is conservative versus normal four-foot load sharing. The exact 7.43 kg nominal row and rounded 7.50 kg sensitivity use the same budget basis; no 6.5 kg load input remains.

## Actuator-family screen

The proposed family role is S wrist/neck, M elbow/reference, L hip/knee. Makiina 10 Nm rated continuous clears the nominal and yaw/knee screens but falls below the high hip-flexion 1.5× screen. CubeMars AK10-9 V3.0 is 18 Nm rated continuous and clears that torque-only screen, but it is a 48 V product and remains below the proposed L continuous band. The third-party T25-40 listing reports 40 Nm continuous, but its profile is explicitly unconfirmed by HEBI. None is a selected actuator.

## Bounds

The leg dimensions, poses, 20% moment-arm sensitivity, full-weight one-leg case and 1.5× headroom are transparent analyst scenarios. Dynamic gait, ground reaction, impact, lateral contact and temperature duty are not part of this static calculation. They are not left as zero; they are outside the modeled scope and cannot be inferred from concept artwork.