# QR-01 — Mechanical Analysis

| Property | Value |
|---|---|
| Document ID | KMECH-MECH-QR-01 |
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

Concept ID/name: QR-01 — Compact Quadruped (four planar two-joint legs, rigid body)

Analysis objective: Check on paper whether the QR-01 arrangement is plausible for standing, sitting and slow walking: load paths and stiffness, joint loading, leg workspace, stability, mass, serviceability and safety, and identify what must be settled first.

Evidence basis:
- Sourced reference: `README.md` v0.3.0 (artwork, CONCEPT_TARGET, L0).
- Calculated (C): CALC-QR01-03 (to be filed), using CALC-QR01-01 (`ACTUATOR_ANALYSIS.md`) and CALC-QR01-02 (`MASS_BUDGET.md`); all three are to be filed, and the section references below point into those documents.
- ESTIMATE: every assumption below.

### 1.1 Assumptions used here

| ID | Assumption |
|---|---|
| S1 | Leg geometry per `ACTUATOR_ANALYSIS.md` A3: thigh 130 mm, shank 150 mm, knee back, hip height 220 mm, hips at body mid-height |
| S2 | Leg planes at x = ±190 mm (outboard of the 250 mm body, which implies hip mounts about 65 mm wide); hips at y = ±120 mm; feet at ±190 mm × ±180 mm |
| S3 | Centre of mass at z = 200 mm with payload on top (184 mm without), centred in plan |
| S4 | Thigh and shank as aluminium tube, 20 mm outer diameter, 1.5 mm wall, E = 69 GPa (illustrative) |
| S5 | Flat, rigid, dry floor; static analysis |
| S6 | Foot pad friction coefficient 0.5 (rubber, assumed) |
| S7 | Moving mass 7.06 kg including 0.8 kg payload |

## 2. Structure and Load Paths

- **Main structure and support configuration:** Rigid body chassis (1 mm aluminium shell assumed) with hip mounts on each side; four legs; foot pads on the ground.
- **Representative load cases:** LC1 four-foot stand. LC2 two-foot support (bounding case for trot or crawl, 34.6 N per foot). LC3 three-foot crawl stance. LC4 sit-to-stand (crouch 120 mm). LC5 touchdown (2× allowance). Not analysed: falls, running, jumping, rough terrain.
- **Load paths:** foot pad → shank → knee module → thigh → hip module → hip mount → body chassis → payload mount and electronics.
- **Structural concerns:**
  1. *Hip mount root moment.* The leg plane sits 65 mm outboard of the body side (S2), so a 34.6 N foot force gives about 2.2 N·m per mount in bending and torsion. The mount geometry is not shown.
  2. *Body torsion.* The chassis shell carries the four hip reactions; its torsional stiffness is not checked.
  3. *Link bending.* The shank carries up to the knee torque of 3.85 N·m near the knee: σ = M·c ÷ I = 3,850 N·mm × 10 mm ÷ 3,754 mm⁴ ≈ 10 MPa (about 21 MPa with the 2× allowance). Comfortable for aluminium; for 3D-printed links the strength is not data and the margin could be thin.
- **Stiffness and deflection considerations:**
  - Shank bending deflection is small: about 25.7 N perpendicular load at 150 mm gives δ ≈ 0.11 mm.
  - Joint and gearbox compliance, pad compliance and body torsion will dominate; data TBD.
  - Foot elastomer damper (optional) affects impact but is not modelled.

## 3. Joint and Mechanism Analysis

Torques are per joint, worst case, from CALC-QR01-01 (to be filed); all are estimates.

| Joint / mechanism | Load case | Required motion | Calculation reference | Result |
|---|---|---|---|---|
| Hip (each leg) | LC2, foot 60 mm from the hip line | Flexion / extension, stride ±60 mm; range TBD | CALC-QR01-01 §2 | ≈ 2.1 N·m static, ≈ 4.2 N·m with 2× allowance; ≈ 0 standing; swing leg ≈ 0.64 N·m |
| Knee (each leg) | LC2, knee back | Flexion / extension; range TBD | CALC-QR01-01 §1 | ≈ 3.85 N·m static, ≈ 7.7 N·m with allowance; ≈ 1.5 N·m standing; sit-to-stand ≈ 2.2 N·m |
| Foot pad and damper | Touchdown | Passive | none | Not analysed: TBD |
| Hip mount and body chassis | LC2 | Static | CALC-QR01-03 §1 | ≈ 2.2 N·m per mount; chassis stiffness TBD |

Torque, speed, range and loading values are derived or marked TBD.

## 4. Dual-Arm Add-on Analysis

Not applicable. QR-01 has no arms or manipulators.

## 5. Legged Add-on Analysis

- **Leg configuration and joint arrangement:** Four identical planar legs, hip then knee, both flexion/extension, in parallel vertical planes 190 mm either side of the centreline (S2). No abduction joint (D1 resolved to 2 DOF). Link lengths are assumed (S1).
- **Support polygon and representative support configurations:**
  - Four feet: rectangle 380 mm (lateral) × 360 mm (fore-aft).
  - Three feet (one leg lifted): a triangle; with the centre of mass at the centre of the body, it lies exactly on the diagonal between the two opposite feet, so the margin is **zero** unless the body is shifted.
