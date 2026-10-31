# Cross-Section Artwork Issues, By File

Date: 2026-10-31. Each section is one file and can be pasted into ChatGPT on its own. The "Target" line is what the matching concept sheet prints (the concept sheets are not changing). The owner decides anything marked OWNER.

Rules for every file: keep the file name; keep the sheet layout; use "Kritva Edge" (not "Kritva Nexus", which is not defined anywhere); show a two-finger gripper (the concept sheets say two-finger); do not add LiDAR, 5G or rear cameras unless the concept sheet lists them.

---

## KMECH-CROSS-SECTION-DA-01.png
Target: fixed tabletop dual-arm, 3 DOF per arm, 6 actuators (optional gripper), overall width 700 mm, height 400 mm, base 300 × 250 mm, reach 350 mm per side, shoulder yaw, elbow pitch, wrist pitch/rotation.

- "Base Width 300 mm" is printed twice and the two labels overlap; keep one.
- The subtitle has a stray glitch character near "(Front and Top)"; reprint it cleanly.
- "Shoulder to Shoulder Width 400 mm" is not on the concept sheet; remove it or confirm it with the owner (OWNER).
- The hands are drawn with four or five fingers; redraw as a two-finger gripper.
- Everything else (700 mm, 400 mm, 300 × 250 mm, 3 DOF per arm, shoulder yaw) matches the concept sheet.

## KMECH-CROSS-SECTION-DA-02.png
Target: humanoid torso dual-arm, 4 DOF per arm (shoulder yaw, shoulder pitch, elbow pitch, wrist pitch), 8 actuators plus 1 optional head DOF, width 800 mm, shoulder to shoulder 600 mm, torso 300 × 250 mm, height 550 mm, base 300 × 250 mm.

- The concept counts one optional head DOF; the sheet shows a "Pan/Tilt Mount (Optional)", which is normally two axes. Show a single-axis head mount, or ask the owner to accept two (OWNER).
- The hands are drawn with several fingers; redraw as a two-finger gripper.
- Replace "Kritva Edge / Nexus" with "Kritva Edge" in the front view, side view, torso section and any other label.
- All dimensions (550, 800, 600, 300, 250 mm) match the concept sheet.

## KMECH-CROSS-SECTION-DA-03.png (wrong robot, regenerate)
Target: compact mobile dual-arm on a differential-drive base, 3 DOF per arm, 6 arm DOF + 2 base DOF = 8 actuators, overall height 650 mm (with sensor mast), overall width 800 mm, base 400 mm wide × 450 mm long, reach 350 mm per side, torso fixed, optional sensor mast.

- The sheet shows a 1000 mm tall humanoid; change the overall height to 650 mm.
- Overall width is printed as 600 mm; it must be 800 mm.
- Base is printed 600 wide × 400 long; it must be 400 wide × 450 long.
- Torso width 350 mm is not on the concept sheet; remove it.
- The robot is drawn as a tall humanoid on two wheels; redraw as the compact low-profile mobile base with a short torso and sensor mast.
- The title says "Humanoid"; change it to "Mobile Dual-Arm Robot".
- Remove the head pan/tilt mount and IMU, or mark them optional only if the owner accepts them (OWNER).
- Show a two-finger gripper instead of a multi-finger hand.
- The concept render shows four wheels while the spec says 2 DOF differential drive; ask the owner whether to show two driven wheels with a caster or four wheels (OWNER).
- Replace "Kritva Edge / Nexus" with "Kritva Edge".

## KMECH-CROSS-SECTION-DA-04.png
Target: humanoid mobile dual-arm, 4 DOF per arm, 8 arm DOF + 2 base DOF = 10 actuators, overall width 1200 mm, overall height 1200 mm, base 500 × 600 mm, torso width 400 mm, shoulder to shoulder 600 mm, reach 450 mm per side.

- "Shoulder to Shoulder Width 400 mm" must be 600 mm; 400 mm is the torso width, so label it "Torso Width 400 mm" and add a separate 600 mm shoulder dimension.
- The "Neck Mount (2 DOF Optional)" and "Head Pan/Tilt (2 DOF Optional)" are not on the concept sheet, which counts no head DOF; remove them or ask the owner to accept them (OWNER).
- Replace "Kritva Edge / Nexus" with "Kritva Edge" everywhere.
- "Battery pack can be in base or torso (configuration option)" is not on the concept sheet; pick one location or mark it TBD (OWNER).
- Overall width 1200 mm, height 1200 mm, base 500 × 600 mm, 4 DOF per arm and 2 base DOF match the concept sheet.

