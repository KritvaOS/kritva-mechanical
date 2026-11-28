# DA-01 — Mass Budget (Week 3/4 estimate)

| Property | Value |
|---|---|
| Document ID | KMECH-MASS-DA-01 |
| Status | PROPOSED — paper estimate; owner review required |
| Version | 0.4.0 |
| Last Updated | 2026-11-28 |
| Assigned Intern | INTERN-01 |

HOLD D-003 remains active. No material selection, process selection or final BOM is authorized.

## 1. Artwork target (not a derived total)

Printed target: 5–8 kg (est.) — CONCEPT_TARGET. The subsystem sum is not forced to equal this range.

## 2. Subsystem mass ranges (ESTIMATE)

The base-plate dimensions are 300 × 250 mm with an assumed aluminium density of 2,700 kg/m³. For a solid plate, 6 / 8 / 10 mm thickness gives 1.22 / 1.62 / 2.03 kg. Material, cut-outs and thickness remain unapproved; this is a geometry-based planning estimate, not a material selection. The enclosure allowance is separately estimated because its geometry is not defined.

| Subsystem | Low (kg) | Nominal (kg) | High (kg) | Notes / method |
|---|---:|---:|---:|---|
| Base plate | 1.22 | 1.62 | 2.03 | ASSUMED solid 300 × 250 mm aluminium plate; 6 / 8 / 10 mm, density 2,700 kg/m³ |
| Central enclosure | 0.15 | 0.30 | 0.60 | ESTIMATE allowance; no geometry or material selected |
| 2 × upper-arm links | 0.20 | 0.30 | 0.45 | A4 scaled ×2 |
| 2 × forearm links | 0.12 | 0.20 | 0.30 | A6 scaled ×2 |
| 6 × joint modules (motor + gear + housing) | 1.20 | 1.80 | 2.70 | 0.20–0.45 kg each; pending S/M/L variant data |
| 2 × grippers (passive baseline) | 0.15 | 0.25 | 0.40 | ESTIMATE; powered grippers excluded |
| Compute + drivers + power distribution | 0.30 | 0.50 | 0.80 | Kritva platform boards + harness provision |
| Sensors / mast (optional) | 0.00 | 0.15 | 0.40 | Excluded from baseline subtotal; OWNER_DECISION |
| Fasteners, bearings, covers, harness | 0.25 | 0.40 | 0.70 | Allowance |
| **Baseline subtotal (optional sensors/mast excluded)** | **3.6** | **5.4** | **8.0** | Includes central-enclosure allowance; rounded to 0.1 kg |
| Battery (if required) | 0.00 | 0.40 | 1.00 | Separate from subtotal; tabletop may be externally powered; UNKNOWN |

The torque calculation now uses a 0.20 kg wrist module, at the lower edge of the stated 0.20–0.45 kg joint-module range. Individual modules are estimates, not measured values.

## 3. Comparison with printed target

The nominal baseline is 5.37 kg (≈5.4 kg), inside the 5–8 kg CONCEPT_TARGET. The low estimate, 3.59 kg, is below the printed lower bound; the high estimate, 7.98 kg, is at the upper edge before optional sensors/mast or battery. The previous 4.7 kg nominal was below 5 kg, not in the lower half of the target band. These estimates remain low-confidence and do not prove the target will be met.

## 4. Centre of mass

UNKNOWN. No datum or component coordinates are defined. A first-order estimate places the CoM near the geometric centre of the base/torso once the arms are folded; extended-arm CoM shifts outward and raises tipping risk (see MECHANICAL_ANALYSIS).

## 5. Required inputs to improve confidence

- Source-controlled actuator module masses and revisioned S/M/L data.
- Selected material, plate cut-outs, enclosure geometry and wall thicknesses (OWNER_DECISION / TBD).
- Exact link lengths and joint offsets.
- Decision on powered vs passive grippers and optional mast/sensors.

## 6. Status

Week 3/4 mass framework updated with a plate-geometry cross-check and an explicit enclosure allowance. Total remains an ESTIMATE; no claim is made that the robot will meet the printed 5–8 kg target.
