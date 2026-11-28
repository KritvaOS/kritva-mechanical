# DA-01 — Mechanical feasibility screen

**Status:** PROPOSED / ESTIMATE; no structural verification. D-003 remains active.

## Load path and packaging

The proposed path is payload → gripper/wrist → forearm → elbow → upper arm → shoulder support → base plate → tabletop. A 350 mm arm reach and 300×250 mm base are concept targets, not controlled CAD dimensions. Two 20×20×2 mm aluminum tube link runs weigh approximately 0.272 kg bare at 0.389 kg/m; end plates, fasteners and wiring are allowances in the mass budget. The 300×250×4 mm 6061 plate is approximately 0.81 kg at 2,700 kg/m³. This establishes a coherent packaging estimate, not bending, deflection, fatigue or fastener adequacy.

## Stability screen

For an illustrative 6.33 kg total-mass case and a 250 mm-deep footprint, assuming the entire mass acts at the footprint center gives an upper-bound restoring moment of 6.33×9.81×0.125 = 7.76 Nm about a front support edge. The conditional shoulder-pitch gravity branch is 2.49 Nm per fully extended arm, or 4.99 Nm for two arms extended forward. That is 64% of the optimistic whole-mass restoring moment before acceleration or contact. Because arm mass is not located at the base center, this is not a pass: actual restoring moment can be lower. A positive clamp or a verified base/arm COM model is not part of the concept target.

## Serviceability and score implications

The paper configuration keeps six baseline joint modules and separates shoulder-pitch and wrist-axis alternatives. The camera mast, two demonstration grippers, cables and optional shoulder axis add packaging and snag risks. A removable cover, accessible fasteners and strain relief are included as design criteria, not a completed layout. The 4.77 Nm conditional shoulder-pitch screen is below the HEBI T5-4 4 Nm reference after headroom, and fits the 10 Nm Makiina load reference; the mass/cost cases remain estimates.

## Evidence boundary

Table dimensions, tube sections, 6.33 kg mass, 0.20 kg payload, moment arms and support edge are explicit assumptions or concept targets. No FEA, hand calculation of plate stress, modal analysis, tipping test, ergonomic assessment or physical evidence is claimed. A material strength number is not used to imply a safety margin.