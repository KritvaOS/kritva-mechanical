# QR-01 — Preliminary Mass Budget

| Property | Value |
|---|---|
| Document ID | KMECH-MASS-QR-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Preliminary Mass Budget |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary estimate; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md` |

Every mass below is an **ESTIMATE** from intern assumptions (evidence C). None comes from a datasheet, CAD or weighing. The printed 2.5 – 4 kg is a CONCEPT_TARGET (concept sheet only, D4) with no stated basis and is kept separate. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Scope and Basis

- Concept ID/name: QR-01 — Compact Quadruped
- Configuration revision: `README.md` v0.3.0 (artwork REVIEWED; not design approval). Baseline = 8 actuators, battery, IMU, no top camera module or LiDAR. Optional items are separate.
- Mass boundary and exclusions: Included: body, hip mounts, legs and feet, actuators, electronics, battery, harness, fasteners. Excluded: payload (0.3 – 0.8 kg), charger, tooling, packaging.
- Target total mass: UNKNOWN in the requirements register. Printed CONCEPT_TARGET 2.5 – 4 kg (est.).
- Calculation/reference basis: paper estimate, CALC-QR01-02 (to be filed).

### 1.1 Mass assumptions

| ID | Assumption | Value |
|---|---|---|
| M1 | Body chassis: 1 mm aluminium shell on four sides and the bottom, about 0.295 m² (about 0.80 kg), plus 0.20 kg internal frame and brackets; carbon option not assumed | 1.0 kg |
| M2 | Hip mounts (outboard), 0.05 kg each | 0.20 kg |
| M3 | Leg links: thigh 0.06 kg and shank 0.05 kg per leg; foot pads 0.02 kg each | 0.44 kg links + 0.08 kg pads |
| M4 | Joint modules: hip 0.30 kg, knee 0.35 kg (A8; S/M/L not mapped) | 1.2 kg + 1.4 kg |
| M5 | Kritva Edge with heatsink 0.15 kg; 8 drivers at 0.04 kg | 0.47 kg |
| M6 | Power distribution board | 0.10 kg |
| M7 | 24 V Li-ion pack, 6S2P of 2.5 Ah cells (5 Ah nominal; capacity not stated), 12 cells at 47 g plus 0.24 kg BMS and housing | 0.80 kg |
| M8 | IMU 0.02 kg; harness 0.30 kg | 0.32 kg |
| M9 | Fasteners, connectors, miscellaneous | 0.25 kg |
| M10 | Optional top module: camera 0.15 kg, mount 0.10 kg, LiDAR 0.20 kg (LiDAR is open, D6) | 0.45 kg |

## 2. Component Mass Breakdown

Per-row uncertainty is an intern band. Each row shows one mass value (ESTIMATE) and one range, computed as the row value × (1 ∓ band); there are no separate low and high columns.

| Component category | Quantity | Mass value (kg) | Evidence label | Basis / source | Uncertainty |
|---|---:|---:|---|---|---|
| **Main structure** | | **ESTIMATE: 1.2** | ESTIMATE | Sum of two rows | 0.7 – 1.7 |
| – Body chassis | 1 | ESTIMATE: 1.0 | ESTIMATE | M1; aluminium or carbon is an open option | ±40% |
| – Hip mounts | 4 | ESTIMATE: 0.20 | ESTIMATE | M2; geometry not shown | ±50% |
| **Arms / legs / joints (links and feet)** | 4 legs | ESTIMATE: 0.52 | ESTIMATE | M3 | ±40% (0.31 – 0.73) |
| **Actuators (joint modules)** | 8 | ESTIMATE: 2.6 | ESTIMATE | M4; no `kritva-actuator` data | ±50% (1.3 – 3.9) |
| **End effector / feet** | 4 | counted in the legs row | ESTIMATE | M3 | n/a |
| **Edge / controllers** | 1 Edge + 8 drivers | ESTIMATE: 0.47 | ESTIMATE | M5 | ±40% (0.28 – 0.66) |
| **Power system: distribution** | 1 | ESTIMATE: 0.10 | ESTIMATE | M6 | ±50% (0.05 – 0.15) |
| **Power system: battery** | 1 | ESTIMATE: 0.80 | ESTIMATE | M7; capacity and placement UNKNOWN | ±50% (0.40 – 1.20) |
| **Sensors and cabling** | IMU + harness | ESTIMATE: 0.32 | ESTIMATE | M8 | ±40% (0.19 – 0.45) |
| **Fasteners and miscellaneous** | – | ESTIMATE: 0.25 | ESTIMATE | M9; fasteners, connectors and labels only. No contingency is included in the rows; the 15% planning allowance is applied separately in Section 4 | ±50% (0.13 – 0.38) |
| **Baseline subtotal** | | **ESTIMATE: 6.26** | ESTIMATE | Sum of the rows above (6.26 kg) | 3.4 – 9.2 (linear sum of bands) |
| Optional top module (camera, mount, LiDAR) | 1 | ESTIMATE: 0.45 | ESTIMATE / UNKNOWN | M10 | ±50% |
| **Subtotal with top module** | | **ESTIMATE: 6.71** | ESTIMATE | 6.26 + 0.45 | 3.6 – 9.8 |

Share of the baseline: actuators about 42%, body and hip mounts about 19%, battery about 13%, legs and feet about 8%.

## 3. Centre of Mass

- Frame: origin on the ground at the centre of the support rectangle; x right, y forward, z up.
- Overall centre of mass, baseline, standing at hip height 220 mm: **x = 0, y = 0, z ≈ 184 mm** (symmetric layout assumed). With 0.8 kg payload on a top mount at 330 mm: z ≈ 201 mm.
- Assumed component heights (z, mm): body and hip mounts 220; hip modules 220; knee modules 122; legs and feet 110 average; Edge, drivers, power board, harness 220; battery 190; other 200.
- Assumptions and uncertainty: x = y = 0 assumes the battery, Edge and drivers are centred; the battery is not drawn on the sheets, so its placement is UNKNOWN. Moving the 0.8 kg battery by 50 mm shifts the centre of mass by about 6 mm.

## 4. Summary

- Estimated subtotal: **6.26 kg** baseline; 6.71 kg with the top module. With a 15% planning allowance (an intern assumption): ≈ 7.2 kg and ≈ 7.7 kg. Range about 3.4 – 9.2 kg.
- Excluded items: payload, charger, tooling, packaging.
- Confidence and limitations: LOW. No actuator, battery or structure data. The estimate is about 1.6 to 2.5 times the printed 2.5 – 4 kg, and the printed target lies mostly below the estimate range (the range starts at 3.4 kg, so the printed 2.5 – 4 kg overlaps it only between 3.4 and 4 kg), so it can only be met if the modules, battery and chassis are all at the light end.
- Mass-sensitive risks:
  1. Actuators are 42% of the mass and their size follows from torque, which follows from mass (`ACTUATOR_ANALYSIS.md` §2.2).
  2. Battery capacity is unstated and placement is not drawn.
  3. Payload of 0.3 – 0.8 kg adds up to 13% of the baseline.
  4. Printed mass target has no stated basis.
- Next steps (paper only): replace assumed module and battery masses with data; iterate mass and torque; confirm the payload mount; file CALC-QR01-02.

## 5. HOLD D-003

Paper mass estimates only. No detailed CAD mass properties, procurement, fabrication, assembly or physical weighing. These activities require explicit owner decision under HOLD D-003.
