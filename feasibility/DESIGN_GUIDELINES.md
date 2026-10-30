# Design Guidelines

| Property | Value |
|---|---|
| Document ID | KMECH-FS-003 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Mechanical Feasibility Design Guidelines |
| Status | PROPOSED |
| Owner | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Proposed engineering guidance; subject to owner direction |
| Related Documents | `feasibility/README.md`, `feasibility/STUDY_PLAN.md`, `feasibility/INTERN_ASSIGNMENTS.md`, `feasibility/EVALUATION_CRITERIA.md`, `feasibility/REQUIREMENTS_REGISTER.md`, `feasibility/RISK_REGISTER.md` |

## 1. Purpose and Scope

These guidelines establish common engineering, documentation and repository practices for the Kritva mechanical feasibility study.

The current activity is limited to paper-based research, preliminary engineering analysis, calculations, sketches and documentation. Mechanical HOLD D-003 remains in force. These guidelines do not authorize detailed design or implementation.

## 2. Common Engineering Constraints

### 2.1 Electrical and Actuator Direction

- Use **24V DC** only as an investigation direction for preliminary actuator and power-system compatibility.
- Do not treat 24V as a finalized system voltage or approved electrical specification.
- Preserve the existing **BLDC/PMSM modular rotary actuator** direction.
- Preserve the existing Option C actuator mechanical direction.
- Retain the actuator S/M/L architecture.
- Derive joint-specific actuator requirements from each concept's loads, geometry, duty cycle and motion requirements.
- Do not copy the elbow actuator reference values directly to other joints.

The existing elbow reference (24V, 10 N·m continuous and 20 N·m peak) is a reference for that elbow discussion only. It is not a universal arm or leg actuator specification.

### 2.2 S/M/L Actuator Mapping

For every joint requiring actuator assessment:

- Identify the joint function and mechanical loading.
- Estimate or calculate continuous and peak torque requirements where inputs permit.
- Identify required speed, range of motion and duty-cycle assumptions.
- Assess candidate S/M/L compatibility against derived requirements.
- Record margins, limitations and missing data.

S/M/L mapping is an engineering assessment, not an assumption based on joint name or the elbow reference. If data is insufficient, mark the mapping `TBD`.

### 2.3 Materials and Manufacturing

Materials and manufacturing processes may be investigated as options only.

Potential categories for research include:
- Aluminium alloys, steel and other suitable engineering metals.
- Engineering polymers and composite materials.
- Sheet-metal fabrication, machining, extrusion and additive manufacturing.

Do not finalize material grades, manufacturing methods, suppliers or process capability. Record suitability, constraints and evidence basis. Actual manufacturability requires later engineering and supplier validation.

### 2.4 Kritva Platform Space Reservation

Concepts should identify preliminary space and interface provisions for relevant Kritva platform components:

- Kritva Edge compute and real-time control hardware.
- Power distribution and electrical protection.
- Sensor modules, wiring and sensor mounting.
- Motor controllers and actuator connections.
- Communication and cable-routing provisions, including the existing EtherCAT architecture direction where relevant.

Do not invent board dimensions, connector locations, thermal limits or cable requirements. Use `TBD` where interface data is unavailable. Space reservation in this study is conceptual, not a released packaging design.

## 3. Documentation Rules

1. Use SI units wherever practical. State units explicitly for every measured, assumed or calculated quantity.
2. Include formulas, input values, assumptions and calculation steps for engineering results.
3. Label every unsupported or preliminary value as `ESTIMATE`.
4. Distinguish sourced values from assumptions and estimates. Record source title, URL or document reference and access date where available.
5. Use `TBD` for a value or decision awaiting definition.
6. Use `UNKNOWN` when information is not currently known or available.
7. Use `BLOCKED` when progress depends on an unresolved input, approval or external dependency.
8. Use `INCOMPLETE` when a required analysis or deliverable has not been completed.
9. Never omit a required field merely because information is unavailable.
10. Record the reason and next action for each `BLOCKED` or `INCOMPLETE` item.
11. Do not present estimates as verified specifications or supplier commitments.
12. Keep conclusions proportional to the quality and completeness of the evidence.

## 4. Per-Concept Folder Standard

Each concept must use the following folder structure:

    feasibility/concepts/<ID>/
      README.md
      REQUIREMENTS.md
      ARCHITECTURE.md
      MECHANICAL_ANALYSIS.md
      ACTUATOR_ANALYSIS.md
      INTERFACES.md
      MASS_BUDGET.md
      COST_MODEL.md
      OPEN_QUESTIONS.md
      calculations/
      references/
      reviews/
      sketches/

Create the relevant files as the study progresses. Required content that is not yet available must be marked `TBD`, `UNKNOWN`, `BLOCKED` or `INCOMPLETE`; do not create empty claims of completion.

