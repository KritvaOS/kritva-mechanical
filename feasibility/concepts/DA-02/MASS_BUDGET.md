# DA-02 — Preliminary Mass Budget

| Property | Value |
|---|---|
| Document ID | KMECH-MASS-DA-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Preliminary Mass Budget |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary estimate; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md` |

Every mass in this document is an **ESTIMATE** built from intern assumptions (evidence C, paper only). No value comes from a datasheet, CAD or weighing, and none is approved. The printed 8 – 12 kg is a concept-sheet target with no stated basis and is kept separate from the estimates below. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Scope and Basis

- Concept ID/name: DA-02 — Humanoid Torso Dual-Arm
- Configuration revision: `README.md` v0.3.1 (artwork sheets REVIEWED 2026-10-31; REVIEWED is not design approval). Baseline = 8 arm actuators, fixed base plate, powered or passive grippers treated as passive-class mass (see M9). The head pan actuator is an optional ninth actuator shown separately; whether to fit it is open (OQ-007), while the D6 count itself (8 baseline, 9 with head, 2026-10-31) is resolved.
- Mass boundary and exclusions:
  - Included: base plate, torso, two arms (links, joint modules, grippers), Kritva Edge and motor drivers, power distribution board, IMU, cabling, fasteners.
  - Excluded: payload (2 × 0.1 – 0.2 kg, not robot mass), external 24 V supply or any battery (the sheets show 24 V in and give no battery capacity), tether or mains cable, tooling, packaging, any mounting surface or table.
- Target total mass: UNKNOWN in the requirements register. Printed CONCEPT_TARGET: 8 – 12 kg (est.).
- Calculation/reference basis: paper estimates, `calculations/` reference CALC-DA02-02 (to be filed). Geometry from the README (base 300 mm × 250 mm, height 550 mm, shoulder-to-shoulder 600 mm, reach 350 mm). Link, elbow, wrist and gripper masses are inherited from `ACTUATOR_ANALYSIS.md` (A4–A8) so the two documents stay consistent; the shoulder yaw and pitch module masses (M5) are new assumptions made in this document and are not inherited.

### 1.1 Mass assumptions

| ID | Assumption | Value |
|---|---|---|
| M1 | Base plate: aluminium, 10 mm thick, 300 mm × 250 mm (thickness not printed) | 750 cm³ × 2.70 g/cm³ ≈ 2.0 kg |
| M2 | Torso: 300 mm × 250 mm × 300 mm high box (height assumed; head and neck take the rest of the 550 mm), 1.5 mm aluminium panels on four sides and top, about 0.41 m² | ≈ 1.6 kg panels, plus 0.6 kg internal frame, brackets and fasteners = 2.2 kg |
| M3 | Shoulder mounts (outboard brackets), 0.15 kg each | 0.30 kg |
| M4 | Upper arm link 0.15 kg, forearm link 0.10 kg (= ACTUATOR_ANALYSIS A4, A6) | 0.25 kg per arm |
| M5 | Joint modules (motor, gearbox, encoder, housing): shoulder yaw 0.40 kg, shoulder pitch 0.60 kg, elbow 0.35 kg (A5), wrist 0.20 kg (A7) | 1.55 kg per arm |
| M6 | Gripper and mount 0.15 kg (= A8) | 0.15 kg per arm |
| M7 | Kritva Edge board with heatsink 0.15 kg; 8 motor drivers at 0.05 kg each | 0.55 kg |
| M8 | Power distribution board 0.15 kg; IMU 0.02 kg; harness for two arms and torso 0.50 kg | 0.15 kg and 0.52 kg |
| M9 | Gripper actuation, if powered, is assumed inside the 0.15 kg gripper figure (type and count are TBD) | n/a |
| M10 | Fasteners, connectors, labels, miscellaneous | 0.40 kg |
| M11 | Optional head: pan module 0.25 kg, neck and head mount 0.20 kg, RGB-D or stereo camera 0.15 kg | 0.60 kg |

Shoulder yaw (0.40 kg) and shoulder pitch (0.60 kg) module masses in M5 are new assumptions introduced here, not inherited from `ACTUATOR_ANALYSIS.md`; they are sized larger than the elbow because the preliminary torque estimates are higher (ACTUATOR_ANALYSIS: shoulder pitch about 2.6 N·m holding).

## 2. Component Mass Breakdown

Uncertainty is a per-row ± band chosen by the intern. Each row shows one mass value (ESTIMATE) and one range, computed as the row value × (1 ∓ band); there are no separate low and high columns.

| Component category | Quantity | Mass value (kg) | Evidence label | Basis / source | Uncertainty |
|---|---:|---:|---|---|---|
| **Main structure** | | **ESTIMATE: 4.5** | ESTIMATE | Sum of three rows below (4.50 kg) | 2.9 – 6.1 kg (low 1.4 + 1.3 + 0.15; high 2.6 + 3.08 + 0.45) |
| – Base plate | 1 | ESTIMATE: 2.0 | ESTIMATE | M1; aluminium or steel is an open option on the sheet | ±30% (1.4 – 2.6) |
| – Torso frame and panels | 1 | ESTIMATE: 2.2 | ESTIMATE | M2; torso height assumed | ±40% (1.3 – 3.1) |
| – Shoulder mounts | 2 | ESTIMATE: 0.30 | ESTIMATE | M3 | ±50% (0.15 – 0.45) |
| **Arms / joints (links only)** | 2 arms | ESTIMATE: 0.50 | ESTIMATE | M4; upper arm and forearm per arm; aluminium CNC or 3D printed, composite options not assumed | ±40% (0.30 – 0.70) |
| **Actuators (joint modules)** | 8 | ESTIMATE: 3.10 | ESTIMATE | M5; 2 each of yaw 0.40, pitch 0.60, elbow 0.35, wrist 0.20 kg. S/M/L not mapped and no `kritva-actuator` data supplied | ±50% (1.55 – 4.65). Largest single uncertainty |
| **End effector (grippers)** | 2 | ESTIMATE: 0.30 | ESTIMATE | M6, M9 | ±50% (0.15 – 0.45) |
| **Edge / controllers** | 1 Edge + 8 drivers | ESTIMATE: 0.55 | ESTIMATE | M7; board dimensions and driver selection TBD | ±40% (0.33 – 0.77) |
| **Power system** | 1 distribution board | ESTIMATE: 0.15 | ESTIMATE | M8; no battery included | ±50% (0.08 – 0.23) |
| **Sensors and cabling** | IMU + harness | ESTIMATE: 0.52 | ESTIMATE | M8; head camera is optional and listed below | ±40% (0.31 – 0.73) |
| **Fasteners and miscellaneous** | – | ESTIMATE: 0.40 | ESTIMATE | M10; fasteners, connectors and labels only. No contingency is included in the rows; the 15% planning allowance is applied separately in Section 4 | ±50% (0.20 – 0.60) |
| **Baseline subtotal (head not fitted)** | | **ESTIMATE: 10.02** | ESTIMATE | Sum of the rows above (10.02 kg) | 5.8 – 14.2 kg (linear sum of bands, deliberately conservative) |
| Optional head (pan module, neck and head mount, camera) | 1 | ESTIMATE: 0.60 | ESTIMATE / UNKNOWN | M11; fitting the head is an open owner decision tracked as OQ-007 / CREQ-004 (the D6 actuator count of 8 baseline, 9 with head is resolved) | ±50% (0.30 – 0.90) |
| **Subtotal with head fitted** | | **ESTIMATE: 10.62** | ESTIMATE | 10.02 + 0.60 | 6.1 – 15.1 kg |

Alternative within the printed options, not selected: a steel base plate (7.85 g/cm³) at the same size is about 5.9 kg, which is **+3.9 kg** over aluminium.

### 2.1 Mass by arm

| Item | Per arm (kg) | Two arms (kg) |
|---|---:|---:|
| Links (M4) | 0.25 | 0.50 |
| Joint modules (M5) | 1.55 | 3.10 |
| Gripper (M6) | 0.15 | 0.30 |
| **Arm total** | **1.95** | **3.90** |
| Shoulder mounts (M3, counted in structure) | 0.15 | 0.30 |

Of the 1.95 kg per arm, 0.95 kg sits beyond the shoulder pitch axis. That 0.95 kg is what ACTUATOR_ANALYSIS uses for the torque load case, so the two documents agree.

## 3. Centre of Mass

- Overall centre of mass (CoM), baseline, head not fitted, arms extended forward at shoulder height, no payload: **x = 0 mm, y ≈ +40 mm, z ≈ 180 mm**. With 0.2 kg payload on each arm: y ≈ +52 mm (payload CoM assumed about 350 mm forward of the shoulder axis, at the printed reach).
- With optional head fitted (same pose, no payload): z ≈ 198 mm; y ≈ +38 mm.
- Coordinate reference frame: origin at the centre of the underside of the base plate; x to the right, y forward, z up. Torso centre is at y = 0. All values are ESTIMATES from assumed positions.
- Component CoM locations (assumed, mm):

| Component | z (mm) | y (mm) | Note |
|---|---:|---:|---|
| Base plate | 5 | 0 | Mid-thickness |
| Torso frame and panels | 160 | 0 | Torso occupies z = 10 – 310 |
| Shoulder axes | 280 | 0 | Assumed height; shoulder axes assumed at torso centre plane |
| Shoulder modules and mounts | 280 | 0 | On the axis |
| Arm beyond shoulder pitch axis (0.95 kg per arm) | 280 | +210 | Extended pose; from ACTUATOR_ANALYSIS moments (0.199 kg·m per arm) |
| Edge, drivers | 150 | 0 | Electronics bay |
| Power distribution | 120 | 0 | Electronics bay |
| IMU and harness | 200 | 0 | Spread through torso and arms |
| Head (optional) | 500 | 0 | Pan head and camera on neck mount |

- Static tipping check (extended-arm case, free-standing, no base fixing): the CoM at y ≈ +52 mm with payload is 73 mm inside the front edge of the base plate (125 mm half-depth − 52 mm). The margin is 73 mm of CoM travel before tipping, not a safety factor. Lateral cases and one-arm-extended cases are **not computed**. This check does not replace the base-loading study in the README.
- Assumptions and uncertainty: UNKNOWN beyond the ranges above. The x = 0 value assumes left-right symmetry of electronics and harness. Torso height, shoulder height, shoulder position and arm pose are all assumed. Moving actuator mass changes y by roughly 2 mm and z by roughly 1 mm per 0.1 kg of arm-side mass at the extended pose.

## 4. Summary

- Estimated subtotal: **10.02 kg** baseline (head not fitted), **10.62 kg** with head fitted. With a 15% planning allowance (an intern assumption, not a validated margin): **≈ 11.5 kg** and **≈ 12.2 kg**. Estimate range from the per-row bands: about 5.8 – 14.2 kg baseline.
- Excluded items: payload, external supply or battery, tether, tooling, packaging, mounting surface (see Section 1).
- Confidence and limitations: LOW. About 31% of the baseline mass is actuators (3.1 of 10.02 kg), and no actuator data exist. Structure is 45% and depends on assumed plate and panel thicknesses. The printed 8 – 12 kg target cannot be confirmed or refuted by the estimate: the baseline falls inside it, the head-fitted case with allowance slightly exceeds it, and the uncertainty band straddles it.
- Mass-sensitive risks:
  1. Actuator mass (±50%): heavier joint modules raise torque on shoulder pitch directly. For example, a 1.0 kg elbow module raises shoulder pitch static torque by about 1.1 N·m (ACTUATOR_ANALYSIS Section 2.4).
  2. Base plate material: steel adds about 3.9 kg.
  3. Head fitted plus 15% allowance puts the total at about 12.2 kg, above the printed target.
  4. Base loading and tipping margin depend on mass distribution (shoulder spacing D5 is not verifiable).
  5. **Geometry check for the owner:** the sheets print 600 mm shoulder-to-shoulder on a 300 mm wide torso and base, and 800 mm overall width with 350 mm reach. Shoulders at ±300 mm sit outside the 150 mm half-width of the base, and an arm extended sideways would exceed 800 mm. This looks inconsistent and needs the owner to clarify what each width refers to. The centre-of-mass figures above assume shoulders on the torso centre plane and do not use 600 mm.
- Next steps (paper only): replace M5 with S/M/L module masses once supplied; confirm torso and shoulder height; compute lateral and one-arm cases; file CALC-DA02-02 in `calculations/`.

## 5. HOLD D-003

Paper mass estimates only. No detailed CAD mass properties, procurement, fabrication, assembly or physical weighing. These activities require explicit owner decision under HOLD D-003.
