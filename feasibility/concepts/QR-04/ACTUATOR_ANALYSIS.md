# QR-04 — Joint and Actuator Requirements (Week 3 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-QR-04 |
| Status | PROPOSED — Week 3 paper calculation |
| Version | 0.3.0 |
| Last Updated | 2026-11-27 |
| Assigned Intern | INTERN-01 |

**HOLD D-003 active.**

## 1. Configuration

Agile Long-Leg Quadruped: 4 legs × 3 DOF = 12 actuators. Body 450 × 280 × 320 mm (CONCEPT_TARGET). Longer legs than QR-02 imply higher joint moments for the same body mass.

## 2. Planning assumptions (ASSUMED)

| ID | Assumption | Value |
|---|---|---|
| A1 | Robot mass | 6.5 kg |
| A2 | Leg length (hip–foot) | 280 mm |
| A3 | Segment split | 140 / 140 mm |
| A4 | Single-leg support force | ≈ 64 N |
| A5 | Planning factor | 1.5× |

## 3. Per-joint demand (one leg, ESTIMATE)

| Joint | Continuous (N·m) | Peak (N·m) | After 1.5× |
|---|---:|---:|---:|
| Hip abduction / yaw | ≈ 1.5 | ≈ 2.5 | ≈ 3.8 |
| Hip flexion | ≈ 5.5 | ≈ 8.0 | ≈ 12.0 |
| Knee flexion | ≈ 3.0 | ≈ 4.5 | ≈ 6.8 |

Higher than QR-02 because of increased leg length (moment arm). Dynamic gait and impact loads remain UNKNOWN and would increase peak further.

## 4. Mounting interface note

Artwork shows indicative 4×M5 + 2×Ø5 dowels on the body (OWNER_DECISION / cross-section only). Torque reaction at the hip must be reacted through this interface; fastener and insert selection is future work.

## 5. Status

Week 3 estimates produced. S/M/L blocked on source data. Mounting interface and sensor-module questions remain OWNER_DECISION.
