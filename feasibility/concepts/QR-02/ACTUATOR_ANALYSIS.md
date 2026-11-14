# QR-02 — Joint and Actuator Requirements (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Scope

Week 2 records every baseline joint/channel and makes missing actuator requirements explicit. Week 3 is scheduled for torque/speed calculations and actuator assessment. This file does not select or validate an actuator.

Preserve:
- BLDC/PMSM modular rotary actuator direction.
- Option C mechanical direction.
- S/M/L architecture; do not redefine size classes.
- 24 V DC as investigation direction only, not a finalized system voltage.
- Existing elbow reference (24 V, 10 N·m continuous, 20 N·m peak) is specific to that elbow discussion and must not be copied to any other joint.

## 2. Per-joint requirements matrix

| Joint instance | Motion | Qty | ROM | Continuous torque | Peak torque | Output speed | Duty cycle | Gear ratio | Technology shown | S/M/L / evidence status |
|---|---|---|---|---|---|---|---|---|---|---|
| Front-left hip abduction/adduction | Abduction / adduction | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Front-right hip abduction/adduction | Abduction / adduction | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Rear-left hip abduction/adduction | Abduction / adduction | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Rear-right hip abduction/adduction | Abduction / adduction | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Front-left hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Front-right hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Rear-left hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Rear-right hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Front-left knee | Flexion / extension | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Front-right knee | Flexion / extension | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Rear-left knee | Flexion / extension | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |
| Rear-right knee | Flexion / extension | 1 | TBD | TBD | TBD | TBD | TBD | TBD | BLDC/PMSM with gearbox, as shown | TBD — no per-joint derivation / actuator comparison yet |

The quantity rows enumerate physical joint instances. `TBD` is intentional: the source does not give range, torque, speed, gear ratio or duty cycle for these joints. Every joint must receive a separate Week 3 derivation or remain explicitly `TBD`.

## 3. Required load and motion inputs

- Source-revision-controlled actuator geometry, mass, mounting interface, continuous/peak torque curves, speed limits, thermal/duty envelope and gearbox data from the actuator owner.
- Concept-specific link dimensions, offsets, joint coordinate frames, centre-of-mass and inertia assumptions.
- Payload/mass distribution and representative operating poses.
- Motion profile: joint range, angular velocity, acceleration, duty cycle and expected transient events.
- For legged concepts: support phase, ground reaction, foot placement, terrain/contact assumptions, gait/stride and impact/transient assumptions.
- For DA-04 wheel channels: wheel radius, wheelbase/track, total mass, load distribution, slope, acceleration, floor friction and desired travel speed.

## 4. Calculation methods to use when inputs exist

State the engineering question, inputs, source revision, units and assumptions before calculation. Do not substitute assumed numbers.

**Static gravity/load moment (joint axis projection):**

\`tau_static = sum((r_i × F_i) · e_axis)\`

where each moment arm vector `r_i` and force `F_i` is in SI units and `e_axis` is the defined unit vector of the joint axis. Inputs are presently `TBD`.

**Dynamic joint demand (conceptual rigid-body form):**

\`tau_required(q, qdot, qddot) = M(q) qddot + C(q,qdot) qdot + g(q) + tau_external + tau_friction\`

This requires a defined kinematic model, mass/inertia parameters, motion profile and external loads; none is complete in Week 2.

**Speed:**

\`omega = delta_theta / delta_t\`

or derive joint rates from a specified end-effector/foot trajectory and Jacobian. No trajectory, time interval or joint range is specified; required speed remains `TBD`.

**Actuator comparison:** compare per-joint continuous and peak torque, output speed, range, duty/thermal limits, mass/envelope, mounting interface and documented margins against the source-revision-controlled S/M/L candidate data. Do not assign S/M/L from joint function or the elbow reference.

## 5. Week 3 carry-forward

For each row, populate results only when inputs are available. Include formula, substitutions, units, result, uncertainty/sensitivity, source commit/revision and limitations. If any input is missing, retain `TBD` or `BLOCKED` with a named dependency. S/M/L remains `TBD` until requirements are derived and data is source-controlled.

## 6. Related requirements and unknowns

- FREQ-009, FREQ-010, FREQ-011, FREQ-012, FREQ-013, FREQ-014.
- FREQ-026 and FREQ-027 for dual-arm concepts; FREQ-029 and FREQ-031 for legged concepts.
- U-007 (joint torque/speed) and U-008 (joint-to-actuator S/M/L mapping).
- Existing global risk FRISK-001 (legged-joint torque capability) and FRISK-005 (actuator source maturity), where applicable.