## KMECH-CROSS-SECTION-DA-05.png (wrong robot, restore or regenerate)
Target: rotating platform dual-arm on a fixed tabletop plate, 3 DOF per arm, 6 arm DOF + 1 base rotation DOF = 7 actuators, overall width 800 mm, overall height 400 mm (with sensor mount), base 300 × 250 mm, 360° continuous rotation through a slip ring, reach 350 mm per side.

- The sheet shows a mobile humanoid on two wheels; remove the wheels and show a fixed base plate with a rotating base.
- Arms are labelled 6 DOF each with a 3 DOF wrist; they must be 3 DOF each (shoulder yaw, elbow pitch, wrist pitch).
- Overall height 1300 mm must be 400 mm.
- Overall width 700 mm must be 800 mm.
- Base 450 mm long with a "Differential Drive" is wrong; the base is 300 × 250 mm.
- Torso width 350 mm and shoulder to shoulder 500 mm are not on the concept sheet; remove them.
- Remove the drive wheels, the base section "Mobile Base" and the head sensor suite; show a camera/sensor mount (optional) on a short mast, as on the concept sheet.
- Show the rotating base with its slip ring, bearing and base actuator (cross-section sheet from round 1 had these).
- Fix the title typo "WOF per Arm" and the title text "Mobile Dual-Arm Humanoid"; use "Rotating Platform Dual-Arm Robot (3 DOF per Arm)".
- Replace "Kritva Edge / Nexus" with "Kritva Edge".
- Show a two-finger gripper.

## KMECH-CROSS-SECTION-DA-06.png (wrong robot, restore or regenerate)
Target: vision-integrated dual-arm on a fixed tabletop base, 4 DOF per arm (shoulder yaw, shoulder pitch, elbow pitch, wrist pitch), 8 actuators, base 0 DOF, overall width 800 mm, overall height 500 mm (with camera mast), base 300 × 250 mm, reach 350 mm per side, adjustable-height mast with top RGB-D/stereo camera plus left and right wide/depth cameras.

- The sheet shows a mobile humanoid on two wheels; remove the wheels and show a fixed tabletop base plate.
- Arms are 6 DOF with a 3 DOF wrist; they must be 4 DOF each.
- Overall height 1600 mm must be 500 mm.
- Base 500 mm wide × 500 mm long is wrong; the base is 300 × 250 mm.
- Torso width 400 mm and shoulder to shoulder 600 mm are not on the concept sheet; remove them.
- There is no humanoid head; show the central camera mast with top, left and right cameras instead of a head sensor suite with pan/tilt.
- Show the mast as adjustable height, as on the concept sheet.
- Fix the title typo "WOF per Arm"; use "Vision-Integrated Dual-Arm Robot (4 DOF per Arm)".
- Replace "Kritva Edge / Nexus" with "Kritva Edge".
- Show a two-finger gripper.

## KMECH-CROSS-SECTION-QR-01.png (wrong robot, regenerate)
Target: compact quadruped, four legs, 2 DOF per leg (hip flexion/extension, knee flexion/extension), 8 actuators, body 300 × 250 × 200 mm, overall length 420 mm, overall width 400 mm, rigid fixed body, top sensor module optional.

- The sheet shows a tabletop dual-arm robot with "2 DOF per Arm"; it must show a four-legged quadruped.
- The title says "Tabletop 2-DOF Arm Robot"; use "Compact Quadruped Robot (8-DOF, 2 DOF per Leg)".
- The subtitle says "4 Arm DOF Total" and "Overall Width 600 mm"; use "8 Leg DOF Total" and overall width 400 mm.
- Show body length 300 mm, body width 250 mm, body height 200 mm and overall length 420 mm.
- Show hip and knee joints for four legs and a foot pad on each leg; remove the shoulder, elbow, gripper and base mounting sections.
- Remove the Torso Width 200 mm, Shoulder to Shoulder 340 mm and Torso Depth 180 mm dimensions.
- The previous round 1 version of this sheet (2 DOF quadruped, 300 × 250 × 200 mm, overall width 400 mm) was close to correct; restore it and apply only the label corrections below.
- Round 1 label corrections: remove "Body Depth" or label it clearly; use Kritva Edge only (no Nexus); remove LiDAR, 5G antenna and rear sensor suite unless the owner accepts them (OWNER); remove "Ankle Interface (Integrated)".

## KMECH-CROSS-SECTION-QR-02.png
Target: standard quadruped, 3 DOF per leg (hip abduction/adduction, hip flexion/extension, knee flexion/extension), 12 actuators, body 350 × 260 × 250 mm, overall length 520 mm, overall width 480 mm.

