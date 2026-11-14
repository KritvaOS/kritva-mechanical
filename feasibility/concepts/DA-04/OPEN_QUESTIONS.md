# DA-04 — Open Questions, Week 2 Risks and Dependencies

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Concept-specific open questions

| Local ID | Classification | Question | Why it matters | Proposed action owner | Status |
|---|---|---|---|---|---|
| DA-04-OQ-01 | OWNER_DECISION | Resolve README heading/name inconsistency: its title says 'Advanced Dual-Arm', while concept name and assignment say 'Humanoid Mobile Dual-Arm'. Do not change artwork brief sections 1–12 without authorization. | Name consistency and traceability. | Owner / assigned intern; see action | OPEN |
| DA-04-OQ-02 | OWNER_DECISION | Confirm whether printed future path (5-DOF arms/advanced base) must stay clearly excluded from current study baseline. | Avoid mixing the alternative with the fixed 10-actuator baseline. | Owner / assigned intern; see action | OPEN |
| DA-04-OQ-03 | UNKNOWN | Define representative arm poses/payload centres, joint ranges, speed and duty cycle. | Required for joint load and workspace analysis. | Owner / assigned intern; see action | OPEN |
| DA-04-OQ-04 | UNKNOWN | Wheel radius, track/wheelbase, wheel loading, floor friction, slope, acceleration and travel speed. | Required for drive, traction and stability analysis. | Owner / assigned intern; see action | OPEN |
| DA-04-OQ-05 | UNKNOWN | Mass distribution/centre of mass and battery envelope; battery is not shown and sizing is explicitly out of scope. | Required for meaningful stability and mass accounting; no battery selection. | Owner / assigned intern; see action | OPEN |
| DA-04-OQ-06 | OWNER_DECISION | Confirm optional grippers and sensor set; cross-section camera/torso IMU vs concept camera/IMU/LiDAR space. | Affects packaging, mass, routing and service access. | Owner / assigned intern; see action | OPEN |
| DA-04-OQ-07 | TBD | Clarify geometry datum/pose for 1200 mm overall width, 600 mm shoulder spacing, 450 mm reach per side and 1200 mm total reach. | The figures cannot be reconciled into a single posture without pose definition. | Owner / assigned intern; see action | OPEN |

## 2. Preliminary risk records

Risk ratings below follow the global risk register scale and are qualitative `ESTIMATE`, not measured probabilities or validated safety assessments.

| Local risk ID | Risk | Cause / evidence gap | Likelihood | Impact | Mitigation / next action | Status | Linked requirements / unknowns |
|---|---|---|---|---|---|---|---|
| DA-04-R-01 | Tall body, mass range and extended arm payload may create tipping risk. | No centre-of-mass or wheel reaction calculation exists. | Med (ESTIMATE) | High (ESTIMATE) | Obtain mass and pose assumptions; calculate later without inventing battery contribution. | OPEN | FREQ-015, FREQ-016, FREQ-027; U-003, U-004, U-005 |
| DA-04-R-02 | Differential-drive traction, wheel loading and turning envelope are undefined. | No wheel geometry, floor friction or motion profile is available. | Med (ESTIMATE) | High (ESTIMATE) | Request wheel/base source dimensions and operating assumptions. | OPEN | FREQ-015, FREQ-027; U-006, U-007 |
| DA-04-R-03 | Moving torso-to-base and articulated arm cable routes are unverified. | Potential bend fatigue, pinch, retention and service-access issue. | Med (ESTIMATE) | Med (ESTIMATE) | Record conceptual routing and request motion/connector envelopes. | OPEN | FREQ-017, FREQ-024, FREQ-025 |

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
