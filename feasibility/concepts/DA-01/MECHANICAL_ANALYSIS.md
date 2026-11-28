# DA-01 — Mechanical Evidence Status (Week 3/4)

**Status:** INCOMPLETE — qualitative configuration review only. HOLD D-003 active.

## Source-backed configuration

Two 3-DOF arms on a fixed tabletop base are transcribed from the concept README/artwork. Printed dimensions (including the 300 × 250 mm base and 350 mm shoulder-to-gripper reach) are CONCEPT_TARGETs; the drawings are not to scale and do not define joint frames, pose, material thickness or support conditions. See README.md sections 2, 4, 6 and 9; ARCHITECTURE.md sections 2–3.

## Load path and missing stability inputs

Qualitative load path: payload/gripper → wrist → forearm → elbow → upper arm → shoulder → central body/base → tabletop support. This is a configuration description, not a verified load case.

No sourced component masses, CoM coordinates, material sections, fastener details, friction coefficient, fixture/clamp design, joint pose or allowable overturning margin are available. The printed mass/payload targets do not fill those gaps. Stability and tipping moment are therefore UNKNOWN; no tipping margin, likelihood, clamp recommendation or safety factor is reported.

## Structural and workspace status

Link sections, material grades, wall thicknesses, joint offsets, ROM, cable drag and stiffness data are absent. Workspace, collision, stress and deflection remain qualitative/TBD. The source README records a reach/overall-width pose ambiguity; no geometry is inferred to resolve it.

## Evidence status

| Topic | Status | Source / next input |
|---|---|---|
| Configuration and DOF | Transcribed CONCEPT_TARGET | README.md / ARCHITECTURE.md |
| Joint loads and speed | TBD; no numeric per-joint load is defensible from current baseline inputs | ACTUATOR_ANALYSIS.md and CALC-DA01-01 |
| Mass and CoM | UNKNOWN | MASS_BUDGET.md; source-controlled component masses/geometry needed |
| Table support and stability | UNKNOWN | OPEN_QUESTIONS.md; support condition, mass distribution and pose needed |
| Cost | UNKNOWN | COST_MODEL.md; priced BOM required |

References: references/SOURCE_REGISTER.md SRC-01–SRC-06; calculations/WEEK2_ARCHITECTURE_CHECKS.md. No simulation, bench or physical evidence is claimed.
