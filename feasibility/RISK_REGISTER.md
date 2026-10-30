# Feasibility Study Risk Register

| Property | Value |
|---|---|
| Document ID | KMECH-FS-006 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Study-Level Risk Register |
| Status | PROPOSED |
| Owner | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Proposed study risk register; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/INTERN_ASSIGNMENTS.md`, `feasibility/DESIGN_GUIDELINES.md`, `feasibility/EVALUATION_CRITERIA.md`, `feasibility/REQUIREMENTS_REGISTER.md` |

## 1. Purpose and Rating Conventions

This register tracks risks affecting the four-week mechanical feasibility study and its recommendations. Likelihood and impact ratings are preliminary qualitative estimates, not measured probabilities or validated risk assessments.

- **Low:** Limited effect; manageable within normal study activities.
- **Med:** Meaningful effect; may require rework, additional analysis or owner attention.
- **High:** Could invalidate a feasibility conclusion, cause significant schedule/budget impact, create a safety concern or breach governance constraints.

Risk ratings are recorded as `ESTIMATE`. Reviewers must update ratings when evidence changes. Risk status remains `OPEN` until an owner-reviewed disposition is recorded.

## 2. Risk Register

| ID | Risk | Category | Cause | Impact | Likelihood | Impact rating | Mitigation | Owner | Status | Linked requirements / open items |
|---|---|---|---|---|---|---|---|---|---|---|
| FRISK-001 | Legged-joint torque may exceed S/M/L actuator capability. | technical | Ground reaction and dynamic loads may exceed preliminary actuator assumptions. | Legged concepts may be infeasible or require architecture changes. | Med (ESTIMATE) | High (ESTIMATE) | Derive joint loads and torque/speed requirements; assess margins and S/M/L compatibility. | Assigned concept intern / Dinesh | OPEN | FREQ-012, FREQ-013, FREQ-031; U-007, U-008 |
| FRISK-002 | Two-DOF leg configurations may not meet required mobility or stability. | technical | Restricted joint motion and workspace. | Reduced locomotion capability or unsuitable demonstration. | Med (ESTIMATE) | Med (ESTIMATE) | Document kinematic limitations and representative support configurations; compare with three-DOF concepts. | Assigned concept intern | OPEN | FREQ-029, FREQ-030, FREQ-031; U-006 |
| FRISK-003 | Actuator availability and cost may be incompatible with the INR 2,00,000 planning ceiling. | budget | Inventory, supplier availability and actual pricing are unknown. | Cost feasibility cannot be established or hardware scope may be constrained. | High (ESTIMATE) | High (ESTIMATE) | Separate estimates from verified costs; identify cost-sensitive components and missing evidence. | Dinesh | OPEN | FREQ-032, FREQ-033; U-009, U-011 |
| FRISK-004 | Three interns may produce inconsistent calculation quality. | data | Different assumptions, methods, units and levels of engineering experience. | Concept comparisons may be misleading or require substantial rework. | Med (ESTIMATE) | High (ESTIMATE) | Use common calculation conventions, templates, cross-intern review and owner review of critical calculations. | Dinesh | OPEN | FREQ-005, FREQ-006, FREQ-007 |
| FRISK-005 | Actuator inputs from `kritva-actuator` may be unverified or preliminary. | data | Repository values may represent assumptions, prototypes or incomplete specifications. | Incorrect torque, speed, mass or cost assumptions may distort feasibility. | Med (ESTIMATE) | High (ESTIMATE) | Record source and revision; classify inputs as preliminary until independently confirmed. Do not treat repository values as validated specifications. | Dinesh / assigned concept interns | OPEN | FREQ-012, FREQ-013; U-007, U-008, U-009 |
| FRISK-006 | Study scope may expand into CAD, BOM finalization or procurement. | governance | Pressure to progress from feasibility into implementation. | Violation of mechanical HOLD D-003 and unauthorized commitments. | Med (ESTIMATE) | High (ESTIMATE) | Keep work paper-based; prohibit CAD, final BOM, quotations and procurement without explicit owner decision. | Dinesh | OPEN | FREQ-002, FREQ-034; U-011, U-012 |
| FRISK-007 | Paper estimates or calculations may be overstated as validated engineering evidence. | governance | Confusion between calculation, estimate, simulation, bench and physical evidence. | False confidence in concept readiness or safety. | Med (ESTIMATE) | High (ESTIMATE) | Label evidence types accurately; distinguish estimates from sourced values; prohibit validation claims without corresponding authorized evidence. | Dinesh / all interns | OPEN | FREQ-006, FREQ-007, FREQ-008 |
| FRISK-008 | Hexapod and mobile concepts may be scored unfairly against simpler concepts. | data | Greater complexity may be penalized, or demonstration potential may be overstated. | Shortlist may reflect scoring bias rather than evidence-based feasibility. | Med (ESTIMATE) | Med (ESTIMATE) | Apply common criteria; record concept-specific assumptions; use independent cross-intern validation and weight sensitivity checks. | Dinesh / reviewers | OPEN | FREQ-001; U-001, U-006 |
| FRISK-009 | Evaluation weights may be tuned retrospectively to favour preferred concepts. | governance | Pressure to achieve a desired ranking or shortlist. | Evaluation loses objectivity and reproducibility. | Low (ESTIMATE) | High (ESTIMATE) | Freeze proposed baseline weights before scoring; document alternatives and sensitivity results; do not change weights to favour a concept. | Dinesh | OPEN | FREQ-001; U-001 |
| FRISK-010 | EtherCAT integration claims may be unsupported by mechanical interface evidence. | technical | Controller, wiring, connector, packaging and integration details remain TBD. | Platform integration feasibility may be overstated. | Med (ESTIMATE) | Med (ESTIMATE) | Treat EtherCAT as the existing architecture direction; document conceptual provisions and unresolved interfaces without claiming validation. | Assigned concept intern / Dinesh | OPEN | FREQ-024, FREQ-025; U-002 |
| FRISK-011 | Payload and reach requirements remain ambiguous. | data | No confirmed payload or arm reach values are available. | Structural, actuator and workspace calculations may be incomplete or incomparable. | High (ESTIMATE) | High (ESTIMATE) | Keep payload and reach UNKNOWN; document required inputs and use clearly labelled scenarios only when justified. | Dinesh | OPEN | FREQ-020, FREQ-026, FREQ-027; U-004, U-005 |
| FRISK-012 | Concept mass may be underestimated. | technical | Incomplete component breakdown, cabling, power, structure or actuator mass data. | Cost, actuator loading and stability conclusions may be invalid. | Med (ESTIMATE) | High (ESTIMATE) | Build traceable mass budgets; identify exclusions and uncertainty; avoid unsupported point estimates. | Assigned concept intern | OPEN | FREQ-015, FREQ-019, FREQ-027; U-003 |
| FRISK-013 | Parallel intern branches may create merge conflicts or overwrite work. | schedule | Shared files, inconsistent branch practices or simultaneous edits. | Lost work, integration delays and inconsistent documentation. | Med (ESTIMATE) | Med (ESTIMATE) | Restrict ownership to assigned concept folders; keep common documents owner-controlled; review changes before merge. | Dinesh / all interns | OPEN | FREQ-001, FREQ-004 |
| FRISK-014 | Future physical work may introduce mechanical hazards not addressed by paper analysis. | safety | Unverified structural limits, pinch points, unstable configurations or actuator behaviour. | Injury or equipment damage during later implementation. | Med (ESTIMATE) | High (ESTIMATE) | Record hazards and safeguards as open requirements; require separate owner authorization, detailed safety review and appropriate validation before physical work. | Dinesh | OPEN | FREQ-018, FREQ-030, FREQ-031; U-012 |

## 3. Risk Review Cadence

Update this register at each formal checkpoint:

- **CP2 — Architecture review:** Review configuration, DOF, interfaces, requirements ambiguity, scope and documentation risks.
- **CP3 — Engineering review:** Reassess actuator capability, loading, stability, mass, cost and calculation-quality risks.
- **CP4 — Final feasibility review:** Reassess all risks, evidence gaps, shortlist sensitivity, hard gates and future-work safety dependencies.

At each review:
1. Reassess likelihood and impact as `Low`, `Med` or `High`, retaining the `ESTIMATE` designation.
2. Record new risks and changes to existing risk descriptions.
3. Update mitigation actions, owner and linked requirements/open items.
4. Record evidence and rationale for any proposed closure.
5. Keep unresolved risks `OPEN`; do not close risks solely because the study has ended.

## 4. Governance and Closure

- Interns may identify risks and propose mitigation or register changes.
- The owner controls changes to this common register and approves risk dispositions.
- A risk closure requires documented evidence and owner review.
- An accepted risk must remain visible with its rationale and owner decision.
- No risk rating, mitigation or checkpoint outcome overrides HOLD D-003.
- Physical implementation risks require a separate review before any future physical activity is authorized.
