# DA-01 — Concept Targets and Requirement Gaps

| Property | Value |
|---|---|
| Document ID | KMECH-REQ-DA-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept requirements working record |
| Status | PROPOSED — INCOMPLETE; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.1.0 |
| Last Updated | 2026-11-27 |
| Authority | No approved concept-specific requirement baseline exists in this file |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `ACTUATOR_ANALYSIS.md`, `OPEN_QUESTIONS.md`, `feasibility/REQUIREMENTS_REGISTER.md` |

**HOLD D-003 remains active.** This record transcribes concept targets and maps applicable study requirements; it does not create product requirements, select hardware, or authorize implementation. No new `CREQ` identifiers are assigned pending owner review.

## 1. Scope

Concept: Fixed Tabletop Dual-Arm (`DA-01`). This file supports paper feasibility only. Values printed on concept artwork are illustrative `CONCEPT_TARGET`s, not approved requirements.

## 2. Concept-target transcription (not approved requirements)

700 mm overall width; 400 mm overall height; 300 × 250 mm base; 350 mm shoulder-to-gripper reach each side; 3 DOF per arm; 6 baseline actuators; printed mass 5–8 kg (est.) and payload 0.1–0.2 kg per arm (both CONCEPT_TARGET).

Source: [concept artwork](../../../docs/images/KMECH-CONCEPT-DA-01.png) and [cross-section](../../../docs/images/KMECH-CROSS-SECTION-DA-01.png); see `references/SOURCE_REGISTER.md`. Cross-section-only values remain owner decisions. A printed `(est.)` is not an independent estimate.

## 3. Applicable study requirements

The following IDs are references to the common proposed register; this file does not redefine them or claim acceptance: FREQ-002, FREQ-004 to FREQ-008, FREQ-012, FREQ-013, FREQ-015, FREQ-019, FREQ-020, FREQ-026 to FREQ-028, FREQ-032 to FREQ-034.

## 4. Assumptions and constraints

- Common study requirements remain `PROPOSED`; evidence is paper review/calculation (`C`) only.
- All unsupported requirements remain `TBD` or `UNKNOWN`; assumptions are tagged `ASSUMED` and calculated values `ESTIMATE`.
- S/M/L family bands are proposal-level screening inputs only; variant-specific mass, envelope, thermal, price and validated output curves are not established.
- CAD, final BOM, supplier quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED under HOLD D-003.

## 5. Open requirements — INCOMPLETE

| Missing input | Current status | Reason / next action |
|---|---|---|
| Approved operating and demonstration requirements | UNKNOWN | Owner to define the use case, duty and acceptance needs; do not infer from artwork. |
| Per-joint torque, speed, ROM and duty basis | INCOMPLETE | Current calculations are assumption-based; unresolved inputs are recorded in `ACTUATOR_ANALYSIS.md` and `OPEN_QUESTIONS.md`. |
| Actuator compatibility | BLOCKED | The family-level class ranges are proposed, while S/L variant inputs are placeholders and M is not frozen; obtain controlled variant data and owner review. |
| Materials, structure and safety limits | UNKNOWN | No material grade, section, allowable, tolerance or safety factor is approved for this concept. |
| Cost and mass confidence | ESTIMATE | Category ranges are planning estimates, not quotes or verified component data. |
| Concept-specific requirements baseline | INCOMPLETE | Owner review is required before any concept-specific requirement IDs or acceptance claims are established. |

## 6. HOLD D-003

This is a paper requirements-gap record. It does not authorize CAD, BOM, quotes, procurement, fabrication, assembly or physical testing.
