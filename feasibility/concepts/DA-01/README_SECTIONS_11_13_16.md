# DA-01 — Suggested README updates (sections 11, 13–16)

Copy or merge into the concept README under the intern-owned sections.

## 11. Feasibility Activity (Week 3 update)

Week 3 engineering assessment completed at paper level:

- Joint torque and speed estimates: `ACTUATOR_ANALYSIS.md` + `calculations/CALC-DA01-01_joint_torque.md`
- Mass subsystem ranges: `MASS_BUDGET.md`
- Category cost model vs INR 2 L: `COST_MODEL.md`
- First-order stability / structure: `MECHANICAL_ANALYSIS.md`
- Open decisions and risks: `OPEN_QUESTIONS.md`

All numeric results are ESTIMATE / ASSUMED. S/M/L mapping remains blocked on actuator source data.

## 13. Folder Contents (current)

- README.md (this file)
- ARCHITECTURE.md, MECHANICAL_ANALYSIS.md, ACTUATOR_ANALYSIS.md
- MASS_BUDGET.md, COST_MODEL.md, INTERFACES.md, OPEN_QUESTIONS.md
- calculations/CALC-DA01-01_joint_torque.md
- sketches/ (Week 2 schematic)
- reviews/ (empty pending formal review records)

## 14. Current Assessment (summary)

| Aspect | Status |
|---|---|
| Configuration & DOF | Documented |
| Torque / speed estimates | ESTIMATE produced |
| Mass ranges | ESTIMATE produced |
| Cost vs ceiling | Nominal inside ceiling |
| S/M/L mapping | NOT STARTED / BLOCKED |
| Stability | First-order; clamping recommended |
| Recommendation | Strong low-risk candidate under current evidence |

## 15. Checkpoint Progress

- CP2 contribution: previously supplied
- CP3 contribution: see `interns/INTERN-01/CP3_CONTRIBUTION.md` (partial)
- CP4: not started

## 16. Open Decisions

See `OPEN_QUESTIONS.md`. Critical items: wrist axis (D4), torso/mast (D3/D5), gripper actuation, actuator data pack.
