# CALC-QR04-01 — Conditional Single-Leg Load Relation

| Property | Value |
|---|---|
| Status | PROPOSED — conditional calculation only |
| Date | 2026-11-28 |
| Evidence | C — arithmetic from printed concept targets; not validation |
| HOLD | D-003 active |

This note separates source-transcribed targets from derived quantities. Printed “est.” values remain CONCEPT_TARGETs; they are not verified mass, payload or performance inputs. No missing mass, geometry, pose or motion value is substituted. See references/SOURCE_REGISTER.md for source revisions and limits.
## Source inputs

| Input | Value | Source / status |
|---|---:|---|
| Printed robot mass target | 5–7 kg (est.) | README.md section 4; CONCEPT_TARGET, no derivation or verified system mass |
| Leg/joint count | Four legs; three DOF per leg; 12 baseline actuators | README.md sections 2 and 6; concept target |
| Gravity | 9.81 m/s² | Standard-gravity approximation used for arithmetic |
| Leg lengths, joint offsets and pose | UNKNOWN | Not specified in README.md or ARCHITECTURE.md |

## Conservative static load-sharing scenario

As a deliberately conservative static boundary, assign the entire printed target mass to one supporting leg (load fraction λ = 1). If the actual robot mass were within the printed 5–7 kg range, this scenario gives Fleg = λ m g = 1 × (5–7) × 9.81 = 49.05–68.67 N. This is conditional on an unverified artwork target; it is not an operating requirement, validated worst-case gait load or measured mass.

For each joint, τj = Fleg d⊥,j. The perpendicular moment arm d⊥,j is UNKNOWN because the source does not define leg segment lengths, joint frames, pose or coordinates. Therefore no numeric joint torque or S/M/L comparison is supported. Hip-yaw demand depends on its axis, pose and perpendicular moment arm; no back-solved moment arm or arbitrary ±20% sensitivity is used. The one-leg full-weight assumption is conservative as a load-share scenario only, not proof of the largest dynamic hip-yaw torque.

## Not calculated

Payload location, gait, ground reaction, impact, acceleration, speed, duty and actuator variant data are UNKNOWN. No 1.5× multiplier is applied: the source set provides no approved factor or load case.

## References

- [Concept README](../README.md), sections 4, 6 and 9; [ARCHITECTURE.md](../ARCHITECTURE.md), sections 2–3 and 8.
- [Source register](../references/SOURCE_REGISTER.md), SRC-01–SRC-07.
- [DESIGN_GUIDELINES.md](../../../DESIGN_GUIDELINES.md), FREQ-006/007/012 and FREQ-031.
