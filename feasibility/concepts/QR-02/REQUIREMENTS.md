# QR-02 — Concept Targets and Requirement Gaps

| Property | Value |
|---|---|
| Document ID | KMECH-REQ-QR-02 |
| Status | PROPOSED — INCOMPLETE; owner review required |
| Version | 0.2.0 |
| Last Updated | 2026-11-28 |
| Authority | No approved concept-specific requirement baseline exists |
| Evidence scope | Paper-only source transcription and gap record |

HOLD D-003 remains active. This file transcribes targets; it does not create requirements, select hardware or authorize implementation.

## 1. Concept-target transcription (not approved requirements)

350 × 260 × 250 mm body; 520 × 480 mm overall envelope with leg extension; 4 legs, 3 DOF per leg, 12 baseline actuators; printed mass 4–6 kg (est.) and payload 0.5–1.0 kg.

Source: [concept README](README.md#4-concept_target), [architecture record](ARCHITECTURE.md), original concept artwork/cross-section and references/SOURCE_REGISTER.md SRC-01–SRC-04. Artwork values, including any printed “est.” mass/payload, are CONCEPT_TARGET only; they are not independently derived estimates or verified operating inputs.

## 2. Common study requirements referenced

Applicable common register references: FREQ-002, FREQ-004 to FREQ-008, FREQ-012, FREQ-013, FREQ-015, FREQ-019, FREQ-020, FREQ-029 to FREQ-034.

These IDs are references to the common proposed register, not claims of completion or approval.

## 3. Evidence status and gaps

| Topic | Status | Basis / next evidence |
|---|---|---|
| Operating and demonstration requirements | UNKNOWN | Owner must define use case, duty and acceptance needs; do not infer from artwork |
| Per-joint torque, speed, ROM and duty | INCOMPLETE / TBD | No complete, source-backed geometry and component-mass model; see ACTUATOR_ANALYSIS.md and calculations/ |
| S/M/L compatibility | NOT SCORED / BLOCKED | Family-level roles/bands are provisional; S/L placeholders and M reference not frozen; no variant-level output data |
| Subsystem mass and CoM | UNKNOWN | No component masses, selected materials or released geometry; see MASS_BUDGET.md |
| Component cost and affordability | UNKNOWN | No priced, source-controlled BOM; see COST_MODEL.md; EC-03 not scored |
| Materials, strength and safety limits | UNKNOWN | No approved material grade, geometry, allowable or safety factor |
| Concept-specific requirements baseline | INCOMPLETE | Owner review required before assigning concept-specific requirements or acceptance claims |

## 4. Constraints

All unsupported quantities remain UNKNOWN/TBD. Calculated values must show formula, exact source inputs, conditional assumptions and limits. No assumed subsystem mass or price may be propagated as fact. CAD, BOM, supplier quotes, procurement, fabrication, assembly and physical testing remain NOT STARTED under HOLD D-003.
