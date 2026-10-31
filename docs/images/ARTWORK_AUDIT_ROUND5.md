# Cross-Section Artwork Audit, Round 5

Date: 2026-10-31. Nine sheets changed (DA-01 to DA-06, QR-04 to QR-06); QR-01 to QR-03 are unchanged and passed earlier. Concept sheets are unchanged. All dimensions, DOF and actuator counts now match the concept sheets on every sheet. What remains is text-level.

## Summary

| File | Result |
|---|---|
| DA-01 | PASS |
| DA-02 | FIX: garbled subtitle |
| DA-03 | PASS (owner decisions only) |
| DA-04 | FIX: duplicate text, wheel count |
| DA-05 | FIX: garbled unit in subtitle |
| DA-06 | PASS |
| QR-01 / QR-02 / QR-03 | PASS |
| QR-04 | FIX: title, CAN |
| QR-05 | FIX: title, CAN |
| QR-06 | PASS (owner decision only) |

## Per file

### KMECH-CROSS-SECTION-DA-01.png
- No issues. Fixed base, 6 actuators, 700 mm, 400 mm, base 300 × 250 mm, reach 350 mm all match.
- Torso Width 300 mm is not on the concept sheet; keep it only if the owner accepts it (OWNER).

### KMECH-CROSS-SECTION-DA-02.png
- The subtitle is garbled in the middle: "Base 300 mm | × 250 mm (D)" is split, and "Fixed Base" is blurred; reprint it cleanly.
- The end of the subtitle repeats and is cut off: "Cross-Section Views (Front, Sidn | Front, Side and Top)"; keep one clean copy.
- Everything else matches: 550 mm height, 800 mm width, 9 actuators (8 arm + 1 head pan), fixed base.

### KMECH-CROSS-SECTION-DA-03.png
- No sheet issues. The four-wheel base is now explained as "2 wheels driven per side, 2 DOF total".
- The concept sheet also draws four wheels, so the two sheets agree.
- The title says "Mobile Manipulator Dual-Arm Robot"; the concept name is "Mobile Dual-Arm". Optional rename.
- Torso Width 300 mm and the adjustable mast are not on the concept sheet; accept or remove (OWNER).

### KMECH-CROSS-SECTION-DA-04.png
- The subtitle prints the width twice: "Overall Width 1200  1200 mm"; keep one.
- Section 5 is titled "(2 DOF, 2 Wheels)" but the photo shows four wheels, and DA-03 says four wheels; make the wheel description the same on both sheets (OWNER decides the layout).
- Matches: 10 actuators, 1200 × 1200 mm, base 500 × 600 mm, torso 400 mm, shoulder to shoulder 600 mm, reach 450 mm.

### KMECH-CROSS-SECTION-DA-05.png
- The subtitle has a garbled unit: "Overall Height 400 hmm" should read "400 mm".
- Everything else matches: title, 7 actuators, slip ring, 800 mm, 400 mm, base 300 × 250 mm.

### KMECH-CROSS-SECTION-DA-06.png
- No issues. Camera mast now shows top, left and right cameras plus IMU; fixed base; 8 actuators; 800 mm; 500 mm.

### KMECH-CROSS-SECTION-QR-01.png / QR-02.png / QR-03.png
- No issues (unchanged).

### KMECH-CROSS-SECTION-QR-04.png
- The title reads "Quadruped Robot (Medium)"; the concept is the Agile Long-Leg Quadruped. Use "Agile Long-Leg Quadruped Robot (3 DOF per Leg, 12 Actuators)".
- "Sensor Interface (USB / MIPI / CAN)" names CAN, which no program document defines; remove CAN or have the owner define it (OWNER).
- Joint names now match QR-02 (Hip Abduction/Adduction, Hip Flexion/Extension, Knee). The "KREE" typo is fixed.
- Matches: 450 × 280 × 320 mm, overall 620 × 520 mm, 12 actuators.

### KMECH-CROSS-SECTION-QR-05.png
- The title reads "Quadruped Robot (Medium)"; use "Modular Quadruped Robot (2 or 3 DOF per Leg, 8 or 12 Actuators)".
- "Sensor Interface (USB / MIPI / CAN - TBD)" names CAN; same as QR-04.
- Fixed: the optional joint is now the hip abduction/adduction, the knee is no longer optional, and joint names match QR-02.
- The M5 holes and Ø5 mm dowels are labelled "indicative concept"; the owner decides whether to keep them (OWNER).
- Matches: 420 × 260 × 250 mm, overall 560 × 520 mm.

### KMECH-CROSS-SECTION-QR-06.png
- The garbled word is fixed. Six legs, 2 DOF per leg (coxa, femur/tibia), 12 actuators, 400 × 280 × 220 mm, overall 520 × 480 mm all match.
- Section 5 "Body Mounting Interface" (4 × M5, 2 × Ø5 mm dowels) is not on the concept sheet; keep it only if the owner accepts it (OWNER).

## Fix list (6 text fixes)
1. DA-02: reprint the subtitle.
2. DA-04: remove the duplicate width; fix "2 Wheels".
3. DA-05: "hmm" to "mm".
4. QR-04: title; remove CAN.
5. QR-05: title; remove CAN.
6. Owner decisions: DA-01 and DA-03 torso width, DA-03 and DA-04 wheel layout, QR-05 and QR-06 mounting interface.

After items 1 to 5, all 12 sheets can be marked `REVIEWED`.
