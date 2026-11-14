# DA-01 — Preliminary Interface Register (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Purpose and boundary

This is a concept-level interface inventory. It is not an interface-control document, dimensional drawing, wiring schematic, connector pinout or approval of actuator mounting. The electrical, compute, sensing and software repositories/owners retain their own authority. Mechanical work only identifies robot-side provisions.

## 2. Interface register

| Interface / block | Preliminary description | Evidence source | Dimensions / specification | Status |
|---|---|---|---|---|
| Primary body / base | Fixed base plate to tabletop/support; central enclosure to base plate; shoulder module to central body; shoulder/elbow/wrist modules to arm links; distal wrist to optional gripper mount; optional mast mount to body; internal compute/power/driver mounting; left/right arm harness paths. Artwork labels USB, Ethernet and power cabling on the mast but no fieldbus. Preserve EtherCAT as a platform architecture direction where relevant, without inventing a DA-01 fieldbus implementation. | Concept artwork / README | TBD | PROPOSED; no released interface |
| Actuator to link / body | Modular rotary actuator with gearbox/output shaft/encoder shown; exact robot-side mounting geometry, datum, fastener pattern, clearance and load limits not supplied. | Concept README; actuator repository required | TBD | BLOCKED pending source-revision-controlled actuator interface |
| Kritva Edge / compute | Conceptual space reservation where shown; board outline, hole locations, connector positions, heat and mass not supplied. | Concept artwork and platform direction | TBD | PROPOSED reservation only |
| Power distribution / protection | 24 V input and 5 V / 12 V rails appear in artwork; these are not an approved electrical specification. | Cross-section artwork | TBD | CONCEPT_TARGET only |
| Motor controllers | Left/right arm driver groups, four-leg driver stack or arm/base driver blocks as shown per concept. | Cross-section artwork | TBD | Controller model and mounting TBD |
| Sensors / mounts | Optional powered grippers: one separate open/close channel per gripper (up to two additional channels if both are powered); not in baseline six. Optional camera mast / RGB-D or stereo camera; concept sheet also mentions IMU space. Camera mast adjustability appears on cross-section only. | Concept artwork / README | TBD | OWNER_DECISION where configuration differs |
| Communication / harness | Arm harnesses pass through shoulders, arm links and joints to wrist/gripper. Base routing passes through the base plate. Optional camera mast carries USB/Ethernet/power. Check bending, twist, pinch, service access and strain relief; no harness dimensions are supplied. | Cross-section artwork / platform direction | TBD | No harness/electrical design |
| Service access | Access to joint fasteners, encoder/connectors, controller/power blocks and replaceable end-effector/foot elements must be considered. | Design-guideline requirement FREQ-017 | TBD | No dimensions or service sequence defined |

## 3. Concept-specific mechanical interfaces

Fixed base plate to tabletop/support; central enclosure to base plate; shoulder module to central body; shoulder/elbow/wrist modules to arm links; distal wrist to optional gripper mount; optional mast mount to body; internal compute/power/driver mounting; left/right arm harness paths. Artwork labels USB, Ethernet and power cabling on the mast but no fieldbus. Preserve EtherCAT as a platform architecture direction where relevant, without inventing a DA-01 fieldbus implementation.

All interface dimensions, coordinate frames, datums, hole coordinates, tolerances, thread specifications, fastener grades, bolt preloads, bearing fits, shaft dimensions, allowable forces/moments and connector details are `TBD` or `UNKNOWN` unless explicitly shown as an indicative concept value. QR-04's 4 × M5 and 2 × Ø5 mm dowel depiction is not an approved interface.

## 4. Platform and electrical space reservations

Preserve the existing Kritva architecture directions:
- Kritva Core: Linux / PREEMPT_RT.
- Kritva Nexus: high-performance computing.
- Kritva Edge: real-time control.
- Kritva Sense: sensor integration.
- Kritva Motion: motion control.
- Kritva Sim: simulation.
- EtherCAT communication architecture.
- BLDC/PMSM modular rotary actuator, Option C mechanical direction, S/M/L actuator family.

The artwork's 24 V DC and 5 V / 12 V rails are concept-level indications only. Do not invent board dimensions, connectors, thermal limits, wiring gauges, cable bend radius, power budgets or communication wiring. Record `TBD` until the relevant owner supplies versioned data.

## 5. Serviceability and cable routing

Arm harnesses pass through shoulders, arm links and joints to wrist/gripper. Base routing passes through the base plate. Optional camera mast carries USB/Ethernet/power. Check bending, twist, pinch, service access and strain relief; no harness dimensions are supplied.

Check service access for fasteners, actuators, encoders, motor drivers, connectors, battery only where documented, sensors, feet/grippers and removable panels. No tool clearances or service procedures are defined in Week 2.

## 6. Interface data required before detailed design

1. Owning actuator repository and exact source commit/revision.
2. Actuator envelope, mounting datums/pattern, fastener definition, shaft/output geometry, allowable loads/moments, mass, cable exit and service access.
3. Controller, compute, sensor and power-block envelope drawings with owner/revision.
4. Harness connector, bend/twist, strain relief, abrasion and thermal limits.
5. Owner disposition of concept-only or disputed interface features.
