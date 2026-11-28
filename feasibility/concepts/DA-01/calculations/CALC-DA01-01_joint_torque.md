# CALC-DA01-01 — DA-01 joint torque screen

| Property | Value |
|---|---|
| Concept | DA-01 Fixed Tabletop Dual-Arm |
| Status | PROPOSED / ESTIMATE; paper calculation only |
| Date | 2026-11-28 |
| Evidence type | C — formula-based scenario screen |
| Related | ACTUATOR_ANALYSIS.md, MASS_BUDGET.md, WEEK3_ESTIMATE_METHOD.md |

HOLD D-003 remains active. No simulation, bench or physical result is claimed. Full sources: [WEEK3_SOURCE_REGISTER.md](../../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

## Inputs

The source concept gives 350 mm reach and 0.1–0.2 kg estimated payload. Use the upper payload in the conservative point-mass screen. No geometry is read from the illustrative rendering.

| Element | Mass kg | Radius from shoulder m | Radius from elbow m | Basis |
|---|---:|---:|---:|---|
| Payload | 0.20 | 0.350 | 0.175 | Upper printed concept target. |
| Gripper and mount | 0.12 | 0.310 | 0.135 | 47 g kit + 30 g servo + estimated 43 g mount; S19–S20. |
| Wrist module | 0.24 | 0.275 | 0.100 | Makiina listed mass; S02. |
| Forearm link | 0.08 | 0.225 | 0.050 | 175 mm tube segment, 20×20×2 mm bare mass 0.068 kg plus small end/harness allowance; S08. |
| Elbow module | 0.30 | 0.175 | At the elbow axis | Estimate within the 0.240–0.450 kg sourced module range; S01–S02. |
| Upper-arm link | 0.12 | 0.0875 | Proximal to elbow | 175 mm tube segment 0.068 kg bare plus joint/harness allowance; S08. |
| Gravity | 9.81 m/s² |  |  | Calculation constant. |
| Angular acceleration | 10 rad/s² |  |  | Planning assumption, not a motion requirement. |
| Speed | 1.57 rad/s = 15.0 rpm |  |  | Planning assumption for comparison only. |

Use τg = Σ(mgr), I = Σ(mr²), τi = Iα, and a 1.5× headroom sensitivity on τg+τi. The 1.5 multiplier is an analyst screen, not a validated safety factor.

## Calculated branches

| Axis / branch | Static gravity Nm | Inertia kg·m² | Inertial Nm | Raw sum Nm | 1.5× screen Nm |
|---|---:|---:|---:|---:|---:|
| Shoulder pitch, conditional horizontal fully extended arm | 2.49 | 0.06834 | 0.68 | 3.18 | 4.77 |
| Shoulder yaw, vertical-axis gravity idealization | ≈0 | 0.06834 | 0.68 | 0.68 | 1.03 |
| Elbow pitch | 0.78 | 0.01091 | 0.11 | 0.89 | 1.33 |
| Wrist pitch branch | 0.19 | 0.00132 | 0.01 | 0.21 | 0.31 |
| Wrist rotation branch, 20–50 mm radial mass offset | ≈0 | 0.00013–0.00080 | 0.001–0.008 | 0.001–0.008 | 0.002–0.012 |

The shoulder-pitch row is not silently merged into the source’s three-axis baseline. The artwork interpretation keeps the six-channel baseline as shoulder yaw, elbow and wrist, and carries pitch as a separate branch. The wrist-pitch and wrist-rotation rows are also alternatives. The rotation branch estimates only gripper+payload radial inertia at 20–50 mm; housing, friction, cable torque and contact are not added.

## Actuator-family screen

The linked family specification proposes S for wrist/neck, M for elbow/reference, and L for hip/knee; its S/L torque values are placeholders, not approved requirements. HEBI T5-4 is 4 Nm continuous and 32 rpm; Makiina is 10 Nm rated continuous up to 75 rpm at 24 V. Thus a T5-4 is above the modeled elbow/wrist screen but below the conditional 4.77 Nm pitch branch; the Makiina 10 Nm candidate clears each modeled branch. This is a torque-only paper comparison, not an actuator selection.

## Bounds

The point-mass locations, 10 rad/s² acceleration, 15 rpm comparison speed, 20–50 mm rotation radius, and 1.5× headroom are scenario assumptions. The results omit link distributed inertia, gearbox efficiency, friction, cable drag, thermal limits and collision/contact loads. Axis names and 350 mm datum are concept targets; the branch tables keep the discrepancy visible for review.