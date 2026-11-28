# QR-02 — Actuator screen

**Status:** PROPOSED / ESTIMATE; no actuator selected. D-003 remains active. See [CALC-QR02-01_leg_torque.md](calculations/CALC-QR02-01_leg_torque.md) for load assumptions and exact arithmetic.

## Role and load screen

The proposed family spec assigns S to wrist/neck, M to elbow/reference and L to hip/knee. It is a role proposal; the S/L figures are placeholders. QR-02 has hip abduction, hip flexion and knee joints, so the literal family mapping would label all twelve axes L. The calculated static one-leg screen at 6.30 kg is 8.34 Nm worst-case at hip flexion after 1.5× headroom; the source role’s proposed L band is 25–40 Nm continuous.

| Joint class | 1.5× screen Nm | Proposed family role | 10 Nm Makiina load screen |
|---|---:|---|---|
| Hip flexion | 6.49–8.34 | L | Clears paper static screen; below role torque band. |
| Hip abduction/yaw | 1.65–2.47 | L | Clears paper static screen; below role torque band. |
| Knee flexion | 2.89–4.34 | L | Clears paper static screen; below role torque band. |

## Sourced references

| Product reference | Rated continuous torque | Speed | Mass | Published price | Interpretation |
|---|---:|---:|---:|---:|---|
| Makiina medium | 10 Nm | up to 75 rpm | 0.240 kg | USD 90 | Load-only economy case; not within L role. |
| HEBI T8-16 | 16 Nm | 15 rpm | 0.575 kg | Not listed | Below proposed L torque band; 15 rpm is below the 19.1 rpm planning comparison speed. |
| CubeMars AK10-9 V3.0 | 18 Nm | Product listing | 0.940 kg | USD 698.90–798.90 | Below L band and requires 48 V, against 24 V concept direction. |
| T25-40 third-party profile | 40 Nm reported | 23 rpm reported | 1.50 kg reported | USD 4,500 reported | Flowntro says HEBI has not confirmed the profile; stress case only, not a verified HEBI product offer. |

The 10 Nm modules clear only the modeled static load screen. Continuous gait, impact, thermal duty, acceleration, and voltage/power integration are not demonstrated by this comparison. The 40 Nm listing is not used to assert product availability or validated rating. Source details and confidence are in [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).