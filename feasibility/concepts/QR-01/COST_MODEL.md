# QR-01 — Preliminary Hardware Cost Model

| Property | Value |
|---|---|
| Document ID | KMECH-COST-QR-01 |
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

- Concept ID/name: QR-01 — Compact Quadruped
- Cost boundary: Hardware only, baseline configuration (8 actuators, battery, IMU, no top camera module or LiDAR). Optional items are listed separately.
- Currency: INR
- Estimate basis and date: Scope taken from `README.md` v0.3.0, `ARCHITECTURE.md` v0.2.0, `MASS_BUDGET.md` v0.2.0 and `ACTUATOR_ANALYSIS.md` v0.2.0, as of 2026-11-25. Cost values are not yet estimated.

## 2. Cost Categories

| Category | Quantity / scope | Cost (INR) | Evidence label | Basis / source | Status |
|---|---|---|---|---|---|
| Structure and materials | Body chassis (1); hip mounts (4) | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` §2; `MASS_BUDGET.md` M1, M2. Aluminium or carbon is an open option | Not estimated |
| Actuators and gearboxes | 8 joint modules (hip 4, knee 4). S/M/L not mapped | UNKNOWN | UNKNOWN | `ACTUATOR_ANALYSIS.md`; no `kritva-actuator` data supplied | Not estimated |
| Controllers and drives | Kritva Edge (1); motor drivers (8, if not integrated in the modules) | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` §4; Edge cost basis and driver selection TBD | Not estimated |
| Power components | 24 V Li-ion battery pack (1) with protection; power distribution board (1); connectors | UNKNOWN | UNKNOWN | `README.md` §7; battery capacity, protection and charging TBD | Not estimated |
| Sensors and cabling | IMU (1); harness through the hips and legs | UNKNOWN | UNKNOWN | `README.md` §7 and §8; sensor baseline open (D6) | Not estimated |
| Mechanical components | Leg links (8: thigh and shank for 4 legs); foot pads (4); bearings and fasteners | UNKNOWN | UNKNOWN | `ARCHITECTURE.md` §2; `MASS_BUDGET.md` M3 | Not estimated |
| Other hardware | Fasteners, connectors, labels, cooling parts if added | UNKNOWN | UNKNOWN | `MASS_BUDGET.md` M9; cooling not drawn | Not estimated |

### 2.1 Optional items (not in the baseline scope)

| Category | Quantity / scope | Cost (INR) | Evidence label | Basis / source | Status |
|---|---|---|---|---|---|
| Top sensor module | Camera or depth camera on a fixed mount (1) | UNKNOWN | UNKNOWN | `README.md` §5 | Not estimated |
| LiDAR | 1 unit, only if added to the baseline (D6) | UNKNOWN | UNKNOWN | `README.md` §10 D6 | Not estimated |
| Foot sensing and damping | Foot force sensors and elastomer dampers (4 each) | UNKNOWN | UNKNOWN | `README.md` §5 | Not estimated |
| Battery charger | Scope TBD; charging not specified | UNKNOWN | UNKNOWN | `README.md` §7 | Not estimated |

### 2.2 Actuator count by option

Counts only; no cost values. The baseline is 8 actuators (hip and knee on each of 4 legs, `README.md` §10 D1). None of the optional items below adds an actuator: the top sensor module, LiDAR, foot sensing and damping, and charger are sensors, passive parts or accessories. The total is 8 in every option.

## 3. Boundary and Exclusions

Outside the hardware boundary: taxes, shipping and import duty; tooling, fabrication jigs and test equipment; engineering and labour; software and licences; spares and rework; payload objects.

## 4. Evidence Rules

Values are labelled `ESTIMATE` or `UNKNOWN`. All cost values in this document are currently `UNKNOWN`. No supplier prices have been invented or presented as quotations.

## 5. HOLD D-003

No supplier quotations, purchase commitments, procurement or spending are authorized. Cost modelling is paper-based only. Any next activity requires explicit owner decision under HOLD D-003.
