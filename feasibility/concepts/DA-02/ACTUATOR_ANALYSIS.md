# DA-02 — Actuator Analysis

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-DA-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Joint and Actuator Feasibility Analysis |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.0 |
| Last Updated | 2026-11-25 |
| Authority | Preliminary paper analysis; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `feasibility/DESIGN_GUIDELINES.md` |

## 1. Scope and Assumptions

- Concept ID: DA-02 (Humanoid Torso Dual-Arm)
- Supply direction: 24V DC investigation only (concept-level indication from the concept sheet, not a confirmed electrical interface)
- Motor direction: BLDC/PMSM
- Actuator architecture: S/M/L (no joint has been mapped to S, M or L yet)
- Joints in scope: shoulder yaw, shoulder pitch, elbow pitch, wrist pitch (per arm, left and right symmetric, so one analysis covers both); optional gripper and optional head pan are listed but not sized
- Baseline actuator count: 8 arm actuators; 9 when the optional head pan is fitted (D6 resolved 2026-10-31)
- Evidence type: C (paper calculation). Nothing here is approved or validated.

### 1.1 Input values taken from the README (CONCEPT_TARGET, unapproved)

| Item | Value as printed |
|---|---|
| Arm reach (shoulder to gripper) | 350 mm |
| Target payload (each arm) | 0.1 – 0.2 kg (est.) |
| Target weight | 8 – 12 kg (est.) |
| Shoulder-to-shoulder spacing | 600 mm (concept sheet only; D5 not verifiable) |

### 1.2 Intern assumptions (ASSUMED, not printed on any sheet)

The sheets give no link lengths, link masses, ranges, speeds or duty. The values below are planning assumptions so that the method can be exercised. Replace them once `MASS_BUDGET.md` and `ARCHITECTURE.md` exist.

| ID | Assumption | Value |
|---|---|---|
| A1 | Gravity | 9.81 m/s² |
| A2 | Worst-case pose | Arm fully extended horizontally (all pitch joints at 90° to gravity) |
| A3 | Link split of the 350 mm reach | Upper arm (shoulder pitch to elbow) 175 mm; forearm (elbow to wrist) 100 mm; wrist to gripper tip 75 mm |
| A4 | Upper arm link mass (excludes joint modules), CoM at mid-length | 0.15 kg at 87.5 mm from shoulder |
| A5 | Elbow joint module mass, at elbow axis | 0.35 kg at 175 mm |
| A6 | Forearm link mass, CoM at mid-length | 0.10 kg at 50 mm from elbow |
| A7 | Wrist joint module mass, at wrist axis | 0.20 kg at 100 mm from elbow |
| A8 | Gripper and mount mass, CoM 40 mm beyond wrist axis | 0.15 kg |
| A9 | Payload, at gripper tip | 0.2 kg (worst) and 0.1 kg (low) |
| A10 | Shoulder pitch module sits on the pitch axis, so it adds no static torque to itself; its mass is carried by shoulder yaw only as inertia and is neglected here | n/a |
| A11 | Yaw and pitch shoulder axes intersect (no offset) | UNKNOWN in the artwork; see Section 5 |
| A12 | Planning output speed | 90 °/s (1.57 rad/s) at every arm joint |
| A13 | Planning angular acceleration | 10 rad/s² (reaches A12 in about 0.16 s) |
| A14 | Planning factor on required torque | 1.5× (covers friction, gearbox efficiency, cable drag, mass growth; not a validated margin) |

## 2. Per-Joint Assessment

All torques are output-shaft torques per joint, one arm, worst case at 0.2 kg payload unless stated. Static torque is gravity holding torque at pose A2. Peak = static + inertial (I·α, with α from A13). Values are **calculated from assumptions A1–A14 and are estimates**.

