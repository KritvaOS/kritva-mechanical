# DA-01 — Bounded decision and review register

**Status:** Paper-stage estimates prepared; D-003 HOLD active. The branches below make the current alternatives explicit; they do not request a design approval by implication.

## Owner choices that change the model

| Decision | Modeled alternatives | Consequence to the estimate |
|---|---|---|
| Shoulder axis | Three-axis baseline (yaw, elbow, wrist) or add shoulder pitch | Three-axis baseline is the source-artwork interpretation. Pitch is separately screened at 4.77 Nm, 1.5×. |
| Wrist axis | Pitch or forearm rotation | Pitch branch screens at 0.31 Nm; rotation branch screens at 0.002–0.012 Nm under the stated radial-offset assumption. Cable routing and ROM differ. |
| Camera and mast | Included in current nominal or omitted | Current 6.33 kg / ₹112,773 case includes camera and mast; concept mockup shows the mounting as an option. |
| Gripper | Two powered MG995 demonstration grippers or passive grippers | Mass/cost budget includes two light servo kits; grip force is not specified by the seller and no payload-force claim is made. |

## Review register

- The published 5–8 kg concept band is a target; current 4.53 / 6.33 / 8.74 kg low/nominal/high cases straddle it.
- The 24 V Makiina 10 Nm listing clears all modeled torque branches; HEBI T5-4 4 Nm does not clear the conditional 4.77 Nm pitch case. No module is selected.
- Central estimates use the published ₹2 lakh study ceiling, source links, and the listed currency conversion. Foreign shipping/customs are excluded rather than assigned invented rates.
- Stability has only an optimistic whole-mass support-edge screen. No clamp or verified center of mass is modeled.
- The source README statement about a 10-channel baseline is not restated as a new approval. No decision ID/date is asserted in this update because the referenced decision record is not in the reviewed package.

## Evidence state

The calculation, cost and mass screens are present in the linked concept files and the central source register. Independent review of assumptions and task acceptance remain separate from this analysis. CAD, BOM release, procurement, fabrication, assembly and physical tests remain prohibited by HOLD D-003.