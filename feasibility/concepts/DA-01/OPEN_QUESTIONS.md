# DA-01 — Open Questions and Decisions (Week 3)

**Status:** PROPOSED | Version 0.3.0 | 2026-11-27 | INTERN-01

## 1. Owner decisions required

| ID | Question | Impact if unresolved | Status |
|---|---|---|---|
| D3 | Confirm or reject 300 mm torso width printed only on cross-section | Affects packaging and CoM | OWNER_DECISION |
| D4 | Confirm wrist axis: rotation, pitch, or explicit frame definition | Blocks ROM, cable routing, torque direction | OWNER_DECISION |
| D5 | Confirm whether adjustable camera mast is in baseline | Affects mass, cost, cable routing | OWNER_DECISION |
| — | Passive vs powered grippers in baseline | Adds actuator channels and cost | OWNER_DECISION |

## 2. Technical unknowns blocking higher confidence

| ID | Unknown | Needed for |
|---|---|---|
| U-01 | Exact link lengths, joint offsets, axis frames | Kinematics, workspace, precise torque |
| U-02 | Joint ROM limits | Workspace, collision, duty |
| U-03 | Source-controlled S/M/L mass, torque, speed, price, envelope | EC-02 scoring, final cost, packaging |
| U-04 | Material grades, wall thicknesses, fastener classes | Stress, deflection, mass confidence |
| U-05 | Tabletop support condition (clamp, friction, allowable tip margin) | Stability claim |
| U-06 | Cable drag / friction contribution to joint torque | Continuous rating margin |

## 3. Risks (qualitative ESTIMATE)

| Risk | Likelihood | Impact | Mitigation direction |
|---|---|---|---|
| Wrist axis ambiguity leads to rework | Med | Med | Owner decision before detailed kinematics |
| Actuator cost higher than low-end estimate | Med | High | Early S/M/L data request |
| Tabletop tipping under dual-arm extension | Low–Med | Med | Specify positive clamping in next revision |
| Printed mass target not met | Low | Low | Target is CONCEPT_TARGET only |

## 4. Calculation and evidence status

- CALC-DA01-01 joint torque: drafted, ESTIMATE.
- Mass and cost ranges: drafted, ESTIMATE.
- Full multi-body dynamic model: NOT STARTED (requires U-01).
- S/M/L comparison table: BLOCKED on U-03.
