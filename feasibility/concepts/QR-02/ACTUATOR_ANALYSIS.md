# QR-02 — Joint and Actuator Evidence Status

| Property | Value |
|---|---|
| Status | INCOMPLETE — per-joint requirements are TBD |
| Version | 0.6.0 |
| Last updated | 2026-11-28 |
| Evidence | Concept-art transcription and conditional paper calculations only |
| HOLD | D-003 active |

## Baseline joint/channel inventory

four legs, three DOF per leg. Baseline count: 12 baseline leg actuators: four legs with three DOF each. The inventory below follows README.md and ARCHITECTURE.md; it is not a torque, speed or actuator assignment.

| Joint/channel | Count | Motion as source-labelled | Torque requirement | Speed / ROM / duty |
|---|---:|---|---|---|
| Hip abduction/adduction | 4 | one per leg | NOT DERIVED — see calculations; geometry/mass inputs missing | UNKNOWN / TBD | UNKNOWN / TBD |
| Hip/thigh flexion/extension | 4 | one per leg | NOT DERIVED — see calculations; geometry/mass inputs missing | UNKNOWN / TBD | UNKNOWN / TBD |
| Knee flexion/extension | 4 | one per leg | NOT DERIVED — see calculations; geometry/mass inputs missing | UNKNOWN / TBD | UNKNOWN / TBD |

The calculation file gives a conditional one-leg full-weight force scenario from the printed mass target. Joint torques remain unknown because moment arms and pose are absent.

## Family roles and ranges (proposal only; not a mapping)

| Variant | Proposed continuous output torque | Proposed peak output torque | Proposed speed | Intended role (proposal) |
|---|---:|---:|---|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to about 60 RPM | Small joints/light mechanisms, e.g. wrist or neck |
| Kritva-M | 10 N·m | 20–25 N·m (stretch) | 45 RPM | Elbow and reference joint; baseline remains unfrozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | about 20–40 RPM | Higher-load joints, e.g. hip or knee, subject to mass/power/thermal feasibility |

Source: the pinned Kritva actuator family specification, 2026-10-15 revision, references/SOURCE_REGISTER.md SRC-07. The spec explicitly says S/L values are placeholders and the M reference is not frozen. It gives proposed roles, not a product selection or validated performance. S is the proposal for small joints/wrist/neck, M for elbow/reference, and L for higher-load hip/knee; these roles are not assignments to this concept.

## Required inputs before per-joint sizing

Exact joint frames/axes, dimensions and offsets, component masses and centres of mass, payload location, representative pose, motion profile, speed, duty, friction/cable loads, output-side variant data, and thermal/envelope limits. For legged concepts add support phase, load share, foot-ground forces and gait/impact cases. Missing values remain UNKNOWN/TBD; no assumed multiplier, back-solved moment arm, torque rating or speed is introduced.

References: [README.md](README.md) sections 4 and 6; [ARCHITECTURE.md](ARCHITECTURE.md); [calculation note](calculations/CALC-QR02-01_leg_torque.md); [SOURCE_REGISTER.md](references/SOURCE_REGISTER.md) SRC-01–SRC-07; [DESIGN_GUIDELINES.md](../../DESIGN_GUIDELINES.md) FREQ-006/007/012.
