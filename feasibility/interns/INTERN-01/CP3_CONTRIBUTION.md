# INTERN-01 — CP3 Contribution Draft (Week 3/4)

| Property | Value |
|---|---|
| Status | PROPOSED — evidence-gap handoff; not CP3 acceptance |
| Version | 0.3.0 |
| Last updated | 2026-11-28 |
| Concepts | DA-01, QR-02, DA-04, QR-04 |
| HOLD | D-003 active |

This contribution records source-backed concept targets, conditional arithmetic and missing evidence for four assigned concepts. It does not mark ROB-MECH-044 complete, change the task register or constitute a 12-concept review.

## 1. Evidence prepared

- Added one REQUIREMENTS.md per assigned concept. Each transcribes artwork targets as CONCEPT_TARGET and leaves unsupported values UNKNOWN/TBD.
- Four not-to-scale SVG concept mockups remain attached to this contribution. Their labels are source-transcribed targets; the sketches are not CAD or manufacturing dimensions.
- Replaced unsupported subsystem mass ranges with source-backed target records and UNKNOWN component masses/total. No system mass is forced to match artwork.
- Replaced unsupported cost bands and break-even prices with quote-ready scopes. Cost totals remain NOT COMPUTABLE; EC-03 is NOT SCORED.
- Replaced assumed link masses, moment arms, accelerations, wheel radii, slope values and multipliers with formulas and explicitly conditional scenarios. DA-04 contains one conditional payload-only horizontal shoulder-pitch term derived from printed payload/reach targets; DA-01 has no numeric torque because the baseline axes/geometry are insufficient. QR-02/QR-04 contain conditional one-leg force scenarios from printed mass targets. These are not total joint requirements or actuator ratings.
- Added source-register entries for concept READMEs/artwork, architecture, the common traceability/scoring rules and the pinned provisional actuator family specification. S/M/L roles and bands are cited as proposals only; no concept-to-family assignment is made.
- Updated the comparison note and matrix to report only source-backed target facts and evidence status. All criteria remain NOT SCORED; no weighted ranking or recommendation is published.

## 2. Task 044 evidence map — review pending

| Criterion | Current evidence | Remaining gap / status |
|---|---|---|
| AC-044-01 — required concept files or explicit gaps | Concept requirements records, source registers and open-input lists are present | INCOMPLETE; no owner-approved concept requirements baseline |
| AC-044-02 — torque/speed formulas, inputs, units and assumptions per joint | Equations and the exact source inputs available are recorded; conditional examples are separated from requirements | INCOMPLETE; joint geometry, component masses, pose, speed and duty are missing for complete per-joint calculations |
| AC-044-03 — S/M/L compatibility per joint | Pinned family spec roles and proposed ranges are cited | BLOCKED; S/L values are placeholders, M is not frozen, per-joint demands and variant data are not available |
| AC-044-04 — numbers labeled, evidence type C, no unsupported validation claims | Source targets, conditional calculations and unknowns are distinguished | INCOMPLETE pending independent review; no simulation, bench or physical evidence |

## 3. Comparison and scoring boundary

feasibility/EVALUATION_CRITERIA.md requires NOT SCORED when evidence is UNKNOWN and prohibits filling missing evidence with assumed scores. The prior score table and numeric partial ordering are withdrawn because costs and several criterion scores did not have the required source/rationale. Current scored weight is 0%; unscored weight is 100%. No ranking or shortlist is submitted.

## 4. Open inputs

1. Provide controlled actuator variant output, mass, speed-under-load, thermal and interface data.
2. Define concept-specific component geometry/masses and joint axes, frames, poses, motion and duty.
3. Define representative load-sharing, ground-contact and dynamic cases for both quadrupeds.
4. Select BOM items and obtain dated prices/quotes with quantities, tax/shipping treatment and budget inclusions.
5. Resolve source-artwork/decision-log questions and obtain owner/reviewer acceptance.

The remaining eight concepts, cross-intern evidence and formal CP3/CP4 reviews remain outside this four-concept contribution. Do not change task states or HOLD D-003 based on this draft.
