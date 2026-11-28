# DA-04 — Joint and Actuator Requirements (Week 3/4 update)

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-DA-04 |
| Status | PROPOSED — paper estimate; owner review required |
| Assigned Intern | INTERN-01 |
| Version | 0.4.0 |
| Last Updated | 2026-11-27 |
| Evidence type | C — paper calculation only |

**HOLD D-003 remains active.** The baseline is four arm DOF per arm plus two base drive channels (10 channels; CONCEPT_TARGET). No actuator, battery, CAD, simulation, bench or physical test is selected or authorized.

## 1. Arm calculation assumptions

| Input | Value | Classification |
|---|---:|---|
| Arm reach | 0.400 m | ASSUMED from prior screening; not a released target |
| Link split | 0.180 / 0.120 / 0.100 m | ASSUMED; totals 0.400 m |
| DA-01 reference masses scaled by 1.2 | Upper link 0.144 kg; elbow 0.360 kg; forearm 0.096 kg; wrist 0.216 kg; gripper+mount 0.144 kg | ASSUMED/ESTIMATE; explicit calculation input, not measured |
| Payload | 0.200 kg | ASSUMED for comparison |
| Gravity | 9.81 m/s² | Calculation constant |
| Angular acceleration | 10 rad/s² | ASSUMED; no trajectory supplied |
| Arm output speed | 1.57 rad/s (15.0 rpm) | ASSUMED; not a speed requirement |
| Planning multiplier | 1.5× | ASSUMED; not a validated safety factor |

Point-mass model locations from the shoulder: upper link COM 0.090 m; elbow 0.180 m; forearm COM 0.240 m; wrist 0.300 m; gripper COM 0.340 m; payload 0.400 m. These are derived from the assumed link split and component locations, not artwork dimensions.

## 2. Arm torque screen, one arm

| Joint | Static gravity (N·m) | Iα estimate (N·m) | Raw sum (N·m) | 1.5× static / raw-sum screen (N·m) | Torque-only family screen |
|---|---:|---:|---:|---:|---|
| Shoulder yaw | ≈ 0 | ≈ 0.864 | ≈ 0.864 | 0 / 1.297 | S is the smallest proposed band to examine; yaw inertia is pose-dependent |
| Shoulder pitch | ≈ 2.889 | ≈ 0.864 | ≈ 3.753 | 4.334 / 5.630 | S torque band is a screening candidate only; no compatibility claim |
| Elbow pitch | ≈ 0.968 | ≈ 0.168 | ≈ 1.137 | 1.453 / 1.705 | S torque band is a screening candidate only |
| Wrist pitch | ≈ 0.253 | ≈ 0.022 | ≈ 0.275 | 0.379 / 0.413 | S torque band is a screening candidate only |

The two arms are treated as symmetric for this estimate. All values are `ESTIMATE`; point-mass inertia omits link self-inertia, friction, cable loads, gearbox losses, simultaneous motion and thermal/duty effects. It is not a capacity or safe-load result.

## 3. Base-drive traction screen

ASSUMED planning inputs: total robot mass 12 kg (rounded from the 11.8 kg nominal mass estimate), two driven wheels, wheel radius 0.050 m, 5° slope and 0.5 m/s² acceleration. Per-wheel torque:

`τ = [m(g sin θ + a) / 2] r = [12(9.81 sin 5° + 0.5) / 2] × 0.050 ≈ 0.407 N·m`.

Applying the stated 1.5× planning multiplier gives ≈ 0.610 N·m per wheel. This replaces the earlier unexplained 0.8–1.2 N·m “after factor” range. Dynamic traction/turning, wheel speed, floor friction, wheel load and duty are UNKNOWN; no peak requirement or S/M/L class is assigned to the base drive channels.

## 4. Proposed family-band screen (not assignment)

| Family band | Proposed continuous torque | Proposed peak torque | Source headline speed | Maturity caveat |
|---|---:|---:|---:|---|
| Kritva-S | 2–5 N·m | 5–10 N·m | up to ~60 rpm | S data are placeholders |
| Kritva-M | 10 N·m | 20–25 N·m | 45 rpm | M reference is not frozen |
| Kritva-L | 25–40 N·m | 50–80 N·m | ~20–40 rpm | L data are placeholders |

These are parent-repository family-level proposal bands, not verified variant output curves. Headline speed is not demonstrated at the required joint load; thermal, duty, packaging and exact model data remain unavailable.

The cited family-level ranges are proposal inputs only: S/L values are placeholders, and the M reference is not frozen. Arm speed/thermal data and exact variant-specific output curves are unavailable. Torque-only S screening does not establish physical compatibility; see `references/SOURCE_REGISTER.md` SRC-11.

## 5. Open inputs

Battery inclusion/capacity, wheel geometry, arm duty and trajectory, mass distribution, slope/acceleration requirements, speed and thermal limits remain ASSUMED or TBD. No battery is drawn in the concept sheets. HOLD D-003 remains active.
