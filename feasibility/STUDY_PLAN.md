# Kritva Mechanical – Four-Week Comparative Robot Feasibility Study Plan

| Property | Value |
|---|---|
| Document ID | KRITVA-MECH-FS-PLAN-001 |
| Repository | KritvaOS/kritva-mechanical |
| Document Type | Feasibility Study Plan |
| Status | PROPOSED |
| Owner | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Proposed study document; does not constitute program approval or implementation authorization. |
| Related Documents | D-003 Mechanical HOLD; INTERN_ASSIGNMENTS.md; DESIGN_GUIDELINES.md; EVALUATION_CRITERIA.md; REQUIREMENTS_REGISTER.md; RISK_REGISTER.md |

## 1. Purpose

Define a four-week comparative mechanical feasibility study covering six dual-arm and six quadruped/legged robot concepts. Three interns will evaluate four concepts each.

The primary objective is to identify candidate mechanical architectures suitable for demonstrating the Kritva robotics platform within a proposed hardware budget ceiling of INR 2,00,000.

This is a paper feasibility study. It does not approve a robot architecture or authorize implementation.

## 2. Objectives

1. Evaluate twelve robot concepts using common engineering criteria.
2. Establish preliminary mechanical configurations, DOF and dimensions.
3. Identify joint, actuator and structural requirements.
4. Assess compatibility with the existing Kritva S/M/L actuator architecture.
5. Evaluate mass, workspace, stability and mechanical loading where applicable.
6. Develop preliminary cost assumptions without procurement activity.
7. Identify technical risks, dependencies and unknowns.
8. Recommend candidate architectures for subsequent owner consideration.

The platform demonstration context includes Kritva Core, Nexus, Edge, Sense, Motion and Sim. Existing platform and actuator decisions must be preserved.

## 3. Scope and Mechanical HOLD D-003

### 3.1 Included

- Reference architecture research.
- Mechanical configuration and conceptual sketches.
- Preliminary dimensions and DOF analysis.
- Joint torque and speed calculations where inputs permit.
- Structural and stability calculations.
- Preliminary mass estimates.
- Actuator compatibility assessment.
- Conceptual fabrication assessment.
- Preliminary cost modelling.
- Risk assessment and comparative recommendation.

### 3.2 Excluded

| Activity | Status |
|---|---|
| Detailed CAD | NOT STARTED – owner decision required |
| Manufacturing drawings | NOT STARTED – owner decision required |
| Final BOM | NOT STARTED – owner decision required |
| Supplier quotations | NOT STARTED – owner decision required |
| Procurement | NOT STARTED – owner decision required |
| Fabrication | NOT STARTED – owner decision required |
| Physical testing | NOT STARTED – owner decision required |
| Hardware integration | NOT STARTED – owner decision required |

CAD and BOM fields are templates or TBD only. No procurement or fabrication commitments are permitted.

D-003 remains in effect throughout this study. Passing a checkpoint does not release the HOLD.

## 4. Robot Concepts

### 4.1 Dual-arm

| ID | Concept | Preliminary configuration | Complexity |
|---|---|---|---|
| DA-01 | Fixed Tabletop Dual-Arm | Fixed base, two 3-DOF arms | Low |
| DA-02 | Humanoid Torso Dual-Arm | Torso, two 4-DOF arms | Medium |
| DA-03 | Mobile Dual-Arm | Mobile base, two 3-DOF arms | High |
| DA-04 | Advanced Dual-Arm | Two 5-DOF arms | High |
| DA-05 | Rotating Platform Dual-Arm | Rotating base, two 3-DOF arms | Low |
| DA-06 | Humanoid Upper-Body | Torso, head provision, two 4-DOF arms | High |

### 4.2 Quadruped and legged

