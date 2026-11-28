# DA-01 — Joint and Actuator Requirements (Week 3/4 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-DA-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Status | PROPOSED — paper estimate; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.4.0 |
| Last Updated | 2026-11-27 |
| Evidence type | C — paper calculation only |

**HOLD D-003 remains active.** No actuator selection, CAD, simulation, bench or physical evidence is claimed. Values below are `CONCEPT_TARGET`, `ASSUMED`, `ESTIMATE`, `TBD` or `UNKNOWN` as stated; none is a released requirement.

## 1. Baseline and axis discrepancy

The concept README / architecture lists 3 DOF per arm and six baseline channels: shoulder yaw, elbow and wrist on each arm. The earlier Week 3 table also listed shoulder pitch, creating four axis labels for a three-DOF arm. This revision does not silently change the baseline: shoulder pitch remains a conditional sensitivity case only until the owner confirms the axis definition. Wrist rotation versus pitch also remains OWNER_DECISION.

## 2. Inputs and assumptions

| Input | Value | Classification |
|---|---:|---|
| Reach, shoulder to gripper | 350 mm | CONCEPT_TARGET; pose and datum undefined |
| Payload per arm | 0.1–0.2 kg | CONCEPT_TARGET; printed estimate, basis unknown |
| Link split for this calculation | 175 / 100 / 75 mm | ASSUMED; totals the printed reach |
| Link / module / gripper masses | 0.12 / 0.30 / 0.08 / 0.18 / 0.12 kg | ESTIMATE; see `CALC-DA01-01` |
| Representative payload | 0.20 kg | CONCEPT_TARGET upper end |
| Gravity | 9.81 m/s² | Calculation constant |
| Angular acceleration | 10 rad/s² | ASSUMED; no trajectory supplied |
| Representative speed | 1.57 rad/s (15.0 rpm) | ASSUMED; not a speed requirement |
| Planning multiplier | 1.5× | ASSUMED; not a validated safety factor |

## 3. Baseline per-joint screening — one arm, mirrored to the other

| Joint instance | Static gravity (N·m) | Inertial estimate (N·m) | Raw sum (N·m) | 1.5× screen (N·m) | Speed input | Torque-only class screen |
|---|---:|---:|---:|---:|---|---|
| Shoulder yaw | ≈ 0 for ideal vertical axis | ≈ 0.638 | ≈ 0.638 | ≈ 0.957 | 1.57 rad/s ASSUMED | S is the smallest proposed band to examine; axis inertia/cable load still uncertain |
| Elbow pitch | ≈ 0.718 | ≈ 0.103 | ≈ 0.821 | ≈ 1.232 | 1.57 rad/s ASSUMED | S torque band is a screening candidate only |
| Wrist pitch branch | ≈ 0.194 | ≈ 0.013 | ≈ 0.208 | ≈ 0.311 | 1.57 rad/s ASSUMED | S torque band only if owner confirms pitch |
| Wrist rotation branch | ≈ 0 static gravity | TBD | TBD | TBD | TBD | No screen until axis and motion are defined |

The same rows apply to left/right arms only under a symmetry assumption. `1.5× screen` is a planning calculation, not a peak requirement, safe working load or actuator selection. Dynamic contact, cable drag, gearbox losses, continuous duty and thermal capability remain UNKNOWN.

## 4. Conditional shoulder-pitch sensitivity — not a baseline joint

The point-mass estimate gives 2.332 N·m static gravity, 0.638 N·m inertial and 2.970 N·m raw sum; 1.5× is 4.455 N·m. This result is available only if an owner-approved shoulder-pitch axis is added or confirmed. It must not be counted as a requirement for the current six-channel baseline.

## 5. Proposed S/M/L family-band screen (not assignment)

| Family band | Proposed continuous torque | Proposed peak torque | Source headline speed | Maturity caveat |
|---|---:|---:|---:|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to ~60 rpm | S data are placeholders |
| Kritva-M | 10 N·m | 20–25 N·m | 45 rpm | M reference is not frozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | ~20–40 rpm | L data are placeholders |

These are parent-repository family-level proposal bands, not verified variant output curves. Headline speed is not demonstrated at the required joint load; thermal, duty, packaging and exact model data remain unavailable.

`KritvaOS/kritva-actuator/docs/architecture/ACTUATOR_FAMILY_SPEC.md` at commit `31bfc20aed0479a3bce64cf8945e86b1fa6f2fa6` gives proposal-level S/M/L ranges. It says S/L values are placeholders; the M reference is not frozen. This is a torque-only screen, not validated actuator compatibility. Speed, envelope, mass, thermal and exact output curves remain unverified. See `references/SOURCE_REGISTER.md` SRC-11.

- The estimated baseline elbow and shoulder-yaw torque screens are below the proposed S band’s lower torque figures; S is only the first family to examine, not a selected model.
- Wrist torque screening is conditional on its axis.
- No baseline shoulder-pitch assignment is made while the DOF discrepancy remains open.

## 6. Open inputs

- Owner decision: shoulder yaw versus an additional shoulder-pitch axis; wrist rotation versus pitch.
- Exact link lengths, joint frames, ROM, speed profile, duty cycle and payload basis are UNKNOWN.
- Exact variant-specific S/M/L data and source-controlled thermal/packaging data are not available.
- Full dynamic model and friction/cable estimates are NOT STARTED; these need defined geometry and trajectory.

No actuator is selected or approved. HOLD D-003 remains in force.
