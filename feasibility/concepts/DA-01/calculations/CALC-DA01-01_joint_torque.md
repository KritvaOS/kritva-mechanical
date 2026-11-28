# DA-01 — Joint-Load Evidence Check

| Property | Value |
|---|---|
| Status | INCOMPLETE — no numeric joint torque is defensible from the available baseline inputs |
| Date | 2026-11-28 |
| Evidence | C — source review and symbolic relations only |
| HOLD | D-003 active |

## Source inputs and limits

The concept README prints 350 mm shoulder-to-gripper reach and 0.1–0.2 kg per-arm payload, both as CONCEPT_TARGETs; the payload is marked “est.” with no method. The three-DOF baseline is labeled shoulder yaw, elbow and wrist. The source does not provide joint frames, dimensions/offsets, representative pose, link/gripper masses, centre of mass, speed, acceleration or duty. See [README.md](../README.md), [ARCHITECTURE.md](../ARCHITECTURE.md) and [SOURCE_REGISTER.md](../references/SOURCE_REGISTER.md), SRC-01–SRC-04.

## Joint-load disposition

- Shoulder yaw: in an ideal vertical-axis static model, gravity has no moment component about the yaw axis. This does not establish dynamic yaw torque; inertia, friction, cable/external loads and axis alignment remain UNKNOWN.
- Elbow and wrist: a numeric gravity moment requires sourced link/payload perpendicular distances and component masses. They are absent, so no number is reported.
- Payload-only relation for a defined pitch axis: τp = mp g r⊥. The concept baseline does not define a pitch axis or r⊥ for a load case. Therefore the printed payload and reach are not combined into a torque estimate for this baseline.

No assumed arm mass, link split, angular acceleration, speed, multiplier or actuator rating is used. The printed payload/reach remain target data, not verified load inputs.

## Remaining evidence needed

Controlled joint axes and frames, dimensioned links, component masses/CoM, payload placement, representative poses, operating motion/duty, friction/cable loading and output-side actuator data. See ACTUATOR_ANALYSIS.md, MASS_BUDGET.md and OPEN_QUESTIONS.md.

## References

- [Concept README](../README.md), sections 4, 6 and 9; [ARCHITECTURE.md](../ARCHITECTURE.md), sections 2–3 and 8.
- [Source register](../references/SOURCE_REGISTER.md), SRC-01–SRC-07.
- [DESIGN_GUIDELINES.md](../../../DESIGN_GUIDELINES.md), FREQ-006/007/012.