| ID | Concept | Preliminary configuration | Complexity |
|---|---|---|---|
| QR-01 | Compact Quadruped | Four legs, 2 DOF per leg | Low |
| QR-02 | Standard Quadruped | Four legs, 3 DOF per leg | Medium |
| QR-03 | Low-Profile Quadruped | Four legs, 2 DOF per leg | Medium |
| QR-04 | Agile Long-Leg Quadruped | Four legs, 3 DOF per leg | High |
| QR-05 | Modular Quadruped | Four interchangeable legs, 2–3 DOF per leg | High |
| QR-06 | Hexapod | Six legs, 2 DOF per leg | High |

Configurations are preliminary study definitions. Dimensions, payload, mass, torque, speed and cost remain TBD unless supported by calculations or evidence.

Complexity classifications are relative engineering categories, not validated cost or implementation assessments.

## 5. Intern Allocation

| Intern | Low | Medium | High 1 | High 2 |
|---|---|---|---|---|
| INTERN-01 | DA-01 | QR-02 | DA-04 | QR-04 |
| INTERN-02 | QR-01 | DA-02 | DA-03 | QR-05 |
| INTERN-03 | DA-05 | QR-03 | DA-06 | QR-06 |

Each intern owns four concepts: two dual-arm and two legged designs, comprising one Low, one Medium and two High complexity assignments.

All three interns remain focused on mechanical feasibility. Integration is outside this study.

Each intern must document architecture, requirements, joints, actuator needs, engineering assumptions, mass, cost and risks for assigned concepts.

## 6. Common Engineering Requirements

Each concept must address:

- Mechanical configuration and major assemblies.
- DOF, joint type and preliminary joint range.
- Dimensions and mechanical interfaces.
- Joint torque and speed requirements.
- Actuator and gearbox requirements.
- Structural loading and stiffness.
- Material and fabrication considerations.
- Mass distribution and packaging.
- Serviceability and mechanical safety.

Additional dual-arm analysis: workspace, reach, payload, arm stiffness, gripper and base stability.

Additional legged analysis: leg workspace, foot placement, ground contact, stability, mass distribution and gait geometry.

All numerical values must have documented derivation or evidence. Otherwise use TBD or UNKNOWN.

## 7. Kritva Architecture and Actuator Constraints

| Component | Existing direction | Study treatment |
|---|---|---|
| Kritva Core | Linux / PREEMPT_RT | Preserve |
| Kritva Nexus | High-performance computing | Preserve |
| Kritva Edge | Real-time control | Preserve |
| Kritva Sense | Sensor integration | Preserve |
| Kritva Motion | Motion control | Preserve |
| Kritva Sim | Simulation | Preserve |
| Communication | EtherCAT architecture | Preserve |
| Actuator architecture | S/M/L | Preserve |
| Actuator technology | BLDC/PMSM modular rotary actuator | Preserve |
| Actuator mechanical direction | Option C | Preserve |

Do not rename or reinterpret P0-P8, A0-A2 or S/M/L.

The existing elbow actuator reference is not automatically suitable for quadruped or arm joints. Joint-specific requirements must be calculated.

The study may identify potential actuator incompatibilities but cannot approve actuator redesign.

## 8. Four-Week Execution Plan

| Period | Activities | Expected delivery |
|---|---|---|
| Week 1 | Reference study, architecture, DOF, preliminary requirements and sketches | Four concept descriptions and initial risk entries per intern |
| Week 2 | Mechanical configuration, preliminary dimensions, joints, interfaces and mass assumptions | Architecture documentation and preliminary mechanical assessment for all 12 concepts |
| Week 3 | Torque/speed calculations, actuator assessment, structural analysis, stability, mass and cost modelling | Engineering feasibility assessment and preliminary cost assumptions |
| Week 4 | Consolidation, comparative scoring, risk review and recommendation | Twelve concept assessments and final comparative recommendation |

CAD, procurement, fabrication and physical testing remain NOT STARTED throughout all four weeks.

## 9. Checkpoints and Acceptance Criteria

### 9.1 CP2 – Week 2: Architecture Review

