# DA-02 — Preliminary Hardware Cost Model

| Property | Value |
|---|---|
| Document ID | KMECH-COST-DA-02 |
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

- Concept ID/name: DA-02 — Humanoid Torso Dual-Arm
- Cost boundary: Hardware only, baseline configuration (8 arm actuators, fixed base plate, no head). Optional items are listed separately.
- Currency: INR
- Estimate basis and date: Scope taken from `README.md` v0.3.1, `ARCHITECTURE.md` v0.2.0, `MASS_BUDGET.md` v0.2.0 and `ACTUATOR_ANALYSIS.md` v0.2.0, as of 2026-11-25. Cost values are not yet estimated.

## 2. Cost Categories

| Category | Quantity / scope | Cost (INR) | Evidence label | Basis / source | Status |
|---|---|---:|---|---|---|
| Structure and materials | Base plate (1); torso frame and panels (1); shoulder mounts (2) | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` Section 2; `MASS_BUDGET.md` M1–M3. Aluminium or steel base plate is an open option | Not estimated |
| Actuators and gearboxes | 8 joint modules: shoulder yaw (2), shoulder pitch (2), elbow (2), wrist (2). S/M/L not mapped | UNKNOWN | UNKNOWN | `ACTUATOR_ANALYSIS.md`; no `kritva-actuator` data supplied | Not estimated |
| Controllers and drives | Kritva Edge (1); motor drivers (8, if not integrated in the joint modules) | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` Section 4; Edge cost basis and driver selection TBD | Not estimated |
| Power components | Power distribution board (1) with 24 V input and 5 V and 12 V rails; protection and connectors | UNKNOWN | UNKNOWN | `README.md` Section 7; electrical requirements TBD | Not estimated |
| Sensors and cabling | IMU (1); harness for two arms and torso | UNKNOWN | UNKNOWN | `README.md` Sections 7 and 8; sensor selection TBD | Not estimated |
| Mechanical components | Arm links (4); gripper mechanisms without actuator (2); bearings, timing belts, couplings | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` Section 2; `MASS_BUDGET.md` M4, M6 | Not estimated |
| Other hardware | Fasteners, connectors, fan, thermal parts, labels | UNKNOWN | UNKNOWN | `MASS_BUDGET.md` M10 | Not estimated |

### 2.1 Optional items (not in the baseline scope)

| Category | Quantity / scope | Cost (INR) | Evidence label | Basis / source | Status |
|---|---|---:|---|---|---|
| Gripper actuation | 2 servos or small actuators, only if grippers are powered | UNKNOWN | UNKNOWN | `README.md` Section 16 open decision 2 | Not estimated |
| Head | Pan module (1); RGB-D or stereo camera (1); neck and head mount (1) | UNKNOWN | UNKNOWN | `README.md` Section 16 open decision 1 | Not estimated |

### 2.2 Actuator count by option

Counts only; no cost values. Baseline is 8 arm actuators (D6, resolved 2026-10-31). The head adds 1 pan actuator. Powered grippers would add 2 actuators (one per arm); a passive gripper adds none. Whether the head is fitted and whether grippers are powered are open owner decisions (`README.md` Section 16).

| Option | Arm actuators | Head | Gripper actuators | Total actuators |
|---|---:|---:|---:|---:|
| Baseline: no head, passive grippers | 8 | 0 | 0 | 8 |
| Head fitted, passive grippers | 8 | 1 | 0 | 9 |
| No head, powered grippers | 8 | 0 | 2 | 10 |
| Head fitted, powered grippers | 8 | 1 | 2 | 11 |

## 3. Boundary and Exclusions

Outside the hardware boundary: taxes, shipping and import duty; the external 24 V supply, tether and any battery; fabrication jigs, tooling and test equipment; engineering and labour; software and licences; spares and rework; payload objects.

## 4. Evidence Rules

Values are labelled `ESTIMATE` or `UNKNOWN`. All cost values in this document are currently `UNKNOWN`. No supplier prices have been invented or presented as quotations.

## 5. HOLD D-003

No supplier quotations, purchase commitments, procurement or spending are authorized. Cost modelling is paper-based only. Any next activity requires explicit owner decision under HOLD D-003.
