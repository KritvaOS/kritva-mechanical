# DA-04 — Research-backed preliminary cost model

**Status:** PROPOSED planning estimate; no quotation, purchase authorization or final BOM. D-003 remains HOLD.

The comparison ceiling is ₹2,00,000 from [EVALUATION_CRITERIA.md, EC-03](../../EVALUATION_CRITERIA.md) and FREQ-032. The baseline price scenario uses eight 24 V Makiina arm modules, two 24 V base motor/driver listings, a 10 Ah battery plus BMS, computer, camera, two light grippers, frame material, machining time and basic safety/harness. Full assumptions and references: [WEEK3_ESTIMATE_METHOD.md](../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md) and [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).

| Cost line | Quantity / rate | INR |
|---|---|---:|
| Makiina 10 Nm arm modules | 8 × USD 90 × ₹92.9139/USD | 66,898 |
| 24 V 100 W drive motor/driver listings | 2 × ₹11,664 × 1.18 tax assumption | 27,527 |
| 10 Ah battery plus 20 A BMS | ₹6,899 + ₹629 | 7,528 |
| Raspberry Pi 5 4 GB board | USD 110 × ₹92.9139/USD | 10,221 |
| OAK-D Lite camera | Listed price | 36,799 |
| Two light grippers | 2 × (₹489 kit + ₹304.27 MG995 servo) | 1,587 |
| 6061 material | 11.61 kg × ₹430/kg | 4,992 |
| Machining time | 20 h × ₹600/h | 12,000 |
| Fabrication/setup allowance | Estimate | 3,000 |
| Harness and safety allowance | Estimate | 4,500 |
| **24 V economy subtotal** | Before foreign actuator shipping/customs | **175,052** |

Applying an 18% tax-only sensitivity to the eight imported Makiina modules gives ₹187,093; no foreign shipping or customs duty is included. The economy case is under ₹2,00,000 but does not clear the 1.0 kg payload shoulder-pitch screen. Replacing the two shoulder-pitch modules with 18 Nm AK10-9 units raises the subtotal to ₹288,202 before landing costs; those products require 48 V. Using 18 Nm modules for all eight arm axes gives a ₹627,654 subtotal before tax/shipping.

The two base motor/driver price listings conservatively double-count a dual-driver board. At a 50 mm wheel radius, the product title’s 25 rpm corresponds to 0.131 m/s; the listing description elsewhere says 35 rpm, so 25 rpm is used as the lower-speed case. The 10 Ah battery is a planning scenario, not a runtime guarantee. Its 22.2 V nominal listing is not assumed directly compatible with the 24 V motors/modules; voltage conditioning is not priced. The 40 Ah listing is not treated as a complete alternative because its high-current BMS pairing is not included in the source. The source README’s 10-channel baseline is reported as the existing concept statement; this model does not assert an unverified approval date or decision ID.