| Joint | Load case | Peak torque | Continuous torque | Speed | Range | Duty assumptions | Calculation reference | S/M/L compatibility | Margin | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Shoulder yaw (each arm) | Arm extended, rotating about vertical axis; no gravity torque in this pose | ≈ 0.71 N·m (inertial only, I ≈ 0.071 kg·m², α = 10 rad/s²) | ≈ 0 N·m static; friction and cable torque TBD | 1.57 rad/s (A12, assumed) | TBD | TBD | CALC-DA02-01 §4 (to be filed in `calculations/`) | TBD (not mapped) | TBD | ESTIMATE |
| Shoulder pitch (each arm) | Arm fully extended horizontal, 0.2 kg at tip | ≈ 3.35 N·m (2.64 static + 0.71 inertial) | ≈ 2.64 N·m (holding) | 1.57 rad/s (A12, assumed) | TBD | TBD | CALC-DA02-01 §1 | TBD (not mapped) | TBD | ESTIMATE |
| Elbow pitch (each arm) | Forearm horizontal, 0.2 kg at tip | ≈ 0.91 N·m (0.80 static + 0.11 inertial) | ≈ 0.80 N·m (holding) | 1.57 rad/s (A12, assumed) | TBD | TBD | CALC-DA02-01 §2 | TBD (not mapped) | TBD | ESTIMATE |
| Wrist pitch (each arm) | Gripper horizontal, 0.2 kg at tip | ≈ 0.22 N·m (0.21 static + 0.01 inertial) | ≈ 0.21 N·m (holding) | 1.57 rad/s (A12, assumed) | TBD | TBD | CALC-DA02-01 §3 | TBD (not mapped) | TBD | ESTIMATE |
| Gripper (each arm, optional) | Not sized; actuation type and count TBD, may be passive | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | NOT STARTED |
| Head pan (optional, 1 actuator) | Pan about vertical axis; camera mass and neck geometry not printed | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | NOT STARTED |

### 2.1 Required torque with planning factor (A14, 1.5×)

This is the figure to compare with S/M/L data once the owner supplies it. It is not a requirement.

| Joint | Peak × 1.5 | Continuous × 1.5 |
|---|---|---|
| Shoulder yaw | ≈ 1.1 N·m | TBD (friction-dominated) |
| Shoulder pitch | ≈ 5.0 N·m | ≈ 4.0 N·m |
| Elbow pitch | ≈ 1.4 N·m | ≈ 1.2 N·m |
| Wrist pitch | ≈ 0.33 N·m | ≈ 0.31 N·m |

### 2.2 Low-payload case (0.1 kg at tip), static torque

| Joint | Static torque |
|---|---|
| Shoulder pitch | ≈ 2.30 N·m |
| Elbow pitch | ≈ 0.62 N·m |
| Wrist pitch | ≈ 0.13 N·m |

### 2.3 Hand calculation (CALC-DA02-01 summary)

Static torque is the sum of mass × distance × g about each joint axis. Distances are measured from the joint axis along the extended arm.

**§1 Shoulder pitch.** Σ m·d = 0.15(0.0875) + 0.35(0.175) + 0.10(0.225) + 0.20(0.275) + 0.15(0.315) + 0.20(0.350) = 0.2691 kg·m. T = 0.2691 × 9.81 = **2.64 N·m**.

**§2 Elbow pitch.** Σ m·d = 0.10(0.050) + 0.20(0.100) + 0.15(0.140) + 0.20(0.175) = 0.0810 kg·m. T = 0.0810 × 9.81 = **0.795 N·m**.

**§3 Wrist pitch.** Σ m·d = 0.15(0.040) + 0.20(0.075) = 0.0210 kg·m. T = 0.0210 × 9.81 = **0.206 N·m**.

**§4 Inertia and dynamic torque.** Point-mass inertia I = Σ m·d², link self-inertia neglected.
- About shoulder (yaw and pitch, same value in pose A2): I ≈ 0.0714 kg·m², so I·α = **0.71 N·m**.
- About elbow: I ≈ 0.0113 kg·m², I·α = **0.11 N·m**.
- About wrist: I ≈ 0.00137 kg·m², I·α = **0.014 N·m**.

