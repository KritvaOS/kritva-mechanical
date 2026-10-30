# Requirements Register

| Property | Value |
|---|---|
| Document ID | KMECH-FS-005 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Study-Level Requirements Register |
| Status | PROPOSED |
| Owner | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Proposed feasibility-study requirements; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/INTERN_ASSIGNMENTS.md`, `feasibility/DESIGN_GUIDELINES.md`, `feasibility/EVALUATION_CRITERIA.md`, `feasibility/RISK_REGISTER.md` |

## 1. Purpose and Conventions

This register defines common requirements and review criteria for the 12 concepts in the Kritva mechanical feasibility study. Concept-specific requirements belong in each concept's `REQUIREMENTS.md`.

All requirements have status `PROPOSED`. This register does not establish approved product specifications.

Verification is limited to paper-based review and calculation under mechanical HOLD D-003. No requirement may be marked physically validated.

**Evidence types:** C = calculation; S = software/configuration evidence; Sim = simulation; B = bench; P = physical. Sim, B and P are not authorized by this study. Use `ESTIMATE`, `UNKNOWN`, `TBD`, `BLOCKED` or `INCOMPLETE` where appropriate.

## 2. General and Scope Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-001 | Assess all 12 concepts defined in STUDY_PLAN. | STUDY_PLAN | Review | C | PROPOSED | Six dual-arm and six legged concepts |
| FREQ-002 | Keep work limited to paper feasibility study activities. | User decision / STUDY_PLAN | Review | C | PROPOSED | HOLD D-003 |
| FREQ-003 | Preserve current Kritva platform and actuator architecture directions. | User decision / program | Review | S | PROPOSED | No architecture changes |
| FREQ-004 | Record concept assumptions, unknowns, risks and dependencies explicitly. | DESIGN_GUIDELINES | Review | C | PROPOSED | No silent omissions |

## 3. Documentation Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-005 | Use explicit units for all engineering quantities. | DESIGN_GUIDELINES | Review | C | PROPOSED | SI units where practical |
| FREQ-006 | Document formulas, inputs, assumptions and calculation results. | DESIGN_GUIDELINES | Review / calculation | C | PROPOSED | Calculations must be traceable |
| FREQ-007 | Distinguish sourced values, assumptions and estimates. | DESIGN_GUIDELINES | Review | C | PROPOSED | Label estimates `ESTIMATE` |
| FREQ-008 | Mark missing values as TBD or UNKNOWN and unfinished work as INCOMPLETE or BLOCKED. | DESIGN_GUIDELINES | Review | C | PROPOSED | Include reason and next action |

## 4. Actuator and S/M/L Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-009 | Preserve the BLDC/PMSM modular rotary actuator direction. | User decision / program | Review | S | PROPOSED | Existing direction |
| FREQ-010 | Preserve the actuator S/M/L architecture. | User decision / program | Review | S | PROPOSED | Do not redefine size classes |
| FREQ-011 | Investigate 24V DC as a preliminary actuator/power direction only. | User decision / DESIGN_GUIDELINES | Review | C | PROPOSED | Not a finalized system voltage |
| FREQ-012 | Derive torque and speed requirements separately for each relevant joint. | DESIGN_GUIDELINES | Calculation / review | C | PROPOSED | Inputs and duty assumptions required |
| FREQ-013 | Assess S/M/L compatibility against derived joint requirements. | DESIGN_GUIDELINES | Calculation / review | C | PROPOSED | Mapping cannot be copied from elbow reference |
| FREQ-014 | Preserve the Option C actuator mechanical direction. | User decision / program | Review | S | PROPOSED | No redesign authorization |

## 5. Mechanical Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-015 | Document structural configuration and representative load paths. | DESIGN_GUIDELINES | Review / calculation | C | PROPOSED | Concept-specific |
| FREQ-016 | Identify stiffness and deflection considerations for relevant structures and joints. | DESIGN_GUIDELINES | Calculation / review | C | PROPOSED | No invented limits |
| FREQ-017 | Assess serviceability, assembly access and maintainability. | DESIGN_GUIDELINES | Review | C | PROPOSED | Conceptual assessment |
| FREQ-018 | Identify mechanical hazards and preliminary safety concerns. | DESIGN_GUIDELINES / program | Review / calculation | C | PROPOSED | Not safety certification |
| FREQ-019 | Record mass estimates and their assumptions where inputs permit. | STUDY_PLAN / DESIGN_GUIDELINES | Calculation / review | C | PROPOSED | Target mass TBD/UNKNOWN |
| FREQ-020 | Record payload and reach requirements or explicitly identify them as unknown. | User decision / STUDY_PLAN | Review | C | PROPOSED | Payload and reach TBD/UNKNOWN |

## 6. Kritva Platform Space and Interface Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-021 | Identify conceptual space reservation for Kritva Edge compute and control hardware. | User decision / program | Review | S | PROPOSED | Board dimensions TBD |
| FREQ-022 | Identify conceptual space for power distribution and protection. | DESIGN_GUIDELINES | Review | C | PROPOSED | Electrical requirements TBD |
| FREQ-023 | Identify sensor mounting, placement and wiring provisions. | User decision / program | Review | S | PROPOSED | Sensor selection TBD |
| FREQ-024 | Identify communication and cable-routing provisions, preserving EtherCAT as the existing architecture direction where relevant. | User decision / program | Review | S | PROPOSED | Interface details TBD |
| FREQ-025 | Identify motor-controller and actuator interface provisions. | DESIGN_GUIDELINES / program | Review | S | PROPOSED | Controller and connector details TBD |

## 7. Dual-Arm Add-on Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-026 | Document arm DOF, joint arrangement and workspace considerations. | DESIGN_GUIDELINES | Review / calculation | C | PROPOSED | Reach TBD/UNKNOWN |
| FREQ-027 | Assess base/torso support, load paths and stability under representative arm configurations. | DESIGN_GUIDELINES | Review / calculation | C | PROPOSED | Payload TBD/UNKNOWN |
| FREQ-028 | Assess inter-arm interference, end-effector interfaces and cable routing. | DESIGN_GUIDELINES | Review | C | PROPOSED | Gripper direction preserved where applicable |

## 8. Legged Add-on Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-029 | Document leg count, DOF per leg, joint arrangement and body configuration. | STUDY_PLAN / DESIGN_GUIDELINES | Review | C | PROPOSED | Concept-specific |
| FREQ-030 | Assess ground contact, support configuration and static stability considerations. | DESIGN_GUIDELINES | Review / calculation | C | PROPOSED | No validated gait claims |
| FREQ-031 | Assess representative leg-joint loading, clearance and locomotion workspace. | DESIGN_GUIDELINES | Review / calculation | C | PROPOSED | Torque and speed TBD until derived |

## 9. Budget Requirements

| ID | Requirement | Source | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|
| FREQ-032 | Evaluate preliminary hardware cost against the ₹2,00,000 planning ceiling. | User decision / STUDY_PLAN | Review / calculation | C | PROPOSED | Planning ceiling, not approved procurement budget |
| FREQ-033 | Trace cost assumptions to sources or explicitly label them ESTIMATE/UNKNOWN. | DESIGN_GUIDELINES | Review | C | PROPOSED | No supplier quotations required or authorized |
| FREQ-034 | Keep final BOM, quotations and procurement NOT STARTED pending owner decision. | User decision / STUDY_PLAN | Review | C | PROPOSED | HOLD D-003 |

## 10. Open Items

The following study-level unknowns must be resolved, bounded or explicitly carried forward. They are not permission to invent specifications.

| ID | Open item | Current status | Required treatment |
|---|---|---|---|
| U-001 | Final preferred mechanical architecture | TBD | Compare all 12 concepts |
| U-002 | Concept-specific dimensions and envelopes | TBD | Derive or record unknowns |
| U-003 | Target mass and mass distribution | UNKNOWN | Estimate only with traceable assumptions |
| U-004 | Payload requirements | UNKNOWN | Do not assume a payload value |
| U-005 | Arm reach requirements | UNKNOWN | Do not assume a reach value |
| U-006 | Locomotion and operating requirements | UNKNOWN | Define per legged concept or carry forward |
| U-007 | Joint torque and speed requirements | TBD | Derive per joint from documented loads |
| U-008 | Joint-to-actuator S/M/L mapping | TBD | Assess after requirements derivation |
| U-009 | Actuator inventory, availability and actual cost | UNKNOWN | Requires verified inventory or supplier evidence |
| U-010 | Materials and manufacturing process selection | TBD | Options only; no final selection |
| U-011 | Final BOM and component quotations | NOT STARTED | Requires owner decision under D-003 |
| U-012 | CAD and physical implementation authorization | OWNER DECISION REQUIRED | HOLD D-003 remains active |

## 11. Change Control

- Interns may propose requirement additions, edits, clarifications or status changes.
- Interns must not directly change this common register.
- Submit proposed changes with rationale, source, affected concepts and impact.
- The owner reviews and makes authorized changes.
- Preserve stable requirement IDs. Do not reuse retired IDs or silently change requirement meaning.
- Record approved changes in the repository's applicable change history.
- No change to this register releases HOLD D-003 unless the owner explicitly makes that decision.
