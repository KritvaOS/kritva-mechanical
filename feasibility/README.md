# Kritva Mechanical Feasibility Study

| Property | Value |
|---|---|
| Document ID | KMECH-FS-007 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Feasibility Folder Navigation |
| Status | PROPOSED |
| Owner | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Study navigation and working guidance; subject to owner direction |
| Related Documents | `STUDY_PLAN.md`, `INTERN_ASSIGNMENTS.md`, `DESIGN_GUIDELINES.md`, `EVALUATION_CRITERIA.md`, `REQUIREMENTS_REGISTER.md`, `RISK_REGISTER.md` |

## 1. Purpose and Current State

This folder contains the planning, requirements, engineering guidelines, concept assessments and checkpoint reviews for the Kritva robot mechanical feasibility study, which compares six dual-arm and six quadruped/legged concepts.

**Current state:** Paper-only feasibility study. No CAD, final BOM, quotations or procurement. Mechanical HOLD D-003 remains in effect.

The study evaluates 12 concepts over four weeks. All specifications not supported by evidence remain TBD or UNKNOWN.

## 2. Document Index

| Path | Label | Status |
|---|---|---|
| [STUDY_PLAN.md](STUDY_PLAN.md) | Study scope, allocation, timeline and gates | PROPOSED |
| [INTERN_ASSIGNMENTS.md](INTERN_ASSIGNMENTS.md) | Intern responsibilities and concept ownership | PROPOSED |
| [DESIGN_GUIDELINES.md](DESIGN_GUIDELINES.md) | Common engineering and documentation rules | PROPOSED |
| [EVALUATION_CRITERIA.md](EVALUATION_CRITERIA.md) | Weighted criteria, scoring and shortlist method | PROPOSED |
| [REQUIREMENTS_REGISTER.md](REQUIREMENTS_REGISTER.md) | Study-level requirements | PROPOSED |
| [RISK_REGISTER.md](RISK_REGISTER.md) | Study-level risk tracking | OPEN |
| [templates/](templates/) | Reusable concept and review templates | PROPOSED |
| [CONCEPT_VARIATION_AUDIT.md](CONCEPT_VARIATION_AUDIT.md) | Audit of how the 12 concepts differ, with findings F1 to F10 and a cross-check with the ChatGPT audit | DRAFT, PROPOSED |
| [FUNCTIONAL_COMPARISON_MATRIX.md](FUNCTIONAL_COMPARISON_MATRIX.md) | Family comparison dimensions with printed targets; unknowns stay NOT SCORED | DRAFT, PROPOSED |
| [concepts/](concepts/) | Twelve concept-specific feasibility assessments | Artwork-based concept READMEs (v0.3.0) drafted; feasibility assessments NOT STARTED |
| [interns/](interns/) | Per-intern weekly status | NOT STARTED |
| [reviews/](reviews/) | Checkpoint and comparative review records | NOT STARTED (templates only) |

## 3. Folder Structure

    feasibility/
      README.md
      STUDY_PLAN.md
      INTERN_ASSIGNMENTS.md
      DESIGN_GUIDELINES.md
      EVALUATION_CRITERIA.md
      REQUIREMENTS_REGISTER.md
      RISK_REGISTER.md
      templates/
        ROBOT_CONCEPT_README_TEMPLATE.md
        REQUIREMENTS_TEMPLATE.md
        ARCHITECTURE_TEMPLATE.md
        MECHANICAL_ANALYSIS_TEMPLATE.md
        ACTUATOR_ANALYSIS_TEMPLATE.md
        INTERFACES_TEMPLATE.md
        MASS_BUDGET_TEMPLATE.md
        COST_MODEL_TEMPLATE.md
        OPEN_QUESTIONS_TEMPLATE.md
        WEEKLY_STATUS_TEMPLATE.md
        CHECKPOINT_REVIEW_TEMPLATE.md
      concepts/
        DA-01/
        DA-02/
        DA-03/
        DA-04/
        DA-05/
        DA-06/
        QR-01/
        QR-02/
        QR-03/
        QR-04/
        QR-05/
        QR-06/
      interns/
        INTERN-01/
          WEEKLY_STATUS.md
        INTERN-02/
          WEEKLY_STATUS.md
        INTERN-03/
          WEEKLY_STATUS.md
      reviews/
        CP2_ARCHITECTURE_REVIEW.md
        CP3_ENGINEERING_REVIEW.md
        CP4_FINAL_REVIEW.md
        DESIGN_COMPARISON.md
        ACTUATOR_COMPARISON.md
        COST_COMPARISON.md
        FINAL_RECOMMENDATION.md

