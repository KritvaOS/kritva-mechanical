# DA-03 — Mechanical Architecture

| Property | Value |
|---|---|
| Document ID | KMECH-ARCH-DA-03 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Architecture |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary architecture assessment; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md` |

Tags: **[Sheet]** printed on the artwork (CONCEPT_TARGET or illustrative, unapproved); **[Assumed]** intern assumption; **TBD** not given. The artwork is concept art (evidence C, L0), not CAD. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Configuration

- Concept ID/name: DA-03 — Mobile Dual-Arm
- Mechanical family: Dual-arm
- Overall configuration: Differential-drive base (four wheels, left pair and right pair, one drive channel per side) carrying a fixed torso with two symmetric 3-DOF arms (shoulder yaw, elbow pitch, wrist pitch), two-finger grippers, a 24 V Li-ion battery in the base and an optional sensor mast. **[Sheet]**
- Complexity: High (relative category, not a validated assessment): adds mobility, battery and base drive to the dual-arm family. **[Sheet]**
- Intended demonstration: Kritva platform; compact tabletop-height mobile manipulation, pick-and-place, inspection, teleoperation. **[Sheet]**

| Item (CONCEPT_TARGET) | Value |
|---|---|
| Base W × L | 400 mm × 450 mm |
| Overall height (with mast) | 650 mm |
| Overall width, arm to arm | 800 mm (cannot be reconciled with reach and torso: D5) |
| Torso width | 300 mm (cross-section only: D6) |
| Arm reach, each side | 350 mm |
| Target weight | 12 – 18 kg (est., no stated basis) |

## 2. Mechanical Breakdown

| Assembly / subsystem | Function | Configuration | Status |
|---|---|---|---|
| Main structure | Carry torso, arms, battery and wheels | Aluminium or steel base frame; fixed central torso with electronics enclosure **[Sheet]** | Illustrative |
| Joints / arms | Position the gripper | Two arms, three joints each: shoulder yaw, elbow pitch, wrist pitch. Aluminium or 3D-printed links; BLDC/PMSM, harmonic or planetary gearbox, encoder per joint **[Sheet]** | Illustrative; no shoulder pitch, so the upper arm is a fixed cantilever (orientation **[Assumed]** horizontal) |
| End effector | Grasp | Two-finger linkage, optional servo or BLDC, optional force sensor, rubber or TPU pads **[Sheet]** | Optional actuation, TBD |
| Wheels and drive | Move the platform | Four wheels as left and right pairs; BLDC with encoder per side, optional gearbox, hub and rubber tyre **[Sheet]** | Illustrative; wheel size, tyre, gear ratio TBD |
| Base / torso | Housing | Base holds battery between the wheel drives and the drive drivers; torso holds Kritva Edge and arm drivers **[Sheet]** | Packaging not assessed |
| Sensor mast | Carry camera | Mast on the torso, height adjustable per cross-section only (D6), optional RGB-D or stereo camera **[Sheet]** | Optional |
| Mounting and interfaces | Mount arms, mast, battery | Shoulder mounts on torso sides **[Assumed]**; no fastener or load-path detail | TBD |

## 3. DOF and Joint Arrangement

| Joint / mechanism | Count | DOF | Motion / range | Notes |
|---|---:|---:|---|---|
| Shoulder yaw | 2 | 2 | Yaw; range TBD | Baseline |
| Elbow | 2 | 2 | Pitch; range TBD | Baseline |
| Wrist | 2 | 2 | Pitch (D3: concept sheet also says rotation); range TBD | Baseline |
| Wheel drive channels | 2 (left pair, right pair) | 2 | Drive rotation | D2 resolved: not four independent motors |
| Gripper | 2 | 0 (counted separately) | Parallel open and close | Optional, TBD |
| **Total** | 8 actuators | **8 DOF** | | 6 arm + 2 base |

Axis directions are ASSUMED, not printed on the sheets; joint names and DOF are as labelled. With one yaw and two parallel pitch joints, each arm positions the gripper in 3D but cannot set its orientation independently and has no roll.

## 4. Interfaces and Packaging

- **Kritva Edge reservation:** In the torso electronics enclosure **[Sheet]**; dimensions TBD; fit not assessed.
- **Power distribution:** 24 V in with 5 V and 12 V rails **[Sheet]**; the battery is 24 V Li-ion, capacity TBD, protection and charging TBD. 24 V is a concept-level indication, not a confirmed interface.
- **Sensors and mounting:** Optional camera on the mast; concept sheet mentions space for LiDAR, camera and IMU, LiDAR not drawn on the cross-section (D4). IMU space TBD.
- **Actuator/controller interfaces:** Left and right drive drivers in the base, arm drivers in the torso **[Sheet]**; driver selection TBD; whether S/M/L modules integrate drivers UNKNOWN.
- **EtherCAT-related provisions:** Not shown on either sheet. TBD.
- **Cable routing and service access:** Arm cables pass through the shoulders and links; power and signal run from battery and enclosure to the wheel drives and arms **[Sheet]**. A moving base needs strain relief, connector retention and vibration allowance. Service access (battery swap, drives, torso panels) not shown. TBD.
- **Emergency stop:** A red button is visible on the concept side-view but is unlabelled. Author observation; safety design TBD.

## 5. Architecture Assumptions and Risks

**Assumptions [Assumed]**
- Link split 175 / 100 / 75 mm; upper arm rigid and horizontal.
- Shoulders on the torso sides (shoulder spacing 300 mm from the torso width), 400 mm above ground; torso 250 mm deep, 300 mm tall.
- Wheel contact points at ±190 mm × ±150 mm; 100 mm wheels.
- Baseline excludes LiDAR, powered grippers and the adjustable mast feature until the owner decides.

**Unknowns:** shoulder spacing and the 800 mm width (D5); wrist terminology (D3); LiDAR (D4); torso width and mast (D6); work surface height; joint ranges; battery capacity; wheel and tyre data; S/M/L mapping.

**Architecture risks**
1. 3-DOF arms: no independent gripper orientation or roll, which limits tasks.
2. Working height: assumed lowest gripper height about 225 mm and highest about 575 mm; floor level and normal table heights may be out of reach.
3. Paired wheel drive: turning scrub sets wheel torque and wears tyres; steering behaviour unknown.
4. Base packaging of battery, two drivers and wheel drives is not checked; the battery is also a safety item.
5. Cable routing and strain on a moving base.
6. Mast (if used) raises the centre of mass and adds sway.
7. Printed weight and payload targets have no stated basis.

**Alternatives considered:** only printed options are recorded (aluminium or steel base frame, machined or printed links, harmonic or planetary gearbox, powered or passive gripper, mast height adjustable or fixed, LiDAR or none). None is selected.

## 6. References and Evidence

| Ref | Item | Evidence type |
|---|---|---|
| R1 | `docs/images/KMECH-CONCEPT-DA-03.png` | C (concept artwork, L0) |
| R2 | `docs/images/KMECH-CROSS-SECTION-DA-03.png` | C (concept artwork, L0) |
| R3 | `docs/images/ARTWORK_MANIFEST.json` (both sheets REVIEWED_WITH_ISSUES; not design approval) | Record |
| R4 | `README.md` v0.3.1 | Summary of R1, R2 |
| R5 | `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `MECHANICAL_ANALYSIS.md` | C (paper calculations) |

Planned sketches in `sketches/`: base layout with battery, drivers and wheels; arm kinematic sketch; cable path with strain relief.

## 7. HOLD D-003

Architecture documentation and conceptual sketches only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
