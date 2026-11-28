# DA-01 — Preliminary Cost Model (Week 3)

| Property | Value |
|---|---|
| Document ID | KMECH-COST-DA-01 |
| Status | PROPOSED — Week 3 category-level ESTIMATE |
| Version | 0.3.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 |

**HOLD D-003 active.** No supplier quotations, procurement or final BOM are authorised. All figures are category-level planning estimates in INR and are tagged ESTIMATE.

## 1. Planning ceiling

Study-level hardware ceiling: **INR 2,00,000**. This is a comparison constraint, not an approved procurement budget.

## 2. Category cost ranges (ESTIMATE, INR)

Ranges reflect typical Indian academic / small-batch robotics component pricing at the 2026 planning horizon and the scale of DA-01. Confidence is Low until source-controlled prices and quantities exist.

| Category | Qty basis | Low (INR) | Nominal (INR) | High (INR) | Notes |
|---|---|---:|---:|---:|---|
| Actuator modules (motor + gearbox + encoder) | 6 | 45,000 | 75,000 | 1,20,000 | Dominant cost driver; S/M/L data pending |
| Structural (base, links, enclosures) | 1 set | 8,000 | 15,000 | 25,000 | Al plate + CNC / printed links |
| Bearings, shafts, fasteners | lot | 3,000 | 6,000 | 12,000 | |
| Grippers (passive or simple servo) | 2 | 2,000 | 5,000 | 12,000 | Optional powered version higher |
| Compute / motor drivers / power dist. | 1 set | 12,000 | 20,000 | 35,000 | Kritva platform boards |
| Sensors / mast / cameras (optional) | 0–1 | 0 | 8,000 | 20,000 | Excluded from baseline |
| Harness, connectors, covers, misc. | lot | 4,000 | 8,000 | 15,000 | |
| Fabrication / finishing / assembly labour (in-house) | 1 | 5,000 | 12,000 | 25,000 | No external quote |
| **Baseline subtotal (no optional sensors)** | | **79,000** | **1,41,000** | **2,44,000** | |

## 3. Affordability observation

- Nominal baseline ≈ INR 1.41 L sits inside the INR 2 L ceiling with ≈ 30 % margin.
- High-end actuator pricing or addition of optional sensors / powered grippers can push the total above the ceiling.
- Actuator modules are the single largest lever; S/M/L selection and source pricing will dominate the final comparison.

## 4. Exclusions

- No supplier quotations.
- No import duties, taxes, shipping or contingency reserve quantified.
- No software / NRE / test equipment.
- Battery cost excluded (tabletop may be externally powered).

## 5. Status

Category-level ESTIMATE produced for Week 3. Ready for comparison once actuator source data and the other eleven concept cost models are available. No claim of affordability or design release is made.
