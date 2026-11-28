# QR-04 — Actuator screen

**Status:** PROPOSED / ESTIMATE; no actuator selected. D-003 remains active. See [CALC-QR04-01_leg_torque_screen.md](calculations/CALC-QR04-01_leg_torque_screen.md).

## Role and load screen

The proposed family spec assigns S to wrist/neck, M to elbow/reference and L to hip/knee. S/L torque bands are draft placeholders. All three QR-04 joint classes fall under the proposed L role. Exact budget mass is 7.43 kg; a separate 7.50 kg rounded case is retained for the review comparison.

| Joint class | 1.5× screen at 7.43 kg Nm | 1.5× screen at 7.50 kg Nm | Proposed role | 10 Nm Makiina load screen |
|---|---:|---:|---|---|
| Hip flexion | 7.54–11.31 | 7.61–11.42 | L | Clears nominal 9.42 Nm, not upper scenario. |
| Hip abduction/yaw | 2.06–3.08 | 2.07–3.11 | L | Clears static screen, below role band. |
| Knee flexion | 4.11–6.17 | 4.15–6.22 | L | Clears static screen, below role band. |

## Sourced references

| Product reference | Rated continuous torque | Speed | Mass | Published price | Interpretation |
|---|---:|---:|---:|---:|---|
| Makiina medium | 10 Nm | up to 75 rpm | 0.240 kg | USD 90 | Under-ceiling scenario; misses upper hip-flexion screen. |
| HEBI T8-16 | 16 Nm | 15 rpm | 0.575 kg | Not listed | Clears the paper torque screen but is below proposed L torque band and below the 19.1 rpm comparison speed. |
| CubeMars AK10-9 V3.0 | 18 Nm | Product listing | 0.940 kg | USD 698.90–798.90 | Clears paper torque screen but is 48 V and below L band. |
| T25-40 third-party profile | 40 Nm reported | 23 rpm reported | 1.50 kg reported | USD 4,500 reported | Flowntro states HEBI has not confirmed the profile; sensitivity only. |

The calculations use one-leg full weight at each joint moment arm, including hip yaw, as a conservative static load-share case. The hip-yaw offset is a sensitivity, not measured geometry. Gait, ground reaction, impact, thermal duty, and dynamic stabilization are not modeled. None of the comparison products is selected. Full source details and confidence are in [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).