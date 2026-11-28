# INTERN-01 — Weekly Feasibility Status (Week 3 update)

| Property | Value |
|---|---|
| Document ID | KMECH-WEEKLY-INTERN-01 |
| Status | PROPOSED — Week 3 working update |
| Version | 0.2.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 (Amardeep) |
| HOLD | D-003 remains active |

## 1. Reporting period

- Week: 3 (torque / actuator / mass / cost modelling)
- Concepts: DA-01, QR-02, DA-04, QR-04
- Task linkage: contributes to ROB-MECH-044 / Week-3 engineering assessment (registration pending)

## 2. Work completed this period

| Concept | Actuator torque estimates | Mass ranges | Cost ranges | Notes |
|---|---|---|---|---|
| DA-01 | Yes (CALC-DA01-01) | Yes | Yes | Lowest demand; nominal cost inside ceiling |
| QR-02 | Yes | Yes | Yes | Nominal cost near/above ceiling |
| DA-04 | Yes (arms + drive) | Yes | Yes | Nominal cost above ceiling |
| QR-04 | Yes | Yes | Yes | Highest leg moments; cost above ceiling |

All estimates are tagged ASSUMED / ESTIMATE. No S/M/L assignment performed (blocked on actuator source data). No CAD, BOM, quotations or physical work.

## 3. Key observations (paper only)

1. **DA-01** is the most budget-friendly of the four under current assumptions; shoulder continuous demand ≈ 3.2 N·m after margin.
2. **QR-02 / QR-04** and **DA-04** nominal cost models sit at or above the INR 2 L planning ceiling; actuator module cost is the dominant lever in every case.
3. Longer legs on QR-04 raise hip/knee moments relative to QR-02; dynamic gait would raise them further.
4. Mobile DA-04 adds battery and drive channels that further pressure both mass and cost.

## 4. Open decisions still required from owner

- DA-01 wrist axis (D4) and torso/mast items (D3/D5).
- QR-02 / QR-04 optional sensor and mounting-interface questions.
- Actuator S/M/L source data pack (mass, torque, price, envelope) with controlled revision.
- Confirmation whether battery is in-scope for mobile concepts under the current HOLD interpretation.

## 5. Next actions (Week 4 direction)

- Incorporate any owner decisions and actuator data.
- Produce comparative scoring matrix across the four concepts (and later all 12).
- Risk register updates and recommendation draft for CP4.
- Keep all work on a feature branch and open a PR; never push to main.

## 6. D-003 compliance

Paper documentation and calculation only. No CAD, procurement, fabrication or physical testing. Intern confirmation of compliance: pending local integration and review.
