# CALC-QR02-01 — QR-02 leg torque screen

| Property | Value |
|---|---|
| Concept | QR-02 Standard Quadruped |
| Status | PROPOSED / ESTIMATE; paper calculation only |
| Date | 2026-11-28 |
| Evidence type | C — formula-based scenario screen |
| Related | ACTUATOR_ANALYSIS.md, MASS_BUDGET.md, WEEK3_ESTIMATE_METHOD.md |

HOLD D-003 remains active. No gait, impact, simulation, bench or physical result is claimed. Sources: [WEEK3_SOURCE_REGISTER.md](../../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

## Load basis

The nominal component model is 6.30 kg with optional sensors excluded; the OAK-D Lite branch adds 0.102 kg. The conservative case assigns the whole robot weight to one representative leg: F = 6.30 × 9.81 = 61.80 N. Equal static sharing over four feet would be 15.45 N per foot; the one-leg case is four times that average. It is a deliberately conservative static screen, not a normal gait claim or impact bound.

Use τ = F × d⊥. The 1.5 multiplier is an explicit 50% headroom sensitivity, not a validated safety factor. Hip-pitch geometry uses an assumed 70–90 mm perpendicular offset, nominal 80 mm. Hip-yaw and knee offsets are back-solved from earlier estimates and scaled consistently; their ±20% bands are sensitivities, not measured geometry.

## Results at 6.30 kg

| Joint | d⊥ scenario | Static torque Nm | 1.5× static screen Nm | Evidence |
|---|---:|---:|---:|---|
| Hip flexion | 70–90 mm; nominal 80 mm | 4.33–5.56; nominal 4.94 | 6.49–8.34 | Assumed pose band. |
| Hip abduction / yaw | 17.8–26.7 mm; nominal 22.2 mm | 1.10–1.65; nominal 1.37 | 1.65–2.47 | Sensitivity back-solved from earlier 5.5 kg estimate. |
| Knee flexion | 31.1–46.7 mm; nominal 38.9 mm | 1.92–2.89; nominal 2.41 | 2.89–4.34 | Sensitivity back-solved from earlier 5.5 kg estimate. |

The hip-yaw bound is deliberately conservative: the complete 61.80 N robot weight is applied at the yaw offset even though normal four-foot stance shares load. The yaw offsets are back-solved sensitivity values, not measured anatomy. The optional camera version is 6.40 kg; its force is 62.80 N and it raises torque by 1.6%. The baseline calculation is sensor-excluded, resolving the prior ambiguity over the QR-02 total.

## Actuator-family screen

The family proposal assigns S to wrist/neck, M to elbow/reference and L to hips/knees. QR-02’s three joints per leg are hip abduction, hip flexion and knee, so the literal proposed role labels all three as L. For load-only comparison, the 10 Nm rated Makiina candidate clears the 8.34 Nm upper static-only hip-flexion screen at the modeled 15–19 rpm range; it does not satisfy the proposed L continuous band of 25–40 Nm. That difference is stated as a family-role versus load-screen discrepancy, not a hidden hardware assignment.

## Bounds

The 0.22 m total leg length with 0.11/0.11 m split, 2 rad/s comparison speed (19.1 rpm), one-leg load sharing, back-solved yaw/knee offsets and 1.5× headroom are scenario inputs. Results omit dynamic gait, impact, friction, actuator thermal behavior, mass distribution and a validated stance pose. None is promoted to a continuous actuator requirement.