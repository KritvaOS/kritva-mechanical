# Artwork Regeneration Request

| Field | Value |
|---|---|
| Document | Artwork Regeneration Request |
| Version | 0.1.0 |
| Last Updated | 2026-10-31 |
| Status | DRAFT |
| Source | Concept sheet vs cross-section sheet comparison, recorded in each concept README (section 10) and `ARTWORK_MANIFEST.json` |

Purpose: list where the concept sheet and the cross-section sheet of the same concept disagree, so the artwork can be regenerated. The owner decides which value is correct. Where this file says "keep the concept sheet", that is a suggestion, not a decision.

## 1. Priority A: wrong robot or different variant (regenerate the cross-section)

| Concept | Concept sheet says | Cross-section says | Suggested fix |
|---|---|---|---|
| QR-06 Hexapod | 6 legs, 2 DOF per leg, 12 actuators; body 400 × 280 × 220 mm; overall 520 × 480 mm | Shows a 4-legged robot, 3 DOF per leg; body 1000 × 420 mm, height 520 mm, width 750 mm; titled "Quadruped (Modular / Expandable)" | Redraw as a hexapod internal structure to the concept values |
| QR-01 Compact Quadruped | 2 DOF per leg, 8 actuators; body 300 × 250 × 200 mm; overall 420 × 400 mm | 3 DOF per leg (12); body 500 × 300 mm, height 350 mm, width 500 mm; titled "Basic" | Redraw with 2 DOF legs and concept dimensions |
| QR-03 Low-Profile Quadruped | 2 DOF per leg, 8 actuators; body 400 × 350 × 180 mm; overall 520 × 480 mm | 3 DOF per leg (12); body 700 × 340 mm, height 420 mm, width 600 mm; titled "Premium"; payload bay | Redraw as a low 2-DOF body with concept dimensions |
| QR-05 Modular Quadruped | 2 or 3 DOF per leg (8 or 12); body 420 × 260 × 250 mm; overall 560 × 520 mm; interchangeable leg modules | Fixed 3 DOF (12); body 900 × 400 mm, height 500 mm, width 700 mm; titled "Heavy-Duty / Research"; no leg-module interface | Redraw to concept dimensions and show the leg-module mounting interface |
| DA-04 Humanoid Mobile Dual-Arm | Width 1200 mm, height 1200 mm, base 500 × 600 mm, torso 400 mm, reach 450 mm | Width 800 mm, height 650 mm, base 400 × 450 mm (the DA-03 numbers) | Redraw one sheet so both carry the same dimensions; owner to pick the size |

## 2. Priority B: same robot, different sizes or details

| Concept | Difference | Concept sheet | Cross-section |
|---|---|---|---|
| QR-02 | Body size | 350 × 260 × 250 mm; overall width 480 mm | 600 × 350 mm; height 400 mm; width 500 mm; titled "Advanced" with extra sensors |
| QR-04 | Body size | 450 × 280 × 320 mm; overall width 520 mm | 800 × 380 mm; height 450 mm; width 620 mm; titled "High-Performance"; "Kritva Nexus" compute; ankle actuator |
| DA-01 | Overall width | 700 mm | 800 mm |
| DA-01 | Shoulder axis label | Yaw / rotation | Pitch |
| DA-01 | Camera mast | Not shown | Added |
| DA-02 | Overall height | 550 mm | 600 mm |
| DA-02 | Base width | 300 mm | 400 mm |
| DA-02 | Camera arrangement | Optional head | Adjustable mast with three cameras |

## 3. Priority C: minor corrections

| Concept | Sheet | Fix |
|---|---|---|
| DA-03 | Concept | Renders show four wheels, but the base is a 2-DOF differential drive; show a two-wheel layout with a caster, or state how four wheels are driven by two actuators |
| DA-03 | Both | LiDAR is mentioned on the concept sheet but not labelled on the cross-section; make them agree. Label the red button if it is an emergency stop |
| DA-05 | Concept | "Slip ring or cable loop" conflicts with continuous 360° rotation; state slip ring |
| DA-05 | Cross-section | Subtitle typo "Cross-Section 0eion Views" |
| DA-06 | Cross-section | Title reads "KMECH-CONCEPT-DA-06"; it should read "KMECH-CROSS-SECTION-DA-06" |
| DA-06 | Cross-section | Drivers labelled "per joint" but drawn as left and right arm stacks; make consistent |
| DA-06 | Both | IMU labelled on the concept mast only |
| QR-04, QR-05, QR-06 | Cross-section | "Kritva Nexus" is not defined in any approved document; use Kritva Edge only, or have the owner define Nexus |

## 4. Sheets with no value differences

DA-05 and DA-06 dimensions and DOF agree between sheets, and DA-03 dimensions and DOF agree. Only the minor corrections in section 3 apply.

## 5. After regeneration

1. Replace the PNG file under the same name in `docs/images/`.
2. Recompute `sha256`, width and height in `ARTWORK_MANIFEST.json` and set the status to `PENDING_REVIEW`.
3. Update the concept README discrepancy table and add a CHANGELOG entry.
