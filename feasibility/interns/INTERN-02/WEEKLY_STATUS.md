# INTERN-02 — Weekly Feasibility Status

| Property | Value |
|---|---|
| Document ID | KMECH-WEEKLY-INTERN-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Intern Weekly Status |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.1.0 |
| Last Updated | TBD (set on commit) |
| Authority | Weekly progress report; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/INTERN_ASSIGNMENTS.md` |

## 1. Reporting Period

- Intern: INTERN-02
- Week: TBD (confirm 1 / 2 / 3 / 4)
- Reporting dates: TBD
- Branch: `feasibility/intern-02`
- Commit references: TBD (add after commit)

## 2. Concepts Worked

Assigned concepts: QR-01, DA-02, DA-03, QR-05.

| Concept ID | Planned activity | Actual activity | Status |
|---|---|---|---|
| QR-01 | Leg kinematic sketch with joint axes, coordinate frames and foot workspace (README §11, evidence C) | Drew the planar 2-DOF leg side view with hip O, knee K and foot F, the x/z frame and θ1/θ2 definitions. Wrote forward and inverse kinematics. Computed four poses and the foot workspace. Added a top view of hip layout against the printed 300 × 250 mm body and 420 × 400 mm overall extents. | COMPLETE (draft, pending owner review) |
| QR-01 | Static joint torque estimate (stand and lifted-leg poses) | Not started | NOT STARTED |
| DA-02 | Start §11 activities (torso layout, four-axis arm kinematic sketch) | Reviewed the DA-02 README only. Noted open points (see §5 and §6). No §11 activity started. | NOT STARTED |
| DA-03 | Start §11 activities (paired-drive sketch, three-axis arm kinematic sketch, tipping margin) | Reviewed the DA-03 README only. Noted open points (see §5 and §6). No §11 activity started. | NOT STARTED |
| QR-05 | Start §11 activities (module kinematic sketches, interface sketch) | Reviewed the QR-05 README only. Noted open points (see §5 and §6). No §11 activity started. | NOT STARTED |

## 3. Deliverables vs Plan

| Planned deliverable | Actual result / evidence | Status |
|---|---|---|
| QR-01 leg kinematic sketch (axes, frames, workspace) | `sketches/QR-01_leg_kinematic_sketch.png` (side view with workspace, plus top view) and `sketches/QR-01_single_leg_kinematic_diagram.png` (single-leg annotated diagram). Evidence type C. | COMPLETE (draft) |
| QR-01 kinematics write-up | Draft section for `MECHANICAL_ANALYSIS.md`: frames, FK/IK equations, pose table, workspace, assumptions A1–A5, observations. Evidence type C. | COMPLETE (draft) |
| QR-01 static joint torque estimate | Not started | INCOMPLETE |
| QR-01 stability margin, mass budget, body layout, cable path, cost assumptions | Not started | INCOMPLETE |

## 4. Blocked and Incomplete Items

| Item | Status | Reason | Dependency / action |
|---|---|---|---|
| QR-01 torque estimate | INCOMPLETE | Depends on confirmed link lengths and a body mass basis | Owner to confirm or replace assumptions A1–A5; then proceed |
| QR-01 foot lateral offset | INCOMPLETE | Overall width 400 mm implies about 75 mm sideways foot offset; a planar 2-DOF leg cannot produce it and the sheets do not show how it is built | Owner decision (see §5) |
| Other QR-01 §11 items | INCOMPLETE | Sequenced after torque estimate | Proceed in README §11 order |
| QR-05 §11 activities | NOT STARTED | Time went to QR-01 first | Start with the kinematic sketch for 2-DOF and 3-DOF modules |
| DA-02 §11 activities | NOT STARTED | Time went to QR-01 first | Start with the four-axis arm kinematic sketch |
| DA-03 §11 activities | NOT STARTED | Time went to QR-01 first | Start with the three-axis arm kinematic sketch and the paired-drive sketch |

## 5. Unknowns and Assumptions

- New or unresolved unknowns:
  - How the 75 mm lateral foot offset implied by the 400 mm overall width is realised for a planar 2-DOF leg.
  - Standing hip height and whether the 200 mm body height includes the leg.
  - Which knee configuration (knee-back or knee-forward) is intended.
  - Basis for the printed 2.5–4 kg weight.
  - QR-05: the 560 × 520 mm overall footprint implies about 130 mm sideways foot offset, which only the 3-DOF module's abduction joint could explain; the 2-DOF module cannot.
  - QR-05: the 4–6 kg weight is stated for 12 DOF only; the 8-DOF case has no weight.
  - DA-02: shoulders are 600 mm apart on a 300 mm wide torso (about 150 mm outboard of each torso edge); the supporting structure is not shown.
  - DA-02: the 800 mm arm-to-arm width is ambiguous (it cannot be full reach, since 600 mm spacing plus 350 mm reach would be about 1,300 mm).
  - DA-02: the arm has no roll axis (yaw, pitch, elbow pitch, wrist pitch), so gripper orientation is limited.
  - DA-02 README §9 still lists D6 as open and mentions an adjustable mast; both appear stale.
  - DA-03: four wheels driven as a left pair and a right pair behave as skid steer; scrub in turns and turning behaviour are unassessed.
  - DA-03: battery capacity is not stated, so runtime cannot be estimated; weight (12–18 kg) and payload have no stated basis.
  - DA-03: 350 mm reach, 800 mm width and 800 mm total reach cannot be reconciled without the shoulder spacing (D5).
  - DA-03: an emergency-stop button appears on the concept render but is not listed on either sheet.
  - DA-03 open artwork items: D3 (wrist labelled rotation/pitch), D4 (LiDAR), D6 (torso width and adjustable mast).
  - QR-05: the leg-module mounting interface (4 × M5, 2 × Ø5 mm dowels) is indicative and on the cross-section only (D6, open).
- Assumptions requiring confirmation (all intern assumptions, not from any approved source):
  - A1: thigh L1 = shank L2 = 120 mm.
  - A2: standing hip height H = 180 mm.
  - A3: hip axes at X = ±125 mm, Y = ±125 mm.
  - A4: joint limits of ±90° at the hip and 0°–150° at the knee.
  - A5: knee-back configuration.
- Values marked TBD / UNKNOWN: joint torque, speed, stride, battery capacity, camera models, S/M/L mapping, and all requirements-register values remain TBD / UNKNOWN. None of the above assumptions approves any value.

## 6. Risks Raised

| Risk ID | Description | Impact | Proposed mitigation |
|---|---|---|---|
| R-QR01-01 | Planar 2-DOF leg gives no lateral motion, and the sheets do not explain the lateral foot offset implied by the 420 × 400 mm extents | Gait and task capability, and the footprint claim, cannot be verified | Owner to confirm intended leg structure; record in `OPEN_QUESTIONS.md` |
| R-QR01-02 | Link lengths and hip height are intern assumptions | Torque and workspace results may change if replaced | Owner review of A1–A5 before the torque estimate |
| R-QR05-01 | The modular claim has no interface definition on the concept sheet; torque path, connector and 2-DOF/3-DOF swap are UNKNOWN | The modularity concept cannot be assessed | Sketch the interface (QR-05 §11) and list the open points for the owner |
| R-DA02-01 | Shoulder spacing (600 mm) exceeds the torso width (300 mm) with no structure shown, and 4 DOF without roll limits gripper orientation | Workspace and packaging cannot be verified | Sketch the shoulder layout and four-axis kinematics (DA-02 §11); list open points for the owner |
| R-DA03-01 | Tipping stability of a 650 mm, 12–18 kg robot with arms extended on a 400 × 450 mm base is not calculated; battery capacity and runtime are unspecified | Safe operating envelope and runtime cannot be stated | Static tipping margin and energy estimate (DA-03 §11), assumptions listed for owner review |
| R-QR01-03 | Equal link lengths put the standing pose near a bent leg but full reach (240 mm) is near a singularity | Reach limits may be optimistic | Add a singularity margin in the next analysis step |

## 7. Next Actions

| Action | Concept | Owner | Target date |
|---|---|---|---|
| Confirm or replace assumptions A1–A5 | QR-01 | Dinesh | TBD |
| Static joint torque estimate (stand and lifted-leg poses) | QR-01 | INTERN-02 | TBD |
| Static stability margin for simple walking gait | QR-01 | INTERN-02 | TBD |
| Kinematic sketch for 2-DOF and 3-DOF modules | QR-05 | INTERN-02 | TBD |
| Leg-module interface sketch | QR-05 | INTERN-02 | TBD |
| Four-axis arm kinematic sketch and torso layout | DA-02 | INTERN-02 | TBD |
| Three-axis arm kinematic sketch, paired-drive sketch, tipping margin | DA-03 | INTERN-02 | TBD |

## 8. Repository Evidence

- Branch: `feasibility/intern-02`
- Commit references: TBD
- Relevant file paths:
  - `feasibility/concepts/QR-01/MECHANICAL_ANALYSIS.md`
  - `feasibility/concepts/QR-01/sketches/QR-01_leg_kinematic_sketch.png`
  - `feasibility/concepts/QR-01/sketches/QR-01_single_leg_kinematic_diagram.png`
  - (QR-05, DA-02 and DA-03: none yet)
- Review / pull request references: TBD

## 9. D-003 Compliance

I confirm that this week's work remained within paper feasibility scope. No CAD, final BOM, quotations, procurement, fabrication, assembly or physical testing was initiated.

- Intern confirmation: TBD (to be confirmed by INTERN-02 on submission)
- Date: TBD
- Exceptions, if any: NONE

Mechanical HOLD D-003 remains in effect. Any exception requires explicit owner review.
