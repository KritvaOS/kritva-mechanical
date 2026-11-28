# CALC-DA01-01 — DA-01 Joint Torque Screening

| Property | Value |
|---|---|
| Calculation ID | CALC-DA01-01 |
| Concept | DA-01 Fixed Tabletop Dual-Arm |
| Status | PROPOSED / ESTIMATE |
| Date | 2026-11-27 |
| Evidence type | C — paper calculation only |
| Related | `ACTUATOR_ANALYSIS.md`, `ARCHITECTURE.md` v0.3.x |

**HOLD D-003 remains active.** No CAD, simulation, bench or physical evidence is claimed. All results are estimates, not requirements or actuator selections.

## 1. Baseline axes and scope

`ARCHITECTURE.md` lists three axes per arm: shoulder yaw, elbow and wrist (six baseline channels total). The Week 3 actuator table also introduced a shoulder-pitch calculation, yielding four axis labels. This file keeps that pitch result as a conditional sensitivity case only; it is not mapped to the baseline until the owner resolves the discrepancy. Wrist rotation versus pitch also remains unresolved.

## 2. Inputs and assumptions

| Input | Value | Classification / source |
|---|---:|---|
| Gravity | 9.81 m/s² | Standard calculation constant |
| Reach | 0.350 m | CONCEPT_TARGET; artwork; datum/pose undefined |
| Link split | 0.175 m upper arm / 0.100 m forearm / 0.075 m wrist-to-tip | ASSUMED; totals 0.350 m |
| Upper-arm link | 0.12 kg at 0.0875 m from shoulder | ESTIMATE |
| Elbow module | 0.30 kg at 0.175 m from shoulder | ESTIMATE |
| Forearm link | 0.08 kg at 0.225 m from shoulder; 0.050 m from elbow | ESTIMATE |
| Wrist module | 0.18 kg at 0.275 m from shoulder; 0.100 m from elbow | ESTIMATE |
| Gripper + mount | 0.12 kg at 0.310 m from shoulder; 0.135 m from elbow; 0.040 m beyond wrist | ESTIMATE |
| Payload | 0.20 kg at 0.350 m from shoulder; 0.175 m from elbow; 0.075 m beyond wrist | CONCEPT_TARGET upper end |
| Angular acceleration | 10 rad/s² | ASSUMED planning input; no trajectory |
| Speed | 1.57 rad/s ≈ 15.0 rpm | ASSUMED, not a speed requirement |
| Planning factor | 1.5× | ASSUMED; not a validated safety factor |

Loads are treated as point masses at their stated centres. Link inertia, friction, cable drag, gearbox losses, dynamic contact and thermal limits are not independently modelled.

## 3. Static gravity calculation

For a joint axis and pose, `τ_g = Σ (r_i × m_i g) · e_axis`. For the **conditional shoulder-pitch** case with a fully extended horizontal arm:

| Element | m (kg) | r (m) | m·g·r (N·m) |
|---|---:|---:|---:|
| Payload | 0.20 | 0.350 | 0.6867 |
| Gripper + mount | 0.12 | 0.310 | 0.3649 |
| Wrist module | 0.18 | 0.275 | 0.4856 |
| Forearm link | 0.08 | 0.225 | 0.1766 |
| Elbow module | 0.30 | 0.175 | 0.5150 |
| Upper-arm link | 0.12 | 0.0875 | 0.1030 |
| **Sum** | | | **2.3318 ≈ 2.33** |

This replaces the prior 2.15 N·m working value; the listed terms sum to 2.332 N·m, not 2.15 N·m. The axis is not part of the current three-axis baseline in `ARCHITECTURE.md`.

## 4. Baseline elbow and wrist branches

- **Elbow pitch:** `τ_g = 9.81 × (0.20×0.175 + 0.12×0.135 + 0.18×0.100 + 0.08×0.050) = 0.718 N·m`. Point-mass inertia is `I = Σmr² = 0.01031 kg·m²`, so `Iα = 0.103 N·m`; raw screening sum is 0.821 N·m and 1.5× is 1.23 N·m.
- **Wrist-pitch branch only:** `τ_g = 9.81 × (0.20×0.075 + 0.12×0.040) = 0.194 N·m`. `I = 0.001317 kg·m²`, `Iα = 0.013 N·m`; raw sum is 0.208 N·m and 1.5× is 0.311 N·m.
- **Wrist-rotation branch:** ideal static gravity torque about the forearm axis is approximately zero; dynamic torque needs the actual axis, mass distribution and motion. Keep dynamic demand TBD.
- **Shoulder yaw:** ideal static gravity torque about a vertical axis is approximately zero. Under the straight-arm horizontal pose, the point-mass estimate `I = 0.0638 kg·m²` gives `Iα ≈ 0.638 N·m`; 1.5× ≈ 0.957 N·m. Orientation, cable drag and acceleration are assumed, so this is an ESTIMATE only.

## 5. Conditional shoulder-pitch sensitivity (not baseline)

For the same point-mass model, `I = Σmr² = 0.0638 kg·m²`; `Iα = 0.638 N·m`. Static 2.332 plus inertial 0.638 gives a raw planning sum of 2.970 N·m; 1.5× gives 4.455 N·m. These figures apply only if an owner-approved shoulder-pitch axis and pose are added to the baseline. Do not use them to claim the six-channel concept has a shoulder-pitch requirement.

## 6. Limits and next inputs

- Exact link dimensions, joint frames, ROM, duty cycle, speed profile and payload basis are UNKNOWN.
- Wrist-axis direction and the shoulder-axis mismatch need owner resolution before joint mapping.
- S/M/L compatibility is torque-screening only against the proposed family ranges; variant-specific output data are not established.
- Replace all assumptions only with traceable inputs and update the parent actuator analysis together.
