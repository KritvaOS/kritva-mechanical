# INTERN-01 — Weekly Feasibility Status

| Property | Value |
|---|---|
| Document ID | KMECH-WEEKLY-INTERN-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Intern Weekly Status |
| Status | PROPOSED — Week 2 working update; owner review pending |
| Owner | Dinesh |
| Assigned Intern | INTERN-01 |
| Version | 0.1.0 (existing status record; update only through branch review) |
| Authority | Weekly progress report; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/INTERN_ASSIGNMENTS.md`, `feasibility/interns/INTERN-01/CP2_CONTRIBUTION.md` |

## 1. Reporting Period

- Intern: INTERN-01
- Week: 2
- Reporting dates: TBD
- Branch: `feasibility/intern-01`
- Commit references: TBD
- Task linkage: `ROB-MECH-044` (local proposed task; registration/approval pending)
- HOLD: D-003 remains active

## 2. Concepts Worked

Assigned concepts: DA-01, QR-02, DA-04, QR-04.

| Concept ID | Planned activity | Week 2 artefacts supplied in overlay | Status |
|---|---|---|---|
| DA-01 | Configuration, dimensions, joints, interfaces, mass assumptions and preliminary mechanical assessment | Architecture, mechanical analysis, per-joint matrix, interfaces, mass framework, sketch, source register | IMPLEMENTED IN OVERLAY; NOT_REVIEWED |
| QR-02 | Same Week 2 scope; quadruped support/contact and gait geometry considerations | Architecture, mechanical analysis, 12 joint instances, interfaces, mass framework, sketch, source register | IMPLEMENTED IN OVERLAY; NOT_REVIEWED |
| DA-04 | Same Week 2 scope; torso/base interfaces and differential-drive configuration | Architecture, mechanical analysis, 10 joint/channel instances, interfaces, mass framework, sketch, source register | IMPLEMENTED IN OVERLAY; NOT_REVIEWED |
| QR-04 | Same Week 2 scope; long-leg geometry, support, indicative mounting and sensor decision | Architecture, mechanical analysis, 12 joint instances, interfaces, mass framework, sketch, source register | IMPLEMENTED IN OVERLAY; NOT_REVIEWED |

## 3. Deliverables vs Plan

| Planned deliverable | Actual result / evidence | Status |
|---|---|---|
| Mechanical configuration | Four concept architectures expanded | IMPLEMENTED IN OVERLAY; review pending |
| Preliminary dimensions | Source dimensions listed with units and source classification | IMPLEMENTED IN OVERLAY; owner review pending |
| DOF and joint configurations | Joint instances enumerated; axis/range gaps preserved | IMPLEMENTED IN OVERLAY; incomplete where source lacks data |
| Major assemblies and interfaces | Concept-level inventories created | IMPLEMENTED IN OVERLAY; not released interfaces |
| Mass assumptions | Printed target weight ranges separated from unknown subsystem contributions | IMPLEMENTED IN OVERLAY; mass budget incomplete |
| Preliminary mechanical assessment | Qualitative load paths, support/workspace/stiffness/serviceability questions recorded | IMPLEMENTED IN OVERLAY; calculations deferred |
| CP2 contribution | Four of 12 concepts documented | PARTIAL; other interns and reviewer required |
| CP2 architecture review | Not performed by INTERN-01 alone | NOT_RUN |

## 4. Blocked and Incomplete Items

| Item | Status | Reason | Dependency / action |
|---|---|---|---|
| Joint range / coordinate frames | TBD | Artwork and README do not define every axis frame or ROM | Owner/source confirmation |
| Torque / speed / S/M/L | BLOCKED for calculation | Requires link geometry, mass/load/motion and source-controlled actuator data | Week 3; actuator owner inputs |
| Subsystem mass and centre of mass | INCOMPLETE | Only printed total weight target range available; no component mass breakdown | Obtain geometry/material/component mass sources |
| Interface dimensions and tolerances | BLOCKED | No released robot-to-actuator interface data | Obtain actuator owner/revision and owner disposition |
| CP2 all-12 architecture coverage | BLOCKED / PARTIAL | INTERN-02 and INTERN-03 deliverables not included in this assigned contribution | Await their four-concept records each |
| CP2 review decision | NOT_RUN | Official cross-team review not completed | Authorized reviewer; record exact commit |

## 5. Unknowns and Assumptions

- All source artwork dimensions / masses / payload / voltage remain `CONCEPT_TARGET`.
- Printed weight ranges marked `(est.)` are not independent subsystem estimates.
- DA-01 wrist axis and cross-section-only torso/mast details remain OWNER_DECISION.
- QR-02 optional sensor/force-foot configuration remains OWNER_DECISION.
- DA-04 fixed head/no pan and ten-actuator baseline are preserved; battery sizing is not part of study.
- QR-04 indicative 4 × M5 / 2 × Ø5 mm mounting and adjustable sensor module remain OWNER_DECISION.
- ROM, torque, speed, duty cycle, gear ratio, S/M/L, component masses, CoM, material grade and detailed interfaces remain TBD/UNKNOWN.

## 6. Risks Raised

See each concept's `OPEN_QUESTIONS.md`. Global risk register is not edited. Related global risk categories include actuator capability, cost/inventory, calculation consistency, source maturity, D-003 scope creep and evidence overstatement.

## 7. Next Actions

| Action | Concept | Owner | Target |
|---|---|---|---|
| Resolve artwork / baseline decisions | DA-01, QR-02, QR-04 | Dinesh / owner | TBD |
| Provide actuator source data and revision | All four | Actuator owner / Dinesh | Week 3 |
| Define geometry, support and motion assumptions | All four | INTERN-01 with owner | Week 3 |
| Perform torque/speed and S/M/L assessment per joint | All four | INTERN-01 | Week 3 |
| Develop traceable subsystem mass estimates | All four | INTERN-01 | Week 3 |
| Complete other intern architecture contributions and CP2 | Other eight concepts | INTERN-02 / INTERN-03 / reviewer | CP2 |

## 8. Repository Evidence

- Branch: `feasibility/intern-01` (not created by this overlay)
- Commit references: TBD
- Relevant file paths: see `CP2_CONTRIBUTION.md` and concept folders
- Review / pull request references: TBD
- Integration state: Files supplied as overlay; not copied into the user's local repository by this package

## 9. D-003 Compliance

The supplied work is paper-only documentation and conceptual sketching. No CAD, final BOM, quotation, procurement, fabrication, assembly, physical testing or hardware integration is included.

- Intern confirmation: TBD
- Date: TBD
- Exceptions: NONE in this overlay; confirmation required after local integration

Mechanical HOLD D-003 remains in effect. Any exception requires explicit owner review.
