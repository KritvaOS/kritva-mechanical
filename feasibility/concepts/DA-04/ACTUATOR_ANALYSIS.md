# DA-04 — Joint and Actuator Requirements (Week 3 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-DA-04 |
| Status | PROPOSED — Week 3 paper calculation |
| Version | 0.3.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 |

**HOLD D-003 active.**

## 1. Configuration

Humanoid Mobile Dual-Arm: two 4-DOF arms (shoulder yaw/pitch, elbow, wrist) + differential-drive base (2 wheel channels) = **10 actuators** (owner-approved baseline; head pan excluded). Overall 1200 × 1200 mm envelope (CONCEPT_TARGET). Target mass and payload still CONCEPT_TARGET / TBD in register.

## 2. Planning assumptions (ASSUMED)

| ID | Assumption | Value |
|---|---|---|
| A1 | Gravity | 9.81 m/s² |
| A2 | Arm reach (shoulder–gripper) | 400 mm (scaled from artwork) |
| A3 | Link split | 180 / 120 / 100 mm |
| A4–A8 | Link & module masses | similar to DA-01 scaled +20 % |
| A9 | Payload per arm | 0.2 kg |
| A10 | Robot mass for drive calc | 12 kg (planning) |
| A11 | Wheel radius | 50 mm (ASSUMED) |
| A12 | Max slope | 5° (ASSUMED) |
| A13 | Max accel | 0.5 m/s² |
| A14 | Planning factor | 1.5× |

## 3. Arm joints (one arm, ESTIMATE)

| Joint | Continuous (N·m) | Peak (N·m) | After 1.5× |
|---|---:|---:|---:|
| Shoulder yaw | ≈ 0.8 | ≈ 1.4 | ≈ 2.1 |
| Shoulder pitch | ≈ 3.4 | ≈ 4.6 | ≈ 6.9 |
| Elbow | ≈ 1.1 | ≈ 1.5 | ≈ 2.3 |
| Wrist | ≈ 0.25 | ≈ 0.35 | ≈ 0.5 |

(Method identical to DA-01; longer reach and slightly higher module masses raise the numbers.)

## 4. Base drive channels (ESTIMATE)

Traction torque per wheel (level + 5° slope + accel):

```
τ_wheel ≈ (m g sinθ + m a) × r_wheel / 2
```

≈ (12×9.81×0.087 + 12×0.5) × 0.05 / 2 ≈ 0.41 N·m continuous; peak higher with dynamic margin → ≈ 0.8–1.2 N·m after planning factor.

## 5. Status

Week 3 estimates produced. S/M/L mapping blocked on actuator data. Wheel radius, exact mass and slope requirements remain ASSUMED / TBD. Battery not sized (study exclusion under current HOLD interpretation for mobile concepts).
