# QR-04 — Concept targets and evidence requirements

| Property | Value |
|---|---|
| Document ID | KMECH-REQ-QR-04 |
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

Concept: Agile Long-Leg Quadruped. This record supports paper feasibility only. Artwork values below are CONCEPT_TARGETs, not accepted requirements.

## 2. Concept-target transcription

450×280×320 mm body; 3 DOF per leg; 12 baseline joint actuators; 5–7 kg mass target; 0.5–1.0 kg payload target; 24 V concept direction. Artwork also shows a 4×M5 / 2×Ø5 mm layout indicator and optional sensor module. These are not approved requirements.

Source: README.md, concept artwork and cross-section, with figure-level references in references/SOURCE_REGISTER.md. Rendered artwork is illustrative, not dimensioned CAD.

## 3. Applicable study requirements

These IDs reference the common proposed register and are not redefined or claimed accepted here: 7.43 kg nominal sensor-excluded; 7.50 kg rounded review case; hip-flexion screen 11.31 / 11.42 Nm at 1.5×..

## 4. Evidence and scenario inputs

- Current evidence is paper review and formula-based estimates only; the calculations name every assumed geometry, mass, payload and acceleration input.
- The proposed family role mapping is S for wrist/neck, M for elbow/reference, and L for hip/knee. The family spec labels S/L torque values as placeholders and M as a reference; it does not qualify a specific actuator variant.
- Materials, dimensions, assembly masses, prices and seller specifications are separated in the central source register. Structure estimates use published density and section geometry, but do not establish strength, deflection, fatigue, tolerance or safety margins.
- CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain prohibited under HOLD D-003.

## 5. Requirement evidence register

| Topic | Current evidence | Boundary and review action |
|---|---|---|
| Operating/demo use | Artwork targets and task objectives | No owner-accepted operating envelope is present in this working record; review the explicitly modeled scenarios before adopting acceptance criteria. |
| Per-joint demand | Makiina10Nm misses the upper hip-flexion scenario; the 18Nm candidate is 48V and below the proposed L role torque band. | Torque is a paper screen; the calculation does not convert a static or assumed-acceleration case into a continuous product requirement. |
| Actuator compatibility | Product references and proposed family roles in ACTUATOR_ANALYSIS.md | Compare torque, speed, mass, voltage and listing status; no module is selected or qualified. |
| Material and structure | Mass takeoff in MASS_BUDGET.md; density and tube data cited | Thickness/sections are estimate inputs; no structural rating or material purchase is implied. |
| Mass and cost | Low/nominal/high mass and component-price scenario in MASS_BUDGET.md and COST_MODEL.md | Seller listings and planning allowances are not quotations; the ₹2 lakh study ceiling is not a procurement budget. |
| Concept requirement baseline | Owner review pending | Do not assign new concept requirement IDs or acceptance claims in this paper update. |

## 6. HOLD D-003

This is a paper requirements and evidence record. It does not authorize CAD, BOM release, quotations, procurement, fabrication, assembly or physical testing.