- **Ground contact and foot assumptions:** Point-like rubber pad with friction 0.5 (S6) on a flat rigid dry floor. Outdoor ground (grass, gravel, wet surfaces) and the optional damper are not assessed.
- **Static stability considerations:**
  - Standing: margin 180 mm fore-aft and 190 mm lateral; with the centre of mass at 200 mm, the static tipping angle is about 42° (fore-aft) and 43° (lateral). The friction slip angle (atan 0.5) is about 27°, so foot slip, not tipping, limits slopes.
  - Crawl gait: margin = 0.726 × δ, where δ is the fore-aft shift of the body relative to the feet (diagonal at 380 mm × 360 mm). A 30 mm margin needs about 41 mm; 20 mm needs about 28 mm. Planar legs cannot shift the body sideways, so the whole margin must come from fore-aft shift, which the leg workspace allows (stance foot reach up to ±173 mm at hip height 220 mm when fully extended, which is a singular pose).
  - Trot (two-foot support) is not statically stable and needs dynamic control; not assessed.
- **Leg-joint loading and clearance:** See Section 3. Ground clearance under the body is about 120 mm (hip height 220 mm minus half of the 200 mm body height, assumed). Knee and thigh swing clearance against the body and the hip mounts, and foot swing height, are TBD.
- **Locomotion workspace limitations:**
  - Foot workspace per leg: an annulus of about 20 – 280 mm radius around the hip, limited by joint ranges (TBD). Practical stride about ±60 mm (assumed), giving a stride of about 120 mm.
  - No side-stepping and no lateral balance correction.
  - Turning needs the feet to slip sideways: a left-right stride difference of 60 mm over a 380 mm track gives only about 9° of yaw per gait cycle (60 ÷ 380 rad), with foot scrub and wear. Turning in place by stepping is not possible with parallel leg planes.
  - Slow walking speed: a 120 mm stride at 1 Hz gives about 0.12 m/s (assumed).
  - Overall size check: feet at ±180 mm are 60 mm beyond the assumed hips at ±120 mm, consistent with the printed 420 mm overall length; the 400 mm overall width needs leg planes about 65 mm outboard of the body.

## 6. Mass, Serviceability and Safety

- **Preliminary mass breakdown (from `MASS_BUDGET.md`, ESTIMATE):** 6.26 kg baseline (actuators 2.6, body and hip mounts 1.2, battery 0.80, legs and feet 0.52, Edge and drivers 0.47, harness 0.32, fasteners and miscellaneous 0.25, power board 0.10); range about 3.4 – 9.2 kg. The printed 2.5 – 4 kg lies mostly below this range (it overlaps only between 3.4 and 4 kg).
- **Service access and maintenance:** Not shown. Open points: battery access (not drawn), driver and Edge access, joint module replacement with cables inside links, foot pad replacement (shown on the concept sheet as replaceable), cable wear at the hips.
- **Pinch/crush and structural hazards:**
  1. Pinch points at hip and knee joints and between leg and body.
  2. Falls and tipping of a 6 – 7 kg robot, especially when turning or on slopes.
  3. Collapse on power loss: knee holding torque about 1.5 N·m standing; without backdrive resistance or a brake the legs fold.
  4. Li-ion battery hazards; no battery safety assessment is made in this study.
  5. Foot scrub and sudden leg motion near people; sharp edges of machined links.
  6. Heat in the motors holding the standing pose (cooling not drawn).
- **Safeguards and unresolved safety questions:** emergency stop (not shown on either sheet), torque and speed limits, safe sit-down on power loss, battery protection, fall handling. None is defined or selected.

## 7. Conclusions and Open Items

- **Findings:**
  1. Worst-case static joint loads are small to moderate (knee about 3.9 N·m, hip about 2.1 N·m, about 7.7 and 4.2 N·m with allowance). The mass and torque estimates feed each other.
  2. The estimated mass (6.26 kg) is well above the printed 2.5 – 4 kg.
  3. Link bending is negligible for aluminium; hip mounts, body torsion and joint compliance are the open structural items.
  4. Standing is stable (tipping about 42°) and friction limits slopes to about 27°.
  5. A crawl gait is statically possible only with a fore-aft body shift of about 41 mm (30 mm margin), since the legs cannot shift the body sideways.
  6. Planar legs give no side-stepping, and turning needs foot slip (about 9° per cycle at a 60 mm stride difference).
- **Limitations:** link lengths, hip height, leg plane offset, friction, stride and component masses are assumptions. No joint ranges, stiffness or impact data. Static or simple dynamic loads only. No finite-element or CAD work (HOLD D-003).
- **Required follow-up calculations:** leg kinematics with joint ranges (sketch); gait cycle with torque history; touchdown impact; hip mount and chassis stiffness; battery placement and centre of mass; thermal limits at standing; power-off collapse; turning strategy.
- **Open items and dependencies:** D4, D6; leg link lengths and joint ranges; hip mount geometry; battery capacity and placement; S/M/L mapping; safety requirements; owner-supplied weight and payload values.

## 8. HOLD D-003

Paper calculations and conceptual analysis only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
