# QR-02 — Open Questions and Decisions (Week 3)

**Status:** PROPOSED | Version 0.3.0 | 2026-11-27 | INTERN-01

## Owner decisions
- Optional sensors (IMU, LiDAR, force feet) — concept sheet only; OWNER_DECISION.
- Exact hip axis definition (abduction vs yaw) for torque direction.

## Key unknowns
- Gait parameters, ground reaction profiles, impact loads → peak torque still planning-level only.
- Source-controlled S/M/L data.
- Battery inclusion and size.
- Foot contact geometry and friction assumptions.

## Risks (ESTIMATE)
- Cost exceeds INR 2 L if actuators land in mid/high range.
- Dynamic gait may push hip/knee peaks beyond current 1.5× planning factor.
- Sensor addition increases distal mass and knee demand.
