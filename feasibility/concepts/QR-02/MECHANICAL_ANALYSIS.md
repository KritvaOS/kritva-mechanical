# QR-02 — Mechanical feasibility screen

**Status:** PROPOSED / ESTIMATE; no structural verification. D-003 remains active.

## Load path and packaging

Load path: body plate → hip abduction/flexion modules → 0.11 m upper/lower leg links → knee/ankle modules → feet. The paper mass scenario uses two 350×260 mm light panels, 0.880 m total 20×20×2 mm tube (0.342 kg bare at 0.389 kg/m), feet/brackets and fasteners. The 1.60 kg body/link/mount allowance assumes 1.5 mm 6061-equivalent panels plus brackets; that thickness is a modeling input, not a selected material or verified structure. Camera is optional and excluded from 6.30 kg nominal.

## Support/load-sharing screen

At 6.30 kg, weight is 61.80 N. Equal static four-foot sharing would be 15.45 N per foot. The torque calculation assigns all 61.80 N to one representative leg, four times the equal-share average. At 6.40 kg with the optional camera, the corresponding values are 62.78 N and 15.70 N. This is a conservative static load allocation, not a stability or gait result. Foot dimensions and support polygon are not specified, so no tipping margin is reported.

## Serviceability and risk

The compact 4–6 kg target is challenged by the 6.30 kg nominal estimate before the optional camera. Wiring, foot sensors and hip-axis crossing require clear routing; every added distal sensor adds mass that increases the knee moment. The low-cost 10 Nm actuator passes the modeled static torque screen but not the proposed L role. That mismatch and mass-over-target result are the main mechanical feasibility risks. A rigid foot sensor, LiDAR or additional payload is not silently counted in the baseline.

## Evidence boundary

The 1.5 mm panel, leg split, joint-axis offsets, foot contact, equal-sharing comparison and one-leg load case are assumptions. No section stress, buckling, fastener pull-out, gait, traction, center-of-mass or tipping analysis is claimed. An impact case is outside the static screen rather than assigned a zero load.