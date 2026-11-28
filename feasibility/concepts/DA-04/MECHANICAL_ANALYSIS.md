# DA-04 — Mechanical Evidence Status (Week 3/4)

**Status:** INCOMPLETE — qualitative configuration review only. HOLD D-003 active.

## Source-backed configuration

The concept record describes a mobile humanoid with two four-DOF arms and a differential-drive base with two drive channels. Four wheels are shown; the source also prints a 25–35 kg (est.) target mass, a 0.5–1.0 kg (est.) per-arm payload and a 450 mm reach. These are CONCEPT_TARGETs, not measured or independently derived inputs. See README.md sections 2, 4, 6 and 9; ARCHITECTURE.md sections 2–3.

## Load paths and stability

Qualitative arm load path: gripper/payload → wrist → elbow → shoulder → torso → mobile base/support. Drive loads pass through wheel/tyre, drive channel and base structure. No approved component masses, CoM, wheel radius, track, load distribution, friction, slope, acceleration or travel-speed inputs are available. The battery is not drawn in the source artwork.

No tipping moment, drive torque, traction margin or stability result is calculated. Arm payload torque is limited to the conditional payload-only shoulder-pitch case in CALC-DA04-01; it is not a complete joint load. No operating slope or clamp/fixture recommendation is made.

## Structure and packaging

Material/process callouts on the artwork are illustrative options. No selected material, section, tolerance, wheel geometry, interface allowables, battery package or released dimensions exist for calculation. Stress, deflection, packaging, cable flex and collision remain UNKNOWN/TBD.

## Evidence status

| Topic | Status | Source / next input |
|---|---|---|
| Configuration and actuator count | Transcribed CONCEPT_TARGET | README.md / ARCHITECTURE.md |
| Arm joint loads | TBD except conditional payload-only term | ACTUATOR_ANALYSIS.md and CALC-DA04-01 |
| Base drive torque and stability | UNKNOWN | Wheel radius, contact/load distribution, friction, operating case and CoM required |
| Mass and cost | UNKNOWN | MASS_BUDGET.md and COST_MODEL.md |

References: references/SOURCE_REGISTER.md SRC-01–SRC-06; no dynamic, simulation, bench or physical evidence is claimed.
