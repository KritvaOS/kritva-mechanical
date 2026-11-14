# QR-04 — Week 2 Architecture Checks and Calculation Readiness

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. DOF count arithmetic

The listed baseline joint instances in `ARCHITECTURE.md` total **12**:
- Legged concept: Agile Long-Leg Quadruped.
- Baseline count is a transcription/check of the stated conceptual joints/channels.
- This is not proof of actuator performance, motion independence, torque capacity, speed, stability or design suitability.

## 2. Dimensional checks

The dimensional data are transcribed without geometric reconstruction. The source art provides no approved coordinate origin, datum, pose, dimension tolerances or scale calibration. Therefore no derived link dimensions, arm span closure, leg length, wheelbase, clearances or packaging volumes are calculated.

## 3. Mass checks

The top-level printed target is recorded in `MASS_BUDGET.md`. No subsystem sum or centre-of-mass result is calculated because component mass, geometry, material and coordinate inputs are unavailable.

## 4. Mechanical calculations deferred

The following are intentionally NOT calculated in Week 2:
- Joint torque and speed (Week 3, per joint).
- Link/joint stress and deflection.
- Static/dynamic stability margin.
- Foot / end-effector workspace numerical envelope.
- Drive traction and wheel load calculations.
- Battery runtime / power sizing.
- Cost totals.

For every deferred item, the source data and next action are recorded in `OPEN_QUESTIONS.md`, `ACTUATOR_ANALYSIS.md` and `MASS_BUDGET.md`. A missing result is not a pass.