Folder purposes:

- `README.md`: concept summary, owner, complexity, status and document index.
- `REQUIREMENTS.md`: concept-specific requirements, assumptions and unknowns.
- `ARCHITECTURE.md`: configuration, DOF, joints and assembly breakdown.
- `MECHANICAL_ANALYSIS.md`: structural, stability, workspace and mechanical feasibility.
- `ACTUATOR_ANALYSIS.md`: joint requirements and S/M/L compatibility.
- `INTERFACES.md`: mechanical, electrical, sensor and platform interface provisions.
- `MASS_BUDGET.md`: mass breakdown and traceable estimates.
- `COST_MODEL.md`: preliminary cost assumptions and component categories.
- `OPEN_QUESTIONS.md`: unresolved inputs, decisions and dependencies.
- `calculations/`: calculation notes and supporting worksheets.
- `references/`: sourced reference material and source register.
- `reviews/`: concept-level review comments and dispositions.
- `sketches/`: paper sketches and conceptual illustrations.

**Do not create a `cad/` folder while HOLD D-003 is active.** Sketches must remain conceptual and must not be treated as CAD or manufacturing drawings.

## 5. Dual-Arm Concept Add-on Analyses

In addition to the common requirements, dual-arm concepts should assess:

- Base, torso or support configuration and load path.
- Arm DOF, joint arrangement and reachable workspace.
- Payload and reach requirements, or explicit `UNKNOWN` status.
- Joint torque and speed requirements based on the concept's geometry and loading.
- Base stability under representative arm extension and motion assumptions.
- Inter-arm workspace overlap, interference and collision risks.
- Gripper or end-effector interface assumptions.
- Sensor mounting, cable routing and service access.
- Space reservation for compute, power and motor-control hardware.

Mobile, rotating-platform and humanoid upper-body concepts must additionally assess their respective base, rotation, torso and head-provision interfaces.

## 6. Legged Concept Add-on Analyses

In addition to the common requirements, legged concepts should assess:

- Leg count, DOF per leg and joint arrangement.
- Body, hip and leg structural configuration.
- Ground-contact and support-polygon considerations.
- Static stability and preliminary dynamic stability concerns.
- Joint loading during representative support and movement assumptions.
- Foot geometry and ground-contact assumptions.
- Ground clearance and body clearance where relevant.
- Locomotion-related workspace and joint-range requirements.
- Sensor placement, wiring and controller space reservation.

Quadruped concepts should assess four-leg support and gait-related requirements. The hexapod should assess six-leg support configurations and their mechanical implications. Do not claim validated gait performance or dynamic stability without appropriate analysis and evidence.

## 7. Calculation Conventions

- State the engineering question and intended result before presenting a calculation.
- Identify all inputs, units, sources and assumptions.
- Show the formula and substitution of values.
- Record the result, units and interpretation.
- Identify uncertainty and sensitivity to important assumptions.
- Distinguish continuous, peak and transient loading where applicable.
- State whether a result is a calculation, estimate or sourced specification.
- Use conservative assumptions only when explicitly stated and justified.
- If inputs are insufficient, document the required inputs and mark the result `TBD`.

Calculation evidence is classified as **C**. Software evidence is **S**, simulation **Sim**, bench **B**, and physical **P**. Do not imply that a calculation is simulation, bench or physical validation.

## 8. Naming and Versioning

- Preserve concept IDs: `DA-01` through `DA-06` and `QR-01` through `QR-06`.
- Preserve complexity labels: Low, Medium and High.
- Preserve the frozen program phases `P0`–`P8` (owned by kritva-program). The study is not a program phase.
- Preserve the actuator family milestone names `A0`–`A2` (owned by kritva-actuator). Robot hardware baselines, if ever defined, use the proposed `ROB-A*` namespace; the 12 concepts are feasibility alternatives, not hardware revisions.
- Preserve actuator size classes `S`, `M` and `L`.
- Use descriptive uppercase Markdown filenames as specified in the folder standard.
- Use consistent units and terminology across concepts.
- Do not create new naming schemes or change established identifiers without owner direction.

## 9. Prohibited Activities Under HOLD D-003

Until an explicit owner decision changes the hold, interns must not:

- Create CAD models, detailed CAD assemblies or production drawings.
- Finalize a BOM or release component selections.
- Request or represent supplier quotations as approved costs.
- Procure, order or commit funds for components or services.
- Fabricate, machine, print, assemble or modify physical hardware.
- Conduct bench tests, actuator tests or physical experiments.
- Claim mechanical, electrical, safety or locomotion validation.
- Change approved platform or actuator architecture directions.

Any proposed next-stage activity must be documented as a recommendation and submitted for owner decision. Completion of this feasibility study or its checkpoints does not release HOLD D-003.
