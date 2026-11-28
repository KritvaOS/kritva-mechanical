# QR-04 — Mechanical Assessment (Week 3)

**Version 0.3.0 | 2026-11-27 | INTERN-01 | HOLD D-003**

## Configuration
Agile long-leg quadruped, 3 DOF/leg, 12 actuators. Longer legs than QR-02 raise joint moments and lower natural frequency of the leg structure.

## Stability / support
- Static standing and single-leg support treated in ACTUATOR_ANALYSIS.
- Dynamic gait stability and recovery from disturbance remain UNKNOWN.
- Body mounting interface (4×M5 + dowels) must react full hip torque; insert pull-out and joint stiffness are future checks.

## Structure
- Long links increase bending deflection under body weight and payload.
- No section properties selected; deflection estimates blocked.

## Sensor module
Adjustable sensor module on cross-section only — OWNER_DECISION. Its mass and location affect CoM and knee demand.
