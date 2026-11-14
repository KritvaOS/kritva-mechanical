# QR-02 — Preliminary Mechanical Assessment (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Configuration and mechanical boundary

Four-legged robot with a central rigid/modular body and four symmetric three-joint legs. Each leg has hip abduction/adduction, hip flexion/extension and knee flexion/extension. Each leg ends in a replaceable foot pad; alternative feet and optional force-sensing/damping are not baseline selections. A top sensor module is optional. The concept sheet describes optional IMU/cameras; cross-section details differ and remain open.

## 2. Load path and structural assembly

Primary load path: body/chassis → hip module → thigh/link → knee module → lower-leg link → foot pad → ground. Evaluate four-leg support geometry, stance and lifted-leg cases, foot placement, support polygon, ground contact/traction/impact, body/ground clearance, leg workspace and joint range, link/joint stiffness and service access. A static margin or gait claim cannot be made because centre of mass, leg lengths, joint limits, contact/friction and stride are not specified.

Material/process options from the existing README/artwork: Artwork shows central chassis in aluminium or carbon; hip/thigh/lower-leg links in aluminium (CNC) or 3D printed, with composite options named on concept sheet; joint housings in aluminium/CNC; harmonic or planetary gearbox; absolute or incremental encoder; rubber/TPU feet, optional force sensor and elastomer damper. All are illustrative options.

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

Leg workspace and reachable foot region; support polygon for relevant support sets; foot placement and contact; ground/body clearance; leg link bending/torsion; joint housing stiffness; footpad traction/impact; hip cable twist and internal channel; body battery/compute thermal access.

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
