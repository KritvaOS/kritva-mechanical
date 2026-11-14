# DA-01 — Open Questions, Week 2 Risks and Dependencies

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Concept-specific open questions

| Local ID | Classification | Question | Why it matters | Proposed action owner | Status |
|---|---|---|---|---|---|
| DA-01-OQ-01 | OWNER_DECISION | Confirm wrist axis: rotation, pitch, or another explicitly defined axis/frame. | Affects joint architecture, workspace and load-axis mapping. | Owner / assigned intern; see action | OPEN |
| DA-01-OQ-02 | OWNER_DECISION | Confirm whether cross-section-only 300 mm torso width and adjustable mast belong to the study baseline. | Affects package envelope and space reservations. | Owner / assigned intern; see action | OPEN |
| DA-01-OQ-03 | TBD | Define the pose, datum and measurement method for 350 mm reach per side, 700 mm total reach and 700 mm overall width. | The README flags these values as not describing the same posture without a stated pose. | Owner / assigned intern; see action | OPEN |
| DA-01-OQ-04 | UNKNOWN | Arm link lengths, joint offsets, axis frames, joint limits/ranges, payload location, speed and duty cycle. | Needed for kinematics, workspace and later Week 3 joint loading. | Owner / assigned intern; see action | OPEN |
| DA-01-OQ-05 | UNKNOWN | Tabletop support condition, friction, fastener/fixture assumptions and allowed overturning/sliding margin. | Needed for a stability calculation. | Owner / assigned intern; see action | OPEN |
| DA-01-OQ-06 | OWNER_DECISION | Confirm passive versus powered grippers and the intended optional sensor/mast configuration. | Changes actuator count, wiring, mass and packaging. | Owner / assigned intern; see action | OPEN |

## 2. Preliminary risk records

Risk ratings below follow the global risk register scale and are qualitative `ESTIMATE`, not measured probabilities or validated safety assessments.

| Local risk ID | Risk | Cause / evidence gap | Likelihood | Impact | Mitigation / next action | Status | Linked requirements / unknowns |
|---|---|---|---|---|---|---|---|
| DA-01-R-01 | Wrist-axis terminology is unresolved. | May invalidate joint mapping, workspace and torque direction. | Med (ESTIMATE) | High (ESTIMATE) | Obtain owner disposition; preserve both artwork labels until then. | OPEN | FREQ-026, FREQ-028; U-002, U-005, U-007, U-008 |
| DA-01-R-02 | Arm extension and payload could cause tabletop sliding/tipping or excessive base/link deflection. | No support model, load case, mass distribution or measured stiffness exists. | Med (ESTIMATE) | High (ESTIMATE) | Define representative poses/support; carry the calculation to Week 3 with sourced inputs. | OPEN | FREQ-015, FREQ-016, FREQ-027; U-003, U-004, U-005 |
| DA-01-R-03 | Cable bends/twist and optional mast/gripper packaging are unresolved. | Harness interference, service access and configuration changes may be missed. | Med (ESTIMATE) | Med (ESTIMATE) | Record cable corridor and owner-selected options; no harness design in Week 2. | OPEN | FREQ-017, FREQ-023, FREQ-024, FREQ-028 |

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