| ID | Acceptance criterion |
|---|---|
| CP2-01 | All 12 architecture descriptions documented |
| CP2-02 | Mechanical configurations identified |
| CP2-03 | DOF and joint configurations documented |
| CP2-04 | Available dimensions recorded with units |
| CP2-05 | Major assemblies and interfaces identified |
| CP2-06 | Unknown specifications explicitly recorded |
| CP2-07 | Initial risks documented |
| CP2-08 | Intern assignments represented in repository |
| CP2-09 | D-003 restrictions respected |

Delivery: `reviews/CP2_ARCHITECTURE_REVIEW.md`

### 9.2 CP3 – Week 3: Engineering Review

| ID | Acceptance criterion |
|---|---|
| CP3-01 | Joint torque requirements calculated or TBD |
| CP3-02 | Joint speed requirements calculated or TBD |
| CP3-03 | Assumptions and formulas documented |
| CP3-04 | S/M/L compatibility assessed |
| CP3-05 | Structural loading assumptions documented |
| CP3-06 | Stability/workspace addressed where applicable |
| CP3-07 | Mass estimates documented |
| CP3-08 | Major component categories identified |
| CP3-09 | Preliminary cost assumptions traceable |
| CP3-10 | Risks and unknowns updated |
| CP3-11 | D-003 restrictions respected |

Delivery: `reviews/CP3_ENGINEERING_REVIEW.md`

### 9.3 CP4 – Week 4: Final Feasibility Review

| ID | Acceptance criterion |
|---|---|
| CP4-01 | All 12 concepts assessed |
| CP4-02 | Mechanical architecture and DOF documented |
| CP4-03 | Joint and actuator requirements documented or TBD |
| CP4-04 | Structural and stability assessments addressed |
| CP4-05 | Mass assumptions consolidated |
| CP4-06 | Cost assumptions documented |
| CP4-07 | Technical risks consolidated |
| CP4-08 | Comparative evaluation completed |
| CP4-09 | INR 2,00,000 budget constraint evaluated |
| CP4-10 | Candidate architectures identified with rationale |
| CP4-11 | Outstanding owner decisions recorded |
| CP4-12 | D-003 restrictions respected |

Delivery: `reviews/CP4_FINAL_REVIEW.md`

Review results must use PASS, FAIL, BLOCKED or NOT REVIEWED. A review PASS does not authorize implementation.

## 10. Delivery Matrix

| Deliverable | CP2 | CP3 | CP4 |
|---|---|---|---|
| Architecture | Preliminary | Updated | Consolidated |
| Requirements | Preliminary | Updated | Consolidated |
| Dimensions and DOF | Preliminary | Updated | Consolidated |
| Joint requirements | Initial | Calculated where possible | Consolidated |
| Actuator analysis | Initial | Required | Consolidated |
| Structural analysis | Initial assumptions | Required | Consolidated |
| Stability/workspace | Initial assumptions | Analysis | Consolidated |
| Mass budget | Initial estimate | Updated | Consolidated |
| CAD | NOT STARTED | NOT STARTED | NOT STARTED |
| BOM | Template / TBD | Component breakdown only | Template / TBD |
| Quotations | NOT STARTED | NOT STARTED | NOT STARTED |
| Cost model | Initial assumptions | Preliminary | Consolidated |
| Procurement/fabrication | NOT STARTED | NOT STARTED | NOT STARTED |
| Physical testing | NOT STARTED | NOT STARTED | NOT STARTED |
| Risk register | Initial | Updated | Consolidated |
| Recommendation | — | Preliminary | Final |

## 11. Evidence Classification

| Type | Meaning |
|---|---|
| S | Software evidence |
| C | Calculation evidence |
| Sim | Simulation evidence |
| B | Bench evidence |
| P | Physical evidence |

For this paper study, C is applicable. S may apply to relevant software/configuration references. Sim requires separately authorized simulation activity. B and P remain NOT STARTED.

