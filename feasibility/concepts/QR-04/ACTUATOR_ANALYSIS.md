# QR-04 — Joint and Actuator Requirements (Week 3/4 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-QR-04 |
| Status | PROPOSED — paper estimate; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.4.0 |
| Last Updated | 2026-11-27 |
| Evidence type | C — paper calculation only |

**HOLD D-003 remains active.** No gait, impact, simulation, bench or physical evidence is claimed; all results are estimates, not requirements or actuator selections.

## 1. Inputs and method

Single-leg static support force is `F = 6.5 kg × 9.81 m/s² = 63.77 N ≈ 64 N` (6.5 kg ASSUMED). The 280 mm leg length and 140/140 mm segment split are ASSUMED from the prior screen, not a released dimension. Use `τ = F × d⊥`. The earlier torque estimates (hip yaw 1.5 N·m, hip flexion 5.5 N·m, knee 3.0 N·m) imply effective moment arms of 23.4, 85.9 and 46.9 mm respectively. These moment arms are back-solved from prior estimates, not independently derived from an approved pose or geometry. A ±20% sensitivity is an explicit planning assumption, not a statistical confidence interval. The 1.5× multiplier is a static-only screen, not a validated safety factor.

## 2. Static torque and sensitivity screen, one leg

| Joint | Implied d⊥ (mm) | ±20% d⊥ band (mm) | Static torque band (N·m) | 1.5× static-only screen (N·m) |
|---|---:|---:|---:|---:|
| Hip abduction / yaw | 23.4 | 18.8–28.1 | 1.20–1.80 | 1.80–2.70 |
| Hip flexion | 85.9 | 68.8–103.1 | 4.40–6.60 | 6.60–9.90 |
| Knee flexion | 46.9 | 37.5–56.3 | 2.40–3.60 | 3.60–5.40 |

`τ = 63.77 N × d⊥`; values are rounded. The screen exposes sensitivity to the unknown pose; it is not an independent geometry-derived load result. Static load share may differ from one-leg support and dynamic gait/impact may exceed these values.

## 3. Proposed family-band screen (not assignment)

| Family band | Proposed continuous torque | Proposed peak torque | Source headline speed | Maturity caveat |
|---|---:|---:|---:|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to ~60 rpm | S data are placeholders |
| Kritva-M | 10 N·m | 20–25 N·m | 45 rpm | M reference is not frozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | ~20–40 rpm | L data are placeholders |

These are parent-repository family-level proposal bands, not verified variant output curves. Headline speed is not demonstrated at the required joint load; thermal, duty, packaging and exact model data remain unavailable.

| Joint | Static sensitivity band (N·m) | 1.5× static-only screen (N·m) | Torque-band observation only |
|---|---:|---:|---|
| Hip abduction / yaw | 1.20–1.80 | 1.80–2.70 | Below the proposed S continuous band's upper edge; pose and dynamic loads unverified |
| Hip flexion | 4.40–6.60 | 6.60–9.90 | Static high end exceeds proposed S continuous maximum 5; proposed M band may be examined, not assigned |
| Knee flexion | 2.40–3.60 | 3.60–5.40 | Upper static-only screen slightly exceeds proposed S continuous maximum; dynamic requirement unknown |

These are demand-versus-family-range observations, not compatibility conclusions. The cited family spec labels S/L values as placeholders and the M reference is not frozen. Exact variant speed under load, thermal, packaging and duty data remain unavailable; no model selection is claimed. See `references/SOURCE_REGISTER.md` SRC-11.

## 4. Open inputs

Leg joint axes, exact link lengths/pose, load sharing, gait, impact, ROM, speed, duty, contact friction, body mass/CoM and sensor configuration remain UNKNOWN or ASSUMED. The indicated mounting interface and adjustable sensor module remain OWNER_DECISION. HOLD D-003 remains active.
