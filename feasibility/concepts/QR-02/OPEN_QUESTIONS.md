# QR-02 — Open Questions, Week 2 Risks and Dependencies

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Concept-specific open questions

| Local ID | Classification | Question | Why it matters | Proposed action owner | Status |
|---|---|---|---|---|---|
| QR-02-OQ-01 | OWNER_DECISION | Confirm intended sensor baseline among IMU, camera/RGB-D or stereo, and whether foot force sensing is included. | Affects body envelope, mass, cable routing and interfaces. | Owner / assigned intern; see action | OPEN |
| QR-02-OQ-02 | TBD | Define link lengths, joint offsets/frames, joint ranges, nominal body pose, foot positions and ground clearance. | Required for leg workspace and kinematic assessment. | Owner / assigned intern; see action | OPEN |
| QR-02-OQ-03 | UNKNOWN | Representative standing, lifted-leg and simple walking support poses; stride, terrain, payload position, speed and duty cycle. | Required for static support and later joint loading. | Owner / assigned intern; see action | OPEN |
| QR-02-OQ-04 | UNKNOWN | Ground-contact friction, footpad properties, impact and compliant/damper parameters. | Needed for traction/contact assessment. | Owner / assigned intern; see action | OPEN |
| QR-02-OQ-05 | UNKNOWN | Battery capacity/protection/charging and thermal path; battery space is mentioned in concept sheet but not drawn on cross-section. | Packaging and runtime remain open. | Owner / assigned intern; see action | OPEN |
| QR-02-OQ-06 | UNKNOWN | Actuator variant mass/envelope/mounting and source revision for each joint. | Needed for compatibility and detailed packaging. | Owner / assigned intern; see action | OPEN |

## 2. Preliminary risk records

Risk ratings below follow the global risk register scale and are qualitative `ESTIMATE`, not measured probabilities or validated safety assessments.

| Local risk ID | Risk | Cause / evidence gap | Likelihood | Impact | Mitigation / next action | Status | Linked requirements / unknowns |
|---|---|---|---|---|---|---|---|
| QR-02-R-01 | Joint loads may exceed candidate actuator S/M/L envelope. | No link geometry, mass distribution, gait, ground reaction or actuator data exists. | Med (ESTIMATE) | High (ESTIMATE) | Build per-joint load cases in Week 3 only after inputs are defined; compare per joint. | OPEN | FREQ-012, FREQ-013, FREQ-031; U-007, U-008 |
| QR-02-R-02 | Support polygon and ground-contact assumptions are not defined. | A stability or locomotion conclusion could be misleading. | Med (ESTIMATE) | High (ESTIMATE) | Document canonical stances and unknown ground properties; do not claim gait validation. | OPEN | FREQ-030, FREQ-031; U-006 |
| QR-02-R-03 | Optional sensors/foot force features and battery/cooling packaging are unresolved. | Mass, thermal, wiring and service access may change. | Med (ESTIMATE) | Med (ESTIMATE) | Obtain owner selection and platform envelope data. | OPEN | FREQ-021 to FREQ-025; U-003, U-010 |

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
