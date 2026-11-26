# DA-03 — Preliminary Mass Budget

| Property | Value |
|---|---|
| Document ID | KMECH-MASS-DA-03 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Preliminary Mass Budget |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary estimate; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md` |

Every mass below is an **ESTIMATE** from intern assumptions (evidence C). None comes from a datasheet, CAD or weighing. The printed 12 – 18 kg is a CONCEPT_TARGET with no stated basis and is kept separate. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Scope and Basis

- Concept ID/name: DA-03 — Mobile Dual-Arm
- Configuration revision: `README.md` v0.3.1 (artwork REVIEWED_WITH_ISSUES; not design approval). Baseline = 6 arm actuators, 2 wheel drive channels, battery, no camera or LiDAR. Optional items are separate.
- Mass boundary and exclusions: Included: base frame, torso, mast, arms, grippers, wheel drive and wheels, battery, electronics, harness, fasteners. Excluded: payload (2 × 0.1 – 0.2 kg), charger, tooling, packaging, any dock.
- Target total mass: UNKNOWN in the requirements register. Printed CONCEPT_TARGET 12 – 18 kg (est.).
- Calculation/reference basis: paper estimate, CALC-DA03-02 (to be filed). Arm masses match `ACTUATOR_ANALYSIS.md` (A4 – A8, A10).

### 1.1 Mass assumptions

| ID | Assumption | Value |
|---|---|---|
| M1 | Base frame: 5 mm aluminium plate 400 mm × 450 mm (about 2.4 kg) plus 1.0 kg frame, skirts and brackets | 3.4 kg |
| M2 | Torso: 300 mm × 250 mm × 300 mm box with 1.5 mm aluminium panels (about 1.6 kg) plus 0.6 kg internal frame and brackets (torso depth and height assumed) | 2.2 kg |
| M3 | Mast with height adjustment, aluminium | 0.5 kg |
| M4 | Shoulder mounts, 0.15 kg each | 0.30 kg |
| M5 | Upper arm 0.15 kg, forearm 0.10 kg (A4, A6) | 0.25 kg per arm |
| M6 | Joint modules: shoulder yaw 0.45 kg, elbow 0.35 kg, wrist 0.20 kg (A5, A7, A10) | 1.00 kg per arm |
| M7 | Gripper and mount (A8) | 0.15 kg per arm |
| M8 | Wheel drive: 2 motors with optional gearbox at 0.60 kg; 4 wheels with tyres at 0.20 kg; hubs, axles, bearings, belts 0.60 kg | 2.6 kg |
| M9 | 24 V Li-ion pack, 6S4P of about 2.5 Ah cells (10 Ah nominal, capacity not stated on the sheets), with BMS and housing | 1.8 kg |
| M10 | Kritva Edge with heatsink 0.15 kg; 2 drive drivers at 0.10 kg; 6 arm drivers at 0.05 kg | 0.65 kg |
| M11 | Power board 0.15 kg plus fuses, e-stop and connectors 0.10 kg; IMU 0.02 kg and harness 0.70 kg | 0.25 kg and 0.72 kg |
| M12 | Fasteners, connectors, labels, miscellaneous | 0.50 kg |

## 2. Component Mass Breakdown

Per-row uncertainty is an intern band. Each row shows one mass value (ESTIMATE) and one range, computed as the row value × (1 ∓ band); there are no separate low and high columns.

| Component category | Quantity | Mass value (kg) | Evidence label | Basis / source | Uncertainty |
|---|---:|---:|---|---|---|
| **Main structure** | | **ESTIMATE: 6.4** | ESTIMATE | Sum of four rows | 4.1 – 8.7 |
| – Base frame | 1 | ESTIMATE: 3.4 | ESTIMATE | M1; aluminium or steel is an open option | ±30% |
| – Torso frame and panels | 1 | ESTIMATE: 2.2 | ESTIMATE | M2 | ±40% |
| – Sensor mast | 1 | ESTIMATE: 0.5 | ESTIMATE | M3; adjustability open (D6) | ±50% |
| – Shoulder mounts | 2 | ESTIMATE: 0.30 | ESTIMATE | M4 | ±50% |
| **Arms / joints (links)** | 2 arms | ESTIMATE: 0.50 | ESTIMATE | M5 | ±40% (0.30 – 0.70) |
| **Actuators (arm modules)** | 6 | ESTIMATE: 2.0 | ESTIMATE | M6; S/M/L not mapped | ±50% (1.0 – 3.0) |
| **End effector (grippers)** | 2 | ESTIMATE: 0.30 | ESTIMATE | M7 | ±50% (0.15 – 0.45) |
| **Wheel drive and wheels** | 2 channels, 4 wheels | ESTIMATE: 2.6 | ESTIMATE | M8; wheel size, gear ratio TBD | ±40% (1.6 – 3.6) |
| **Power system: battery** | 1 | ESTIMATE: 1.8 | ESTIMATE | M9; capacity UNKNOWN | ±50% (0.9 – 2.7) |
| **Edge / controllers** | 1 Edge + 8 drivers | ESTIMATE: 0.65 | ESTIMATE | M10 | ±40% (0.39 – 0.91) |
| **Power system: distribution and protection** | 1 | ESTIMATE: 0.25 | ESTIMATE | M11 | ±50% (0.13 – 0.38) |
| **Sensors and cabling** | IMU + harness | ESTIMATE: 0.72 | ESTIMATE | M11; camera and LiDAR optional | ±40% (0.43 – 1.01) |
| **Fasteners and miscellaneous** | – | ESTIMATE: 0.50 | ESTIMATE | M12; fasteners, connectors and labels only. No contingency is included in the rows; the 15% planning allowance is applied separately in Section 4 | ±50% (0.25 – 0.75) |
| **Baseline subtotal** | | **ESTIMATE: 15.72** | ESTIMATE | Sum of the rows above (15.72 kg) | 9.2 – 22.2 (linear sum of bands) |
| Optional camera and LiDAR | 1 + 1 | ESTIMATE: 0.40 | ESTIMATE / UNKNOWN | Camera 0.15, LiDAR 0.25 (LiDAR is an open decision D4) | ±50% |
| **Subtotal with camera and LiDAR** | | **ESTIMATE: 16.12** | ESTIMATE | 15.72 + 0.40 | 9.4 – 22.8 |

Alternative not selected: a steel base frame would add several kilograms. Arm mass beyond the shoulder yaw axis is about 0.95 kg per arm (links 0.25, elbow 0.35, wrist 0.20, gripper 0.15), as used in `ACTUATOR_ANALYSIS.md`.

## 3. Centre of Mass

- Frame: origin on the ground at the centre of the base; x right, y forward, z up. Torso and shoulders at y = 0.
- Overall centre of mass, baseline, arms extended forward, no payload: **x = 0, y ≈ +25 mm, z ≈ 198 mm**. With 0.2 kg payload on each arm: y ≈ +33 mm. With camera and LiDAR on the mast top: z ≈ 209 mm.
- Assumed component heights (z, mm): base frame 70; torso 300; mast 550; shoulders, arms and grippers 400; wheel drive 50; battery 70; base drivers 80; Edge and arm drivers 250; power board 120; harness 250; other 200.
- Arm moment about the yaw axis: 0.199 kg·m per arm without payload and 0.269 kg·m with payload (from `ACTUATOR_ANALYSIS.md`).
- Wheel load split with payload (arms forward): front pair about 97 N, rear pair about 62 N (about 61% on the front).
- Assumptions and uncertainty: symmetric left-right layout; torso on the base centre; shoulder position and heights assumed (D5, D6). The result is only as good as the component masses (±50% on the largest items).

## 4. Summary

- Estimated subtotal: **15.72 kg** baseline; 16.12 kg with camera and LiDAR. With a 15% planning allowance (an intern assumption): ≈ 18.1 kg and ≈ 18.5 kg. Range about 9.2 – 22.2 kg.
- Excluded items: payload, charger, tooling, packaging, dock.
- Confidence and limitations: LOW. Structure is about 41%, wheel drive 17%, arm actuators 13% and battery 11% of the baseline. No actuator, battery or wheel data exist. The estimate sits inside the printed 12 – 18 kg, but the band straddles both ends.
- Mass-sensitive risks:
  1. Battery capacity is unstated; a larger pack adds mass and changes the centre of mass.
  2. Actuator mass (±50%) loads the yaw bearing moment and wheel torque.
  3. Mast and sensors raise the centre of mass.
  4. A steel frame or thicker plate quickly pushes the total over 18 kg.
  5. Wheel drive torque and traction scale with total mass (`ACTUATOR_ANALYSIS.md` §2).
- Next steps (paper only): replace assumed module and battery masses with data; confirm torso height and shoulder height; file CALC-DA03-02.

## 5. HOLD D-003

Paper mass estimates only. No detailed CAD mass properties, procurement, fabrication, assembly or physical weighing. These activities require explicit owner decision under HOLD D-003.
