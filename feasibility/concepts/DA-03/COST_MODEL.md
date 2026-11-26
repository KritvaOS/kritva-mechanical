# DA-03 — Preliminary Hardware Cost Model

| Property | Value |
|---|---|
| Document ID | KMECH-COST-DA-03 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Preliminary Cost Model |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary cost assessment; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MASS_BUDGET.md`, `ACTUATOR_ANALYSIS.md`, `feasibility/EVALUATION_CRITERIA.md` |

This version lists the hardware categories and their scope only. No cost values have been entered, and no cost summary has been prepared.

## 1. Cost Basis

- Concept ID/name: DA-03 — Mobile Dual-Arm
- Cost boundary: Hardware only, baseline configuration (6 arm actuators, 2 wheel drive channels, battery, no camera or LiDAR). Optional items are listed separately.
- Currency: INR
- Estimate basis and date: Scope taken from `README.md` v0.3.1, `ARCHITECTURE.md` v0.2.0, `MASS_BUDGET.md` v0.2.0 and `ACTUATOR_ANALYSIS.md` v0.2.0, as of 2026-11-25. Cost values are not yet estimated.

## 2. Cost Categories

| Category | Quantity / scope | Cost (INR) | Evidence label | Basis / source | Status |
|---|---|---|---|---|---|
| Structure and materials | Base frame (1); torso frame and panels (1); sensor mast (1); shoulder mounts (2) | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` §2; `MASS_BUDGET.md` M1 – M4. Aluminium or steel is an open option | Not estimated |
| Actuators and gearboxes | 6 arm joint modules (shoulder yaw 2, elbow 2, wrist 2); 2 wheel drive motors with optional gearbox. S/M/L not mapped | UNKNOWN | UNKNOWN | `ACTUATOR_ANALYSIS.md`; no `kritva-actuator` data supplied | Not estimated |
| Controllers and drives | Kritva Edge (1); motor drivers (2 drive, 6 arm, if not integrated in the modules) | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` §4; Edge cost basis and driver selection TBD | Not estimated |
| Power components | 24 V Li-ion battery pack (1) with protection; power distribution board (1); fuses, emergency stop and connectors | UNKNOWN | UNKNOWN | `README.md` §7; battery capacity, protection and charging TBD | Not estimated |
| Sensors and cabling | IMU (1); harness for base, torso and two arms | UNKNOWN | UNKNOWN | `README.md` §7 and §8; sensor selection TBD | Not estimated |
| Mechanical components | Arm links (4); gripper mechanisms without actuator (2); wheels with tyres (4); hubs, axles, bearings, belts, couplings | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` §2; `MASS_BUDGET.md` M5, M7, M8 | Not estimated |
| Other hardware | Fasteners, connectors, labels, thermal parts | UNKNOWN | UNKNOWN | `MASS_BUDGET.md` M12 | Not estimated |

### 2.1 Optional items (not in the baseline scope)

| Category | Quantity / scope | Cost (INR) | Evidence label | Basis / source | Status |
|---|---|---|---|---|---|
| Gripper actuation | 2 servos or small actuators, only if powered | UNKNOWN | UNKNOWN | `README.md` §16 | Not estimated |
| Camera | RGB-D or stereo camera on the mast (1) | UNKNOWN | UNKNOWN | `README.md` §5 | Not estimated |
| LiDAR | 1 unit, only if added to the baseline (D4) | UNKNOWN | UNKNOWN | `README.md` §10 D4 | Not estimated |
| Battery charger | Scope TBD; charging not specified | UNKNOWN | UNKNOWN | `README.md` §9 | Not estimated |

### 2.2 Actuator count by option

Counts only; no cost values. Baseline is 8 actuators: 6 arm joint modules and 2 wheel drive channels (`README.md` §10 D2). Powered grippers would add 2 actuators (one per arm); a passive gripper adds none. The camera, LiDAR and charger add no actuators. Whether grippers are powered is an open owner decision (`README.md` §16).

| Option | Arm actuators | Wheel drive channels | Gripper actuators | Total actuators |
|---|---:|---:|---:|---:|
| Baseline: passive grippers | 6 | 2 | 0 | 8 |
| Powered grippers | 6 | 2 | 2 | 10 |

## 3. Boundary and Exclusions

Outside the hardware boundary: taxes, shipping and import duty; tooling, fabrication jigs and test equipment; engineering and labour; software and licences; spares and rework; payload objects; any docking station.

## 4. Evidence Rules

Values are labelled `ESTIMATE` or `UNKNOWN`. All cost values in this document are currently `UNKNOWN`. No supplier prices have been invented or presented as quotations.

## 5. HOLD D-003

No supplier quotations, purchase commitments, procurement or spending are authorized. Cost modelling is paper-based only. Any next activity requires explicit owner decision under HOLD D-003.
