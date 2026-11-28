# DA-04 — Mechanical Assessment (Week 3)

**Version 0.3.0 | 2026-11-27 | INTERN-01 | HOLD D-003**

## Configuration
Humanoid torso on differential-drive base, two 4-DOF arms, 10 actuators baseline, fixed head.

## Stability notes (ESTIMATE)
- Base footprint and wheelbase still CONCEPT_TARGET / ASSUMED.
- Extended dual-arm payload creates a significant pitching moment about the wheel axis.
- First-order check: with nominal 12 kg and arms fully forward, restoring moment from CoM location may be marginal on a 5° slope or during acceleration.
- Recommendation: keep arms folded during base transit; define explicit tip-over criteria once geometry is frozen.

## Structure
- Torso must react full arm loads plus dynamic base accelerations.
- Shoulder and torso interface is the critical structural joint.
- No stress numbers claimed.

## Drive
- Traction and turning loads derived in ACTUATOR_ANALYSIS under ASSUMED wheel radius and mass.
- Floor friction and slope requirements remain TBD.
