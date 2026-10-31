# Cross-Section Artwork Audit, Round 3

Date: 2026-10-31. All 12 cross-sections were re-read and compared with the unchanged concept sheets. Result: 11 of 12 are accepted apart from small text fixes; 1 (DA-04) has a corrupted subtitle. No sheet has a wrong robot, wrong DOF or wrong dimension any more. The manifest and READMEs have not been updated yet.

## Summary

| File | Result | Remaining issues |
|---|---|---|
| DA-01 | Minor fixes | 4 |
| DA-02 | Pass, minor | 2 |
| DA-03 | Pass, minor | 2 |
| DA-04 | Fix needed | 2 |
| DA-05 | Pass | 1 |
| DA-06 | Pass, minor | 3 |
| QR-01 | Pass | 0 |
| QR-02 | Pass | 0 |
| QR-03 | Pass | 0 |
| QR-04 | Fix needed | 1 |
| QR-05 | Fix needed | 2 |
| QR-06 | Fix needed | 1 |

## Per file

### KMECH-CROSS-SECTION-DA-01.png
- Subtitle typo: "Overall Heigt 400 mm" should read "Height".
- "Kritva Edge / Nexus" still appears in the front view, the head detail and the torso section; use "Kritva Edge" (Nexus is not defined anywhere).
- A head with LiDAR, pan/tilt mount and IMU was added; the concept sheet has a camera mast only. Remove the pan/tilt, IMU and LiDAR, or the owner accepts them (OWNER).
- "Head Cable Routing (with Slip Ring or Cable Loop)" does not apply to a fixed head; remove the slip ring wording.
- Matches the concept: 700 mm width, 400 mm height, base 300 × 250 mm, 3 DOF per arm, 2-finger gripper.

### KMECH-CROSS-SECTION-DA-02.png
- Title typo: "Intternal Structure" should read "Internal".
- The subtitle has stray double separators ("| |") after "Torso 300 × 250 mm" and before "Base".
- Matches the concept: 800 / 600 / 300 / 250 / 550 mm, 4 DOF per arm, 1 DOF head pan.

### KMECH-CROSS-SECTION-DA-03.png
- The subtitle is set in very small typo and "Base 400 mm (W) × 450mm (L)" has uneven spacing; reprint at a readable size.
- The sheet now shows a two-wheel drive with an optional caster, but the concept sheet DA-03 still draws four wheels. One of the two must change (OWNER).
- Matches the concept: 800 mm width, 650 mm height with mast, base 400 × 450 mm, 3 DOF per arm, 2 base DOF, 8 actuators.

### KMECH-CROSS-SECTION-DA-04.png
- The subtitle text is corrupted and unreadable in the middle ("Oegiyht 1200 mm | Overall Hmm | Shoulder to Shoulder | Torso Width 600 mm | Torsode 600 mm(L) …"); reprint it.
- The sheet shows no head or sensor detail; the concept sheet has a head with a camera and sensor mount. Add a small head section, or confirm the omission (OWNER).
- Matches the concept: 1200 mm width, 1200 mm height, base 500 × 600 mm, torso 400 mm, shoulder to shoulder 600 mm, reach 450 mm, 4 DOF per arm, 2 base DOF. The battery is now placed in the base.

### KMECH-CROSS-SECTION-DA-05.png
- The subtitle is set in very small type; reprint at a readable size.
- Matches the concept: 800 mm, 400 mm, base 300 × 250 mm, 3 DOF per arm, 1 rotating base DOF with slip ring, 7 actuators. The slip ring resolves the concept sheet's "slip ring or cable loop" wording.

### KMECH-CROSS-SECTION-DA-06.png
- The subtitle has a doubled bracket: "(with Camera Mast) )".
- In the front view the "Overall Width 800 mm" label overlaps "Base Width 300 mm" and the bottom of the label is clipped.
- The concept sheet labels the mast "camera / IMU"; this sheet shows no IMU. Add one or accept the difference (OWNER).
- Matches the concept: 800 mm, 500 mm with mast, base 300 × 250 mm, 4 DOF per arm, fixed base, 8 actuators, adjustable-height mast with top, left and right cameras.

### KMECH-CROSS-SECTION-QR-01.png
- No issues found. Matches the concept: 300 × 250 × 200 mm body, overall 420 × 400 mm, 2 DOF per leg, 8 actuators, Kritva Edge.

### KMECH-CROSS-SECTION-QR-02.png
- No issues found. Matches the concept: 350 × 260 × 250 mm, overall 520 × 480 mm, 3 DOF per leg, 12 actuators.

### KMECH-CROSS-SECTION-QR-03.png
- No issues found. Matches the concept: 400 × 350 × 180 mm, overall 520 × 480 mm, 2 DOF per leg, 8 actuators.

### KMECH-CROSS-SECTION-QR-04.png
- Section 4 title typo: "KREE JOINT SECTION" should read "KNEE JOINT SECTION".
- Matches the concept: 450 × 280 × 320 mm, overall 620 × 520 mm, 3 DOF per leg, 12 actuators.

### KMECH-CROSS-SECTION-QR-05.png
- The word "OWNER" is printed into the artwork: "Leg Module Interface (Indicative Concept – OWNER)" and the section 6 title "(INDICATIVE CONCEPT – OWNER)". It is an instruction, not a label; replace with "Indicative concept, definition TBD".
- The 4 × M5 holes and 2 × Ø5 mm dowels are a design choice, not on the concept sheet; keep them labelled "indicative concept" (OWNER to accept). The CAN reference is gone, which is correct.
- Matches the concept: 420 × 260 × 250 mm, overall 560 × 520 mm, 2 or 3 DOF modules (8 or 12).

### KMECH-CROSS-SECTION-QR-06.png
- The subtitle has a garbled word: "Optional Top Ŀemecs Module" should read "Top Sensor Module".
- Six legs are shown in the top view. Matches the concept: 400 × 280 × 220 mm, overall 520 × 480 mm, 2 DOF per leg (coxa, femur/tibia), 12 actuators.

## Across all 12 sheets
- "Kritva Nexus" is gone from 11 sheets and remains only on DA-01.
- LiDAR, 5G antennas and rear cameras were removed from the quadrupeds, and the quadrupeds now match their concept sheets.
- Several subtitles on DA-03 to DA-06 are in very small type; DA-04 is corrupted.
- Concept sheets are unchanged, so the earlier concept-sheet notes (DA-03 four wheels, DA-05 "slip ring or cable loop", QR-06 "CoXa + Femur/Tibia") still apply to the concept side.

## Fix list (10 items, all text or label level)
DA-01 (4), DA-02 (2), DA-03 (1 plus owner decision), DA-04 (2), DA-05 (1), DA-06 (3), QR-04 (1), QR-05 (1), QR-06 (1). After these, mark the sheets `REVIEWED`.
