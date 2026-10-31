# Cross-Section Artwork Audit, Round 6

Date: 2026-10-31. Six sheets changed (DA-02, DA-04, DA-05, QR-04, QR-05, QR-06). The other six are unchanged and passed in round 5.

## Summary

| File | Result |
|---|---|
| DA-02 | PASS |
| DA-04 | PASS (one owner decision) |
| DA-05 | FIX: joint labels |
| QR-04 | PASS (owner decision) |
| QR-05 | PASS (owner decision) |
| QR-06 | FIX: duplicated dimension |
| DA-01, DA-03, DA-06, QR-01, QR-02, QR-03 | PASS (unchanged) |

## Per file

### KMECH-CROSS-SECTION-DA-02.png
- No issues. The subtitle is clean; 9 actuators (8 arm + 1 head pan), 550 mm, 800 mm, torso 300 × 250 mm, fixed base all match.

### KMECH-CROSS-SECTION-DA-04.png
- The garbled text is fixed; the width is printed once, and section 5 now says "2 DOF, 4 Wheels", consistent with DA-03.
- New: "Head with Camera (1 Pan DOF)". The concept sheet counts no head DOF and the actuator total is 10 (8 arm + 2 base), so a pan joint would make it 11. Remove the pan DOF or have the owner accept it and update the count (OWNER).

### KMECH-CROSS-SECTION-DA-05.png
- The shoulder is labelled "Shoulder Pitch Joint" in the front view, section 2 and the subtitle; the concept sheet says shoulder yaw. Change to "Shoulder Yaw".
- The front view labels "Wrist Pitch Joint" twice (once per arm) while the shoulder and elbow are labelled once; label one arm only, like the other sheets.
- Everything else matches: 7 actuators, 800 mm, 400 mm, base 300 × 250 mm, slip ring, "400 mm" typo fixed.

### KMECH-CROSS-SECTION-QR-04.png
- No sheet issues; the title, CAN reference and joint names are fixed.
- New "Body Mounting Interface (4 × M5 holes, 2 × Ø5 mm dowels, indicative concept)" and the optional height-adjustable sensor module are not on the concept sheet (OWNER).

### KMECH-CROSS-SECTION-QR-05.png
- No sheet issues. The 2 DOF / 3 DOF sections are now labelled correctly: abduction is "3 DOF – with Abduction", flexion is "2 DOF – without Abduction", and the knee is present in both.
- The body mounting interface is still "indicative concept" (OWNER).

### KMECH-CROSS-SECTION-QR-06.png
- The subtitle prints the body size as "400 × 280 × 280 × 220 mm (L × W × H)"; remove the duplicated 280 so it reads 400 × 280 × 220 mm.
- Six legs, 2 DOF per leg (coxa, femur/tibia), 12 actuators, 520 × 480 mm all match. The body mounting interface is indicative (OWNER).

## Remaining
1. DA-05: shoulder yaw label; duplicate wrist label.
2. QR-06: duplicated 280 in the subtitle.
3. Owner decisions: DA-04 head pan DOF; body mounting interface and height-adjustable sensor module on QR-04, QR-05, QR-06; torso width on DA-01 and DA-03.
