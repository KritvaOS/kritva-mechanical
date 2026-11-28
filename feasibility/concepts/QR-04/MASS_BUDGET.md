# QR-04 — Research-backed mass budget

**Status:** PROPOSED ESTIMATE; paper-only, D-003 active. No measured mass or selected material is claimed.

The source README target is 5–7 kg. The nominal case uses the listed 10 Ah 22.2 V pack and excludes the optional camera; camera mass is a separate branch. The 7.43 kg nominal is the same scenario used to calculate the one-leg force. See [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md) and [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Subsystem | Economy kg | Nominal kg | High L-class kg | Basis |
|---|---:|---:|---:|---|
| Twelve rotary modules | 2.88 | 2.88 | 12.96 | 12 × 0.240 kg Makiina economy case; high case is 8 × 1.50 kg T25-40 profile + 4 × 0.240 kg lower-torque abduction modules; S02, S06. |
| Body, long links, feet and mounts | 2.06 | 2.30 | 2.60 | Two 450×280 mm body plates, 1.120 m of 20×20×2 tube (0.436 kg bare), plus brackets/feet; S07–S08. |
| Battery and BMS | 1.01 | 1.65 | 1.65 | 6 / 10 / 10 Ah scenarios scaled from S11 plus 45 g BMS S12. |
| Compute assembly | 0.15 | 0.20 | 0.25 | Analyst allowance. |
| Power and harness | 0.30 | 0.40 | 0.60 | Estimated packaging allowance. |
| **Subtotal, sensor excluded** | **6.39** | **7.43** | **18.06** | High case is a role/torque-class stress scenario, not a proposed build. |
| Optional OAK-D Lite camera | +0.10 | +0.10 | +0.10 | Listed camera mass; S14. |

Displayed component rows are rounded to 0.01 kg; totals use unrounded pack, BMS and camera masses. The nominal sensor-excluded estimate is 0.43 kg above the printed 7 kg upper target; with camera it is 7.53 kg. The previous 7.5 kg load case is retained as a rounded upper-planning check alongside the exact 7.43 kg model case. The 18.06 kg high case is not a build proposal; it shows the mass consequence of eight L-class references. A strict 12-axis L mapping would be heavier.

The 6 Ah case is a linear estimate from the listed 10 Ah product, not a catalogued SKU. The indicated 4×M5 / 2×Ø5 interface and adjustable sensor mount are treated as explicit scope branches; neither interface capacity nor sensor fit is approved by this estimate.

**Related:** [CALC-QR04-01_leg_torque_screen.md](calculations/CALC-QR04-01_leg_torque_screen.md), [ACTUATOR_ANALYSIS.md](ACTUATOR_ANALYSIS.md), [COST_MODEL.md](COST_MODEL.md), and [FREQ-019/020/029/030/031](../../REQUIREMENTS_REGISTER.md).