**Mechanical power check (not simultaneous peaks):** shoulder pitch 3.35 N·m × 1.57 rad/s ≈ 5.3 W at output, before gearbox and motor efficiency.

### 2.4 Sensitivity to the biggest unknown

The largest uncertainty is the joint module mass (A5, A7), because real S/M/L units with gearbox and encoder may be much heavier than assumed. Example: if the elbow module were 1.0 kg instead of 0.35 kg, shoulder pitch static torque rises by 0.65 × 0.175 × 9.81 ≈ **1.1 N·m** (about 40%). Re-run this sheet once actual module masses are known.

## 3. Reference Limitations

The elbow discussion reference of 24V, 10 N·m continuous and 20 N·m peak is not a universal specification. It has **not** been used in or copied into this analysis. Every joint above is derived independently from the DA-02 geometry and the stated assumptions. The calculated DA-02 elbow estimate (≈ 0.8 N·m continuous) should not be read as a comparison with, or a challenge to, that reference; the two come from different loads and unknown assumptions.

## 4. Actuator Source Traceability

No input from `kritva-actuator` has been supplied for DA-02 yet. All S/M/L data fields stay open.

- Source repository and path: TBD (none supplied)
- Revision / commit: TBD
- Source document or specification: TBD
- Maturity: UNKNOWN
- Verification status and limitations: None. The concept sheet calls the actuators "Kritva S/M/L compatible", but this study has not mapped any joint to S, M or L. Preliminary repository values, when received, must not be treated as validated specifications.

## 5. Findings and Open Items

- **Torque/speed feasibility:** Not assessable. The preliminary estimates show shoulder pitch as the most demanding joint (≈ 2.6 N·m holding, ≈ 3.4 N·m peak at 0.2 kg), roughly 3× the elbow and 12× the wrist. Feasibility cannot be stated until S/M/L torque and speed data exist.
- **S/M/L mapping rationale:** NOT STARTED. The large spread between joints (about 0.2 to 5 N·m with planning factor) suggests one size may not suit all four joints, but this is an observation, not a mapping.
- **Margin interpretation:** TBD. Margin is only meaningful as (actuator rating ÷ required torque from Section 2.1) once ratings are supplied. The 1.5× factor is a planning placeholder.
- **Missing inputs and risks:**
  1. Link lengths, link masses and module masses are assumed (A3–A8); no `MASS_BUDGET.md` exists.
  2. Joint range, speed and duty cycle are not printed on either sheet (A12, A13 assumed).
  3. Shoulder yaw/pitch axis intersection or offset is UNKNOWN (A11); an offset would add a static moment about yaw and change workspace.
  4. Payload (0.1 – 0.2 kg) and reach (350 mm) targets have no stated basis; they remain CONCEPT_TARGET.
  5. Gripper actuation (powered or passive) is an open decision; a powered gripper changes the wrist and elbow loads (A8).
  6. Head pan (optional) is not sized; camera mass and neck geometry are TBD.
  7. Gearbox efficiency, backdrive and holding-torque strategy (brake or continuous current) are not assessed.
  8. Thermal and continuous-current limits at 24 V DC are not assessed.
  9. Cable drag across four joints per arm (see README Section 8) is not included in the torque figures beyond the 1.5× factor.
- **Next steps (paper only):** obtain S/M/L data with traceability from `kritva-actuator`; replace assumed masses with the mass budget; add range and duty assumptions; sweep pose (not just fully extended) for peak torque; file CALC-DA02-01 in `calculations/`.

## 6. HOLD D-003

Paper calculations and compatibility assessment only. No actuator purchase, detailed CAD, final BOM, fabrication, assembly or physical testing. All require explicit owner decision under HOLD D-003.
