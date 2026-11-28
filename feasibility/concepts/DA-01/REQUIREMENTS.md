# DA-01 — Concept targets and evidence requirements

| Property | Value |
|---|---|
| Document ID | KMECH-REQ-DA-01 |
| Repository | KritvaOS/kritva-mechanical |
| Document Type | Concept requirements working record |
| Status | PROPOSED — owner review pending |
| Assigned Intern | INTERN-01 |
| Version | 0.2.0 |
| Last Updated | 2026-11-28 |
| Authority | No accepted concept-specific requirement baseline is recorded here |
| Related Documents | README.md, ARCHITECTURE.md, ACTUATOR_ANALYSIS.md, OPEN_QUESTIONS.md, ../../REQUIREMENTS_REGISTER.md |

**HOLD D-003 remains active.** This record transcribes printed concept targets and maps proposed study requirements. It does not create approved product requirements, select hardware, or authorize implementation. No new CREQ identifiers are assigned.

## 1. Scope

Concept: Fixed Tabletop Dual-Arm. This record supports paper feasibility only. Artwork values below are CONCEPT_TARGETs, not accepted requirements.

## 2. Concept-target transcription

700 mm overall width; 400 mm height; 300×250 mm base; 350 mm reach per arm; 3 DOF per arm; six baseline joint actuators; 5–8 kg mass target; 0.1–0.2 kg payload per arm; 24 V concept direction. All are artwork targets, not approved requirements.

Source: README.md, concept artwork and cross-section, with figure-level references in references/SOURCE_REGISTER.md. Rendered artwork is illustrative, not dimensioned CAD.

## 3. Applicable study requirements

These IDs reference the common proposed register and are not redefined or claimed accepted here: Elbow 1.33 Nm, shoulder yaw 1.03 Nm, wrist pitch 0.31 Nm, and conditional shoulder pitch 4.77 Nm at 1.5×..

## 4. Evidence and scenario inputs

- Current evidence is paper review and formula-based estimates only; the calculations name every assumed geometry, mass, payload and acceleration input.
- The proposed family role mapping is S for wrist/neck, M for elbow/reference, and L for hip/knee. The family spec labels S/L torque values as placeholders and M as a reference; it does not qualify a specific actuator variant.
- Materials, dimensions, assembly masses, prices and seller specifications are separated in the central source register. Structure estimates use published density and section geometry, but do not establish strength, deflection, fatigue, tolerance or safety margins.
- CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain prohibited under HOLD D-003.

## 5. Requirement evidence register

| Topic | Current evidence | Boundary and review action |
|---|---|---|
| Operating/demo use | Artwork targets and task objectives | No owner-accepted operating envelope is present in this working record; review the explicitly modeled scenarios before adopting acceptance criteria. |
| Per-joint demand | Makiina10Nm clears the four modeled branches; HEBI T5-4 4Nm does not clear the conditional shoulder-pitch branch. | Torque is a paper screen; the calculation does not convert a static or assumed-acceleration case into a continuous product requirement. |
| Actuator compatibility | Product references and proposed family roles in ACTUATOR_ANALYSIS.md | Compare torque, speed, mass, voltage and listing status; no module is selected or qualified. |
| Material and structure | Mass takeoff in MASS_BUDGET.md; density and tube data cited | Thickness/sections are estimate inputs; no structural rating or material purchase is implied. |
| Mass and cost | Low/nominal/high mass and component-price scenario in MASS_BUDGET.md and COST_MODEL.md | Seller listings and planning allowances are not quotations; the ₹2 lakh study ceiling is not a procurement budget. |
| Concept requirement baseline | Owner review pending | Do not assign new concept requirement IDs or acceptance claims in this paper update. |

## 6. HOLD D-003

This is a paper requirements and evidence record. It does not authorize CAD, BOM release, quotations, procurement, fabrication, assembly or physical testing.
