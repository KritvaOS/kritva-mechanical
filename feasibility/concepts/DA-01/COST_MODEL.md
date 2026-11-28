# DA-01 — Research-backed preliminary cost model

**Status:** PROPOSED planning estimate; no quotation, purchase authorization or final BOM. D-003 remains HOLD.

The comparison ceiling is ₹2,00,000 from [EVALUATION_CRITERIA.md, EC-03](../../EVALUATION_CRITERIA.md) and FREQ-032. The nominal configuration includes six joint modules, Pi 5 compute, camera/mast, two light grippers, 24 V supply, frame material, machine-time allowance, and basic harness/safety. Full model and sources: [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md) and [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Cost line | Quantity / rate | INR |
|---|---|---:|
| Makiina 10 Nm joint modules | 6 × USD 90 × ₹92.9139/USD | 50,174 |
| Raspberry Pi 5 4 GB board | USD 110 × ₹92.9139/USD | 10,221 |
| OAK-D Lite camera | Listed price | 36,799 |
| 24 V 10 A PSU | Listed price | 1,732 |
| Two light grippers | 2 × (₹489 kit + ₹304.27 MG995 servo) | 1,587 |
| 6061 material | 2.7 kg × ₹430/kg | 1,161 |
| Machining time | 6 h × ₹600/h | 3,600 |
| Fabrication/setup allowance | Estimate anchored to actuator A0 allowance | 3,000 |
| Harness and safety allowance | Estimate anchored to actuator A0 component lines | 4,500 |
| **Scenario subtotal** | Before foreign actuator shipping/customs | **112,773** |

The Makiina price is a foreign product-page listing, not a landed cost. Applying an 18% tax-only sensitivity to its six-module subtotal gives ₹121,804; shipping and customs duty are additional and are not guessed. The vendor-listed local AK80-8 alternative is ₹113,980 per 10 Nm module before tax; replacing the six modules gives a ₹746,480 subtotal before tax and delivery. This is a supplier-listing sensitivity, not a quote.

The ₹112,773 case is within the study ceiling and the modeled 4.77 Nm conditional shoulder-pitch screen fits the 10 Nm rated candidate. The candidate is not approved and its shipping/tax, repeatability, thermal duty and control integration are not validated. Optional scope and every mass/cost assumption are listed in the central report; do not treat this subtotal as a procurement budget.