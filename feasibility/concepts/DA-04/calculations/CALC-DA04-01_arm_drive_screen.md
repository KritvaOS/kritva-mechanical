# CALC-DA04-01 — DA-04 Arm and Drive Torque Screen

| Property | Value |
|---|---|
| Calculation ID | CALC-DA04-01 |
| Concept | DA-04 Humanoid Mobile Dual-Arm |
| Status | PROPOSED / ESTIMATE |
| Date | 2026-11-27 |
| Evidence type | C — paper calculation only |
| Related | `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `MECHANICAL_ANALYSIS.md` |

**HOLD D-003 remains active.** Results are a point-mass planning screen, not requirements, validation or an actuator selection.

## 1. Arm inputs (ASSUMED)

| Input | Value |
|---|---:|
| Reach | 0.400 m |
| Link split | 0.180 / 0.120 / 0.100 m |
| Upper link / elbow / forearm / wrist / gripper masses | 0.144 / 0.360 / 0.096 / 0.216 / 0.144 kg |
| Payload | 0.200 kg |
| Angular acceleration | 10 rad/s² |
| Planning multiplier | 1.5× |
| Representative speed | 1.57 rad/s (15.0 rpm) |

Masses are the DA-01 planning estimates scaled by 1.2 per the previous DA-04 assumption. They are not measured or source-controlled. Point-mass positions from shoulder are 0.090, 0.180, 0.240, 0.300, 0.340 and 0.400 m respectively.

## 2. Arm calculation

Static gravity: `τ_g = Σm g r`. Simplified inertia: `I = Σm r²`; inertial screen: `τ_i = Iα`. This omits link self-inertia, joint offsets, friction, cable forces, gearbox efficiency and dynamic coupling.

| Joint | Static gravity (N·m) | I (kg·m²) | Iα (N·m) | Raw sum (N·m) | 1.5× static / raw sum (N·m) |
|---|---:|---:|---:|---:|---:|
| Shoulder yaw | ≈ 0 | 0.08645 | 0.865 | 0.865 | 0 / 1.297 |
| Shoulder pitch | 2.889 | 0.08645 | 0.865 | 3.753 | 4.334 / 5.630 |
| Elbow pitch | 0.968 | 0.01682 | 0.168 | 1.137 | 1.453 / 1.705 |
| Wrist pitch | 0.253 | 0.002230 | 0.022 | 0.275 | 0.379 / 0.413 |

Elbow static input uses distal masses at 0.060, 0.120, 0.160 and 0.220 m from the elbow. Wrist pitch uses gripper COM at 0.040 m and payload at 0.100 m beyond the wrist. Yaw gravity is idealized as zero for a vertical axis; actual yaw inertia depends on arm pose.

## 3. Base drive traction

ASSUMED total mass `m=12 kg`, two driven wheels, wheel radius `r=0.050 m`, slope `θ=5°`, acceleration `a=0.5 m/s²`. Per-wheel level/slope/acceleration torque:

`τ_wheel = [m(g sin θ + a)/2] r = [12(9.81 sin 5° + 0.5)/2] × 0.050 = 0.407 N·m`.

A 1.5× static planning screen is 0.610 N·m per wheel. Wheel speed, friction, turning, transient traction and duty remain UNKNOWN; this is not a dynamic peak.

## 4. Limits

The 12 kg, 5° and acceleration values are ASSUMED only; 12 kg is rounded from the nominal 11.8 kg mass estimate. The concept art does not define wheel geometry or a battery. Do not use this screen to claim mobile stability, runtime, traction safety or S/M/L compatibility.
