# DA-02 — Mechanical Analysis

| Property | Value |
|---|---|
| Document ID | KMECH-MECH-DA-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Mechanical Feasibility Analysis |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary paper analysis; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md` |

All results below are **ESTIMATES** from paper calculations (evidence C) on intern assumptions. Nothing is approved, validated or a requirement. Printed values from the artwork are CONCEPT_TARGET. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Analysis Scope

Concept ID/name: DA-02 — Humanoid Torso Dual-Arm (fixed torso, two 4-DOF arms, fixed base plate, optional one-axis head)

Analysis objective: Check on paper whether the DA-02 mechanical arrangement is plausible: load paths and stiffness, joint loading, workspace and arm overlap, base stability, mass, serviceability and safety. Identify what must be settled before the owner can assess feasibility.

Evidence basis:
- Sourced reference: `README.md` v0.3.1 (artwork, CONCEPT_TARGET, L0): base 300 mm × 250 mm, height 550 mm, reach 350 mm, shoulder-to-shoulder 600 mm (concept sheet only, D5), payload 0.1 – 0.2 kg.
- Calculated (C): hand calculations, filed as CALC-DA02-03 in `calculations/` (to be filed). Joint torques and masses are taken from CALC-DA02-01 (`ACTUATOR_ANALYSIS.md`) and CALC-DA02-02 (`MASS_BUDGET.md`); both are to be filed, and the section references in this document point into those two documents.
- ESTIMATE: every assumption below.

### 1.1 Assumptions used in this document

| ID | Assumption |
|---|---|
| S1 | Shoulder yaw axis is vertical; shoulder pitch, elbow and wrist pitch axes are horizontal and parallel (axis directions are ASSUMED: the sheet labels name the joints but this study does not take axis directions from them; intersection of yaw and pitch also assumed, ACTUATOR_ANALYSIS A11) |
| S2 | Shoulder axes at height z = 280 mm above the underside of the base plate and at the torso centre plane (y = 0); torso height 300 mm (MASS_BUDGET M2) |
| S3 | Link split 175 / 100 / 75 mm; masses per ACTUATOR_ANALYSIS A3–A8 and MASS_BUDGET M1–M11 |
| S4 | Representative accidental load at a gripper tip: 20 N (not printed on the sheets, chosen only to test margins) |
| S5 | Upper arm link modelled as an aluminium tube, 30 mm outer diameter, 2 mm wall, E = 69 GPa (illustrative, not a design choice) |
| S6 | Finger pad friction coefficient 0.5 (rubber or TPU pads are named on the concept sheet; the value is assumed) |
| S7 | Free-standing base on a flat, rigid surface; base fixing method is not defined |

## 2. Structure and Load Paths

- **Main structure and support configuration:** Fixed aluminium or steel base plate (10 mm aluminium assumed) under a humanoid torso frame (aluminium, 1.5 mm panels assumed) with an internal electronics bay. Arms attach at shoulder mounts on the torso sides. The base plate is not fixed to anything in the concept (S7).
- **Representative load cases:**
  - LC1: both arms fully extended forward and horizontal, 0.2 kg at each tip. Worst static case for the pitch joints.
  - LC2: LC1 with one arm carrying 0.1 kg, the other 0.2 kg (low-payload sensitivity).
  - LC3: arm acceleration, 10 rad/s² about the shoulder (inertial torque from ACTUATOR_ANALYSIS).
  - LC4: accidental 20 N load at one gripper tip, downward or horizontal (S4).
  - Not analysed: transport and handling, power-off droop, vibration.
- **Load paths:** payload and gripper → wrist module → forearm → elbow module → upper arm → shoulder pitch module → shoulder yaw module → shoulder mount → torso frame → base plate → supporting surface. Cables and the electronics are carried by the torso only and take no structural load.
- **Structural concerns:**
  1. *Shoulder mount root moment.* Per arm in LC1 the mount carries about 21 N vertical (modules, arm and payload) and a shoulder pitch reaction of 2.64 N·m. If shoulders sit 300 mm from the centre (D5, concept sheet only) on a torso 300 mm wide, the bracket overhangs the torso edge by about 150 mm. That adds about 3.2 N·m root bending (21 N × 0.15 m). The combined moment of about 4.1 N·m is the root-sum-square of two components assumed to act about perpendicular axes: the 2.64 N·m shoulder pitch reaction (about the horizontal pitch axis) and the 3.2 N·m overhang bending (about a horizontal axis along the arm direction). If both acted about the same axis the arithmetic sum would be about 5.8 N·m; the axis directions are assumed (S1), so the actual combination is not established. These mount results are valid only for the D5 case (600 mm spacing, shoulders at ±300 mm). If shoulders are at the torso edge, the overhang term is about zero. D5 decides.
  2. *Torso panels.* A 1.5 mm shell is only assumed; its racking stiffness and the local stiffness at the shoulder mounts are not checked.
  3. *Base plate.* Local bending near the torso walls and the fixing pattern are not checked.
- **Stiffness and deflection considerations:**
  - Link bending is small. For the assumed tube (S5, I ≈ 17,300 mm⁴) with about 9.8 N at the elbow end of the upper arm: δ = F·L³ / (3·E·I) = 9.81 × 175³ / (3 × 69,000 × 17,330) ≈ **0.015 mm**. Forearm and wrist links add only comparable amounts, so link bending is of the order of 0.01 – 0.05 mm at the tip.
  - Joint compliance will dominate (gearbox torsional stiffness, bearings, belts). Tip deflection from one joint is about (torque ÷ joint stiffness) × distance to tip. Illustration only, not a data value: if shoulder pitch had a stiffness of 1,000 N·m/rad, 2.64 N·m would give 2.6 mrad, or about 0.9 mm at a 350 mm tip. Gearbox stiffness data from S/M/L (TBD) are needed.
  - Cable and link compliance, if 3D-printed links are chosen, are not assessed.

## 3. Joint and Mechanism Analysis

Torques are per joint, one arm, 0.2 kg payload, arm extended (from CALC-DA02-01, to be filed); all are estimates. Joint torque derivations are not repeated here.

| Joint / mechanism | Load case | Required motion | Calculation reference | Result |
|---|---|---|---|---|
| Shoulder yaw (each arm) | LC1 pose, rotating about the vertical axis | Yaw sweep, range TBD; 90 °/s assumed | CALC-DA02-01 §4 | Inertial peak ≈ 0.71 N·m; static ≈ 0 N·m; the yaw bearing carries the shoulder pitch reaction moment (≈ 2.64 N·m) and about 21 N vertical load from the modules, arm and payload (bearing check TBD) |
| Shoulder pitch (each arm) | LC1 | Pitch, range TBD; 90 °/s assumed | CALC-DA02-01 §1 | ≈ 2.64 N·m holding, ≈ 3.35 N·m peak. Output bearing sees radial load ≈ 11.3 N (arm beyond the axis plus payload) and this moment. LC4 (20 N at tip, 0.35 m) gives ≈ 7.0 N·m, about 2.7× the holding torque |
| Elbow (each arm) | LC1 | Pitch, range TBD | CALC-DA02-01 §2 | ≈ 0.80 N·m holding, ≈ 0.91 N·m peak. LC4 at 0.175 m gives ≈ 3.5 N·m |
| Wrist (each arm) | LC1 | Pitch, range TBD | CALC-DA02-01 §3 | ≈ 0.21 N·m holding, ≈ 0.22 N·m peak. LC4 at 0.075 m gives ≈ 1.5 N·m |
| Gripper (each arm) | Parallel two-finger pick of 0.2 kg by friction (S6) | Open and close; stroke and speed TBD | CALC-DA02-03 §1 | Normal force per finger ≈ m·g / (2·μ) = 0.2 × 9.81 / (2 × 0.5) ≈ 2.0 N static; ≈ 4 N with a 2× planning factor. Actuation type and count TBD, may be passive |
| Head pan (optional) | Camera on neck mount; mass and geometry not printed | Pan about the vertical axis | none | Not analysed: TBD |
| Timing belts, bearings, mounting interfaces | Not defined on the sheets | TBD | none | Not analysed: TBD |

Torque, speed, range and loading values here are derived or marked TBD.

## 4. Dual-Arm Add-on Analysis

- **Arm workspace and reach:**
  - Each arm reaches a radius of 350 mm from its shoulder (printed, shoulder to gripper). With axis directions per S1, three parallel pitch joints plus yaw give three-dimensional gripper position and one controllable approach pitch. There is no gripper roll, so orientation is only partly controllable.
  - Joint ranges are not printed, so the real workspace is smaller than the 350 mm sphere and is TBD.
  - Wrist-reach assumption: the 275 mm shoulder-to-wrist reach used below is derived (175 mm upper arm + 100 mm forearm, S3), not printed; the sheets give only the 350 mm total.
  - Singular regions: full elbow extension at the reach limit, and the line through the yaw axis, where the azimuth is undefined.
  - *Table-level picking (shoulder height 280 mm, base standing on the work surface, S2):* with the arm straight, the gripper reaches the surface only within about 210 mm horizontally of the shoulder, which is about 85 mm beyond the 125 mm half-depth of the base. With the gripper pointing down (wrist at 75 mm height), the horizontal reach drops to about 183 mm, or about **58 mm** beyond the base edge. This is a finding for the owner, since the printed uses include pick-and-place.
- **Payload and payload location:** UNKNOWN as a requirement. Printed target 0.1 – 0.2 kg per arm, taken at the gripper tip (S3). Payload CoM offset in the grasp is not defined.
- **Base / torso stability under representative arm configurations (free-standing, S7):** Static estimates from the MASS_BUDGET centre of mass (total about 10.4 kg including 2 × 0.2 kg payload, weight about 102 N, CoM about 52 mm forward of the torso centre, 73 mm from the front edge of the 125 mm half-depth base). Restoring moment about the front edge ≈ 102 N × 0.073 m ≈ 7.5 N·m.

| Case | Overturning moment about front edge | Margin (restoring ÷ overturning) |
|---|---:|---:|
| LC1, both arms extended, with payload | n/a (CoM inside base) | CoM is 73 mm inside the front edge (125 mm − 52 mm); a distance, not a margin ratio |
| LC4a: extra 20 N downward at one tip (tip is 225 mm beyond the edge) | ≈ 4.5 N·m | ≈ 1.7 (tips at about 33 N) |
| LC4b: 20 N horizontal push forward at shoulder height (0.28 m) | ≈ 5.6 N·m | ≈ 1.3 |

  - These margins are thin for a robot with arms out. A fixed or clamped base is likely required. Lateral and one-arm cases and dynamic effects are not computed. The shoulder spacing question (D5) matters here: the CoM and tipping results use shoulders on the torso centre plane, so they are not valid for the D5 case (shoulders at ±300 mm), and lateral cases are not computed.
- **Inter-arm interference and collision considerations:**
  - Valid only for the D5 case: with 600 mm shoulder spacing and 350 mm reach, the two reach spheres overlap in a lens about 100 mm wide (±50 mm either side of the midline), with a maximum diameter of about 360 mm at the midline (√(350² − 300²) ≈ 180 mm radius).
  - Both shoulders are at the same height (S2), so grippers meeting in the lens are at the same height and can collide. Link, gripper and torso envelopes are not defined, so clearances are TBD.
  - Arm-to-torso clearance when an arm yaws inward or hangs down is TBD.
  - Geometry check for the owner: 600 mm shoulder spacing on a 300 mm torso and base, and an 800 mm overall width, are not clearly consistent (see D5 and `MASS_BUDGET.md`).
- **End-effector and support interfaces:** Two-finger linkage on a gripper mount with optional force sensor (on the concept sheet). Mount geometry, quick-change and any support for the base or table fixing are TBD.

## 5. Legged Add-on Analysis

Not applicable. DA-02 is in the dual-arm family with a fixed base plate and no legs or mobility. A mobile base is printed only as a future path and is not part of the study baseline, so no legged or locomotion analysis is performed here.

## 6. Mass, Serviceability and Safety

- **Preliminary mass breakdown (from `MASS_BUDGET.md`, ESTIMATE):** 10.02 kg baseline (structure 4.5, arm links 0.5, actuators 3.1, grippers 0.3, Edge and drivers 0.55, power 0.15, sensors and cabling 0.52, fasteners and miscellaneous 0.40), 10.62 kg with the head fitted. Range about 5.8 – 14.2 kg; the printed 8 – 12 kg has no stated basis. Arm mass beyond the shoulder pitch axis is about 0.95 kg each.
- **Service access and maintenance:** Not shown on the sheets. Open points: access to the electronics bay for Kritva Edge, drivers and the power board; replacing a joint module with cables routed through hollow links and shoulders; reaching the shoulder modules under the mounts; connector access at the wrist and gripper; the fan, if fitted. Modular joints with common interfaces (on the concept sheet) would help but are not defined.
- **Pinch/crush and structural hazards:**
  1. Pinch points at each joint, mainly shoulder yaw and pitch, the elbow and the wrist.
  2. Gripper finger closure (low force at about 2 – 4 N for the assumed payload, but actuator capability is TBD).
  3. Arm-to-arm shear in the overlap lens, and arm-to-torso crush.
  4. Gravity droop on power loss: holding torque is 2.64 N·m at the shoulder pitch, so the arm falls on power loss unless a holding strategy (brake or self-locking) is provided. That strategy is TBD; gearbox type is not selected and no backdrivability property is assumed.
  5. Free-standing tipping when arms are extended (Section 4).
  6. Tip speed: about 0.55 m/s from the shoulder alone at the assumed 90 °/s (higher with several joints moving).
  7. Sharp edges of CNC or sheet parts, and loose cables in moving joints.
- **Safeguards and unresolved safety questions:** emergency stop, torque and speed limits, brake or backdrivability, soft stops and hard stops at joint limits, guarding of pinch points, behaviour on power loss, base fixing, and operating rules around people. None is defined on the sheets and none is selected here.

## 7. Conclusions and Open Items

- **Findings:**
  1. Shoulder pitch is the dominant structural and actuator load (2.64 N·m holding); wrist and elbow loads are small.
  2. Link bending is negligible compared with expected joint compliance; stiffness will be set by gearboxes, bearings and mounts.
  3. Free-standing stability with arms extended has thin margins (about 1.3 – 1.7 against a 20 N disturbance), so base fixing should be assumed.
  4. Table-level picking reaches only about 58 – 85 mm beyond the base front edge, which may limit pick-and-place.
  5. The two workspaces overlap in a narrow lens about 100 mm wide on the midline, so the interference zone is small but at the same height.
  6. Four DOF give position plus approach pitch but no gripper roll.
  7. The shoulder spacing (D5) strongly affects mount loads, stability and overlap.
- **Limitations:** link split, shoulder height, torso height, tube section, accidental load and friction coefficient are assumptions. No joint ranges, stiffness data, bearing data or S/M/L data. Point masses and static or simple dynamic loads only. No finite-element or CAD work (HOLD D-003).
- **Required follow-up calculations:** workspace with joint ranges (kinematic sketch with frames); collision envelopes of links, grippers and torso; shoulder mount and bracket bending for each D5 outcome; bearing loads at each joint; joint and mount stiffness once S/M/L data exist; base fixing pattern and bolt loads; lateral and one-arm stability; power-off droop and braking; torso panel stiffness; head pan loading if fitted.
- **Open items and dependencies:** D5 shoulder spacing; shoulder height and torso height; joint ranges; whether the head is fitted; whether grippers are powered; S/M/L mapping (`ACTUATOR_ANALYSIS.md`); base fixing method; clarification of overall width versus shoulder spacing; owner-supplied requirements for payload, reach and mass (`REQUIREMENTS.md`).

## 8. HOLD D-003

Paper calculations and conceptual analysis only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
