# DA-01 — Preliminary Mechanical Assessment (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Configuration and mechanical boundary

Two symmetric 3-DOF arms mounted on opposite sides of a fixed central base/torso enclosure and base plate. The central enclosure contains the conceptual compute, power-distribution and left/right motor-driver blocks. There is no mobile base. Two-finger parallel grippers are optional and may be passive or powered; powered-gripper motion is not part of the six-actuator baseline. The cross-section shows an optional adjustable camera mast; its inclusion in the baseline is not authorized.

## 2. Load path and structural assembly

Primary load path: gripper/payload → wrist → forearm/link → elbow → upper arm/link → shoulder → central torso/base → base plate → tabletop/support. Preliminary assessment must examine extended-arm overturning/sliding, base support and stiffness, link/joint deflection, left/right workspace overlap and collision, payload/reach pose assumptions, gripper mounting, and access to the central enclosure. The README itself warns that 350 mm per-side reach, 700 mm total reach and 700 mm overall width do not describe one posture without a stated pose. Do not infer a pose or geometry.

Material/process options from the existing README/artwork: Artwork shows a base plate in aluminium or steel; central enclosure; aluminium, CNC-machined or 3D-printed arm links; aluminium/CNC joint housings; harmonic or planetary gearbox examples; absolute or incremental encoder examples; rubber/TPU gripper pads. These are illustrative options, not selected materials or manufacturing processes.

No material grade, cross-section, wall thickness, fastener class, bearing series, allowable stress, safety factor, stiffness limit or process is selected. These require traceable requirements and owner review.

## 3. Preliminary dimensions and packaging

See `ARCHITECTURE.md` section 2 for all artwork dimensions and their exact source. The concept sheets are not to scale and do not establish datums or tolerances.

Packaging elements to reserve conceptually:
- Body/base and structural members.
- Joint housings, actuators, gearboxes, output shafts and encoders.
- Compute/control (Kritva Edge where shown), motor drivers and power distribution/protection.
- Sensor modules and their mounting/wiring where applicable.
- Cable channels, strain relief and service access.
- End effectors or feet.
- Battery only where the source says a battery space exists; DA-04 battery is not drawn and its sizing is explicitly outside this study. Do not invent battery mass or envelope.

## 4. Week 2 preliminary mechanical checks

| Topic | Week 2 conclusion | Evidence / gap |
|---|---|---|
| Mechanical configuration | Identified conceptually | `ARCHITECTURE.md`, source artwork |
| Major load path | Identified qualitatively | Section 2 above |
| Joint and link layout | Listed by joint instance | `ARCHITECTURE.md`, `ACTUATOR_ANALYSIS.md` |
| Joint range / swept envelope | INCOMPLETE | Joint ranges, link lengths and coordinate frames are TBD |
| Structural stiffness / deflection | INCOMPLETE | Geometry, material properties, section sizes, loads and allowable deflection unavailable |
| Stability / support | INCOMPLETE | Support conditions, mass distribution, loads and operational poses unavailable |
| Workspace / reach / clearance | INCOMPLETE | Joint ranges, link geometry, reference pose and coordinate system unavailable |
| Interfaces | Preliminary inventory only | `INTERFACES.md`; not a released interface-control document |
| Serviceability / maintenance | Conceptual issues identified | No service door, tool clearance or maintenance interval is defined |
| Mechanical safety | Preliminary hazards recorded | Not a hazard analysis certification or safety approval |

## 5. Concept-specific assessment questions

Pose-specific reach and collision envelope; workspace overlap; base plate support and clamp/foot condition; bending stiffness of links and shoulder support; optional gripper load path; cable twist/bend at all three joints; enclosure heat rejection and access.

## 6. Week 3 calculation plan

Only after inputs become traceable:
- Define free-body diagrams and representative load cases.
- Derive joint gravity and dynamic loads for each relevant joint.
- Assess link and mount stress/deflection with sourced material properties and geometry.
- Assess stability/support with an explicit support polygon and centre-of-mass model where applicable.
- Assess reach/workspace and clearances over documented ranges of motion.
- For legged concepts, keep static standing/lifted-leg and dynamic gait/impact cases distinct.
- For mobile DA-04, distinguish drive traction/turning from arm-manipulation tipping.

## 7. Risks and limitations

See `OPEN_QUESTIONS.md`. Qualitative risk levels use the repository's Low/Med/High scale and are marked `ESTIMATE`; status remains OPEN until owner disposition. Do not report a feasibility score merely because this preliminary review exists.
