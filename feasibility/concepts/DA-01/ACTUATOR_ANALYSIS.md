# DA-01 — Joint and Actuator Requirements (Week 3 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-DA-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Joint and Actuator Feasibility Analysis |
| Status | PROPOSED — Week 3 paper calculation; subject to owner review |
| Owner | Dinesh |
| Assigned Intern | INTERN-01 |
| Version | 0.3.0 |
| Last Updated | 2026-11-27 |
| Authority | Preliminary paper analysis; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `MASS_BUDGET.md`, `feasibility/DESIGN_GUIDELINES.md` |

**HOLD:** Mechanical HOLD D-003 remains active. No actuator selection, S/M/L assignment or procurement is authorised.

**Evidence boundary:** Paper calculation only. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`. Planning numbers introduced by the intern are tagged `ASSUMED` or `ESTIMATE`. Missing quantities remain `TBD` / `UNKNOWN` / `OWNER_DECISION`.

## 1. Scope and preserved directions

- Concept: Fixed Tabletop Dual-Arm (Low complexity)
- Baseline actuator count: 6 (3 DOF × 2 arms). Optional powered grippers and optional mast are excluded from the baseline.
- Motor direction: BLDC/PMSM modular rotary actuators (preserved).
- Actuator architecture: S/M/L (no joint has been mapped yet).
- Supply investigation direction: 24 V DC only (not a confirmed electrical interface).
- Existing elbow reference (24 V, 10 N·m continuous, 20 N·m peak) is **not** copied to any joint.
- Option C mechanical direction preserved.

## 2. CONCEPT_TARGET inputs (from artwork / README)

| Item | Value | Classification |
|---|---|---|
| Arm reach (shoulder to gripper) | 350 mm | CONCEPT_TARGET; pose/datum undefined |
| Target payload (each arm) | 0.1–0.2 kg (est.) | CONCEPT_TARGET |
| Target robot mass | 5–8 kg (est.) | CONCEPT_TARGET |
| Overall width / height / base | 700 mm / 400 mm / 300×250 mm | CONCEPT_TARGET |
| DOF per arm | 3 (shoulder yaw, elbow pitch, wrist pitch/rotation ambiguity) | CONCEPT_TARGET; wrist axis OWNER_DECISION (D4) |

## 3. Intern planning assumptions (ASSUMED — replace when better data exists)

These values exist only so that the calculation method can be exercised. They are **not** requirements.

| ID | Assumption | Value | Rationale / source |
|---|---|---|---|
| A1 | Gravity | 9.81 m/s² | Standard |
| A2 | Worst-case gravity pose | Arm fully extended horizontally (shoulder & elbow at 90° to gravity) | Conservative static case for tabletop pick-and-place |
| A3 | Link length split of 350 mm reach | Upper arm (shoulder→elbow) 175 mm; forearm (elbow→wrist) 100 mm; wrist→gripper tip 75 mm | Equal-ish split of printed reach; no printed link lengths |
| A4 | Upper-arm link mass (ex-joint), CoM mid-length | 0.12 kg at 87.5 mm from shoulder | ESTIMATE for aluminium/CNC or printed link at this scale |
| A5 | Elbow joint module mass | 0.30 kg at elbow axis | ESTIMATE pending S/M/L data |
| A6 | Forearm link mass, CoM mid-length | 0.08 kg at 50 mm from elbow | ESTIMATE |
| A7 | Wrist joint module mass | 0.18 kg at wrist axis | ESTIMATE |
| A8 | Gripper + mount mass (optional, passive baseline) | 0.12 kg at 40 mm beyond wrist | ESTIMATE; passive gripper assumed for baseline |
| A9 | Payload mass (high end of printed range) | 0.20 kg at gripper tip | CONCEPT_TARGET upper bound |
| A10 | Representative joint speed | 1.57 rad/s (90° in 1 s) | ASSUMED planning value; no trajectory given |
| A11 | Representative angular acceleration | 10 rad/s² | ASSUMED; reaches A10 in ~0.16 s |
| A12 | Planning factor on required torque | 1.5× | Covers friction, gearbox efficiency, cable drag, mass growth; not a validated margin |

## 4. Per-joint torque demand (output shaft, one arm, 0.2 kg payload)

Static gravity torque at pose A2 uses moment arms about each joint axis. Inertial contribution uses a simplified rigid-body estimate I·α with α = A11. All results are **ESTIMATE**.

| Joint | Static torque (N·m) | Inertial (N·m) | Peak (N·m) | Continuous (holding) | Speed (rad/s) | Calc ref | S/M/L | Status |
|---|---:|---:|---:|---:|---:|---|---|---|
| Shoulder yaw | ≈ 0 (vertical axis) | ≈ 0.55 | ≈ 0.55 | friction / cable TBD | 1.57 (A10) | CALC-DA01-01 | TBD | ESTIMATE |
| Shoulder pitch | ≈ 2.15 | ≈ 0.55 | ≈ 2.70 | ≈ 2.15 | 1.57 | CALC-DA01-01 | TBD | ESTIMATE |
| Elbow pitch | ≈ 0.68 | ≈ 0.09 | ≈ 0.77 | ≈ 0.68 | 1.57 | CALC-DA01-01 | TBD | ESTIMATE |
| Wrist (pitch or rotation) | ≈ 0.18 | ≈ 0.01 | ≈ 0.19 | ≈ 0.18 | 1.57 | CALC-DA01-01 | TBD | ESTIMATE |

### 4.1 Required torque after planning factor (A12 = 1.5×)

| Joint | Peak × 1.5 (N·m) | Continuous × 1.5 (N·m) |
|---|---:|---:|
| Shoulder yaw | ≈ 0.83 | TBD (friction-dominated) |
| Shoulder pitch | ≈ 4.05 | ≈ 3.23 |
| Elbow pitch | ≈ 1.16 | ≈ 1.02 |
| Wrist | ≈ 0.29 | ≈ 0.27 |

These figures are the quantities to compare against source-controlled S/M/L candidate data once the actuator owner supplies it. They are **not** requirements and do **not** select an actuator.

### 4.2 Low-payload check (0.1 kg)

Static shoulder-pitch torque drops to ≈ 1.65 N·m; elbow ≈ 0.52 N·m; wrist ≈ 0.12 N·m. Order of magnitude is unchanged.

## 5. Calculation method summary (CALC-DA01-01)

**Static gravity moment about joint axis**

```
τ_static = Σ (r_i × m_i g) · e_axis
```

where r_i is the position of each distal mass relative to the joint, e_axis is the unit vector of the joint axis, and g = 9.81 m/s².

For shoulder pitch at full horizontal extension the dominant terms are:

- payload 0.20 kg × 0.350 m
- gripper 0.12 kg × 0.310 m
- wrist module 0.18 kg × 0.275 m
- forearm 0.08 kg × 0.225 m
- elbow module 0.30 kg × 0.175 m
- upper-arm 0.12 kg × 0.0875 m

yielding ≈ 2.15 N·m (rounded).

**Inertial contribution (simplified)**

Approximate I about the joint from point-mass contributions and multiply by α = 10 rad/s².

Full expansion, sensitivity tables and unit checks live in `calculations/CALC-DA01-01_joint_torque.md`.

## 6. Speed, ROM, duty cycle

- ROM: still TBD / OWNER_DECISION (wrist axis ambiguity D4).
- Speed: only the planning value A10 is available; no trajectory or cycle time is specified.
- Duty: TBD. Tabletop pick-and-place is expected to be intermittent; continuous rating should still be sized for the holding case plus margin.

## 7. S/M/L mapping status

**Not started.** Mapping requires:

1. Derived continuous and peak torque (this file).
2. Source-controlled S/M/L mass, envelope, continuous/peak torque, speed and thermal data from the actuator repository (commit/revision controlled).
3. Owner review of margins and packaging.

Until those exist, every joint remains “TBD — no S/M/L assignment”.

## 8. Risks and open items carried forward

- Wrist axis (rotation vs pitch) remains OWNER_DECISION (D4).
- Link lengths, joint offsets and coordinate frames remain UNKNOWN.
- Actuator source data maturity is a global risk (FRISK-005).
- Cable routing torque and friction not yet quantified.
- Optional powered gripper would add a seventh actuator channel per arm; currently excluded.

See `OPEN_QUESTIONS.md` for the full decision register.

## 9. Week 3 status for this concept

| Item | Status |
|---|---|
| Joint instance list | Complete (Week 2) |
| Assumption set for calculation | Documented (this revision) |
| Static + inertial torque estimates | ESTIMATE produced |
| S/M/L comparison | BLOCKED on actuator source data |
| Speed / ROM / duty | Still TBD |
| Calculation file | CALC-DA01-01 drafted |

Mechanical HOLD D-003 remains in force. No actuator is selected or approved.
