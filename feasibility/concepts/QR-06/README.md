# QR-06 — Hexapod

| Property | Value |
|---|---|
| Document ID | KMECH-CONCEPT-QR-06 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Overview |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-03 |
| Version | 0.3.0 |
| Last Updated | 2026-10-31 |
| Authority | Feasibility study; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/REQUIREMENTS_REGISTER.md`, `docs/images/ARTWORK_MANIFEST.json`, `REQUIREMENTS.md`, `ARCHITECTURE.md` |


## 1. Purpose and Scope

QR-06 is the six-legged concept: a hexapod with two DOF per leg (named coxa and femur/tibia on the concept sheet), 12 actuators, and a low centre of gravity for statically stable walking and multi-leg coordination. This README records the printed values of both sheets and decides neither. It does not approve any value.

- Concept ID: QR-06
- Concept name: Hexapod
- Family: Legged
- Complexity: High (relative engineering category, not a validated assessment)
- Assigned intern: INTERN-03
- Assessment revision: none yet (NOT STARTED)

## 2. Reference Artwork

![KMECH-CONCEPT-QR-06 — Hexapod concept design](../../../docs/images/KMECH-CONCEPT-QR-06.png)

*Concept sheet: `docs/images/KMECH-CONCEPT-QR-06.png`. This is the primary configuration reference.*

![KMECH-CROSS-SECTION-QR-06 — Hexapod internal structure](../../../docs/images/KMECH-CROSS-SECTION-QR-06.png)

*Cross-section sheet: `docs/images/KMECH-CROSS-SECTION-QR-06.png`. This is an illustrative internal arrangement.*

Both sheets are concept artwork (evidence type C, PROPOSED, maturity L0 as proposed in the planning discussion). They are not to scale, are not CAD, and are not engineering evidence. The earlier `.svg` sketch is superseded by these sheets.

## 3. Configuration

| Item | Value | Source |
|---|---|---|
| Robot type | Hexapod legged robot, six legs, rigid central body | Concept and Cross-section |
| Legs | 6 (left and right pairs at front, middle and rear) | Concept and Cross-section |
| DOF per leg | 2 (coxa; femur/tibia) | Concept and Cross-section |
| Total leg DOF / actuators | 12 (6 × 2) | Concept and Cross-section |
| Feet | High-friction rubber pad (concept); interchangeable rubber or TPU with 6-axis optional force sensor (cross-section) | Concept and Cross-section |
| Sensors and compute | Concept: space for battery, controllers and sensors. Cross-section: Kritva Edge and an optional top sensor module (RGB-D camera and IMU), height adjustable | Concept and Cross-section |
| Environment | Indoor and outdoor flat terrain testing | Concept |

## 4. CONCEPT_TARGET

Every value is printed on the artwork and is `CONCEPT_TARGET`: indicative, unapproved, and not a requirement. Requirements-register values stay `UNKNOWN` or `TBD` until the owner resolves them. Where the sheets disagree, both values are shown and marked `DISCREPANCY — OWNER REVIEW`; nothing is chosen by inference.

| Item | Value as printed | Source sheet | Status |
|---|---|---|---|
| Total actuators | 12 | Concept and Cross-section | CONCEPT_TARGET |
| Leg count | 6 | Concept and Cross-section | CONCEPT_TARGET |
| Body length (L) | 400 mm | Concept and Cross-section | CONCEPT_TARGET |
| Body width (W) | 280 mm | Concept and Cross-section | CONCEPT_TARGET |
| Body height (H) | 220 mm | Concept and Cross-section | CONCEPT_TARGET |
| Overall length (with leg extension) | 520 mm | Concept and Cross-section | CONCEPT_TARGET |
| Overall width (with leg extension) | 480 mm | Concept and Cross-section | CONCEPT_TARGET |
| Target weight | 3 – 5 kg (est.) | Concept | CONCEPT_TARGET |
| Target payload | 0.5 – 1.0 kg (est.) | Concept | CONCEPT_TARGET |
| Supply voltage | 24 V DC (concept-level power indication, not a confirmed electrical interface) | Concept and Cross-section | CONCEPT_TARGET |
| Power rails shown inside | 24 V in; 5 V and 12 V rails | Cross-section | CONCEPT_TARGET |
| Primary use | Stable walking, multi-leg coordination, gait control, perception and autonomy research, Kritva platform demonstration | Concept | CONCEPT_TARGET |
All dimensions, DOF and actuator counts printed on both sheets agree after the cross-section sheets were regenerated on 2026-10-31. A value printed on one sheet only names that sheet. The concept sheet's own view notes say dimensions are indicative. Items not printed on either sheet (for example joint torque, speed, stride, battery capacity, camera models) stay TBD.

## 5. Mechanical Architecture

Subsystem-level description from the sheets. Materials and mechanisms are options shown on the artwork, not selections. There is no CAD. The cross-section sheet is not used to infer hexapod internals because it shows a different robot.

| Element | What the artwork shows | Status |
|---|---|---|
| Body | Compact rigid central body with modular mounting, electronics bay for Kritva Edge, power distribution and sensors; top sensor puck shown on the concept render | Illustrative |
| Legs | Six lightweight interchangeable leg assemblies of two joints each, arranged in left and right pairs at front, middle and rear | Illustrative; see D1 |
| Joint assemblies | BLDC/PMSM actuator housings compatible with Kritva S/M/L architecture (concept); the cross-section shows coxa and femur/tibia joints with BLDC and gearbox | Illustrative |
| Feet | High-friction rubber pad (concept) | Illustrative |
| Body mounting interface | 4 × M5 holes and 2 × Ø5 mm dowels labelled 'indicative concept' on the cross-section only | Illustrative; see D6 |
| Sensor module | Optional top sensor module on a height-adjustable mount | Optional |

## 6. Joint and Actuator Mapping

Mapping as printed on the concept sheet. Motor model, torque, speed, gear ratio and S/M/L assignment are not given by any approved source and stay TBD.

| Joint or actuator | Intended motion or axis | DOF | Proposed technology (as shown) | Baseline or optional |
|---|---|---|---|---|
| Coxa (each leg) | Hip joint of the leg; axis not stated on the sheet | 1 | BLDC/PMSM, Kritva S/M/L compatible | Baseline |
| Femur/Tibia (each leg) | Leg bend joint; whether the label means one combined joint or femur and tibia joints is unclear (see D2) | 1 | BLDC/PMSM, Kritva S/M/L compatible | Baseline |

Count: 2 DOF × 6 legs = 12 actuators; both sheets state 12. The labels 'Coxa' and 'Femur/Tibia' name two joints at 1 DOF each on the cross-section; whether femur and tibia are one combined joint is not stated (D2). The concept sheet calls the actuators Kritva S/M/L compatible; this study has not mapped any joint to S, M or L.

## 7. Electronics and Power

Block-level placement and interfaces as shown on the sheets; there is no wiring schematic.

| Block | What the artwork shows | Status |
|---|---|---|
| Kritva Edge (compute and control) | Board in the central body | Illustrative; board dimensions TBD |
| Power distribution | 24 V in with 5 V and 12 V rails | Illustrative; electrical requirements TBD |
| Battery, controllers | Space in the central body (concept); no battery is drawn on the cross-section | Illustrative; capacity and layout TBD |
| Sensors | Optional top sensor module (RGB-D camera and IMU), height adjustable; USB / MIPI sensor interface | Optional; sensor selection TBD |

## 8. Cable Routing and Serviceability

Routes as labelled on the cross-section sheet ('cable routing through leg') and on the concept sheet. No harness design is implied.

- Cable routing runs through the leg structure and links (both sheets).
- Concern to investigate: six legs with two joints each means twelve joint harnesses and a denser hip region than any quadruped concept; not designed here.

## 9. Risks and Unknowns

1. The body mounting interface (D6) is not on the concept sheet; its effect on six-leg packaging is UNKNOWN until the owner decides.
2. Leg joint definition is ambiguous (D2); kinematics, workspace and gait planning cannot start until it is clarified.
3. Two-DOF planar legs cannot move laterally; turning and sideways motion of a hexapod with 2-DOF legs depend on the hip axis, which is UNKNOWN.
4. Twelve actuators at 3 – 5 kg (est.) leave little mass per leg; actuator sizing and S/M/L compatibility are unassessed.
5. Packaging: six hip interfaces on a 400 mm × 280 mm body leave little room for battery and electronics; not assessed.
6. Printed weight and payload targets have no stated basis.

## 10. Artwork Discrepancies

| ID | Discrepancy | Sheets | Status |
|---|---|---|---|
| D1 | Leg count and DOF: 6 legs with 2 DOF each (concept) vs a four-legged robot with 3 DOF per leg (cross-section) | Both | RESOLVED (cross-section regenerated 2026-10-31); the cross-section now shows a hexapod with 2 DOF per leg |
| D2 | Joint definition: 'Coxa + Femur/Tibia' is listed as 2 DOF; the cross-section labels coxa 1 DOF and femur/tibia 1 DOF, so whether femur and tibia are one joint is not stated | Both | OPEN — OWNER REVIEW |
| D3 | Body size: 400 × 280 × 220 mm (concept) vs 1000 × 420 × 520 mm (cross-section) | Both | RESOLVED (cross-section regenerated 2026-10-31); both print 400 × 280 × 220 mm, overall 520 × 480 mm |
| D4 | Titles and extras: 'Modular / Expandable', payload bay, advanced sensors and 'Kritva Nexus' on the cross-section | Cross-section | RESOLVED (cross-section regenerated 2026-10-31); removed |
| D5 | Weight and payload appear on the concept sheet only | Concept | NOT VERIFIABLE FROM CURRENT ARTWORK |
| D6 | Body mounting interface (4 × M5 holes, 2 × Ø5 mm dowels) is 'indicative concept' on the cross-section and is not on the concept sheet | Cross-section | OPEN — OWNER REVIEW |
| D7 | Cross-section subtitle prints the body size as '400 × 280 × 280 × 220 mm' (duplicated 280) | Cross-section | OPEN; fix requested in the next artwork round |

The two sheets now agree on six legs, 2 DOF per leg, 12 actuators, body 400 × 280 × 220 mm and overall 520 × 480 mm. Review status: concept sheet `REVIEWED_WITH_ISSUES` (D2), cross-section `REVIEWED_WITH_ISSUES` (D6, D7) in `docs/images/ARTWORK_MANIFEST.json`. REVIEWED is not design approval.

## 11. Feasibility Activity and Evidence

What the assigned intern investigates, using paper methods only (calculations, comparison tables, sketches and cited datasheets):

- [ ] Clarify the leg joint definition and axes with the owner (D2), then draw the hexapod leg kinematic sketch with frames (evidence C)
- [ ] Draw tripod-gait support polygons and estimate static stability margin for the six-leg arrangement (evidence C)
- [ ] Estimate static joint torque for a stated body mass in tripod stance (evidence C)
- [ ] Estimate mass by subsystem with assumptions listed, separately from the printed 3 – 5 kg (evidence C)
- [ ] Sketch a body layout with six hip interfaces, battery and electronics (evidence C)
- [ ] List harness paths through six legs (evidence C)
- [ ] Record intern-generated cost assumptions separately from printed targets; no quotation or procurement

## 12. Revision and Traceability

| Item | Value |
|---|---|
| README revision | 0.3.0 |
| Concept sheet | `docs/images/KMECH-CONCEPT-QR-06.png` |
| Cross-section sheet | `docs/images/KMECH-CROSS-SECTION-QR-06.png` |
| Manifest | `docs/images/ARTWORK_MANIFEST.json` |
| Review state | Artwork audited by Claude (round 6, 2026-10-31); owner confirmation pending. This README records what the artwork prints and does not approve any value |

## 13. Folder Contents

This README and the two artwork sheets exist today. The files and folders below are created by the assigned intern as work progresses, using `feasibility/templates/`. There is no `cad/` folder while HOLD D-003 is active.

- `REQUIREMENTS.md`
- `ARCHITECTURE.md`
- `MECHANICAL_ANALYSIS.md`
- `ACTUATOR_ANALYSIS.md`
- `INTERFACES.md`
- `MASS_BUDGET.md`
- `COST_MODEL.md`
- `OPEN_QUESTIONS.md`
- `calculations/`
- `references/`
- `reviews/`
- `sketches/`

## 14. Current Assessment

- Overall status: NOT STARTED (README expanded from the artwork on 2026-10-31; no feasibility assessment has been performed)
- Requirements completeness: TBD
- Architecture assessment: TBD
- Engineering assessment: TBD
- Actuator compatibility: TBD
- Cost assessment: TBD
- Major risks: TBD
- Evidence gaps: TBD

## 15. Checkpoint Progress

| Checkpoint | Status | Review reference |
|---|---|---|
| CP2 | TBD | `reviews/` |
| CP3 | TBD | `reviews/` |
| CP4 | TBD | `reviews/` |

## 16. Open Decisions

1. The leg joint definition: coxa and femur/tibia as two joints (D2); the owner decides.
2. Whether the body mounting interface is kept as indicative concept (D6).
3. Subtitle typo (D7), to be fixed in the next artwork round.
4. Weight and payload targets remain `UNKNOWN` in the requirements register until resolved.
5. Joint to S/M/L actuator mapping is not started.

## 17. HOLD D-003

Paper feasibility work only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
