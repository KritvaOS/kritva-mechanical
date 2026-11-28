# QR-04 — Source Register (Week 3/4)

**Status:** PROPOSED — paper-only traceability record; HOLD D-003 active.

| Ref | Source | Numeric or decision use | Limitation |
|---|---|---|---|
| SRC-01 | [../README.md](../README.md) sections 2, 4, 6 and 9 | Printed concept targets, assembly count, baseline channels, payload/mass ranges and documented unknowns | Targets are CONCEPT_TARGET; artwork is not to scale and printed estimates have no derivation |
| SRC-02 | [../ARCHITECTURE.md](../ARCHITECTURE.md) sections 2–3 and 8–9 | Configuration, joint/channel count, dimensions and explicit unknowns | Concept-level; no released geometry, mass breakdown or operating loads |
| SRC-03 | [concept artwork](../../../../docs/images/KMECH-CONCEPT-QR-04.png) and [cross-section](../../../../docs/images/KMECH-CROSS-SECTION-QR-04.png) | Original concept artwork referred to by README | Illustrative, not scale-calibrated or engineering evidence |
| SRC-04 | [../calculations/WEEK2_ARCHITECTURE_CHECKS.md](../calculations/WEEK2_ARCHITECTURE_CHECKS.md) | Prior check on dimensions and mass-data availability | Confirms unsupported geometry and subsystem mass remain TBD/UNKNOWN |
| SRC-05 | [DESIGN_GUIDELINES.md](../../../DESIGN_GUIDELINES.md) and [REQUIREMENTS_REGISTER.md](../../../REQUIREMENTS_REGISTER.md) | Traceability rules; distinguish sourced values, assumptions and calculations | Proposed study guidance; does not approve product requirements |
| SRC-06 | [EVALUATION_CRITERIA.md](../../../EVALUATION_CRITERIA.md), sections 3–6 and EC-03 | Scoring evidence rules and ₹2,00,000 comparison ceiling | Proposed study methodology; unknown evidence must remain NOT SCORED |
| SRC-07 | [Kritva actuator family spec, pinned revision](<https://github.com/KritvaOS/kritva-actuator/blob/31bfc20aed0479a3bce64cf8945e86b1fa6f2fa6/docs/architecture/ACTUATOR_FAMILY_SPEC.md>) | Provisional S/M/L torque bands and intended roles | S/L values are placeholders; M reference is not frozen; no variant mass, price or compatibility evidence |
| SRC-08 | [Actuator prototype sourcing and cost draft, pinned revision](<https://github.com/KritvaOS/kritva-actuator/blob/31bfc20aed0479a3bce64cf8945e86b1fa6f2fa6/docs/architecture/COMPONENTS_SOURCING_AND_COST.md>) | Checked as a possible cost-source reference | Separate A0 prototype scope; listings/estimates are not prices for these robot assemblies and are not used here |

## Source handling

Only values explicitly printed in SRC-01/SRC-02 are copied as CONCEPT_TARGET. No component mass, cost, material property, link length, moment arm, speed or acceleration is inferred from an unscaled drawing. Conditional calculations identify their exact target inputs, equations and scenario limits in the relevant CALC file. Missing inputs remain UNKNOWN/TBD.