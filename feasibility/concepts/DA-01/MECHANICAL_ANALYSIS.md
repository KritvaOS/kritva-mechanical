# DA-01 — Mechanical Assessment (Week 3 update)

| Property | Value |
|---|---|
| Document ID | KMECH-MECH-DA-01 |
| Status | PROPOSED — Week 3 paper assessment |
| Version | 0.3.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 |

**HOLD D-003 active.**

## 1. Configuration recap

Fixed tabletop dual-arm, 3 DOF per arm, 6 actuators baseline. Central enclosure houses compute and drivers. Optional mast and powered grippers excluded from baseline.

## 2. Load path (unchanged from Week 2)

Payload → gripper → wrist → forearm → elbow → upper arm → shoulder → central torso/base plate → tabletop support.

## 3. Stability / tipping (first-order ESTIMATE)

Assumptions for a first-order check:

- Robot mass nominal 4.7 kg (from MASS_BUDGET).
- CoM roughly at geometric centre of base when arms folded.
- Base footprint 300 × 250 mm.
- Worst case: both arms extended horizontally to one side with 0.2 kg payload each.

A quantitative overturning moment is **INCOMPLETE**: the prior note used a 2.15 N·m shoulder term that did not match the listed calculation inputs (2.33 N·m static, about 2.97 N·m including the stated inertial estimate), and shoulder pitch is not in the current three-axis-per-arm baseline. The restoring-moment range also lacks an approved CoM and support condition. Do not report a tipping margin or factor of safety from those figures.

**Conclusion (qualitative only):** Evaluate positive tabletop attachment as a design consideration. A quantified clamp/friction recommendation and stability margin remain TBD until the axis, arm pose, CoM and support interface are defined.

## 4. Structural notes

- Link cross-sections and wall thicknesses are not selected.
- Shoulder support stiffness is the critical structural item for reach accuracy and vibration.
- No stress or deflection numbers are claimed; geometry and material data are still missing.

## 5. Workspace / collision

- Printed reach 350 mm per side; total left-to-right 700 mm matches overall width, implying the arms meet near the centreline when fully extended.
- Self-collision and table collision envelopes remain TBD pending joint limits and exact kinematics.

## 6. Serviceability

Central enclosure access, cable routing through three joints per arm, and thermal path for drivers remain conceptual concerns. No service interval or tool clearance is defined.

## 7. Week 3 status

| Topic | Status |
|---|---|
| Configuration | Documented |
| Load path | Documented |
| First-order tipping | ESTIMATE produced; clamping recommended |
| Stress / deflection | BLOCKED on geometry & material |
| Workspace | Qualitative only |
| Serviceability | Qualitative only |

See `OPEN_QUESTIONS.md` and `ACTUATOR_ANALYSIS.md` for residual unknowns.
