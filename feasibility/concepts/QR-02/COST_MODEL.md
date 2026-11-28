# QR-02 — Research-backed preliminary cost model

**Status:** PROPOSED planning estimate; no quotation, purchase authorization or final BOM. D-003 remains HOLD.

The comparison ceiling is ₹2,00,000 from [EVALUATION_CRITERIA.md, EC-03](../../EVALUATION_CRITERIA.md) and FREQ-032. Camera is included as an optional cost branch here but excluded from the 6.30 kg baseline mass. Full assumptions and references: [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md) and [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Cost line | Quantity / rate | INR |
|---|---|---:|
| Makiina 10 Nm joint modules | 12 × USD 90 × ₹92.9139/USD | 100,347 |
| 8 Ah battery scenario | 0.8 × listed 10 Ah pack ₹6,899 | 5,519 |
| 6S 20 A BMS | Listed price | 629 |
| Raspberry Pi 5 4 GB board | USD 110 × ₹92.9139/USD | 10,221 |
| Optional OAK-D Lite camera | Listed price | 36,799 |
| 6061 material | 1.6 kg × ₹430/kg | 688 |
| Machining time | 8 h × ₹600/h | 4,800 |
| Fabrication/setup allowance | Estimate | 3,000 |
| Harness and safety allowance | Estimate | 4,500 |
| **Economy scenario subtotal** | Before foreign actuator shipping/customs | **166,503** |

An 18% tax-only sensitivity on the twelve imported Makiina modules gives ₹184,565; shipping and customs duty are excluded. The low-price module clears the calculated 8.34 Nm upper static-only screen, but it does not meet the proposed L-family 25–40 Nm role. The ₹1,138,605 hybrid is a load-only lower bound: two 18 Nm AK10-9 modules on each of eight sagittal joints plus four 10 Nm Makiina abduction modules. It does not satisfy the literal proposed L role for all hip/knee axes. A literal 12-axis L-role lower bound uses two AK10-9 modules per joint (36 Nm arithmetic sum, assuming ideal coupling and load sharing) at ₹1,624,657 before couplers, added mounts, tax, shipping or duty; the 48 V supply change is also uncosted. Twelve T25-40 profiles price at ₹5,083,507, but this is a low-confidence third-party profile, not a verified product offer.

The economy subtotal is below ₹2,00,000 only for the static 10 Nm scenario. It is not represented as compatible with the proposed L-family role or a validated walking duty. The battery listing is 22.2 V nominal while the actuator listing specifies 24 V; no voltage-conditioning cost or direct compatibility is claimed. Optional camera cost is included while its mass is a separate branch; the 8 Ah battery price is pro-rated from a 10 Ah listing and is an estimate, not a listed part.