- Overall width is printed 520 mm; it must be 480 mm (520 mm is the overall length).
- "Body Depth 280 mm" matches no concept value; remove it or relabel it with a value from the concept sheet.
- Replace "Kritva Edge / Nexus" with "Kritva Edge".
- Remove LiDAR, Wi-Fi/5G antenna and the rear sensor suite unless the owner accepts them (OWNER); the concept sheet only lists optional IMU and cameras.
- Remove "Ankle Interface (Integrated)", which is not on the concept sheet.
- Body length 350 mm, body width 260 mm, height 250 mm and 3 DOF per leg match.

## KMECH-CROSS-SECTION-QR-03.png
Target: low-profile quadruped, 2 DOF per leg (hip flexion/extension, knee flexion/extension), 8 actuators, body 400 × 350 × 180 mm, overall length 520 mm, overall width 480 mm.

- Overall width is printed 520 mm; it must be 480 mm.
- "Body Depth 350 mm" repeats the body width; remove it or relabel it.
- Replace "Kritva Edge / Nexus" with "Kritva Edge".
- Remove LiDAR, Wi-Fi/5G antenna and the rear sensor suite unless the owner accepts them (OWNER).
- Remove "Ankle Interface (Integrated)".
- Body length 400 mm, body width 350 mm, height 180 mm and 2 DOF per leg match.

## KMECH-CROSS-SECTION-QR-04.png
Target: agile long-leg quadruped, 3 DOF per leg, 12 actuators, body 450 × 280 × 320 mm, overall length 620 mm, overall width 520 mm.

- Overall width is printed 620 mm; it must be 520 mm.
- "Body Depth 320 mm" is the body height; remove it or relabel it.
- The subtitle has a stray glitch character near "(Side and Top)"; reprint it cleanly.
- Remove LiDAR, Wi-Fi/5G antenna and the rear sensor suite unless the owner accepts them (OWNER).
- Remove "Ankle Interface (Integrated)".
- Keep the compute label as "Kritva Edge" (it is already correct on this sheet).
- Body length 450 mm, body width 280 mm, height 320 mm and 3 DOF per leg match.

## KMECH-CROSS-SECTION-QR-05.png
Target: modular quadruped, interchangeable leg modules of 2 or 3 DOF per leg (8 or 12 actuators), body 420 × 260 × 250 mm, overall length 560 mm, overall width 520 mm.

- Overall width is printed 560 mm; it must be 520 mm.
- "Body Depth 250 mm" is the body height; remove it or relabel it.
- Replace "Kritva Edge / Nexus" with "Kritva Edge".
- Remove LiDAR, Wi-Fi/5G antenna and the rear sensor suite unless the owner accepts them (OWNER).
- Remove "Ankle Interface (Integrated)".
- The leg-module interface detail (4 × M5, 2 × Ø5 mm dowels, power + CAN + I/O connector) is a design choice, not on the concept sheet; label it "indicative concept" and ask the owner to accept it (OWNER). "CAN" is not defined in the program documents.
- Body length 420 mm, body width 260 mm, height 250 mm and the 2 DOF / 3 DOF module options match.

## KMECH-CROSS-SECTION-QR-06.png (wrong specification, regenerate)
Target: hexapod, six legs, 2 DOF per leg (coxa and femur/tibia), 12 actuators, body 400 × 280 × 220 mm, overall length 520 mm, overall width 480 mm.

- The sheet shows 3 DOF per leg and "18 Leg DOF Total"; the concept sheet says 2 DOF per leg and 12 actuators. Either redraw with 2 DOF per leg, or ask the owner to change the concept to 3 DOF (OWNER).
- Overall length 700 mm must be 520 mm; overall width 600 mm must be 480 mm; overall height 450 mm must be 220 mm.
- The title says "Hexapod Mobile Robot"; use "Hexapod Legged Robot (6 Legs, 2 DOF per Leg)".
- Remove the tibia joint if 2 DOF is kept, and label the two joints to match the concept sheet.
- Show body 400 × 280 × 220 mm.
- Replace "Kritva Edge / Nexus" with "Kritva Edge".
- Remove LiDAR and the optional RGB-D camera unless the owner accepts them (OWNER).
- The earlier round 2 version (hexapod, 2 DOF per leg, 400 × 280 mm body, overall width 520 mm) was closer; restore it and correct its overall width to 480 mm and the Nexus label.
- Check the side view: a hexapod must show three legs on the near side.
