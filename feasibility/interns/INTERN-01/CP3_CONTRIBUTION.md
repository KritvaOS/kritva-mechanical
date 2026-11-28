# INTERN-01 — CP3 Engineering Review Contribution (draft)

| Property | Value |
|---|---|
| Document ID | KMECH-CP3-INTERN-01 |
| Status | PROPOSED — partial contribution only |
| Version | 0.1.0 |
| Date | 2026-11-27 |
| Concepts | DA-01, QR-02, DA-04, QR-04 |

## 1. Scope of this contribution

Week-3 engineering feasibility assessment for the four assigned concepts:

- Joint torque and speed estimates (assumption-tagged).
- Preliminary mass ranges.
- Category-level cost models against the INR 2,00,000 ceiling.
- First-order stability / structure notes.
- Updated open-question and risk registers.
- Cross-concept comparison matrix (four concepts only).

This is **not** a complete CP3 record. The remaining eight concepts and authorized cross-team review are required before any CP3 acceptance claim.

## 2. Evidence summary

| Deliverable | Location | Status |
|---|---|---|
| Actuator analysis (torque/speed) | `concepts/*/ACTUATOR_ANALYSIS.md` | ESTIMATE produced |
| Calculation files | `concepts/DA-01/calculations/CALC-DA01-01_*.md` | Drafted |
| Mass budgets | `concepts/*/MASS_BUDGET.md` | Ranges produced |
| Cost models | `concepts/*/COST_MODEL.md` | Category ESTIMATE |
| Mechanical / stability notes | `concepts/DA-01/MECHANICAL_ANALYSIS.md` (+ notes in others) | Qualitative + first-order |
| Open questions / risks | `concepts/*/OPEN_QUESTIONS.md` | Updated |
| Comparison matrix | `interns/INTERN-01/COMPARISON_MATRIX.md` | Four-concept draft |
| Weekly status | `interns/INTERN-01/WEEKLY_STATUS.md` | Week 3 |

## 3. Key engineering conclusions (paper only)

1. DA-01 presents the lowest joint demand and is the only concept whose nominal cost sits comfortably inside the planning ceiling.
2. QR-02, DA-04 and QR-04 nominal cost models sit at or above the ceiling; actuator module cost is the dominant driver in every case.
3. QR-04 produces the highest leg joint moments because of increased leg length.
4. No S/M/L mapping is possible until source-controlled actuator data is supplied.
5. All numeric results remain ESTIMATE / ASSUMED and are subject to owner review.

## 4. HOLD and compliance

- No CAD, final BOM, supplier quotations, procurement, fabrication or physical testing.
- D-003 remains active.
- No claim of CP3 acceptance or task completion is made.

## 5. Requested reviewer actions

- Confirm or correct the assumption sets used for torque and mass.
- Supply or point to the controlled S/M/L actuator data pack.
- Resolve the outstanding OWNER_DECISION artwork items (wrist axis, mounting interfaces, sensors, mast).
- Indicate whether battery is in-scope for mobile concepts under the current HOLD reading.
