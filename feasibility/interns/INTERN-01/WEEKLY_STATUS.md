# INTERN-01 — Weekly status (Week 3/4 update)

| Property | Value |
|---|---|
| Intern | Amardeep Singh |
| Assigned concepts | DA-01, QR-02, DA-04, QR-04 |
| Reporting period | Week 3/4 working update |
| Status | PROPOSED contribution; paper feasibility only |
| Last Updated | 2026-11-28 |
| HOLD | D-003 active |
| Task reference | ROB-MECH-044 |

## 1. Work in this update

| Deliverable | Status | Evidence / limit |
|---|---|---|
| Concept requirements records | Revised for review | Four files link concept targets, FREQ references, and bounded evidence scenarios; no owner-approved baseline is claimed. |
| Torque and actuator screens | Recalculated | DA-01 wrist mass corrected; QR-02 6.30 kg sensor-excluded; QR-04 7.43 / 7.50 kg; DA-04 0.5 / 1.0 kg arm cases and wheel screen. |
| Mass and cost | Source-linked estimates | Low/nominal/high masses and seller/manufacturer price scenarios; shipping/customs and structural validation are excluded where not evidenced. |
| Concept mockups | Paper-only SVGs retained from the prior merged contribution | Four existing not-to-scale illustrations remain in the source tree; none is CAD or manufacturing output. |
| Family-role comparison | Provisional screen | S wrist/neck, M elbow/reference, L hip/knee; S/L values remain proposed placeholders in the family source. |
| Four-concept comparison | Updated, provisional | All seven proposed weights scored with evidence rationale; order is partial over four of twelve concepts. |
| Week 2 and FREQ traceability | Restored in overlays | D-003, Week 2 architecture files and relevant common FREQ IDs are linked. |

## 2. ROB-MECH-044 evidence state

The package task map assigns ROB-MECH-044 to INTERN-01. This contribution supplies evidence and does not mark the task accepted or complete. AC-044-01 records are present; AC-044-02 calculations are traceable within explicit pose and geometry scenarios; AC-044-03 compares candidate ratings to proposed family roles; AC-044-04 labels paper evidence and requires independent review. See CP3_CONTRIBUTION.md for the criterion map.

## 3. Concept-specific results

- DA-01 nominal mass/cost: 6.33 kg / ₹112,773. Conditional shoulder-pitch screen is 4.77 Nm at 1.5×; baseline elbow is 1.33 Nm.
- QR-02 nominal mass/cost: 6.30 kg sensor-excluded / ₹166,503 including optional camera. The 8.34 Nm one-leg hip-flexion screen fits the 10 Nm load-only case but not the proposed L family role.
- QR-04 nominal mass/cost: 7.43 kg sensor-excluded / ₹170,584 including optional camera. Hip-flexion 1.5× high screen is 11.31 Nm at 7.43 kg and 11.42 Nm at 7.50 kg.
- DA-04 economy mass/cost: 20.59 kg / ₹175,052; 1.0 kg payload shoulder screen is 14.64 Nm and exceeds the 10 Nm economy module. Two 18 Nm shoulder modules increase cost to ₹288,202 and require 48 V.

All costs are planning scenarios, not quotes; overseas freight/customs and 22.2-to-24 V conditioning are not included. Full L-role price lower bounds assume ideal torque addition from paired 18 Nm modules only for component pricing; coupling and load sharing are not mechanically validated. Results are not design selections or product qualification.

## 4. Review actions and downstream boundary

- Review source links, arithmetic and concept assumptions before accepting ROB-MECH-044.
- Confirm owner-level baseline choices and proposed family roles; any approved changes should update the source record and calculations.
- The remaining eight concepts, cross-intern score review and CP4 are outside this four-concept contribution.
- Retain HOLD D-003: CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain prohibited by the study scope.