# DA-03 — Mechanical Analysis

| Property | Value |
|---|---|
| Document ID | KMECH-MECH-DA-03 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Mechanical Feasibility Analysis |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary paper analysis; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md` |

All results are **ESTIMATES** from paper calculations (evidence C) on intern assumptions. Nothing is approved. Printed values are CONCEPT_TARGET. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Analysis Scope

Concept ID/name: DA-03 — Mobile Dual-Arm (four-wheel paired differential drive, fixed torso, two 3-DOF arms)

Analysis objective: Check on paper whether the DA-03 arrangement is plausible: load paths and stiffness, joint loading, arm workspace, base stability and turning, mass, serviceability and safety, and identify what must be settled first.

Evidence basis:
- Sourced reference: `README.md` v0.3.1 (artwork, CONCEPT_TARGET, L0).
- Calculated (C): CALC-DA03-03 (to be filed), using results from CALC-DA03-01 (`ACTUATOR_ANALYSIS.md`) and CALC-DA03-02 (`MASS_BUDGET.md`); all three are to be filed, and the section references below point into those documents.
- ESTIMATE: every assumption below.

### 1.1 Assumptions used here

| ID | Assumption |
|---|---|
| S1 | Shoulder yaw axes vertical at the torso sides (x = ±150 mm, from the 300 mm torso width), at y = 0, 400 mm above ground; elbow and wrist axes horizontal and parallel; upper arm rigid and horizontal. Axis directions are ASSUMED from the joint names (Yaw, Pitch); the sheets do not print them |
| S2 | Link split 175 / 100 / 75 mm; masses per `ACTUATOR_ANALYSIS.md` A4 – A10 and `MASS_BUDGET.md` M1 – M12 |
| S3 | Wheel contact points at ±190 mm (track 380 mm) and ±150 mm (wheelbase 300 mm); 100 mm wheels |
| S4 | Representative accidental load at a gripper tip: 20 N (not printed) |
| S5 | Upper arm as an aluminium tube, 30 mm outer diameter, 2 mm wall, E = 69 GPa (illustrative) |
| S6 | Finger pad friction coefficient 0.5 |
| S7 | Flat, rigid, dry indoor floor; static analysis |

## 2. Structure and Load Paths

- **Main structure and support configuration:** Base frame (5 mm aluminium assumed) carrying the wheel drives and battery; fixed torso on top with the electronics enclosure; optional mast on the torso. Four wheels support the platform.
- **Representative load cases:** LC1 both arms extended forward, 0.2 kg at each tip. LC2 turning in place (scrub). LC3 driving on a 5° slope. LC4 accidental 20 N load at a gripper tip (S4). LC5 transit shock, 2× holding loads with arms not stowed. Not analysed: vibration, kerbs and steps, collisions.
- **Load paths:** payload and gripper → wrist module → forearm → elbow module → upper arm → shoulder yaw module → shoulder mount → torso → base frame → axles and bearings → wheels → floor.
- **Structural concerns:**
  1. There is no shoulder pitch joint, so the upper arm is a fixed cantilever and the yaw output bearing carries about 2.64 N·m moment (5.28 N·m in LC5) and about 11 N vertical load per arm.
  2. Shoulder mounts (valid only for the S1 case of shoulders at ±150 mm): if shoulders sit at ±150 mm on the torso sides, overhang is small; if the 800 mm width is correct, the shoulder spacing is much less (D5) and the mounts must sit differently.
  3. Axle and wheel bearing loads, and the base frame under battery and drive loads, are not checked.
  4. Mast bending and sway if the mast is tall and the camera heavy (D6).
- **Stiffness and deflection considerations:**
  - Link bending is small: tube I ≈ 17,300 mm⁴; about 9.8 N at 175 mm gives δ ≈ 0.015 mm. Root stress at 2.64 N·m is about 2.3 MPa, which is negligible.
  - Joint and bearing compliance will dominate; illustration only: at 1,000 N·m/rad, 2.64 N·m gives 2.6 mrad, about 0.9 mm at a 350 mm tip. Stiffness data are TBD.
  - Tyre and suspension compliance (no suspension shown) affect the base; not assessed.

## 3. Joint and Mechanism Analysis

Torques are per joint, worst case, 0.2 kg payload, from CALC-DA03-01 (to be filed); all are estimates.

| Joint / mechanism | Load case | Required motion | Calculation reference | Result |
|---|---|---|---|---|
| Shoulder yaw (each arm) | LC1, rotating about the vertical axis | Yaw sweep, range TBD; 90 °/s assumed | CALC-DA03-01 §3 | Actuator ≈ 0.71 N·m peak, ≈ 0 static; bearing carries ≈ 2.64 N·m moment and ≈ 11.3 N |
| Elbow (each arm) | LC1 | Pitch, range TBD | CALC-DA03-01 §1 | ≈ 0.80 N·m holding, ≈ 0.91 N·m peak; LC4 gives ≈ 3.5 N·m; LC5 ≈ 1.6 N·m |
| Wrist (each arm) | LC1 | Pitch, range TBD | CALC-DA03-01 §2 | ≈ 0.21 N·m holding, ≈ 0.22 N·m peak; LC4 gives ≈ 1.5 N·m |
| Wheel drive (each channel) | LC2 and LC3 | Continuous rotation; 0.5 m/s assumed | CALC-DA03-01 §4 | ≈ 0.6 N·m (straight, 5°); ≈ 2.5 N·m turning in place at the wheel |
| Gripper (each arm) | Friction pick of 0.2 kg (S6) | Open and close; stroke TBD | CALC-DA03-03 §1 | Normal force per finger ≈ 0.2 × 9.81 ÷ (2 × 0.5) ≈ 2.0 N; ≈ 4 N with a 2× factor; actuation TBD |
| Axles, bearings, belts, mast | Not defined on the sheets | TBD | none | Not analysed |

Torque, speed, range and loading values are derived or marked TBD.

## 4. Dual-Arm Add-on Analysis

- **Arm workspace and reach:**
  - Each arm reaches 350 mm (printed). With yaw and two parallel pitch joints, the elbow sits 175 mm out from the yaw axis and the gripper stays within 175 mm of the elbow point, in the vertical plane set by yaw. At the assumed 400 mm shoulder height, the gripper therefore spans about 0 – 350 mm radius and about **225 – 575 mm** height (unlimited joint range assumed; real ranges are smaller and TBD).
  - The gripper cannot reach the floor, and the highest point is below a typical table top. Which work surface height the robot must serve ("tabletop-height") is not defined: an owner question.
  - With three DOF the gripper position is controlled but its approach angle follows from the position, and there is no roll. Top-down or side grasps cannot be chosen independently.
- **Payload and payload location:** UNKNOWN. Printed 0.1 – 0.2 kg per arm; taken at the gripper tip.
- **Base / torso stability under representative arm configurations (S3, S7):** Total about 16.1 kg with payload (weight about 158 N). Centre of mass (arms forward, payload): y ≈ +33 mm, z ≈ 198 mm. Restoring moment about the front contact line ≈ 158 × (0.150 − 0.033) ≈ 18.4 N·m.

| Case | Overturning effect | Margin |
|---|---:|---:|
| Extra 20 N downward at one forward tip (tip 200 mm beyond the contact line) | 4.0 N·m | ≈ 4.6 (tips at about 92 N) |
| 20 N horizontal push forward at shoulder height (0.4 m) | 8.0 N·m | ≈ 2.3 |
| One arm extended sideways, 20 N down at the tip (tip 310 mm beyond the contact line) | 6.2 N·m | ≈ 4.4 (tips at about 88 N) |
| Static tipping angle, arms forward (forward / sideways) | n/a | about 30° forward, about 41° sideways |

  - The sideways tipping angle of about 41° is as stated by the author; the basis (for example which arm pose) is not stated. With the CoM at x = 0 and z = 198 mm and contact lines at ±190 mm, the angle would be about 44° (open question OQ-017).
  - These are far above the assumed 5° slope. A push at 0.4 m height would more likely roll the robot than tip it, unless the wheels are braked. Dynamic effects (braking while the arms are extended, turning) are not computed. Uneven terrain, a raised mast and a heavier camera reduce the margins.
  - Wheel loads with arms forward: front pair about 97 N, rear pair about 62 N.
- **Turning and traction:** Four wheels in two driven pairs turn by scrub. Turning in place needs about 19 N·m at the platform (μ = 0.5, S3), about four times the straight-line drag per channel (`ACTUATOR_ANALYSIS.md`). Tyre wear, floor marking and wheel slip are open points. Traction on a 5° slope is ample at μ ≥ 0.1.
- **Inter-arm interference and collision considerations:** Valid only for the S1 case (yaw axes 300 mm apart): the two 350 mm reach discs overlap in a lens 400 mm wide centred on the midline (about 632 mm long at the centre), so the bimanual zone is large and both grippers can be at the same height there. Link, gripper and torso envelopes are not defined, so clearances are TBD. Arm-to-torso clearance and arm-to-wheel clearance when the arm is stowed are TBD.
- **End-effector and support interfaces:** Two-finger linkage on a gripper mount, optional force sensor (on the concept sheet). Mount geometry TBD.
- **Geometry check for the owner (D5):** With shoulders at ±150 mm and 350 mm reach, arms extended sideways span about 1,000 mm, not the printed 800 mm; 800 mm would imply a shoulder spacing near 100 mm. The artwork cannot settle this.

## 5. Legged Add-on Analysis

Not applicable. DA-03 is a wheeled mobile dual-arm; it has no legs. Wheeled mobility is covered in Section 4 and `ACTUATOR_ANALYSIS.md`.

## 6. Mass, Serviceability and Safety

- **Preliminary mass breakdown (from `MASS_BUDGET.md`, ESTIMATE):** 15.72 kg baseline (structure 6.4, wheel drive 2.6, arm actuators 2.0, battery 1.8, harness 0.72, Edge and drivers 0.65, links 0.50, grippers 0.30, power 0.25, fasteners and miscellaneous 0.50); range about 9.2 – 22.2 kg.
- **Service access and maintenance:** Not shown. Open points: battery swap or charge access, drive and wheel replacement, torso panels for the electronics, connector access at the wrist and gripper, cable wear on the moving platform.
- **Pinch/crush and structural hazards:**
  1. Pinch points at each yaw, elbow and wrist joint, and at the gripper fingers (low force, about 2 – 4 N, but actuator capability TBD).
  2. Arm-to-arm shear in the overlap zone and arm-to-torso crush.
  3. A moving base: collision with people, tipping on slopes and steps, wheel pinch at the base edge.
  4. Li-ion battery hazards (short circuit, overcharge, impact); no battery safety assessment is made in this study.
  5. Arm droop on power loss: elbow holding torque about 0.8 N·m; the yaw does not droop; a brake or a non-backdrivable gearbox is not selected.
  6. Base roll-away on a slope if the wheel drives are backdrivable.
  7. Cable snagging on wheels and strain on a moving base.
- **Safeguards and unresolved safety questions:** Emergency stop (a red button is drawn but unlabelled), speed and torque limits for base and arms, bumpers, stowed transit pose, battery protection, behaviour on power loss. None is defined or selected.

## 7. Conclusions and Open Items

- **Findings:**
  1. Arm joint loads are small (elbow about 0.8 N·m, wrist about 0.2 N·m). The yaw output bearing carries about 2.64 N·m because there is no shoulder pitch joint.
  2. Link bending is negligible; joint and bearing compliance will set stiffness.
  3. Static stability is comfortable (about 4.4 – 4.6 against 20 N; tipping angle about 30°), but dynamic and sloped cases are not done.
  4. Turning in place with paired wheels sets the wheel drive size (about 2.5 N·m per channel at the wheel).
  5. With three DOF the gripper has no independent orientation and no roll. The assumed working height is about 225 – 575 mm, with floor level out of reach.
  6. The 800 mm width, 350 mm reach and 300 mm torso cannot all be true (D5).
- **Limitations:** link split, shoulder position and height, torso size, wheel size, friction and the 20 N load are assumptions. No joint ranges, stiffness, bearing, tyre or battery data. Static or simple dynamic loads only. No finite-element or CAD work (HOLD D-003).
- **Required follow-up calculations:** workspace with joint ranges (kinematic sketch); collision envelopes; dynamic stability (braking, turning, slope with arms extended); axle and bearing loads; wheel and tyre options and steering strategy; energy and runtime with battery data; mast deflection; yaw bearing selection; power-off behaviour.
- **Open items and dependencies:** D3, D4, D5, D6; work surface height and shoulder height; S/M/L mapping; battery capacity and protection; wheel, tyre and floor data; safety requirements; owner-supplied payload, reach, mass and runtime.

## 8. HOLD D-003

Paper calculations and conceptual analysis only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
