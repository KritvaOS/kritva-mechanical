# QR-04 — Research-backed preliminary cost model

**Status:** PROPOSED planning estimate; no quotation, purchase authorization or final BOM. D-003 remains HOLD.

The comparison ceiling is ₹2,00,000 from [EVALUATION_CRITERIA.md, EC-03](../../EVALUATION_CRITERIA.md) and FREQ-032. The 10 Ah battery and optional camera price are included; the camera remains a separate mass branch. Full method and references: [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md) and [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Cost line | Quantity / rate | INR |
|---|---|---:|
| Makiina 10 Nm joint modules | 12 × USD 90 × ₹92.9139/USD | 100,347 |
| 10 Ah battery scenario | Listed price | 6,899 |
| 6S 20 A BMS | Listed price | 629 |
| Raspberry Pi 5 4 GB board | USD 110 × ₹92.9139/USD | 10,221 |
| Optional OAK-D Lite camera | Listed price | 36,799 |
| 6061 material | 2.3 kg × ₹430/kg | 989 |
| Machining time | 12 h × ₹600/h | 7,200 |
| Fabrication/setup allowance | Estimate | 3,000 |
| Harness and safety allowance | Estimate | 4,500 |
| **Economy scenario subtotal** | Before foreign actuator shipping/customs | **170,584** |

An 18% tax-only sensitivity on the twelve imported Makiina modules gives ₹188,646; shipping and customs duty are excluded. This low-cost case misses the upper hip-flexion screen of 11.31 Nm at the exact 7.43 kg nominal mass or 11.42 Nm at the rounded 7.50 kg case. Replacing only four hip-flexion modules with 18 Nm AK10-9 units gives ₹396,885 before tax/shipping; the other eight joints stay at 10 Nm, so this is a load-only hybrid and not a literal all-L role configuration. A literal 12-axis L-role lower bound uses two AK10-9 units per joint (36 Nm arithmetic sum, assuming ideal coupling and load sharing) at ₹1,628,738 before couplers, added mounts, tax, shipping or duty; the 48 V supply change is uncosted. Twelve T25-40 profiles price at ₹5,087,588, but that is a low-confidence third-party profile, not a verified product offer.

The under-ceiling subtotal is not a load-compatible design selection. A cost/torque alternative exceeds the study ceiling, and the 7.43 kg mass estimate is above the printed 5–7 kg target. The 22.2 V nominal battery and 24 V actuator listings are not assumed directly compatible; voltage conditioning is not priced. The cross-section-only 4×M5 / 2×Ø5 interface is treated as an estimate branch, not an approved strength-rated mounting interface.