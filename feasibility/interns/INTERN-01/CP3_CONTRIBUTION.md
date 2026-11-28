# INTERN-01 — CP3 Contribution Draft (Week 3/4)

| Property | Value |
|---|---|
| Status | PROPOSED — contribution only; not CP3 review acceptance |
| Version | 0.2.0 |
| Last Updated | 2026-11-27 |
| Concepts | DA-01, QR-02, DA-04, QR-04 |
| HOLD | D-003 active |

This is a partial INTERN-01 evidence handoff for four assigned concepts. It is not a CP3 review of all 12 concepts and does not mark `ROB-MECH-044` complete. The task register and acceptance status are intentionally unchanged pending owner/reviewer action.

## 1. Evidence added or reconciled

- Added `REQUIREMENTS.md` for each assigned concept. Each records artwork targets and common requirement references, and is explicitly **INCOMPLETE** because no owner-approved concept-specific baseline exists.
- Added four accessible, not-to-scale SVG packaging mockups under each concept's `sketches/`. They are labeled paper-only/non-CAD and show unresolved owner decisions.
- Reconciled the DA-01 calculation arithmetic: listed shoulder-pitch terms sum to 2.332 N·m static; the point-mass inertia estimate gives 2.970 N·m raw with the stated acceleration. Shoulder pitch is not part of the current 3-DOF baseline, so it remains a conditional sensitivity only. Elbow/wrist branches and the wrist-axis ambiguity are explicit.
- Added a traceable DA-04 arm/base drive calculation; the base-drive static screen is 0.610 N·m per wheel at the stated 1.5× multiplier, replacing an earlier unexplained 0.8–1.2 N·m range.
- Reworked QR-02 and QR-04 leg screens to show their moment-arm assumptions, sensitivity and static-only boundary. Dynamic gait/impact remain UNKNOWN.
- Corrected the QR-02 mass-budget sums to 3.9 / 6.3 / 9.9 kg low/nominal/high.
- Added break-even actuator unit-price sensitivities at the INR 2,00,000 planning ceiling. These use existing category estimates only; there are no supplier quotes.
- Added source-controlled parent family-spec reference for torque-only screening. The referenced document labels S/L data placeholders and the M baseline not frozen; no exact S/M/L compatibility is claimed.

## 2. Task 044 acceptance-criteria evidence map (review pending)

| Criterion | Current evidence | Remaining gap / status |
|---|---|---|
| AC-044-01 — required concept files or explicit gaps | Required `REQUIREMENTS.md` files are now present; each marks missing approved requirements as INCOMPLETE and lists the next inputs. | **INCOMPLETE pending review**; no owner-approved requirements baseline. |
| AC-044-02 — torque/speed formulas, inputs, units and assumptions per joint | Calculation notes now show formulas, units, assumptions and static/inertial screens for assigned concepts. | **INCOMPLETE**: DA-01 axis mismatch and wrist branch unresolved; QR-02/QR-04 moment arms back-solved; speeds/duty and dynamic requirements remain TBD. |
| AC-044-03 — S/M/L compatibility per joint | Proposed family bands are referenced and compared as a torque-only screen. | **BLOCKED** for compatibility: S/L variant values are placeholders, M is not frozen, and speed/thermal/envelope/duty inputs are missing. EC-02 stays NOT SCORED. |
| AC-044-04 — numbers labeled, evidence type C, no unsupported validation claims | Added labels, formulas and explicit paper-only limitations. | **INCOMPLETE pending independent review**; no simulation, bench or physical evidence is claimed. |

## 3. Open owner/reviewer decisions

1. Resolve DA-01's shoulder yaw / shoulder-pitch axis count and wrist rotation/pitch definition.
2. Supply controlled, revisioned S/M/L variant output data and maturity; confirm operating speed/duty and thermal assumptions.
3. Define DA-04's wheel geometry, mass distribution, battery scope and mobile operating conditions.
4. Define QR-02/QR-04 joint poses and dynamic gait/load cases; decide QR-04's mounting/sensor details.
5. Review all estimates and their source/confidence labels before any task acceptance.

## 4. Downstream task boundary

The 12-concept CP2/CP3/CP4 tasks remain open: the other eight concepts, cross-intern evidence, owner decisions and formal review are outside this four-concept contribution. Do not mark those tasks complete or change HOLD D-003 based on this draft.
