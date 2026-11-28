# INTERN-01 — Week 3/4 cross-concept comparison note

**Status:** PROPOSED partial comparison | 2026-11-28 | HOLD D-003 active

This note compares only DA-01, QR-02, DA-04 and QR-04 using the current paper estimates. Torque figures are the largest 1.5× planning screens in each concept’s calculation, but their poses and load bases differ. None is a continuous actuator rating or validated peak.

| Metric | DA-01 | QR-02 | DA-04 | QR-04 |
|---|---|---|---|---|
| Joint actuator count | 6 | 12 | 10 | 12 |
| Largest 1.5× joint planning screen | 4.77 Nm conditional shoulder-pitch branch; baseline elbow 1.33 Nm | 8.34 Nm hip flexion, 6.30 kg full robot on one leg | 14.64 Nm shoulder pitch at 1.0 kg payload | 11.31 Nm hip flexion at 7.43 kg; 11.42 Nm at rounded 7.50 kg |
| Mass scenario | 6.33 kg nominal, camera and two grippers included | 6.30 kg sensor-excluded; optional camera raises to 6.40 kg | 20.59 kg 24 V economy; 26.19 kg 18 Nm arm scenario | 7.43 kg sensor-excluded; optional camera raises to 7.53 kg |
| Printed mass target | 5–8 kg | 4–6 kg | 25–35 kg | 5–7 kg |
| Economy cost scenario | ₹112,773 | ₹166,503 | ₹175,052 | ₹170,584 |
| Cost-compatible alternative | Six local AK80-8 listings: ₹746,480 | Load-only hybrid: ₹1,138,605; full 12-axis L-role lower bound: ₹1,624,657 | Two 18 Nm shoulder modules: ₹288,202 | Four-axis load-only upgrade: ₹396,885; full 12-axis L-role lower bound: ₹1,628,738 |
| Main constraint | Conditional axis/mounting and stability scenario | Proposed L role conflicts with 10 Nm economy case | 1 kg shoulder case and 24 V direction conflict | Upper hip-flexion screen and 5–7 kg target conflict |

All economy cost scenarios are under the ₹2,00,000 study ceiling, but they do not each meet the concept’s role/load screen. QR-02/QR-04 full L-role estimates pair two 18 Nm AK10-9 modules per joint to reach 36 Nm nominal sum; ideal torque addition/load sharing is assumed only for the price lower bound; couplers, mounts, 48 V integration, freight and customs are excluded. QR-02/QR-04 cost totals include the optional camera; their baseline mass totals exclude it. Costs exclude freight/customs on foreign actuator listings and are not quotes.

## Partial ranking within the four assigned concepts

Each proposed criterion now has a provisional score supported by an estimate or calculation. The resulting weighted values use 100% of the proposed weights for these four concepts. It is a partial ordering because the other eight concepts are not included; it is not a full 12-concept ranking or a final recommendation.

| Partial rank | Concept | Weighted contribution / 5 | Weight represented |
|---:|---|---:|---:|
| 1 | DA-01 | 3.45 | 100% |
| 2 | DA-04 | 2.85 | 100% |
| 3 | QR-02 | 2.80 | 100% |
| 4 | QR-04 | 2.40 | 100% |

The full rationale, scores, cost alternatives and independent hard-gate results are in [COMPARISON_MATRIX.md](COMPARISON_MATRIX.md). Criteria weights remain proposed, and CP4 still requires all 12 concepts, owner review and program approval.