# DA-01 — Joint and Actuator Requirements (Week 3/4 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-DA-01 |
| Repository | KritvaOS/kritva-mechanical |
| Status | PROPOSED — paper estimate; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.5.0 |
| Last Updated | 2026-11-28 |
| Evidence type | C — paper calculation only |

HOLD D-003 remains active. No actuator selection, CAD, simulation, bench or physical evidence is claimed. Values are CONCEPT_TARGET, ASSUMED, ESTIMATE, TBD or UNKNOWN as stated; none is a released requirement.

## 1. Baseline and axis discrepancy

The concept README / architecture lists 3 DOF per arm and six baseline channels: shoulder yaw, elbow and wrist on each arm. The earlier Week 3 table also listed shoulder pitch, creating four axis labels for a three-DOF arm. Shoulder pitch remains a conditional sensitivity case only until the owner confirms the axis definition. Wrist rotation versus pitch also remains OWNER_DECISION.

## 2. Inputs and assumptions

| Input | Value | Classification |
|---|---:|---|
| Reach, shoulder to gripper | 350 mm | CONCEPT_TARGET; pose and datum undefined |
| Payload per arm | 0.1–0.2 kg | CONCEPT_TARGET; printed estimate, basis unknown |
| Link split for this calculation | 175 / 100 / 75 mm | ASSUMED; totals 350 mm |
| Upper-arm / elbow / forearm / wrist / gripper masses | 0.12 / 0.30 / 0.08 / 0.20 / 0.12 kg | ESTIMATE; wrist module now agrees with the 0.20–0.45 kg mass-budget range |
| Representative payload | 0.20 kg | CONCEPT_TARGET upper end |
| Gravity | 9.81 m/s² | Calculation constant |
| Angular acceleration | 10 rad/s² | ASSUMED; no trajectory |
| Representative speed | 1.57 rad/s (15.0 rpm) | ASSUMED; not a speed requirement |
| Planning multiplier | 1.5× | ASSUMED; not a validated safety factor |

## 3. Baseline per-joint screening — one arm, mirrored to the other

| Joint instance | Static gravity (N·m) | Inertial estimate (N·m) | Raw sum (N·m) | 1.5× screen (N·m) | Speed input | Torque-only class screen |
|---|---:|---:|---:|---:|---|---|
| Shoulder yaw | ≈ 0 for ideal vertical axis | ≈ 0.653 | ≈ 0.653 | ≈ 0.980 | 1.57 rad/s ASSUMED | S is the smallest proposed band to examine; axis inertia/cable load uncertain |
| Elbow pitch | ≈ 0.738 | ≈ 0.105 | ≈ 0.843 | ≈ 1.264 | 1.57 rad/s ASSUMED | S torque band is a screening candidate only |
| Wrist pitch branch | ≈ 0.194 | ≈ 0.013 | ≈ 0.207 | ≈ 0.311 | 1.57 rad/s ASSUMED | S torque band only if owner confirms pitch |
| Wrist rotation branch | ≈ 0 static gravity | TBD | TBD | TBD | TBD | No screen until axis and motion are defined |

The same rows apply to left/right arms only under a symmetry assumption. The 1.5× screen is a planning calculation, not a peak requirement, safe working load or actuator selection. Dynamic contact, cable drag, gearbox losses, continuous duty and thermal capability remain UNKNOWN.

## 4. Conditional shoulder-pitch sensitivity — not a baseline joint

The updated point-mass estimate gives 2.386 N·m static gravity, 0.653 N·m inertial and 3.039 N·m raw sum; 1.5× is 4.558 N·m. This result applies only if an owner-approved shoulder-pitch axis is added or confirmed. It is not counted in the current six-channel baseline.

## 5. Proposed S/M/L family-band screen (not assignment)

The parent family specification is proposal-level. S/L values are placeholders and the M reference is not frozen. This is a torque-only screen, not validated actuator compatibility; speed at required load, envelope, mass, thermal and exact output curves remain unverified. See references/SOURCE_REGISTER.md SRC-11.

| Family band | Proposed continuous torque | Proposed peak torque | Source headline speed | Maturity caveat |
|---|---:|---:|---:|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to ~60 rpm | S values are placeholders |
| Kritva-M | 10 N·m | 20–25 N·m | 45 rpm | M reference is not frozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | ~20–40 rpm | L values are placeholders |

Headline speed is not demonstrated at the required joint load. The baseline elbow and shoulder-yaw screens are below the proposed S band’s lower torque figures, making S only the first family to examine. Wrist screening depends on axis confirmation. No model or compatibility is selected.

## 6. Open inputs

- Owner decision: shoulder yaw versus an additional shoulder-pitch axis; wrist rotation versus pitch.
- Exact link lengths, joint frames, ROM, speed profile, duty cycle and payload basis are UNKNOWN.
- Exact variant-specific S/M/L data and source-controlled thermal/packaging data are not available.
- Full dynamic model and friction/cable estimates are NOT STARTED; these need defined geometry and trajectory.

No actuator is selected or approved. HOLD D-003 remains in force.
