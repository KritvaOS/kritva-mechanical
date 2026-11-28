# INTERN-01 — Four-Concept Comparison Matrix (Week 3/4 draft)

| Property | Value |
|---|---|
| Document ID | KMECH-CMP-INTERN-01 |
| Status | PROPOSED — paper comparison; not CP4 acceptance |
| Version | 0.1.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 |
| HOLD | D-003 active |

**Evidence level:** ESTIMATE / C (calculation) where torque/mass/cost files exist. Scores use the 0–5 scale from `EVALUATION_CRITERIA.md`. Missing actuator source data forces several criteria to NOT SCORED.

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
| EC-01 Mechanical feasibility | 4 | 3 | 3 | 2 | DA-01 lowest moments & fixed base; QR-04 highest leg moments & long-leg packaging risk. All ESTIMATE. |
| EC-02 Actuator compatibility | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | No source-controlled S/M/L data pack yet. |
| EC-03 Hardware cost | 4 | 2 | 1 | 1 | Nominal costs: 1.41 / 2.15 / 2.40 / 2.32 L INR. Ceiling = 2.00 L. |
| EC-04 Fabrication simplicity | 4 | 3 | 2 | 2 | Fixed tabletop simplest; mobile + long-leg increase part count and alignment. |
| EC-05 Demo value | 3 | 4 | 5 | 4 | Mobile humanoid (DA-04) and agile quadruped highest platform demo interest. |
| EC-06 Modularity | 3 | 3 | 3 | 4 | QR-04 long-leg + mounting interface offers more upgrade paths (OWNER_DECISION items). |
| EC-07 Mechanical safety | 3 | 3 | 2 | 2 | Fixed base easier to guard; mobile and tall legged raise tip/fall risk. Qualitative only. |

## 3. Scored weight and provisional ranking

- Weight that could be scored: 65% (EC-02 excluded).
- Provisional weighted sum (scored criteria only, renormalised for illustration — **not** official):

| Concept | Provisional score (0–5) | Notes |
|---|---:|---|
| DA-01 | ≈ 3.6 | Best cost + feasibility balance |
| QR-02 | ≈ 3.0 | Balanced but cost marginal |
| QR-04 | ≈ 2.5 | Higher performance potential, higher risk/cost |
| DA-04 | ≈ 2.7 | Highest demo value, highest cost & complexity |

**These numbers are illustrative only.** Official CP4 scoring requires all 12 concepts, owner-approved weights, and actuator data.

## 4. Recommendation direction (paper only)

Under current evidence and the INR 2 L ceiling:

1. **DA-01** is the strongest near-term candidate for a low-risk platform demonstration.
2. **QR-02** remains viable if actuator cost can be held near the low end of the range.
3. **DA-04** and **QR-04** require either a higher budget ceiling or confirmed low-cost S-class actuators before they can be recommended inside the planning constraint.

Final recommendation is deferred to CP4 after the remaining eight concepts and owner decisions.
