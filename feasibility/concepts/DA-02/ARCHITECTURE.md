# DA-02 — Mechanical Architecture

| Property | Value |
|---|---|
| Document ID | KMECH-ARCH-DA-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Architecture |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary architecture assessment; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md` |

Conventions used below: **[Sheet]** = printed on the concept or cross-section artwork (CONCEPT_TARGET or illustrative, unapproved); **[Assumed]** = intern assumption, not printed; **TBD** = not given by any source. The artwork is concept art (evidence C, maturity L0), not CAD and not to scale. REVIEWED status of the sheets is not design approval. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Configuration

- Concept ID/name: DA-02 — Humanoid Torso Dual-Arm
- Mechanical family: Dual-arm
- Overall configuration: Two symmetric 4-DOF arms (shoulder yaw, shoulder pitch, elbow pitch, wrist pitch) on a fixed humanoid torso, mounted on a fixed base plate with no mobility. Optional one-axis pan head carrying a camera. Two-finger gripper on each arm (powered or passive, TBD). **[Sheet]**
- Complexity: Medium (relative engineering category, not a validated assessment). It adds a second shoulder axis to the DA-01 arm and a taller torso, and sits between a tabletop dual-arm and the mobile and 5-DOF concepts. **[Sheet]**
- Intended demonstration: Kritva platform, with manipulation, pick-and-place, and research and development as printed uses. **[Sheet]**
- Future path: an upgrade to 5-DOF arms and a mobile base is printed on the concept sheet as a design feature. It is **not** part of the study baseline.

Indicative envelope (all CONCEPT_TARGET, both sheets agree after the 2026-10-31 regeneration unless noted):

| Item | Value |
|---|---|
| Overall height | 550 mm |
| Overall width, arm to arm | 800 mm |
| Shoulder-to-shoulder spacing | 600 mm (concept sheet only; D5 not verifiable; results that depend on it are valid only for the D5 case) |
| Torso W × D | 300 mm × 250 mm (300 mm is the torso width; torso height is a separate 300 mm intern assumption, MASS_BUDGET M2) |
| Base W × D | 300 mm × 250 mm |
| Arm reach, each side | 350 mm (shoulder to gripper) |
| Target weight | 8 – 12 kg (est., no stated basis) |

## 2. Mechanical Breakdown

| Assembly / subsystem | Function | Configuration | Status |
|---|---|---|---|
| Main structure | Carries the torso, arms and head; houses electronics | Fixed base plate (aluminium or steel) under a humanoid torso with a central electronics bay; the cross-section labels the torso frame as aluminium and shows front and side sections **[Sheet]** | Illustrative; materials are options, not selections |
| Joints / arms | Position the gripper in front of the torso | Two arms, left and right, symmetric. Per arm: shoulder yaw, shoulder pitch, elbow pitch, wrist pitch. Links in aluminium (CNC machined or 3D printed), composite options named on the concept sheet **[Sheet]** | Illustrative |
| Joint assemblies | Drive and sense each joint | Housing (aluminium or CNC), BLDC/PMSM motor, harmonic or planetary gearbox, output shaft with absolute or incremental encoder, timing belt where used; modular joints with common mounting interfaces **[Sheet]** | Illustrative; motor, ratio and S/M/L assignment TBD |
| End effector | Grasp objects | Two-finger parallel linkage on a gripper mount; optional servo or BLDC; optional force sensor; rubber or TPU finger pads **[Sheet]** | Illustrative; actuation type and count TBD |
| Head | Camera and sensor mount | Optional one-axis pan head (BLDC and gearbox) carrying an RGB-D or stereo camera on a neck mount in aluminium or CNC **[Sheet]** | Optional; fitting is an open owner decision (OQ-007, CREQ-004); the D6 count was resolved 2026-10-31 |
| Base / torso | Fixed foundation and electronics enclosure | 300 mm × 250 mm base plate and torso; Kritva Edge, power distribution and driver stacks inside the torso **[Sheet]** | Illustrative; packaging not assessed |
| Mounting and interfaces | Mount arms, head and electronics; carry loads to base | Arms on shoulder mounts at the torso; common joint mounting interfaces; no fastener, bearing or load-path detail on the sheets | TBD |

## 3. DOF and Joint Arrangement

| Joint / mechanism | Count | DOF | Motion / range | Notes |
|---|---:|---:|---|---|
| Shoulder yaw | 2 (1 per arm) | 2 | Yaw / rotation about the shoulder; range TBD | Baseline; BLDC/PMSM with gearbox **[Sheet]** |
| Shoulder pitch | 2 (1 per arm) | 2 | Pitch; range TBD | Baseline; second shoulder axis added over DA-01. Axis intersection or offset with yaw is UNKNOWN |
| Elbow | 2 (1 per arm) | 2 | Pitch; range TBD | Baseline |
| Wrist | 2 (1 per arm) | 2 | Pitch; range TBD | Baseline; no wrist yaw or roll, so orientation authority is limited |
| Gripper | 2 (1 per arm) | 0 (counted separately) | Parallel two-finger open and close | Optional servo or BLDC, may be passive; count TBD |
| Head pan | 1 (optional) | 1 | Pan about the vertical axis; range TBD | Optional; one-axis only |
| **Total** | 8 baseline arm actuators | **8 DOF** (9 with head pan fitted) | | D6 resolved 2026-10-31: baseline 8, 9 when head is fitted; whether the head is fitted stays open (OQ-007) |

Joint names and DOF are as labelled on the sheets. Axis directions (vertical yaw, horizontal parallel pitch axes) are ASSUMED, not read from the sheets and not inferred from rendered motor orientation (`MECHANICAL_ANALYSIS.md` S1).

## 4. Interfaces and Packaging

- **Kritva Edge reservation:** Board shown in the torso electronics enclosure **[Sheet]**. Board dimensions and mounting TBD. Fit inside a 300 mm × 250 mm torso with drivers and power distribution is **not assessed**.
- **Power distribution:** Board inside the enclosure, 24 V DC in with 5 V and 12 V rails **[Sheet]**. The 24 V is a concept-level indication, not a confirmed electrical interface. Electrical requirements TBD.
- **Sensors and mounting:** Head camera (RGB-D or stereo) on the neck mount and an IMU on the torso; IMU mounting space mentioned on the concept sheet **[Sheet]**. Sensor selection TBD.
- **Actuator/controller interfaces:** Left-arm and right-arm motor-driver stacks inside the torso **[Sheet]**. Driver selection, motor-to-driver interface and encoder interface TBD. Camera interface shown as USB / MIPI **[Sheet]**; full interface list TBD (`INTERFACES.md`).
- **EtherCAT-related provisions:** Not shown on either sheet. TBD. Do not infer a fieldbus from the driver stacks.
- **Cable routing and service access:** Routes as labelled on the cross-section **[Sheet]**: left-arm and right-arm cables pass through the shoulders; cables run through the arm links to the wrist and gripper; routing runs through the torso and, through the neck, to the head camera. No harness design is implied. Service access (panels, drive swap, connector access) is not shown. TBD.

## 5. Architecture Assumptions and Risks

**Assumptions**
- **[Assumed]** Link split of the 350 mm reach is 175 mm upper arm, 100 mm forearm and 75 mm wrist to gripper tip (ACTUATOR_ANALYSIS A3). The sheets print only the total reach.
- **[Assumed]** Shoulder yaw and pitch axes intersect with no offset (ACTUATOR_ANALYSIS A11).
- **[Assumed]** Baseline study configuration is the 8-actuator arm set, with head pan and powered grippers treated as optional until the owner decides.
- **[Assumed]** The two arms are mirror images and share one joint design, so one analysis covers both.

**Unknowns**
- Joint ranges, workspace, arm overlap and singularities.
- Shoulder-to-shoulder spacing (D5): 600 mm appears on the concept sheet only; head and torso packaging stay UNKNOWN until the owner decides.
- Whether the head pan is fitted (D6 count resolved 2026-10-31; fitting open, OQ-007), and whether grippers are powered (README open decisions).
- Joint to S/M/L actuator mapping (not started).
- Mass by subsystem; the printed 8 – 12 kg has no stated basis.
- Load path from shoulders through torso to base plate; fastening of the base plate to a surface.
- Stale wording in the README: Section 8 and Section 9 item 6 still refer to a "mast" ("through the neck" and "an adjustable mast"), but D3 was resolved with the cross-section now showing a head camera, not a mast. Treat the mast references as stale until the owner confirms.

**Architecture risks**
1. *Torso packaging.* Kritva Edge, two driver stacks, power distribution and an optional fan in 300 mm × 250 mm is not checked. Highest packaging risk.
2. *Shoulder arrangement.* Two serial shoulder axes per side add mass at the shoulder, raise the load on the shoulder pitch joint (2.64 N·m holding in the preliminary estimate, ACTUATOR_ANALYSIS) and make the workspace and singularities dependent on the unknown axis offset.
3. *Cable routing.* Four joints per arm with two at the shoulder make bend, twist and pinch more severe than DA-01; the head pan adds a rotating cable path. Eight arm joints plus the head are routed through a small torso.
4. *Stability and base loading.* 8 – 12 kg on a fixed 300 mm × 250 mm base plate with arms extended to 350 mm is not calculated; tipping margin and base fixing are open.
5. *Limited wrist.* A single wrist pitch limits end-effector orientation; the pick-and-place capability printed on the sheet is not verified against this.
6. *Printed targets.* Weight and payload (0.1 – 0.2 kg) have no stated basis, so any architecture decision based on them is provisional.

**Alternatives considered**
- Within the study, only the printed options are recorded: aluminium or steel base plate; machined or 3D-printed aluminium links, with composite options; harmonic or planetary gearbox; absolute or incremental encoder; powered or passive gripper; head fitted or not. None is selected.
- Neighbouring concepts (DA-01 tabletop dual-arm, and the 5-DOF and mobile variants) are referenced by the sheets as the future path only; no comparison has been done in this document. TBD.

## 6. References and Evidence

| Ref | Item | Evidence type | Notes |
|---|---|---|---|
| R1 | `docs/images/KMECH-CONCEPT-DA-02.png` | C (concept artwork, L0) | Primary configuration reference; indicative, not to scale |
| R2 | `docs/images/KMECH-CROSS-SECTION-DA-02.png` | C (concept artwork, L0) | Illustrative internal arrangement; regenerated 2026-10-31 |
| R3 | `docs/images/ARTWORK_MANIFEST.json` | Record | Both sheets marked REVIEWED; this is not design approval |
| R4 | `README.md` v0.3.1 | Summary of R1 and R2 | Source for all **[Sheet]** items above; discrepancies D1–D4 and D6 resolved, D5 not verifiable |
| R5 | `ACTUATOR_ANALYSIS.md` v0.2.0 (CALC-DA02-01) | C (paper calculation) | Source for the **[Assumed]** link split and the preliminary torque estimate; all values estimates |

No architecture sketches have been filed yet. Planned in `sketches/`: torso layout with Kritva Edge, drivers and power distribution; four-axis arm kinematic sketch with frames; cable path through each shoulder, joint and the neck.

## 7. HOLD D-003

Architecture documentation and conceptual sketches only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
