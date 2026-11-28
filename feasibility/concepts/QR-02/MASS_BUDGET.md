# QR-02 — Research-backed mass budget

**Status:** PROPOSED ESTIMATE; paper-only, D-003 active. No measured mass or selected material is claimed.

The source README target is 4–6 kg. Baseline excludes the optional top sensor module; the camera is a separate branch. The 6.30 kg load basis is the component-model nominal and reconciles with the torque calculation. Geometry takeoff and references: [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md), [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Subsystem | Economy kg | Nominal kg | High L-class kg | Basis |
|---|---:|---:|---:|---|
| Twelve rotary modules | 2.88 | 2.88 | 12.96 | 12 × 0.240 kg Makiina for economy/nominal; high case is 8 × 1.50 kg T25-40 profile + 4 × 0.240 kg abduction modules; S02, S06. |
| Body, links, feet and mounts | 1.48 | 1.60 | 2.33 | Two 350×260 mm plates, 0.880 m 20×20×2 leg tube (0.342 kg bare), bracket/foot allowance; S07–S08. |
| Battery and BMS | 0.69 | 1.33 | 1.65 | 4 / 8 / 10 Ah scaled scenarios from S11 plus 45 g BMS S12. 8 Ah is an interpolation. |
| Compute assembly | 0.15 | 0.20 | 0.25 | Analyst allowance. |
| Power and harness | 0.25 | 0.30 | 0.60 | Estimated packaging range. |
| **Subtotal, sensor excluded** | **5.45** | **6.30** | **17.78** | The high case is a role/torque-class stress scenario, not a proposed build. |
| Optional OAK-D Lite camera | +0.10 | +0.10 | +0.10 | 0.102 kg listed mass; S14. |

The 6.30 kg nominal is 0.30 kg above the printed 6 kg upper target; the camera variant is 6.40 kg. The 17.78 kg high case uses eight L-class mass references and four lighter abduction modules. A strict interpretation assigning L hardware to all 12 hip/knee axes would be heavier; it is not used as the nominal load basis.

Displayed rows round to 0.01 kg; totals use unrounded component values. The low, nominal and high rows are separate scenarios, not a confidence interval. The 4 Ah and 8 Ah packs are capacity-scaled estimates; only the 10 Ah source listing is a seller product. The battery pack requires a current-compatible BMS and power integration; the 20 A BMS is a comparison anchor, not a verified quadruped current design.

**Related:** [CALC-QR02-01_leg_torque.md](calculations/CALC-QR02-01_leg_torque.md), [ACTUATOR_ANALYSIS.md](ACTUATOR_ANALYSIS.md), [COST_MODEL.md](COST_MODEL.md), and [FREQ-019/020/029/030/031](../../REQUIREMENTS_REGISTER.md).