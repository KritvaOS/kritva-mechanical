# QR-04 — Mass Budget Evidence Record (Week 3/4)

**Status: INCOMPLETE — system mass is UNKNOWN; no component-mass estimate is supported by the available sources.** HOLD D-003 remains active.

## Published target (not a derived mass)

The source concept README prints a robot mass target of 5–7 kg (est.). It is an unapproved CONCEPT_TARGET copied from illustrative artwork, not an independently calculated estimate, measured mass, or basis for allocating component masses. See [README.md, section 4](README.md#4-concept_target), [ARCHITECTURE.md](ARCHITECTURE.md), and [references/SOURCE_REGISTER.md](references/SOURCE_REGISTER.md) SRC-01–SRC-04.

## Traceable subsystem breakdown

| Subsystem | Source-backed configuration | Mass contribution | Evidence needed before calculating |
|---|---|---|---|
| central body/chassis | See source README/ARCHITECTURE; quantities or options only as printed | UNKNOWN | Released geometry, selected material, exact component part numbers and source-controlled mass data |
| four three-joint long legs | See source README/ARCHITECTURE; quantities or options only as printed | UNKNOWN | Released geometry, selected material, exact component part numbers and source-controlled mass data |
| four feet | See source README/ARCHITECTURE; quantities or options only as printed | UNKNOWN | Released geometry, selected material, exact component part numbers and source-controlled mass data |
| compute, drivers and power | See source README/ARCHITECTURE; quantities or options only as printed | UNKNOWN | Released geometry, selected material, exact component part numbers and source-controlled mass data |
| battery and adjustable sensor module not fully defined | See source README/ARCHITECTURE; quantities or options only as printed | UNKNOWN | Released geometry, selected material, exact component part numbers and source-controlled mass data |
| harness, fasteners and indicated mounting interface | See source README/ARCHITECTURE; quantities or options only as printed | UNKNOWN | Released geometry, selected material, exact component part numbers and source-controlled mass data |
| System total / low–nominal–high range | No source-backed component values are available | UNKNOWN — no subtotal computed; unknowns are not treated as zero | Verified component list, mass source per line, and mass/CoM datum |

The family-level actuator specification provides provisional torque bands and proposed roles; it does not provide variant-specific actuator masses. The concept artwork does not provide thicknesses, link sections, enclosure geometry, board models, battery selection or component masses. Therefore no subsystem mass, CoM, or total can be derived from this record. The printed target is not used as a measured load input.

## Required evidence

- Controlled component list and selected actuator variants, with revisioned mass data.
- Dimensioned, approved geometry plus selected material and density source for fabricated parts.
- Exact board, battery, sensor, gripper, fastener and harness part data.
- Confirmation of what the printed target includes (payload, battery, sensors, cables and optional modules).

References: README.md section 4; ARCHITECTURE.md sections 2–3 and 8; calculations/WEEK2_ARCHITECTURE_CHECKS.md; [references/SOURCE_REGISTER.md](references/SOURCE_REGISTER.md) SRC-01–SRC-07. Until those inputs exist, the mass result remains UNKNOWN.