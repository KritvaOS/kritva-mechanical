# QR-04 — Open Questions, Week 2 Risks and Dependencies

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Concept-specific open questions

| Local ID | Classification | Question | Why it matters | Proposed action owner | Status |
|---|---|---|---|---|---|
| QR-04-OQ-01 | OWNER_DECISION | Confirm disposition of cross-section-only 4 × M5 / 2 × Ø5 mm dowel body mount. | No position, datum, tolerance, grade, preload or load capacity is specified. | Owner / assigned intern; see action | OPEN |
| QR-04-OQ-02 | OWNER_DECISION | Confirm whether the cross-section-only adjustable sensor module is part of the baseline and whether it carries RGB-D plus IMU. | Affects packaging, mass, cable route and centre of mass. | Owner / assigned intern; see action | OPEN |
| QR-04-OQ-03 | TBD | Define leg link lengths, joint offsets/frames, joint ranges, standing pose, gait geometry and foot trajectory. | Needed for workspace, clearance and joint requirements. | Owner / assigned intern; see action | OPEN |
| QR-04-OQ-04 | UNKNOWN | Define representative terrain, friction/contact, body mass distribution, payload, gait/stride, speed and duty cycle. | Needed for stability and joint load assessment. | Owner / assigned intern; see action | OPEN |
| QR-04-OQ-05 | UNKNOWN | Battery location/capacity/protection/charging; concept sheet mentions space, cross-section does not show battery. | Mass and thermal packaging remain incomplete. | Owner / assigned intern; see action | OPEN |
| QR-04-OQ-06 | UNKNOWN | Cooling path, compute/driver envelope and actuator mounting specifications. | Cross-section does not show cooling and no interface drawings are supplied. | Owner / assigned intern; see action | OPEN |

## 2. Preliminary risk records

Risk ratings below follow the global risk register scale and are qualitative `ESTIMATE`, not measured probabilities or validated safety assessments.

| Local risk ID | Risk | Cause / evidence gap | Likelihood | Impact | Mitigation / next action | Status | Linked requirements / unknowns |
|---|---|---|---|---|---|---|---|
| QR-04-R-01 | Long-leg geometry and mass distribution may increase joint loads and leg inertia. | No link geometry, mass or gait/load inputs are sufficient to quantify torque or speed. | Med (ESTIMATE) | High (ESTIMATE) | Carry each joint requirement as TBD; request geometry/mass/gait inputs for Week 3. | OPEN | FREQ-012, FREQ-013, FREQ-031; U-003, U-006, U-007, U-008 |
| QR-04-R-02 | Support and dynamic stability cannot be assessed without defined stance/gait/CoM/contact inputs. | A claimed agility or trotting stability would be unsupported. | Med (ESTIMATE) | High (ESTIMATE) | Define representative configurations before calculations; no gait validation. | OPEN | FREQ-030, FREQ-031; U-003, U-006 |
| QR-04-R-03 | Cross-section-only mounting interface may be mistaken for an approved interface. | Unverified hole pattern/load/tolerance could be propagated into later design. | Med (ESTIMATE) | High (ESTIMATE) | Keep it explicitly indicative and obtain owner decision. | OPEN | FREQ-015, FREQ-025; U-002, U-010 |

These are concept-local records. Do not edit or duplicate the shared `feasibility/RISK_REGISTER.md` without owner authorization. Global risks FRISK-001 to FRISK-007 remain in the shared register and should be cross-referenced where applicable.

## 3. Week 2 unresolved architecture data

- Joint coordinate frames and axis unit vectors: `TBD` where not explicitly defined.
- Joint angular ranges / end stops / reference zero: `TBD`.
- Link lengths and offsets: `UNKNOWN` unless source-supported.
- Joint continuous/peak torque and output speed: `TBD` pending Week 3 calculations.
- Actuator size S/M/L: `TBD` pending per-joint compatibility assessment.
- Component mass and centre of mass: `UNKNOWN`; printed total mass range remains a `CONCEPT_TARGET`.
- Interface datums, tolerances, load capacities and detailed mounting geometry: `TBD`.
- Board dimensions, connectors, thermal limits, power budgets and harness dimensions: `TBD`.
- Material grade and manufacturing process: options only; no selection.

## 4. Shared study unknowns linked to this concept

| Global unknown | Status from shared register | Concept treatment |
|---|---|---|
| U-001 preferred architecture | TBD | No ranking / selection in Week 2 |
| U-002 dimensions and envelopes | TBD | Record sourced artwork dimensions only |
| U-003 mass and distribution | UNKNOWN | Target range transcribed; no subsystem estimate |
| U-004 payload | UNKNOWN | Artwork target, not approved requirement |
| U-005 arm reach | UNKNOWN | Relevant to DA concepts; define pose/datum |
| U-006 locomotion/operating requirements | UNKNOWN | Relevant to QR concepts; support/gait/terrain inputs |
| U-007 joint torque and speed | TBD | Per-joint placeholders in `ACTUATOR_ANALYSIS.md` |
| U-008 joint-to-actuator S/M/L | TBD | No assignment until demands and actuator data exist |
| U-009 actuator inventory/cost | UNKNOWN | Requires actuator-owner source |
| U-010 materials/process | TBD | Options only |
| U-011 final BOM/quotations | NOT STARTED | Excluded by D-003 |
| U-012 CAD/physical authorization | OWNER DECISION REQUIRED | D-003 stays active |

## 5. Week 3 dependencies

Prioritize owner decisions affecting baseline interpretation; obtain actuator source revisions and mechanical interface data; define geometry/datum and representative payload/load/motion cases; obtain mass distribution and operating assumptions; then perform only traceable calculations. Do not close a question by selecting an unsupported value.
