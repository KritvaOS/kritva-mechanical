# QR-01 — Mechanical Architecture

| Property | Value |
|---|---|
| Document ID | KMECH-ARCH-QR-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Architecture |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.0 |
| Last Updated | 2026-11-25 |
| Authority | Preliminary architecture assessment; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md` |

Tags: **[Sheet]** printed on the artwork (CONCEPT_TARGET or illustrative, unapproved); **[Assumed]** intern assumption; **TBD** not given. The artwork is concept art (evidence C, L0), not CAD.

## 1. Configuration

- Concept ID/name: QR-01 — Compact Quadruped
- Mechanical family: Legged
- Overall configuration: Rigid central body with four symmetric two-joint planar legs (hip and knee flexion/extension), foot pads, an electronics bay for Kritva Edge and power distribution, and an optional top sensor module. **[Sheet]**
- Complexity: Low (relative category, not a validated assessment): the simplest legged concept. **[Sheet]**
- Intended demonstration: Kritva platform; standing, sitting, slow walking, basic locomotion, flat indoor and outdoor terrain. **[Sheet]**

| Item (CONCEPT_TARGET) | Value |
|---|---|
| Body L × W × H | 300 mm × 250 mm × 200 mm |
| Overall L × W (with leg extension) | 420 mm × 400 mm |
| Target weight | 2.5 – 4 kg (est., concept sheet only: D4) |
| Target payload | 0.3 – 0.8 kg (est., concept sheet only: D4) |

## 2. Mechanical Breakdown

| Assembly / subsystem | Function | Configuration | Status |
|---|---|---|---|
| Main structure | Carry legs, electronics and battery | Rigid chassis in aluminium or carbon with an electronics bay **[Sheet]** | Illustrative; panel thickness TBD |
| Joints / legs | Stand, sit and walk | Four symmetric legs (front-left, front-right, rear-left, rear-right), each with hip and knee in one plane; thigh and lower-leg links in aluminium (CNC) or 3D printed **[Sheet]** | Illustrative; link lengths not printed |
| Joint assemblies | Drive and sense each joint | Housing (aluminium or CNC), BLDC/PMSM motor, harmonic or planetary gearbox, output shaft with absolute or incremental encoder **[Sheet]** | Illustrative; S/M/L not mapped |
| Feet | Ground contact | Replaceable rubber or TPU pad; optional force sensor and elastomer damper (cross-section); spike or custom feet (concept) **[Sheet]** | Illustrative |
| Hip mounts | Place leg planes outboard of the body | Not shown. Overall width 400 mm against a 250 mm body implies the leg planes sit outboard **[Assumed]** | TBD |
| Top sensor module | Carry sensors | Fixed mount, optional camera / depth camera; IMU and LiDAR on the concept sheet only **[Sheet]** | Optional (D6) |
| Mounting and interfaces | Mount legs, battery, electronics | Not detailed on the sheets | TBD |

## 3. DOF and Joint Arrangement

| Joint / mechanism | Count | DOF | Motion / range | Notes |
|---|---:|---:|---|---|
| Hip | 4 (1 per leg) | 4 | Flexion / extension; range TBD | Baseline; BLDC/PMSM with gearbox |
| Knee | 4 (1 per leg) | 4 | Flexion / extension; range TBD | Baseline; BLDC/PMSM with gearbox |
| Foot pad | 4 | 0 | Passive | Optional force sensor and damper |
| **Total** | 8 actuators | **8 DOF** | | D1 resolved: 2 DOF per leg, no abduction |

Axis directions are taken from sheet labels. All four legs move in parallel planes, so the body cannot be shifted or stepped sideways relative to the feet.

## 4. Interfaces and Packaging

- **Kritva Edge reservation:** In the central body **[Sheet]**; dimensions TBD; fit not assessed.
- **Power distribution:** 24 V in with 5 V and 12 V rails **[Sheet]**. 24 V is a concept-level indication, not a confirmed interface. A battery space is mentioned on the concept sheet but no battery is drawn on the cross-section; capacity, placement, protection and charging TBD.
- **Sensors and mounting:** Optional top module with RGB-D or stereo camera (cross-section); IMU and optional LiDAR on the concept sheet only (D6).
- **Actuator/controller interfaces:** Motor driver stack for four legs **[Sheet]**; driver selection TBD; whether S/M/L modules integrate drivers UNKNOWN.
- **EtherCAT-related provisions:** Not shown on either sheet. TBD.
- **Cable routing and service access:** Cables run through the leg links to each joint and through body channels **[Sheet]**. Every leg joint moves relative to the body, so hip and knee cables see repeated bend; the earlier README mentions "twist with an abduction hip", which no longer applies (stale, D1). Service access not shown. TBD.
- **Cooling:** Not drawn; thermal design UNKNOWN.
- **Emergency stop:** Not shown on either sheet. TBD.

## 5. Architecture Assumptions and Risks

**Assumptions [Assumed]**
- Thigh 130 mm and shank 150 mm; knee pointing backward; hip height 220 mm standing; hips at body mid-height.
- Leg planes 190 mm either side of the centreline; hips about 120 mm from the body centre along the length; feet at ±190 mm × ±180 mm.
- Baseline excludes LiDAR, the top camera module and foot sensors until the owner decides.

**Unknowns:** weight and payload basis (D4); sensor baseline (D6); link lengths; joint ranges; battery capacity and placement; cooling; hip mount geometry; S/M/L mapping.

**Architecture risks**
1. Planar legs give no side-stepping, no lateral balance correction and awkward turning (by stride difference with foot scrub).
2. Actuators dominate the mass (about 42% of the estimate); weight target and torque demand feed each other.
3. Body packaging of Kritva Edge, eight drivers, battery and cooling in 300 mm × 250 mm × 200 mm is not checked.
4. Power-off collapse: with no holding torque the legs fold unless gearboxes resist backdriving.
5. Foot impact and traction on outdoor terrain are not assessed.
6. Printed weight and payload targets have no stated basis.

**Alternatives considered:** only printed options are recorded: aluminium or carbon chassis; CNC or printed links; harmonic or planetary gearbox; rubber, TPU, spike or custom feet; foot force sensor and damper; camera and LiDAR. None is selected. A 3-DOF leg with abduction is not part of this concept.

## 6. References and Evidence

| Ref | Item | Evidence type |
|---|---|---|
| R1 | `docs/images/KMECH-CONCEPT-QR-01.png` | C (concept artwork, L0) |
| R2 | `docs/images/KMECH-CROSS-SECTION-QR-01.png` | C (concept artwork, L0) |
| R3 | `docs/images/ARTWORK_MANIFEST.json` (both sheets REVIEWED; not design approval) | Record |
| R4 | `README.md` v0.3.0 | Summary of R1, R2 |
| R5 | `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `MECHANICAL_ANALYSIS.md` | C (paper calculations) |

Planned sketches in `sketches/`: leg kinematic sketch; body layout for battery, Edge and drivers; cable path through hips and legs.

## 7. HOLD D-003

Architecture documentation and conceptual sketches only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