The structure is the target organization for the study. A listed file or folder is not evidence that its contents are complete or approved. There is no `cad/` folder while HOLD D-003 is active.

### Concept artwork

Each concept has a concept sheet and a cross-section sheet (24 PNG files) in [`../docs/images/`](../docs/images/). They are illustrative concept artwork (evidence C, maturity L0, PROPOSED); printed numbers are `CONCEPT_TARGET`, not requirements. Start from [`../docs/images/ARTWORK_INDEX.md`](../docs/images/ARTWORK_INDEX.md) for review status, known issues and pending owner decisions, and from your concept README for the discrepancy table (section 10). Do not edit or replace artwork files; send artwork issues to the owner.

## 4. Concept Index

| ID | Concept | Complexity |
|---|---|---|
| DA-01 | Fixed Tabletop Dual-Arm | Low |
| DA-02 | Humanoid Torso Dual-Arm | Medium |
| DA-03 | Mobile Dual-Arm | High |
| DA-04 | Humanoid Mobile Dual-Arm (approved baseline) | High |
| DA-05 | Rotating Platform Dual-Arm | Low |
| DA-06 | Vision-Integrated Dual-Arm (approved baseline) | High |
| QR-01 | Compact Quadruped | Low |
| QR-02 | Standard Quadruped | Medium |
| QR-03 | Low-Profile Quadruped | Medium |
| QR-04 | Agile Long-Leg Quadruped | High |
| QR-05 | Modular Quadruped | High |
| QR-06 | Hexapod | High |

Each concept has one assigned intern as defined in `INTERN_ASSIGNMENTS.md`. The allocation is fixed: each intern receives two dual-arm and two legged concepts, with one Low, one Medium and two High complexity concepts.

## 5. Study Calendar

| Period | Activity | Checkpoint |
|---|---|---|
| Week 1 | Reference research, architecture, DOF, preliminary requirements and sketches | Internal progress review |
| Week 2 | Mechanical configuration, preliminary dimensions, joints and interfaces | CP2 — Architecture review |
| Week 3 | Torque/speed calculations, actuator assessment, structural analysis, stability, mass and cost modelling | CP3 — Engineering review |
| Week 4 | Consolidated assessments, comparative scoring, risk review and recommendation | CP4 — Final feasibility review |

Checkpoint records belong in `reviews/`. Checkpoint completion does not authorize implementation.

## 6. How to Work

### 6.1 Branches and Ownership

Use the assigned branches:

- `feasibility/intern-01`
- `feasibility/intern-02`
- `feasibility/intern-03`

Interns work only in their assigned concept folders and personal weekly status file. Do not edit common study documents, shared registers, templates or review records. Submit proposed common-document changes to the owner.

### 6.2 Commits

Use the commit message convention:

`type(scope): summary`

Include a `Task` footer identifying the relevant task or concept work item. Do not add AI session trailers or AI attribution trailers.

Keep commits focused and reviewable. Include relevant evidence and references with the associated concept work.

### 6.3 Reporting

- Use the supplied templates consistently.
- Record units, formulas, assumptions and sources.
- Label estimates as `ESTIMATE`.
- Use `TBD` and `UNKNOWN` rather than inventing values.
- Mark unfinished deliverables `INCOMPLETE` or `BLOCKED`; do not omit them.
- Record blockers, dependencies and next actions in `WEEKLY_STATUS.md`.
- Follow the cross-intern independent validation process before CP4.

## 7. Not in Scope

The feasibility study does not include:

- CAD models, detailed assemblies or production drawings.
- Final mechanical design release or final BOM.
- Supplier quotations, purchase orders or procurement.
- Fabrication, machining, 3D printing or assembly.
- Bench testing, actuator testing or physical robot testing.
- Validated locomotion, performance or safety certification.
- Changes to Kritva platform architecture or actuator S/M/L direction.

These activities require explicit owner decisions. Mechanical HOLD D-003 remains active throughout the study unless explicitly changed by the owner.

## 8. Authority

This README is a navigation document, not an approval record. In case of conflict, the owner-controlled study decisions and applicable approved program records take precedence. Interns must raise conflicts rather than independently changing common requirements, allocation or scope.
