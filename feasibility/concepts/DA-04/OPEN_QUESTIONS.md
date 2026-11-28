# DA-04 — Bounded decision and review register

**Status:** Paper-stage estimates prepared; D-003 HOLD active. Each alternative is tied to a quantitative scenario; no source-owner decision is invented.

## Modeled branches

| Choice | Current modeled cases | Impact |
|---|---|---|
| Arm actuator voltage/torque | Eight 24 V Makiina 10 Nm modules or 48 V AK10-9 18 Nm modules | 10 Nm case misses the 1 kg shoulder screen; two shoulder upgrades raise cost above ceiling and change power direction. |
| Battery | Listed 10 Ah pack + 20 A BMS scenario | Runtime is not inferred. The 40 Ah seller listing is not treated as a complete system because no current-matched BMS is included in its source. |
| Drive set | Two listed 24 V, 100 W, 25 rpm motor/driver combos | Two combos are conservatively budgeted; each advertises a dual-channel driver, so electronics may be double-counted. |
| Operating point | 25–35 kg, 50 mm wheel, 5° slope, 0.5 m/s² | Screen gives 1.27–1.78 Nm per side at 1.5× and 0.131 m/s at 25 rpm. These are planning inputs, not selected requirements. |
| Arm payload | 0.5 kg and 1.0 kg at 450 mm reach | Largest 1.5× shoulder screen rises from 9.81 to 14.64 Nm. |

## Review register

- The 24 V economy mass case is 20.59 kg, below the printed 25–35 kg target; the 18 Nm arm scenario is 26.19 kg. High packaging case is 28.92 kg.
- Economy cost is ₹175,052 including a 24 V battery and drive listings, below the ₹2 lakh study ceiling but not compatible with 1 kg shoulder load screen. Two 18 Nm shoulder modules raise it to ₹288,202 before landed costs.
- A 30 kg centered-COM / 600 mm wheelbase illustrative case gives 88.29 Nm restoring moment; two 1 kg extended arms produce 13.81 Nm pitch moment in the simplified screen. This is an optimistic static comparison, not a tip-over pass.
- The source README states a 10-channel baseline and a date claim. This update does not restate the date as independently verified and does not add an invented decision ID.

CAD, BOM release, procurement, fabrication, assembly and physical tests remain prohibited by HOLD D-003. Independent review and acceptance remain separate.