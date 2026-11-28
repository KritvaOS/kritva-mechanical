# QR-02 — Joint and Actuator Requirements (Week 3 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-QR-02 |
| Status | PROPOSED — Week 3 paper calculation |
| Version | 0.3.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 |

**HOLD D-003 active.** S/M/L mapping and actuator selection remain TBD.

## 1. Configuration

Standard Quadruped: 4 legs × 3 DOF (hip abduction/adduction or yaw, hip flexion, knee flexion) = 12 actuators. Body 350 × 260 × 250 mm (CONCEPT_TARGET). Target mass 4–7 kg (est.), payload not separately printed.

## 2. Planning assumptions (ASSUMED)

| ID | Assumption | Value |
|---|---|---|
| A1 | Gravity | 9.81 m/s² |
| A2 | Robot mass (nominal for load share) | 5.5 kg |
| A3 | Static standing on 4 legs, equal share | 13.5 N per leg vertical |
| A4 | Single-leg support (worst static) | 54 N vertical |
| A5 | Leg length (hip to foot, extended) | 220 mm (scaled from body height + leg geometry) |
| A6 | Hip-to-knee / knee-to-foot split | 110 mm / 110 mm |
| A7 | Hip module mass | 0.25 kg |
| A8 | Knee module mass | 0.22 kg |
| A9 | Link masses | 0.08 kg each segment |
| A10 | Planning factor | 1.5× |
| A11 | Representative joint speed | 2 rad/s |
| A12 | Representative angular accel | 15 rad/s² |

## 3. Per-joint demand (one leg, ESTIMATE)

| Joint | Primary load case | Continuous (N·m) | Peak (N·m) | After 1.5× | S/M/L |
|---|---|---:|---:|---:|---|
| Hip abduction / yaw | Lateral shift / turning | ≈ 1.2 | ≈ 2.0 | ≈ 3.0 | TBD |
| Hip flexion | Single-leg support, body lift | ≈ 3.8 | ≈ 5.5 | ≈ 8.3 | TBD |
| Knee flexion | Single-leg support | ≈ 2.1 | ≈ 3.2 | ≈ 4.8 | TBD |

Static knee/hip moments derived from vertical force × horizontal moment arm at the critical pose (leg partially flexed under body). Dynamic contribution from Iα and ground-reaction transients is included in the peak column at planning level only.

## 4. Notes

- Ground reaction and impact loads for dynamic gait remain UNKNOWN; the numbers above are quasi-static plus a modest dynamic allowance.
- Optional sensors / force feet (OWNER_DECISION) would add distal mass and may increase knee demand.
- Full calculation file: `calculations/CALC-QR02-01_leg_torque.md` (to be expanded with free-body diagrams).

## 5. Status

Week 3 torque estimates produced under explicit assumptions. S/M/L comparison blocked on actuator source data. ROM, exact axis directions and gait parameters remain TBD.
