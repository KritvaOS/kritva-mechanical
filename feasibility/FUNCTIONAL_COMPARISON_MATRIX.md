# Functional Comparison Matrix

| Property | Value |
|---|---|
| Document | Functional Comparison Matrix |
| Repository | `KritvaOS/kritva-mechanical` |
| Version | 0.1.0 |
| Last Updated | 2026-10-31 |
| Status | DRAFT, PROPOSED (drafted by Claude; owner review pending) |
| Evidence | Type C, maturity L0. Values are `CONCEPT_TARGET` from the concept artwork unless marked `UNKNOWN` or `NOT SCORED` |
| Related | `feasibility/EVALUATION_CRITERIA.md`, `feasibility/CONCEPT_VARIATION_AUDIT.md`, `docs/images/ARTWORK_INDEX.md` |

## 1. Purpose

Before interns score concepts, each family needs comparison dimensions that can be filled without inventing data. This matrix lists the dimensions, fills in what the artwork prints, and marks everything else `UNKNOWN`. A cell stays `NOT SCORED` until an intern derives it with a documented method; no value here is a score, a ranking or a requirement.

## 2. Dual-arm family

| Dimension | DA-01 | DA-02 | DA-03 | DA-04 | DA-05 | DA-06 |
|---|---|---|---|---|---|---|
| Support | Fixed | Fixed | Differential drive (4 wheels, 2 driven pairs) | Differential drive (4 wheels, 2 driven pairs) | Rotating platform, fixed mount | Fixed |
| Arm DOF (each) | 3 | 4 | 3 | 4 | 3 | 4 |
| Baseline actuators | 6 | 8 (9 with head pan) | 8 | 10 | 7 | 8 |
| Shoulder-to-shoulder (mm) | not printed | 600 | not printed | 600 | not printed | not printed |
| Reach per side (mm) | 350 | 350 | 350 | 450 | 350 | 350 |
| Overall arm-to-arm span (mm) | 700 | 800 | 800 | 1200 | 800 | 800 |
| Payload per arm (kg) | 0.1–0.2 | 0.1–0.2 | 0.1–0.2 | 0.5–1.0 | 0.2–0.5 | 0.2–0.5 |
| Mobility | None | None | Planar, indoor flat | Planar, indoor flat | Base yaw 360° | None |
| Vision and sensing | Optional mast | Torso, optional head | Mast | Head camera | Top mount | Multi-camera mast (top, left, right) and IMU |
| Maximum reachable workspace | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED |
| Base stability and tipping margin | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED |
| Joint torque and S/M/L fit | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED |

Comparison groups: fixed-base manipulation (DA-01, DA-02, DA-06), mobile manipulation (DA-03, DA-04), rotating manipulation (DA-05).

## 3. Legged family

| Dimension | QR-01 | QR-02 | QR-03 | QR-04 | QR-05 | QR-06 |
|---|---|---|---|---|---|---|
| Legs | 4 | 4 | 4 | 4 | 4 | 6 |
| DOF per leg | 2 | 3 | 2 | 3 | 2 or 3 | 2 (joints to be defined) |
| Baseline actuators | 8 | 12 | 8 | 12 | 8 or 12 | 12 |
| Body L × W × H (mm) | 300 × 250 × 200 | 350 × 260 × 250 | 400 × 350 × 180 | 450 × 280 × 320 | 420 × 260 × 250 | 400 × 280 × 220 |
| Overall L × W (mm) | 420 × 400 | 520 × 480 | 520 × 480 | 620 × 520 | 560 × 520 | 520 × 480 |
| Weight (kg) | 2.5–4 | 4–6 | 3–5 | 5–7 | 4–6 (12 DOF) | 3–5 |
| Payload (kg) | 0.3–0.8 | 0.5–1.0 | 0.5–1.0 | 0.5–1.0 | 0.5–1.0 | 0.5–1.0 |
| Terrain named | Flat | Flat and uneven | Flat | Flat and uneven | Flat | Flat |
| Leg link lengths | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Ground clearance | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| Foot workspace | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED |
| Support polygon and gait stability | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED |
| Joint torque and S/M/L fit | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED | NOT SCORED |

Comparison groups: simple quadruped (QR-01), standard and long-leg (QR-02, QR-04), low-profile (QR-03), modular and hexapod (QR-05, QR-06). QR-05 is two configurations (8 and 12 actuators) and should be assessed as two rows.

## 4. Dimension convention (to be agreed)

Printed dimensions are not measured in a stated pose, so they cannot be compared safely yet. For every concept the README should record:

- Dual-arm: shoulder-to-shoulder distance, shoulder-to-gripper reach, overall arm-to-arm span and the arm pose it is measured in, base width and depth.
- Legged: body dimensions separate from the overall envelope with legs extended, and the stance pose used for the envelope.
- Maximum reachable workspace or foot workspace, calculated separately from the drawing dimensions.

## 5. Rules

1. A `CONCEPT_TARGET` value may be quoted here; it is not an input to a score without owner direction.
2. An intern replaces `NOT SCORED` only with a derived value, its method and its confidence, and links the working in the concept folder.
3. Where the evaluation criteria have no evidence, the result stays `NOT SCORED`; no score is invented.
