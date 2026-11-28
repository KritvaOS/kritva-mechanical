# DA-04 — Research-backed mass budget

**Status:** PROPOSED ESTIMATE; paper-only, D-003 active. This is not a measured mass, BOM or design selection.

The source README target is 25–35 kg. Two paired scenarios show the trade: the low-mass 24 V modules miss the 1 kg payload shoulder screen, while the 18 Nm arm-module scenario uses a 48 V actuator and changes the power architecture. Assumed geometry and sources are in [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md) and [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Subsystem | 24 V economy kg | 18 Nm arm scenario kg | High packaging kg | Basis |
|---|---:|---:|---:|---|
| Eight arm modules | 1.92 | 7.52 | 7.52 | 8 × 0.240 kg Makiina or 8 × 0.940 kg CubeMars AK10-9; S02/S04. |
| Two drive motors | 4.10 | 4.10 | 4.10 | 2 × listed 2.050 kg motor modules; S18. |
| Base plate, rails and brackets | 8.32 | 8.32 | 9.50 | 500×600×4 mm plate = 3.24 kg; 3.40 m 40×40×3 rail = 4.08 kg; brackets. |
| Torso/head structure | 2.44 | 2.44 | 3.00 | Two 400×600×1.5 mm panels = 1.94 kg plus framing allowance. |
| Arm links and mounts | 0.85 | 0.85 | 1.40 | 0.900 m 20×20×2 tube = 0.350 kg bare plus joints/mounts. |
| Battery and BMS | 1.65 | 1.65 | 1.65 | Listed 10 Ah 22.2 V pack plus 45 g BMS; S11–S12. |
| Compute, camera, harness and grippers | 1.31 | 1.31 | 1.75 | Estimated compute and harness; listed camera, gripper kits and servo; S14, S19–S20. |
| **Total** | **20.59** | **26.19** | **28.92** | Economy case is below 25–35 kg target; 18 Nm scenario is within it. |

Displayed component rows are rounded to 0.01 kg; totals use the listed battery (1.600 kg) plus 45 g BMS. The 18 Nm case uses a 48 V actuator and is a packaging/mass sensitivity, not a voltage-compatible selection. The 24 V economy case does not satisfy the 1.0 kg payload shoulder screen. DA-04 source artwork states 24 V conceptually and does not show a battery; the modeled 10 Ah battery is an estimate branch.

Base chassis mass uses a 4 mm plate, 3.40 m total 40×40×3 tube and 1.00 kg bracket allowance. Material mass is calculated from 2,700 kg/m³ density; this is not a strength, stiffness, tipping or structural verification result.

**Related:** [CALC-DA04-01_arm_drive_screen.md](calculations/CALC-DA04-01_arm_drive_screen.md), [ACTUATOR_ANALYSIS.md](ACTUATOR_ANALYSIS.md), [COST_MODEL.md](COST_MODEL.md), and [FREQ-019/020/026/027/032](../../REQUIREMENTS_REGISTER.md).