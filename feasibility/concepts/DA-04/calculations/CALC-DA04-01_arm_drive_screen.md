# CALC-DA04-01 — DA-04 arm and drive torque screen

| Property | Value |
|---|---|
| Concept | DA-04 Humanoid Mobile Dual-Arm |
| Status | PROPOSED / ESTIMATE; paper calculation only |
| Date | 2026-11-28 |
| Evidence type | C — formula-based scenario screen |
| Related | ACTUATOR_ANALYSIS.md, MASS_BUDGET.md, WEEK3_ESTIMATE_METHOD.md |

HOLD D-003 remains active. No CAD, simulation, bench or physical result is claimed. Sources: [WEEK3_SOURCE_REGISTER.md](../../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

## Arm inputs

The source target is 450 mm reach and 0.5–1.0 kg payload. For the horizontal extended pose, use point masses: upper link 0.15 kg at 0.1125 m; elbow module 0.24 kg at 0.225 m; forearm link 0.10 kg at 0.325 m; wrist module 0.24 kg at 0.375 m; gripper+mount 0.147 kg at 0.410 m; payload 0.5–1.0 kg at 0.450 m. Link mass is an estimate based on aluminum tube and end fittings; modules/gripper use S02, S19 and S20. Assume α = 10 rad/s² and 1.5× planning headroom. This acceleration is not a requirement.

Use τg = Σ(mgr), I = Σ(mr²), τi = Iα. The screen omits link distributed inertia, joint offsets, gearbox losses, friction, cable forces and dynamic coupling.

| Joint | Payload | Static gravity Nm | I kg·m² | Inertial Nm | Raw sum Nm | 1.5× screen Nm |
|---|---:|---:|---:|---:|---:|---:|
| Shoulder pitch | 0.5 kg | 4.70 | 0.18432 | 1.84 | 6.54 | 9.81 |
| Shoulder pitch | 1.0 kg | 6.90 | 0.28557 | 2.86 | 9.76 | 14.64 |
| Elbow pitch | 0.5 kg | 1.82 | 0.03674 | 0.37 | 2.19 | 3.28 |
| Elbow pitch | 1.0 kg | 2.93 | 0.06206 | 0.62 | 3.55 | 5.32 |
| Wrist pitch | 0.5 kg | 0.43 | 0.00305 | 0.03 | 0.46 | 0.68 |
| Wrist pitch | 1.0 kg | 0.79 | 0.00586 | 0.06 | 0.85 | 1.28 |
| Shoulder yaw | 0.5 kg | ≈0 | 0.18432 | 1.84 | 1.84 | 2.76 |
| Shoulder yaw | 1.0 kg | ≈0 | 0.28557 | 2.86 | 2.86 | 4.28 |

Shoulder yaw gravity is idealized as zero for a vertical axis; its inertial screen uses the same point masses about that axis. The shoulder-pitch 1.0 kg case is the largest arm screen at 14.64 Nm.

## Differential-drive screen

Use the printed 25–35 kg robot mass target, two driven wheel pairs, assumed wheel radius 0.050 m, slope 5°, and acceleration 0.5 m/s². Per driven side, τ = [m(g sin 5° + a)/2]r.

| Total mass | Static scenario torque per side Nm | 1.5× screen Nm | 25 rpm wheel speed at 50 mm radius |
|---:|---:|---:|---:|
| 25 kg | 0.85 | 1.27 | 0.131 m/s |
| 30 kg | 1.02 | 1.52 | 0.131 m/s |
| 35 kg | 1.19 | 1.78 | 0.131 m/s |

The Robokits 24 V, 100 W, 25 rpm motor/driver listing reports 280 kg·cm rated torque, about 27.46 Nm after unit conversion, above the static wheel screen. The 25 rpm speed is slow; the screen does not establish acceptable travel speed, braking, friction, stability, turning duty or thermal operation. The source listing’s two-channel driver is conservatively counted twice in the cost model.

## Candidate comparison

Makiina 10 Nm at 24 V clears the 0.5 kg shoulder case but not the 1.0 kg 14.64 Nm screen. CubeMars AK10-9 at 18 Nm rated clears the 1.0 kg screen but uses 48 V against the concept’s 24 V direction. Its price increases the two-shoulder-upgrade scenario above ₹2,00,000. No candidate is selected.

## Bounds

Reach split, masses and COM locations, gripper mount, payload pose, α, wheel radius, 5° slope, acceleration and 1.5× multiplier are explicit scenario inputs. This paper screen is not a gait, tip-over, battery runtime or actuator thermal result.