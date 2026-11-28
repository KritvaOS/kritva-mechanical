# DA-01 — Mass Budget (Week 3 estimate)

| Property | Value |
|---|---|
| Document ID | KMECH-MASS-DA-01 |
| Status | PROPOSED — Week 3 paper estimate |
| Version | 0.3.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 |

**HOLD D-003 active.** No material selection, process selection or final BOM is authorised.

## 1. Artwork target (not a derived total)

Printed target: **5–8 kg (est.)** — CONCEPT_TARGET. The study does **not** force the subsystem sum to equal this range.

## 2. Subsystem mass ranges (ESTIMATE)

All values are planning estimates derived from the scale of the printed envelope, typical aluminium/CNC or printed link densities, and order-of-magnitude actuator module masses. Confidence is Low–Medium until source-controlled component data arrives.

| Subsystem | Low (kg) | Nominal (kg) | High (kg) | Notes / method |
|---|---:|---:|---:|---|
| Base plate + central enclosure | 0.80 | 1.20 | 1.80 | Al plate 300×250×6–10 mm + enclosure walls |
| 2 × upper-arm links | 0.20 | 0.30 | 0.45 | A4 scaled ×2 |
| 2 × forearm links | 0.12 | 0.20 | 0.30 | A6 scaled ×2 |
| 6 × joint modules (motor+gear+housing) | 1.20 | 1.80 | 2.70 | 0.20–0.45 kg each; pending S/M/L data |
| 2 × grippers (passive baseline) | 0.15 | 0.25 | 0.40 | Optional; may be lighter if purely passive |
| Compute + drivers + power distribution | 0.30 | 0.50 | 0.80 | Kritva platform boards + harness provision |
| Sensors / mast (optional) | 0.00 | 0.15 | 0.40 | Excluded from baseline; shown for sensitivity |
| Fasteners, bearings, covers, harness | 0.25 | 0.40 | 0.70 | Allowance |
| **Subtotal (baseline, no optional mast)** | **3.0** | **4.7** | **7.2** | |
| Battery (if required) | 0.00 | 0.40 | 1.00 | Tabletop may be externally powered; UNKNOWN |

## 3. Comparison with printed target

Nominal baseline ≈ 4.7 kg sits inside the lower half of the 5–8 kg printed band. High end of the range approaches the upper printed bound only if larger actuators and optional sensors are included. The printed target therefore remains plausible but is **not** treated as a derived or verified mass.

## 4. Centre of mass

Still UNKNOWN. No datum or component coordinates are defined. A first-order estimate places the CoM near the geometric centre of the base/torso once the arms are folded; extended-arm CoM shifts outward and raises tipping risk (see MECHANICAL_ANALYSIS).

## 5. Required inputs to improve confidence

- Source-controlled actuator module masses (S/M/L data pack with commit hash).
- Selected material grades and wall thicknesses (still OWNER_DECISION / TBD).
- Exact link lengths and joint offsets.
- Decision on powered vs passive grippers and inclusion of mast/sensors.

## 6. Status

Week 3 mass framework populated with transparent ranges. Total remains an ESTIMATE. No claim is made that the robot will meet the printed 5–8 kg target.
