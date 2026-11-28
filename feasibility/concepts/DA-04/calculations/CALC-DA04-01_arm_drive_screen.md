# CALC-DA04-01 — Payload-Only Arm and Drive Relations

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
| Shoulder-to-gripper reach per arm | 0.450 m | README.md section 4; CONCEPT_TARGET, pose/datum undefined |
| Payload per arm | 0.5–1.0 kg | README.md section 4; CONCEPT_TARGET printed “est.”, basis not supplied |
| Gravity | 9.81 m/s² | Standard-gravity approximation used for arithmetic |
| Baseline arm axes | Shoulder yaw, shoulder pitch, elbow pitch, wrist pitch | README.md section 6 / ARCHITECTURE.md; concept target |
| Base drive | Two drive channels; four wheels shown | README.md section 6; wheel geometry and load distribution TBD |

## Conditional shoulder-pitch payload contribution

For a fully extended horizontal arm, use the printed reach as the perpendicular payload moment arm: τp = mp g r⊥, with r⊥ = 0.450 m.

- At 0.5 kg payload: 0.5 × 9.81 × 0.450 = 2.207 N·m.
- At 1.0 kg payload: 1.0 × 9.81 × 0.450 = 4.415 N·m.

These are conditional payload-only contributions at the shoulder-pitch axis, not total shoulder torque or actuator requirements. The printed targets have no stated basis; link, joint, gripper and harness masses, joint offsets, friction, acceleration, duty and pose are unavailable. The shoulder-yaw static gravity component is zero in an ideal vertical-axis model; its inertial and cable loads remain UNKNOWN. Elbow/wrist torques cannot be computed without link geometry and masses.

## Differential-drive relation

Per drive channel, an idealized wheel torque relation is τwheel = Ftraction rwheel. Neither wheel radius, load distribution, friction, slope, acceleration, motor/gearbox candidate nor required travel speed is specified by the current concept record. Therefore no numeric wheel torque is reported.

## References

- [Concept README](../README.md), sections 4, 6 and 9; [ARCHITECTURE.md](../ARCHITECTURE.md), sections 2–3 and 8.
- [Source register](../references/SOURCE_REGISTER.md), SRC-01–SRC-07.
- [DESIGN_GUIDELINES.md](../../../DESIGN_GUIDELINES.md), FREQ-006/007/012.
