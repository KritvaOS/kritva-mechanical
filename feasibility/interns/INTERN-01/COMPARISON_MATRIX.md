# INTERN-01 — Four-Concept Comparison Matrix (Week 3/4 draft)

| Property | Value |
|---|---|
| Document ID | KMECH-CMP-INTERN-01 |
| Status | PROPOSED — paper comparison; not CP4 acceptance |
| Version | 0.3.0 |
| Last Updated | 2026-11-28 |
| Assigned Intern | INTERN-01 |
| HOLD | D-003 active |

Evidence level: ESTIMATE / C (paper calculation) where files exist. Scores remain provisional. The four concepts here do not complete the 12-concept comparison.

## 1. Weighted criteria (from EVALUATION_CRITERIA.md)

| ID | Criterion | Weight |
|---|---|---:|
| EC-01 | Mechanical feasibility | 20% |
| EC-02 | Actuator availability and compatibility | 15% |
| EC-03 | Hardware cost | 20% |
| EC-04 | Fabrication simplicity | 10% |
| EC-05 | Kritva platform demonstration value | 20% |
| EC-06 | Modularity and upgrade potential | 10% |
| EC-07 | Mechanical safety | 5% |

## 2. Scorecard (INTERN-01 concepts only)

| Criterion | DA-01 | QR-02 | DA-04 | QR-04 | Evidence / rationale |
|---|---:|---:|---:|---:|---|
| EC-01 Mechanical feasibility | 4 | 3 | 3 | 2 | DA-01 fixed base; QR-04 long-leg packaging risk. Assumption-based, not validated. |
| EC-02 Actuator compatibility | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | Proposed family torque ranges allow screening only; variant compatibility evidence is not available. |
| EC-03 Hardware cost | 4 | 2 | 1 | 1 | Nominal estimates INR 1.41 / 2.15 / 2.40 / 2.32 lakh; no quotes. See cost-ceiling sensitivities below. |
| EC-04 Fabrication simplicity | 4 | 3 | 2 | 2 | Fixed tabletop is conceptually simpler; mobile and long-leg configurations add interfaces/alignment. Qualitative. |
| EC-05 Demo value | 3 | 4 | 5 | 4 | Provisional qualitative judgment; owner/program review needed. |
| EC-06 Modularity | 3 | 3 | 3 | 4 | QR-04 cross-section indicates potential interface, but mounting details remain OWNER_DECISION. |
| EC-07 Mechanical safety | 3 | 3 | 2 | 2 | Qualitative only; no stability, gait or safety validation. |

## 3. Scored weight and partial ranking

- Scored weight: 85% (EC-02 remains NOT SCORED); weight not scored: 15%.
- Per EVALUATION_CRITERIA.md, missing weights are not renormalized. These are partial weighted contributions on the full 100% scale, not complete scores or a final ranking.
- The table gives a partial order among these four assigned concepts only; it must not be presented as a full 12-concept comparison or final recommendation.
- Calculation: sum(score × criterion weight) / 100; the unscored 15% remains visible.

| Partial rank | Concept | Partial weighted contribution (out of 5) | Scored weight |
|---:|---|---:|---:|
| 1 | DA-01 | 3.05 | 85% |
| 2 | QR-02 | 2.55 | 85% |
| 3 | DA-04 | 2.40 | 85% |
| 4 | QR-04 | 2.10 | 85% |

## 4. Cost-ceiling sensitivity (derived ESTIMATE; INR)

These break-even actuator prices hold each existing nominal non-actuator category total fixed. They are estimates derived from the current cost models, not quotes, availability data or an instruction to buy components.

| Concept | Actuator count | Current nominal per-module estimate | Max per-module estimate at ceiling | Current concept nominal | Difference to ceiling |
|---|---:|---:|---:|---:|---:|
| DA-01 | 6 | 12,500 | 22,333 | 1,41,000 | 59,000 below |
| QR-02 | 12 | 12,500 | 11,250 | 2,15,000 | 15,000 above |
| DA-04 | 10 | 14,000 | 10,000 | 2,40,000 | 40,000 above |
| QR-04 | 12 | 13,333 | 10,667 | 2,32,000 | 32,000 above |

## 5. Recommendation boundary

No final concept recommendation is made here. The partial ordering above is only a four-concept, 85%-weighted input while EC-02 is unscored. The official CP4 review requires all 12 concepts, owner-approved evidence/weights and the missing actuator data. No procurement or design selection is implied.
