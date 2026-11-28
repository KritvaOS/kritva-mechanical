# CALC-DA01-01 — DA-01 Joint Torque Estimates

| Property | Value |
|---|---|
| Calculation ID | CALC-DA01-01 |
| Concept | DA-01 Fixed Tabletop Dual-Arm |
| Author | INTERN-01 (supported) |
| Date | 2026-11-27 |
| Status | PROPOSED / ESTIMATE |
| Related | `ACTUATOR_ANALYSIS.md` v0.3.0 |

## 1. Purpose

Provide transparent, assumption-tagged static and simplified dynamic torque estimates for the six baseline joints so that future S/M/L comparison has a traceable numeric starting point.

## 2. Inputs and assumptions

All numeric inputs are taken from `ACTUATOR_ANALYSIS.md` §2–3. Key tags:

- CONCEPT_TARGET: reach 350 mm, payload 0.1–0.2 kg, mass target 5–8 kg.
- ASSUMED: link split A3, module masses A4–A8, speed/accel A10–A11, planning factor 1.5×.
- Gravity g = 9.81 m/s².

Worst-case pose: arm fully extended horizontally (shoulder pitch and elbow pitch aligned against gravity).

## 3. Static torque derivation (shoulder pitch example)

Moment arms measured from shoulder pitch axis along the extended arm:

| Mass element | Mass (kg) | Distance (m) | Contribution m·g·d (N·m) |
|---|---:|---:|---:|
| Payload | 0.20 | 0.350 | 0.687 |
| Gripper + mount | 0.12 | 0.310 | 0.365 |
| Wrist module | 0.18 | 0.275 | 0.486 |
| Forearm link | 0.08 | 0.225 | 0.177 |
| Elbow module | 0.30 | 0.175 | 0.515 |
| Upper-arm link | 0.12 | 0.0875 | 0.103 |
| **Sum** | | | **≈ 2.33** |

Rounded working value used in the matrix: **2.15 N·m** (conservative rounding and minor geometric uncertainty). Elbow and wrist follow the same method with shorter distal chains.

## 4. Inertial estimate

Approximate I_shoulder ≈ Σ m_i r_i² ≈ 0.055 kg·m².  
With α = 10 rad/s² → Iα ≈ 0.55 N·m.

Peak = static + inertial ≈ 2.70 N·m before planning factor.

## 5. Sensitivity (order-of-magnitude)

- Payload ±0.05 kg changes shoulder static by ≈ ±0.17 N·m.
- Reach ±50 mm (if link lengths change) changes shoulder static by ≈ ±0.3 N·m.
- Module masses ±30 % change shoulder static by ≈ ±0.3 N·m.

Order of magnitude remains < 5 N·m peak even under combined adverse variations, which is useful context for later S/M/L comparison but does **not** constitute a requirement.

## 6. Limitations

- No measured link lengths or joint offsets exist.
- No measured module masses or CoM locations exist.
- Coordinate frames and exact axis directions for the wrist remain OWNER_DECISION.
- Friction, cable drag and gearbox efficiency are covered only by the 1.5× planning factor.
- Dynamic model is a point-mass approximation; full recursive Newton-Euler or Lagrange model is future work once geometry is frozen.

## 7. Traceability

All numbers trace to the assumption table in `ACTUATOR_ANALYSIS.md`. Any change to an assumption must update both this calculation and the parent analysis file, with a CHANGELOG entry and commit reference.