Estimates must be labelled ESTIMATE and include assumptions. Reference values must identify their sources. Unsupported values remain TBD or UNKNOWN.

## 12. Evaluation Criteria

| Parameter | Proposed weight |
|---|---:|
| Mechanical feasibility | 20% |
| Actuator availability and compatibility | 15% |
| Hardware cost | 20% |
| Fabrication simplicity | 10% |
| Kritva platform demonstration value | 20% |
| Modularity and upgrade potential | 10% |
| Mechanical safety | 5% |
| Total | 100% |

These are proposed study weights, not program-approved values.

Missing evidence must not be hidden through aggregate scoring. The scoring method and evidence requirements belong in `EVALUATION_CRITERIA.md`.

## 13. Governance and Repository Rules

1. Dinesh is the document owner.
2. Each intern maintains assigned concept documentation.
3. Common architecture and study documents remain under owner oversight.
4. Weekly status reports must record completed work, blockers, unknowns and next activities.
5. All contributions must be committed to the existing repository.
6. Changes must follow the repository contribution and review process.
7. Common requirements and architecture decisions must not be changed independently by interns.
8. All review outcomes and corrective actions must be documented.
9. Existing mechanical HOLD and naming conventions remain unchanged.
10. No checkpoint or recommendation constitutes program approval.

## 14. Decision Gates

| Gate | Purpose | Required outcome |
|---|---|---|
| G1 – Architecture Feasibility | Review configuration, DOF, dimensions and assemblies | Architectures sufficiently defined for engineering assessment |
| G2 – Engineering Feasibility | Review torque, speed, actuator, structural and stability analysis | Documented engineering feasibility and limitations |
| G3 – Budget Feasibility | Evaluate preliminary component and cost assumptions | Budget feasibility assessment against INR 2,00,000 |
| G4 – Owner Decision | Review final comparative study and recommendation | Explicit decision on any subsequent activity |

G1-G3 are study assessment gates. G4 requires owner review. None automatically releases D-003.

Any subsequent CAD, BOM finalization, supplier quotations, procurement, fabrication, physical testing or integration requires a separate explicit owner decision.

## 15. Open Questions and Unknowns

| ID | Item | Status |
|---|---|---|
| U-001 | Final demonstrator architecture | TBD |
| U-002 | Robot dimensions | TBD |
| U-003 | Target robot mass | TBD |
| U-004 | Payload requirements | UNKNOWN |
| U-005 | Arm reach requirements | UNKNOWN |
| U-006 | Locomotion requirements | UNKNOWN |
| U-007 | Joint torque and speed | TBD |
| U-008 | Actuator size mapping | TBD |
| U-009 | Actuator availability and actual cost | UNKNOWN |
| U-010 | Materials and fabrication process | TBD |
| U-011 | Final BOM and supplier pricing | NOT STARTED |
| U-012 | CAD and physical implementation authorization | OWNER DECISION REQUIRED |

Unknowns must remain visible until supported by evidence or resolved through an owner decision.

## 16. Completion Criteria

The study is complete when:

1. All twelve concepts have documented assessments.
2. All three interns have submitted assigned deliverables or documented blockers.
3. CP2, CP3 and CP4 review records exist.
4. Engineering calculations and assumptions are traceable.
5. Actuator compatibility is assessed.
6. Mass and cost assumptions are documented.
7. Comparative evaluation and technical risks are consolidated.
8. Candidate architectures and outstanding decisions are documented.
9. D-003 has been respected throughout.

## 17. Final Authority and Status

The expected outcome is a documented comparison of six dual-arm and six legged architectures, providing evidence for a subsequent owner decision.

The final recommendation may identify candidate designs for further engineering consideration. It does not approve implementation or change existing mechanical or actuator baselines.

**Document Status: PROPOSED**

**Mechanical HOLD D-003: REMAINS IN EFFECT**

**Program Approval: NOT CLAIMED**
