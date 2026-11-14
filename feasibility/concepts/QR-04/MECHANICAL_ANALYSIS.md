# QR-04 — Preliminary Mechanical Assessment (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Configuration and mechanical boundary

Four symmetric long-leg assemblies on a central rigid body; three joints per leg: hip abduction/adduction, hip flexion/extension and knee flexion/extension. Baseline is 12 actuators. No ankle or foot actuator is in the current baseline. Feet are conceptually rubber/PU or interchangeable rubber/TPU; optional top RGB-D/IMU sensor module is height adjustable in the cross-section only. The cross-section also shows an indicative 4 × M5 / 2 × Ø5 mm dowel body mounting interface that requires owner review.

## 2. Load path and structural assembly

Primary load path: body/chassis → hip joint → thigh link → knee joint → lower-leg link → foot pad → ground. Assess leg workspace, foot placement, ground/body clearance, stance support polygon, static stability, dynamic stability concerns for trotting/gait, ground impact/contact, joint loads and long-link bending/inertia. The cross-section's indicative body mount is not an approved mechanical interface. No gait/stability/strength result is demonstrated.

Material/process options from the existing README/artwork: Artwork shows rigid body in aluminium or carbon; long legs with hip/thigh/lower-leg links; joint housings aluminium/CNC; BLDC/PMSM with harmonic/planetary gearbox and absolute/incremental encoder; rubber/PU foot pad. Carbon/aluminium link options are illustrative only. No grade, layup, process, supplier or selection.

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

Long-leg swept workspace; stance and support polygon; trotting support assumptions; foot contact/friction/impact; ground clearance; body clearance; leg inertia and flexural stiffness; hip/knee joint housing stiffness; adjustable sensor and indicative body-mount packaging; long harness flex-fatigue.

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
