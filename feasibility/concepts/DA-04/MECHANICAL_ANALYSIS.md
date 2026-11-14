# DA-04 — Preliminary Mechanical Assessment (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Configuration and mechanical boundary

Humanoid upper torso with fixed head, mounted on a differential-drive chassis. Two arms each have four baseline DOF (shoulder yaw, shoulder pitch, elbow pitch and wrist pitch). The base has two driven channels: left wheel pair and right wheel pair, with four physical wheels shown. The approved study baseline is 10 actuators (8 arm + 2 base); head pan is excluded and grippers are optional/not counted. A printed future path to five-DOF arms and an advanced mobile base is not part of the baseline.

## 2. Load path and structural assembly

Arm load path: payload/gripper → wrist → forearm → elbow → upper arm → shoulder → torso → base chassis → wheel contact patch/floor. Base drive load path: motor/gearbox → wheel hub → tyre/contact patch. Examine tall-body/arm-extension tipping, wheel reactions, base footprint, differential traction and turn envelope, arm-arm workspace/interference, stiffness of torso/shoulder mounts and cable passage across moving chassis. Printed target 25–35 kg and 1200 mm overall height are unverified concept targets, not a stability analysis.

Material/process options from the existing README/artwork: Artwork shows differential-drive base with four wheels, left and right driven pairs, BLDC motor/encoder per side, optional gearbox, hub and rubber tyre; torso frame aluminium or carbon; arm links aluminium/CNC/3D-printed with composites as options; BLDC/PMSM joints with harmonic/planetary gearboxes, output shaft encoder and timing belt where used; rubber/TPU finger pads. No material/process selected.

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

Standing, turning and arm-manipulation load cases; wheel reactions; centre-of-mass and support polygon; tipping under forward/lateral arm extension; drive torque/traction/slope; workspace overlap; shoulder/torso stiffness; torso-to-base harness flex; head and sensor packaging.

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
