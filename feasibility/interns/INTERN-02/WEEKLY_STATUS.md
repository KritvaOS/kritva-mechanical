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
| DA-02 | TBD | TBD | TBD |
| DA-03 | TBD | TBD | TBD |
| QR-05 | TBD | TBD | TBD |

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
| Other §11 items | INCOMPLETE | Sequenced after torque estimate | Proceed in README §11 order |

## 5. Unknowns and Assumptions

- New or unresolved unknowns:
  - How the 75 mm lateral foot offset implied by the 400 mm overall width is realised for a planar 2-DOF leg.
  - Standing hip height and whether the 200 mm body height includes the leg.
  - Which knee configuration (knee-back or knee-forward) is intended.
  - Basis for the printed 2.5–4 kg weight.
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
| R-QR01-03 | Equal link lengths put the standing pose near a bent leg but full reach (240 mm) is near a singularity | Reach limits may be optimistic | Add a singularity margin in the next analysis step |

## 7. Next Actions

| Action | Concept | Owner | Target date |
|---|---|---|---|
| Confirm or replace assumptions A1–A5 | QR-01 | Dinesh | TBD |
| Static joint torque estimate (stand and lifted-leg poses) | QR-01 | INTERN-02 | TBD |
| Static stability margin for simple walking gait | QR-01 | INTERN-02 | TBD |
| Start planned activity | DA-02, DA-03, QR-05 | INTERN-02 | TBD |

## 8. Repository Evidence

- Branch: `feasibility/intern-02`
- Commit references: TBD
- Relevant file paths:
  - `feasibility/concepts/QR-01/MECHANICAL_ANALYSIS.md`
  - `feasibility/concepts/QR-01/sketches/QR-01_leg_kinematic_sketch.png`
  - `feasibility/concepts/QR-01/sketches/QR-01_single_leg_kinematic_diagram.png`
- Review / pull request references: TBD

## 9. D-003 Compliance

I confirm that this week's work remained within paper feasibility scope. No CAD, final BOM, quotations, procurement, fabrication, assembly or physical testing was initiated.

- Intern confirmation: TBD (to be confirmed by INTERN-02 on submission)
- Date: TBD
- Exceptions, if any: NONE

Mechanical HOLD D-003 remains in effect. Any exception requires explicit owner review.
