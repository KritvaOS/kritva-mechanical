# Artwork Review, Round 2 (cross-sections regenerated)

| Field | Value |
|---|---|
| Document | Artwork Review, Round 2 |
| Date | 2026-10-31 |
| Scope | 12 regenerated `KMECH-CROSS-SECTION-*.png` sheets compared with the unchanged concept sheets |
| Status | DRAFT; the manifest still holds the round 1 hashes and is not updated |

The 12 concept sheets are byte-identical to round 1 (hash check). All 12 cross-sections changed. Dimensions below are read from the images; "OK" means the printed value equals the concept sheet.

## 1. Result by concept

| Concept | Verdict | Summary |
|---|---|---|
| DA-05 | REJECT | Shows a mobile humanoid on two wheels with 6 DOF per arm, 1300 mm tall. The concept is a fixed-tabletop rotating platform, 3 DOF per arm, 400 mm tall |
| DA-06 | REJECT | Same mobile humanoid image, 6 DOF per arm, 1600 mm tall. The concept is a fixed-tabletop vision dual-arm, 4 DOF per arm, 500 mm tall |
| DA-03 | REJECT | Shows a 1000 mm tall humanoid on two wheels, base 600 × 400 mm, width 600 mm. The concept is 650 mm tall, 800 mm wide, base 400 × 450 mm, compact with four wheels |
| DA-04 | FIX | Dimensions now match; two label errors |
| QR-06 | FIX | Now a hexapod; several label errors |
| QR-01 | FIX | Now 2 DOF; label issues only |
| QR-02 | FIX | Overall width wrong; label issues |
| QR-03 | FIX | Overall width wrong; label issues |
| QR-04 | FIX | Overall width wrong; label issues |
| QR-05 | FIX | Overall width wrong; label issues; new interface details need owner decision |
| DA-01 | FIX (minor) | Matches the concept; text glitches |
| DA-02 | FIX (minor) | Matches the concept; head DOF still unresolved |

DA-05 and DA-06 were correct in round 1 and are worse now. If the earlier files are in Git history or your downloads, restoring them is quicker than regenerating.

## 2. Corrections by sheet

### DA-05 and DA-06 (restore or regenerate)
- Fixed tabletop base, not wheels. DA-05 has one rotating base DOF (360°, slip ring); DA-06 has a fixed base.
- 3 DOF per arm for DA-05, 4 DOF per arm for DA-06, not 6.
- Heights 400 mm (DA-05) and 500 mm (DA-06), width 800 mm, base 300 × 250 mm.
- DA-06 needs the top, left and right cameras on the adjustable mast; there is no humanoid head.
- Title typo "WOF per Arm" on both.

### DA-03 (regenerate)
- Height 650 mm (with mast), overall width 800 mm, base 400 mm wide × 450 mm long, torso on a compact differential-drive base.
- It is not a humanoid; drop the head pan/tilt and IMU unless the owner wants them.
- Keep 3 DOF per arm, 2 base DOF, 8 actuators in total.

### DA-04
- "Shoulder to Shoulder Width 400 mm" should be 600 mm; 400 mm is the torso width on the concept sheet.
- Neck mount "2 DOF optional" and head pan/tilt "2 DOF optional" are new. The concept counts no head DOF. Remove them or have the owner approve them.
- "Kritva Nexus" is not defined; label Kritva Edge only.
- Battery "base or torso (configuration option)": the concept does not say; pick one or mark TBD.

### QR-01
- Top view has "Body Width 250" and "Body Depth 250" for the same body. The concept gives body length 300, width 250, height 200; remove "Body Depth" or rename it consistently.
- Overall width 400 mm now matches the concept.
- "Kritva Nexus", LiDAR, Wi-Fi/5G antenna and rear sensor suite are not on the concept. Use Kritva Edge and the concept's optional IMU and camera only.

### QR-02
- Overall width should be 480 mm; the sheet prints 520 mm, which is the overall length.
- "Body Depth 280 mm" matches no concept value (width 260, height 250). Correct or remove.
- Nexus, LiDAR, 5G antenna and rear suite as for QR-01.

### QR-03
- Overall width should be 480 mm; the sheet prints 520 mm (the overall length).
- "Body Depth 350 mm" repeats the width. Correct or remove.
- Nexus, LiDAR, 5G, rear suite.

### QR-04
- Overall width should be 520 mm; the sheet prints 620 mm (the overall length).
- "Body Depth 320 mm" is the concept's body height. Correct or remove.
- Subtitle has a glitch character near "(Side and Top)".
- This sheet correctly uses Kritva Edge, not Nexus. The compute label is fine.

### QR-05
- Overall width should be 520 mm; the sheet prints 560 mm (the overall length).
- "Body Depth 250 mm" is the concept's body height. Correct or remove.
- New leg-module interface detail (4 × M5, 2 × Ø5 mm dowels, power + CAN + I/O connector) is welcome but is a design choice. The owner must accept it as a concept indication. CAN is not defined anywhere in the program documents.
- Nexus, LiDAR, 5G, rear suite.

### QR-06
- Overall width should be 480 mm; the sheet prints 520 mm (the overall length).
- Top view labels body width 280 horizontally and body length 400 vertically, which is the opposite orientation to the other quadrupeds; make consistent.
- Hip is labelled "Pitch" and knee "Pitch". The concept says "coxa + femur/tibia". Ask the owner whether the hip is a yaw (coxa) or pitch joint.
- Nexus, LiDAR, 5G, rear suite; the "Ankle Interface (Integrated)" is not on the concept.
- Check the side view: it appears to show four legs; a hexapod side view should show three on the near side.

### DA-01
- "Base Width 300 mm" is printed twice and overlaps.
- Subtitle glitch near "(Front and Top)".
- Shoulder-to-shoulder 400 mm is not on the concept sheet; confirm or remove.
- Hands are drawn with four or five fingers; the concept says a two-finger gripper.

### DA-02
- The concept counts one optional head DOF; the sheet shows a pan/tilt mount (normally two axes). Pick one.
- Hands are drawn with several fingers; the concept says a two-finger gripper.
- Nexus.

## 3. Common to all 12
1. "Kritva Nexus" is still on 10 of 12 sheets (all except QR-04 and DA-01). It is not defined anywhere. Use Kritva Edge, or the owner defines Nexus.
2. Hands on DA-01, DA-02, DA-03 and DA-05/06 render as multi-finger hands, while every concept sheet says two-finger gripper.
3. Quadruped cross-sections now all show an advanced sensor suite (LiDAR, 5G, rear camera) that the concept sheets do not have. Quadruped concepts say IMU and cameras optional.
4. "Overall width" on QR-02 to QR-06 uses the overall length number. QR-01 is correct.
5. Cross-section hip labels that read "Pitch" are consistent with the concept sheets' flexion/extension.

## 4. Next steps
1. Fix or restore DA-03, DA-05 and DA-06 first.
2. Apply the label corrections above to the other nine.
3. Send the new files; I will recompute hashes, update `ARTWORK_MANIFEST.json`, and rewrite the discrepancy tables in the concept READMEs. Until then the READMEs still describe the round 1 cross-sections, and I have not changed them.
