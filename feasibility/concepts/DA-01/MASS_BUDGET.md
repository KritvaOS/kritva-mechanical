# DA-01 — Research-backed mass budget

**Status:** PROPOSED ESTIMATE; paper-only, D-003 active. No mass is measured and no materials are selected.

The source README prints 5–8 kg as a CONCEPT_TARGET. The nominal case below includes two light demonstration grippers and one camera/mast. It is an estimated component takeoff, not a released BOM. Geometry assumptions and source references are in [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md) and [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Subsystem | Low kg | Nominal kg | High kg | Method / source |
|---|---:|---:|---:|---|
| Six rotary modules | 1.44 | 2.04 | 2.70 | 6 × 0.240 / 0.340 / 0.450 kg; S02 and S01. |
| 300×250 mm base plate | 0.61 | 0.81 | 1.22 | 6061 at 2,700 kg/m³; 3 / 4 / 6 mm; S07. Nominal 0.810 kg. |
| Two arm-link runs | 0.52 | 0.67 | 0.87 | Two 350 mm runs of 20×20×2 tube: 0.272 kg bare, plus estimated joints/fasteners; S08. |
| Enclosure and mount structure | 0.80 | 1.20 | 1.80 | Packaging allowances around 300×250 mm target footprint. |
| Compute assembly | 0.15 | 0.20 | 0.25 | Board + thermal/storage/mount allowance; estimate. |
| PSU, wiring and safety | 0.40 | 0.60 | 0.80 | S17 PSU plus estimated harness/protection. |
| Two grippers and mounts | 0.30 | 0.40 | 0.50 | Two 47 g gripper kits + 30 g MG995 servos, plus mounts; S19–S20. |
| Camera and mast | 0.30 | 0.40 | 0.60 | 102 g camera + estimated mast; S14. |
| **Total** | **4.53** | **6.33** | **8.74** | Low/high scenarios straddle the printed 5–8 kg target. |

Displayed component rows are rounded to 0.01 kg; totals use unrounded camera/kit masses (102 g camera, 2×(47 g kit + 30 g servo), plus mount allowances). The nominal estimate is within the printed band; the economy case is below it and the heavier scenario above it. The former “lower half of the band” wording is removed. The calculation does not treat mass target as measured evidence. The gripper force is not specified by the product sources, so these kits support a light demonstration concept only.

**Included:** six baseline joints, two grippers, camera/mast, frame/enclosure, compute, PSU and basic harness. Optional scope is stated rather than silently counted. No CoM value is inferred from total mass.

**Related:** [CALC-DA01-01_joint_torque.md](calculations/CALC-DA01-01_joint_torque.md), [ACTUATOR_ANALYSIS.md](ACTUATOR_ANALYSIS.md), [COST_MODEL.md](COST_MODEL.md), [FREQ-019/020/027](../../REQUIREMENTS_REGISTER.md), and Week 2 architecture in [ARCHITECTURE.md](ARCHITECTURE.md).