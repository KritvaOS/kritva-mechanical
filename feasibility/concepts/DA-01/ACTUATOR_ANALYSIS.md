# DA-01 — Actuator screen

**Status:** PROPOSED / ESTIMATE; no actuator selected. D-003 remains active. This analysis uses the re-run results in [CALC-DA01-01_joint_torque.md](calculations/CALC-DA01-01_joint_torque.md).

## Intended role versus calculated load

The proposed family spec assigns S to wrist/neck and M to elbow/reference; its S/L torque bands are draft placeholders. The DA-01 baseline is interpreted as shoulder yaw, elbow and wrist per arm. Shoulder pitch and wrist pitch are retained as explicit alternative-axis branches.

| Axis branch | 1.5× screen Nm | Proposed role | Paper screen |
|---|---:|---|---|
| Wrist pitch / rotation alternative | 0.31 / 0.01 | S | Low calculated torque; radial inertia estimate is geometry-sensitive. |
| Elbow pitch | 1.33 | M | Clears available S and M torque references numerically; role sizing should use M, not infer S from torque alone. |
| Shoulder yaw | 1.03 | Not defined by source family role | Inertial-only paper estimate. |
| Conditional shoulder pitch | 4.77 | M sensitivity | HEBI T5-4 4 Nm does not clear this branch; Makiina 10 Nm does. |

## Sourced product comparison

| Product reference | Rated continuous torque | Speed | Mass | Published price | Interpretation |
|---|---:|---:|---:|---:|---|
| Makiina medium | 10 Nm | up to 75 rpm | 0.240 kg | USD 90 | Clears the modeled torque branches at 24 V; preliminary lab data and foreign landed cost not established. |
| HEBI T5-4 | 4 Nm | 32 rpm | 0.450 kg | Not listed | Clears the elbow/wrist screen but not conditional 4.77 Nm shoulder-pitch screen. |
| CubeMars AK70-10 | 8.3 Nm | Product listing | 0.621 kg | USD 398.90–498.90 | Less than 10 Nm; not a match for the M 10 Nm reference. |
| CubeMars AK10-9 V3.0 | 18 Nm | Product listing | 0.940 kg | USD 698.90–798.90 | Clears conditional torque screen but is 48 V, against the artwork’s 24 V direction. |

At the assumed 15 rpm comparison speed, the listed Makiina and HEBI T5-4 speeds are above the screen; no acceleration or thermal-duty compatibility is established. This is a comparison, not a chosen actuator set. Full source details and prices are in [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).