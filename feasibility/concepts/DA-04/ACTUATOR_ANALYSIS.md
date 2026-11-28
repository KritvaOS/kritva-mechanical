# DA-04 — Actuator screen

**Status:** PROPOSED / ESTIMATE; no actuator selected. D-003 remains active. See [CALC-DA04-01_arm_drive_screen.md](calculations/CALC-DA04-01_arm_drive_screen.md).

## Arm load screen

The proposed family spec assigns S to wrist/neck, M to elbow/reference and L to hip/knee. It does not provide a validated arm-shoulder role assignment. Treat S as a wrist reference and M as an elbow/reference only; shoulder is evaluated against the measured product references rather than inventing a category.

| Joint | Largest 1.5× screen Nm | 0.5 kg case Nm | 1.0 kg case Nm |
|---|---:|---:|---:|
| Shoulder pitch | 14.64 | 9.81 | 14.64 |
| Elbow pitch | 5.32 | 3.28 | 5.32 |
| Wrist pitch | 1.28 | 0.68 | 1.28 |
| Shoulder yaw | 4.28 | 2.76 | 4.28 |

Makiina’s 10 Nm rated continuous module at 24 V clears the 0.5 kg shoulder case but does not clear the 1.0 kg 14.64 Nm screen. CubeMars AK10-9 V3.0 (18 Nm rated, 0.940 kg, 48 V) clears the modeled torque case but requires a different power direction. HEBI T8-16 is 16 Nm continuous, 0.575 kg, 15 rpm; it clears the torque screen at the stated speed, but is a 48 V product and the source concept’s 24 V direction remains. These are paper comparisons, not selections.

## Base drive

The Robokits listing reports a 24 V, 100 W, 25 rpm geared motor/driver, 2.050 kg and 280 kg·cm rated torque (27.46 Nm converted). The 1.5× wheel screen is 1.27–1.78 Nm per driven side for 25–35 kg, 50 mm radius, 5° slope and 0.5 m/s² acceleration. Speed at that radius is 0.131 m/s. Torque is ample in this simplified screen, while speed, braking, wheel traction, turning and thermal duty remain outside the claim. The quoted combo has a two-channel driver; two combos are conservatively priced, so the cost model may double-count driver electronics.

## Power and cost compatibility

The battery listing is 22.2 V nominal and the drive/low-cost arm listings specify 24 V; direct compatibility or needed regulation is not established, and no converter price is included. The 10 Ah battery case is a planning scenario, not a runtime guarantee. The 40 Ah source lacks a current-matched BMS price, so it is not treated as a complete alternative. The concept artwork states 24 V direction. The eight-module economy scenario uses 24 V Makiina; two shoulder AK10-9 upgrades yield a ₹288,202 pre-landing subtotal, over the ₹2,00,000 study ceiling. The product is 48 V. A 40 Ah battery listing is not treated as a compatible system: the source does not identify a current-matched BMS and it is excluded from the complete configuration estimate.

No actuator family or drive motor is selected. Ratings, candidate prices, links and confidence are in [WEEK3_SOURCE_REGISTER.md](../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md).