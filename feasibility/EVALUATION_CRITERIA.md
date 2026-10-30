# Evaluation Criteria

| Property | Value |
|---|---|
| Document ID | KMECH-FS-004 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Feasibility Evaluation Criteria |
| Status | PROPOSED |
| Owner | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Proposed study methodology; weights and results require owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/INTERN_ASSIGNMENTS.md`, `feasibility/DESIGN_GUIDELINES.md`, `feasibility/REQUIREMENTS_REGISTER.md`, `feasibility/RISK_REGISTER.md` |

## 1. Purpose

This document defines a common evaluation method for comparing the 12 dual-arm and legged concepts. Scores support feasibility discussion; they do not constitute design approval, procurement authorization or release of mechanical HOLD D-003.

## 2. Proposed Weighted Criteria

The following weights are proposed study weights, not approved program priorities.

| ID | Criterion | Weight |
|---|---|---:|
| EC-01 | Mechanical feasibility | 20% |
| EC-02 | Actuator availability and compatibility | 15% |
| EC-03 | Hardware cost | 20% |
| EC-04 | Fabrication simplicity | 10% |
| EC-05 | Kritva platform demonstration value | 20% |
| EC-06 | Modularity and upgrade potential | 10% |
| EC-07 | Mechanical safety | 5% |
| | **Total** | **100%** |

## 3. Scoring Scale

Apply the same 0–5 scale to each criterion. A score must be supported by recorded evidence and rationale.

| Score | Definition |
|---:|---|
| 0 | Infeasible or unacceptable against the criterion, supported by evidence |
| 1 | Very weak; major unresolved limitations or substantial redesign likely |
| 2 | Weak; significant constraints, risks or assumptions remain |
| 3 | Plausible; appears feasible subject to identified conditions and further work |
| 4 | Strong; good feasibility with manageable limitations and supporting evidence |
| 5 | Very strong; compelling feasibility with well-supported evidence and limited unresolved concerns |

Do not assign zero merely because information is missing. Missing evidence must be recorded as `NOT SCORED`.

## 4. Required Evidence Recording

Every criterion score must include the following fields:

| Field | Required content |
|---|---|
| Criterion ID | EC-01 through EC-07 |
| Score | 0–5 or `NOT SCORED` |
| Evidence level | C, S, Sim, B, P, ESTIMATE or UNKNOWN |
| Evidence reference | File, calculation, source or record |
| Rationale | Reason for score and limitations |
| Assumptions | Relevant assumptions and their impact |

Evidence levels:
- **C:** Engineering calculation.
- **S:** Software or configuration evidence.
- **Sim:** Simulation evidence.
- **B:** Bench evidence.
- **P:** Physical evidence.
- **ESTIMATE:** Preliminary estimate, not independently verified.
- **UNKNOWN:** Evidence unavailable or insufficient to assess.

Evidence level identifies the basis of the assessment; it does not automatically imply evidence quality or validation.

### 4.1 UNKNOWN and NOT SCORED Rule

If a criterion has `UNKNOWN` evidence, its score must be `NOT SCORED`.

- Show the missing criterion explicitly in every scorecard.
- Do not substitute zero, a midpoint or an assumed score.
- Do not silently exclude the criterion or renormalize the remaining weights.
- Report the total scored weight and the weight not scored.
- Do not present a partial weighted result as a complete concept ranking.

An `ESTIMATE` may support a provisional score only when its assumptions, source and uncertainty are documented. Clearly label the resulting score provisional.

## 5. Minimum Evidence Rule

A concept is eligible for comparative scoring only when:

1. Its architecture and DOF are documented.
2. Major mechanical interfaces and load paths are identified.
3. Critical joint requirements are calculated or explicitly marked `TBD`.
4. Relevant stability, workspace or structural considerations are assessed.
5. Actuator compatibility has a documented basis or is marked `UNKNOWN`.
6. Mass and preliminary cost assumptions are traceable, or explicitly marked `UNKNOWN`.
7. Mechanical risks and safety concerns are recorded.

A concept that does not meet this minimum must be marked `INCOMPLETE` and excluded from any complete comparative ranking. Its missing evidence must remain visible.

## 6. Criterion Interpretation

- **EC-01 Mechanical feasibility:** Assess configuration, load paths, joint requirements, structural concerns, workspace and stability as applicable.
- **EC-02 Actuator availability and compatibility:** Assess derived joint torque/speed requirements against the S/M/L actuator direction. Distinguish technical compatibility from confirmed availability.
- **EC-03 Hardware cost:** Assess traceable preliminary hardware cost estimates against the ₹2,00,000 planning ceiling. Estimates are not quotations or procurement approval.
- **EC-04 Fabrication simplicity:** Assess part complexity, assembly, tolerance sensitivity and potential manufacturing routes. Manufacturing processes remain options only.
- **EC-05 Kritva platform demonstration value:** Assess whether the mechanical concept can support a reliable demonstration of Kritva Core, Edge, Sense and Motion capabilities as applicable. Consider compute integration, real-time control, sensing, actuation and integration complexity—not just mechanical capability.
- **EC-06 Modularity and upgrade potential:** Assess modular interfaces, serviceability, extensibility and compatibility with the existing Kritva architecture.
- **EC-07 Mechanical safety:** Assess foreseeable mechanical hazards, stability, pinch/crush risks, structural failure modes and required safeguards. Missing safety evidence must not be treated as a passing result.

## 7. Hard Gates — Independent of Score

A high weighted score cannot override a failed or unresolved hard gate.

| Gate | Requirement | Outcome if unmet or unknown |
|---|---|---|
| HG-01 | Preliminary hardware cost evaluated against INR 2,00,000 planning ceiling | `NOT PASSED` or `NOT ASSESSED` |
| HG-02 | S/M/L actuator compatibility assessed against derived joint requirements | `NOT PASSED` or `NOT ASSESSED` |
| HG-03 | Mechanical safety concerns assessed with no unresolved unacceptable hazard | `NOT PASSED` or `NOT ASSESSED` |
| HG-04 | Mechanical HOLD D-003 respected throughout the study | `NOT PASSED` if violated |

Hard-gate outcomes must be recorded separately from weighted scores. An unresolved gate prevents a concept from being represented as ready for implementation.

## 8. Weight Sensitivity Check

Before finalizing comparative recommendations:

1. Calculate the baseline comparison using the proposed weights.
2. Test reasonable alternative weight distributions, documenting each change and its rationale.
3. Identify whether concept rankings or shortlist membership change.
4. Highlight concepts whose ranking is sensitive to weight changes.
5. Do not adjust weights retrospectively to favour a preferred concept.

If evidence is incomplete, report sensitivity limitations rather than manufacturing a complete ranking.

## 9. Concept Scorecard Template

Create one scorecard per concept using this table. Repeat all seven criteria; do not omit unscored rows.

| Criterion | Weight | Score (0–5) | Evidence level | Evidence reference / rationale |
|---|---:|---:|---|---|
| EC-01 Mechanical feasibility | 20% | TBD | UNKNOWN | TBD |
| EC-02 Actuator compatibility | 15% | TBD | UNKNOWN | TBD |
| EC-03 Hardware cost | 20% | TBD | UNKNOWN | TBD |
| EC-04 Fabrication simplicity | 10% | TBD | UNKNOWN | TBD |
| EC-05 Platform demonstration value | 20% | TBD | UNKNOWN | TBD |
| EC-06 Modularity and upgrade | 10% | TBD | UNKNOWN | TBD |
| EC-07 Mechanical safety | 5% | TBD | UNKNOWN | TBD |
| **Total** | **100%** | **Not calculated** | | |

Additional scorecard fields:

- Concept ID and description:
- Assigned intern:
- Assessment revision and date:
- Minimum evidence rule: `PASS / INCOMPLETE`
- Total scored weight:
- Total weight not scored:
- Hard gates HG-01 to HG-04:
- Baseline weighted result, if valid:
- Sensitivity result:
- Key risks and unknowns:
- Recommendation and conditions:

## 10. Cross-Intern Independent Validation

Before CP4 recommendations are consolidated:

- Each intern independently reviews at least one concept assessed by another intern.
- The reviewer checks assumptions, units, calculations, evidence references, scoring rationale and hard-gate treatment.
- The reviewer records findings in the concept's `reviews/` folder.
- The original author responds to findings and records corrections or unresolved disagreements.
- The owner resolves material disagreements and reviews the final comparative assessment.

Independent validation is a review activity, not formal design verification or safety certification.

## 11. Shortlist Rule

The study recommendation should identify:
- Two dual-arm candidates.
- Two legged candidates.

Selection must consider evidence completeness, hard gates, risks, platform demonstration value and weight sensitivity. If fewer than two candidates in either family meet the minimum evidence and hard-gate expectations, report the shortfall; do not force a shortlist.

A shortlist is a recommendation for owner review only. It does not authorize CAD, BOM finalization, quotations, procurement, fabrication or physical testing.

## 12. HOLD D-003

All evaluation is paper-based. Do not create CAD, finalize a BOM, obtain quotations, procure components, fabricate hardware or conduct bench/physical testing under this study. Any subsequent activity requires an explicit owner decision. Evaluation scores and checkpoint completion do not release HOLD D-003.
