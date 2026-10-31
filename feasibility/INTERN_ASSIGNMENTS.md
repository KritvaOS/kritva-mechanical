# Intern Assignments

| Property | Value |
|---|---|
| Document ID | KMECH-FS-002 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Feasibility Study – Intern Assignment |
| Status | PROPOSED |
| Owner | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Proposed assignment plan; subject to owner direction |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/EVALUATION_CRITERIA.md`, `reviews/CP2_ARCHITECTURE_REVIEW.md`, `reviews/CP3_ENGINEERING_REVIEW.md`, `reviews/CP4_FINAL_REVIEW.md` |

## 1. Purpose and Scope

This document assigns the 12 mechanical feasibility concepts across three interns for the four-week paper feasibility study.

Each intern owns four concepts and their associated analysis and evidence. The work is limited to research, engineering calculations, documentation, sketches and preliminary feasibility comparisons.

Mechanical HOLD D-003 remains in force. This assignment does not authorize CAD development, final BOM preparation, quotations, procurement, fabrication, assembly or physical testing.

## 2. Fixed Allocation

The allocation below is fixed for this study. Each intern receives exactly:
- Two dual-arm concepts and two legged concepts.
- One Low-complexity concept.
- One Medium-complexity concept.
- Two High-complexity concepts.

| Intern | Low | Medium | High 1 | High 2 |
|---|---|---|---|---|
| INTERN-01 | DA-01 | QR-02 | DA-04 | QR-04 |
| INTERN-02 | QR-01 | DA-02 | DA-03 | QR-05 |
| INTERN-03 | DA-05 | QR-03 | DA-06 | QR-06 |

The complexity balance and concept-family balance are fixed. Do not exchange, add, remove or reclassify concepts without an explicit owner decision.

## 3. Intern Responsibilities

### 3.1 INTERN-01

**Assigned concepts**

| Concept | Description | Complexity |
|---|---|---|
| DA-01 | Fixed Tabletop Dual-Arm: fixed base, two 3-DOF arms | Low |
| QR-02 | Standard Quadruped: four legs, 3 DOF per leg | Medium |
| DA-04 | Humanoid Mobile Dual-Arm: humanoid torso with head on a differential-drive base, two 4-DOF arms, 10 actuators (approved baseline) | High |
| QR-04 | Agile Long-Leg Quadruped: four legs, 3 DOF per leg | High |

**Responsibilities**
- Study fixed-base and advanced dual-arm configurations.
- Evaluate arm joint arrangement, workspace and interface requirements.
- Study standard and agile quadruped configurations.
- Identify leg-joint loading, stability and locomotion-related requirements.
- Record assumptions, calculations, unknowns and concept-specific risks.

**Branch:** `feasibility/intern-01`

**Owned folders:**
- `feasibility/concepts/DA-01/`
- `feasibility/concepts/QR-02/`
- `feasibility/concepts/DA-04/`
- `feasibility/concepts/QR-04/`

### 3.2 INTERN-02

**Assigned concepts**

| Concept | Description | Complexity |
|---|---|---|
| QR-01 | Compact Quadruped: four legs, 2 DOF per leg | Low |
| DA-02 | Humanoid Torso Dual-Arm: torso, two 4-DOF arms | Medium |
| DA-03 | Mobile Dual-Arm: mobile base, two 3-DOF arms | High |
| QR-05 | Modular Quadruped: four interchangeable legs, 2–3 DOF per leg | High |

**Responsibilities**
- Study compact quadruped configuration and joint arrangement.
- Evaluate humanoid torso and dual-arm integration requirements.
- Study mobile-base and dual-arm mechanical interfaces.
- Evaluate modular leg interchangeability and its mechanical implications.
- Record assumptions, calculations, unknowns and concept-specific risks.

**Branch:** `feasibility/intern-02`

**Owned folders:**
- `feasibility/concepts/QR-01/`
- `feasibility/concepts/DA-02/`
- `feasibility/concepts/DA-03/`
- `feasibility/concepts/QR-05/`

### 3.3 INTERN-03

**Assigned concepts**

| Concept | Description | Complexity |
|---|---|---|
| DA-05 | Rotating Platform Dual-Arm: rotating base, two 3-DOF arms | Low |
| QR-03 | Low-Profile Quadruped: four legs, 2 DOF per leg | Medium |
| DA-06 | Vision-Integrated Dual-Arm: fixed tabletop, two 4-DOF arms, multi-camera mast, 8 actuators (approved baseline) | High |
| QR-06 | Hexapod: six legs, 2 DOF per leg | High |

**Responsibilities**
- Study rotating-platform and dual-arm mechanical configuration.
- Evaluate low-profile quadruped layout and joint arrangement.
- Study humanoid upper-body structure and head provision.
- Evaluate hexapod leg configuration, support and stability considerations.
- Record assumptions, calculations, unknowns and concept-specific risks.

**Branch:** `feasibility/intern-03`

**Owned folders:**
- `feasibility/concepts/DA-05/`
- `feasibility/concepts/QR-03/`
- `feasibility/concepts/DA-06/`
- `feasibility/concepts/QR-06/`

## 4. Weekly Deliverables

Each intern must submit separate, traceable deliverables for all four assigned concepts.

| Week / Checkpoint | Required deliverables |
|---|---|
| Week 1 | Reference research, architecture description, DOF and joint arrangement, preliminary requirements, sketches, assumptions and unknowns |
| Week 2 / CP2 | Mechanical configuration, preliminary dimensions where supported, assemblies, interfaces, initial risks and concept-level architecture review inputs |
| Week 3 / CP3 | Joint torque/speed calculations or TBD, actuator S/M/L compatibility assessment, structural loading, stability/workspace analysis as applicable, mass estimates and preliminary component categories |
| Week 4 / CP4 | Completed concept assessments, updated calculations and risks, cost assumptions with traceable basis, comparison inputs, feasibility findings and recommendation with unresolved questions |

### 4.1 Checkpoint Submissions

- **CP2:** Submit architecture and configuration evidence for all four assigned concepts. Identify every unresolved dimension, interface and requirement.
- **CP3:** Submit engineering calculations and analysis, or explicitly mark unavailable work as TBD or INCOMPLETE. Identify assumptions and calculation sources.
- **CP4:** Submit consolidated feasibility assessments and recommendations for all four concepts, including evidence limitations and owner decisions required.

Checkpoint review documents are maintained separately under `reviews/`. Interns provide inputs; they do not approve checkpoints.

## 5. Branch and Folder Rules

1. Work only in the assigned branch: `feasibility/intern-01`, `feasibility/intern-02` or `feasibility/intern-03`.
2. Commit concept-specific work only within the four assigned concept folders.
3. Do not edit common documents, shared registers, evaluation criteria, study plans, review records or program baseline files.
4. Raise proposed changes to common documents for owner review rather than editing them directly.
5. Keep evidence, assumptions, calculations and references traceable to the relevant concept.
6. Do not overwrite another intern's work. Coordinate shared technical questions through the owner.

## 6. Reporting and Evidence Rules

- Do not invent dimensions, payloads, reach, mass, torque, speed, material properties, component availability or costs.
- Use `TBD` when a value has not been established. Use `UNKNOWN` when the required information is not known.
- Mark unfinished or unsupported work as `INCOMPLETE` or `BLOCKED`; never silently omit a required item.
- Record the reason, dependency and action needed for every `BLOCKED` item.
- Distinguish sourced facts, engineering assumptions and calculated estimates.
- Identify evidence type accurately: S (software), C (calculation), Sim (simulation), B (bench) or P (physical).
- Do not claim simulation, bench or physical evidence unless that activity was separately authorized and actually completed.
- Keep calculations reproducible, with units, formulas, assumptions and references.

## 7. Mechanical HOLD D-003

All intern activity is paper feasibility work only.

The following remain NOT STARTED and require explicit owner decision:
- CAD modelling and detailed mechanical design.
- Final BOM and component selection.
- Supplier quotations and procurement.
- Fabrication, assembly and integration.
- Bench testing and physical testing.

The ₹2,00,000 figure is a planning ceiling, not procurement authorization or an approved budget. No intern may initiate spending or external commitments.

## 8. Completion and Review

Each intern is responsible for submitting all four concept assessments by CP4, with missing information explicitly identified. The owner reviews the submissions and decides whether any subsequent activity may proceed.

Completion of this assignment or any checkpoint does not release HOLD D-003 or constitute program approval.
