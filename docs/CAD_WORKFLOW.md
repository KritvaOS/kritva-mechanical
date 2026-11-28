# Kritva Mechanical CAD Workflow

Status: PROPOSED
Implementation Gate: HOLD (D-003)
Owner Approval: PENDING
Draft: v2, 2026-11-28 (reviewed against ChatGPT's check of main)
Intended path: `docs/CAD_WORKFLOW.md` in KritvaOS/kritva-mechanical
Maintenance: owner-maintained. This is not an intern deliverable (INTERN_ASSIGNMENTS section 5 bars interns from editing common documents).

## 1. Purpose and Scope

Describe the CAD methodology Kritva intends to follow if and when CAD is authorized, so that no tool, convention or format is decided by accident before then. The policy is independent of which of the six dual-arm (DA-01..06) and six quadruped (QR-01..06) concepts is eventually shortlisted. It is not a decision about which architecture to implement.

## 2. Current Governance Constraints

This document defines a proposed future engineering workflow. It does not authorize CAD implementation, geometry creation, simulation, component selection, design release, or any activity prohibited by D-003. D-003 (Mechanical work on HOLD: CAD, actuators, BOM, quotes, procurement, fabrication, prototype, design freeze; status Accepted) is recorded in [kritva-program v2/DECISIONS.md](https://github.com/KritvaOS/kritva-program/blob/main/v2/DECISIONS.md). D-052 lifted the hold for the actuator workstreams only (ACT_S, ACT_M, ACT_L, ACT_EMB, ACT_INT, run in the actuator repositories); it does not cover robot-level CAD. The restatements in AGENTS.md and STUDY_PLAN.md apply. No CAD application may be used to create Kritva robot geometry, including training or demonstration geometry, until the owner explicitly authorizes that activity.

| Activity | Current status |
|---|---|
| Documentation and paper analysis | Permitted within study scope |
| Reading public CAD tool documentation | Permitted |
| Comparing tool capabilities from public documentation | Permitted |
| CAD geometry generation | HOLD |
| CAD training exercises that generate geometry | HOLD |
| CAD-derived mass, inertia or CoM | HOLD |
| FEA and CAD-based simulation | HOLD |
| Actuator, bearing, slip-ring selection | Paper analysis only; no selection or commitment |
| Final BOM, supplier quotations | HOLD |
| Procurement, fabrication, prototypes | HOLD |

Feasibility evidence stays paper-based. Mass estimates (CP3-07) and major component categories (CP3-08) are satisfied by paper estimates and categories, not CAD properties or final selections. Week-4 plans that mention CAD mass properties, component selection or FEA are paper-only analysis while the hold is in force.

## 3. CAD Engineering Principles

1. Tool independence: no single CAD application is mandatory for contributors.
2. Native source ownership: the originating tool's native file is authoritative for that component.
3. Neutral exchange: exchange files carry geometry between tools; they never replace the source.
4. Traceability: every released component has an identity, revision, source and approval status.
5. Human review: automated checks never substitute for engineering review. A model that renders is not evidence of feasibility or safety.

## 4. Supported CAD Ecosystem (candidates; none selected)

| Tool | Possible role | Status |
|---|---|---|
| OpenSCAD | Simple scripted CSG parts | Candidate; not default |
| CadQuery | Python parametric solids, STEP export | Candidate for evaluation |
| build123d | Python parametric solids on OpenCascade, STEP export | Candidate for evaluation |
| FreeCAD (GUI and Python API) | Integration, assemblies, drawings; possible native modelling | Candidate |
| KiCad | PCB and electronics, STEP/IDF mechanical export | Candidate |
| SolidWorks, Creo, NX, CATIA | External or consultant work via neutral exchange | Accepted for collaboration |

## 5. CAD Tool Selection Policy

No primary code-CAD tool is selected, and OpenSCAD is not assumed as the default. A detailed weighted comparison belongs in a separate follow-up document (`docs/CODE_CAD_TOOL_EVALUATION.md`), not in this PR, and is paper-based using public documentation. It must not become a reason to assign CAD exercises to interns.

Three capabilities are kept distinct and not treated as interchangeable:

1. Exact solid geometry generation.
2. Assembly hierarchy and component positioning.
3. Mechanical mate/constraint solving and kinematic simulation.

| Capability | OpenSCAD | CadQuery | build123d | FreeCAD |
|---|---|---|---|---|
| Parametric source | Yes | Yes | Yes | Yes |
| Native STEP export | No | Yes | Yes | Yes |
| Assembly hierarchy and positioning | Limited | Yes | Yes | Yes |
| Mechanical constraint solver | No | Not a native strength | Not a native strength | Assembly workbench |
| Kinematic simulation | No | No | No | Needs a separate simulation workflow |
| Git-friendly source | Excellent | Excellent | Excellent | Limited (binary document) |
| Headless automation | Yes | Yes | Yes | Possible; version/workbench dependent |

Tool-specific qualifications (to be source-checked before merge):

- CadQuery: documentation confirms STEP export for solids and assemblies. Default assembly export auto-generates object names and does not preserve assigned names; additional metadata mechanisms exist.
- build123d: documentation confirms STEP export of shapes and assemblies, including labels and colours. It does not establish a commercial-CAD-style constraint or kinematic solver.
- FreeCAD: STEP import does not recover the source tool's feature history, sketches or constraints. Its OpenSCAD workbench converts input to CSG, discarding variable names and expanding loops, so parametric behaviour is lost. An STL converted to a solid is faceted, not the original analytic features.
- OpenSCAD: no native STEP export; standard exports are STL, 3MF, DXF, SVG and CSG.

Future evaluation criteria and weights (proposed for owner review, not approved): STEP fidelity and interoperability 20%; parametric modelling and reusable components 15%; assembly structure, positioning and constraints 15%; Git review-friendliness and reproducibility 10%; headless/CI support 10%; FreeCAD and commercial-CAD interoperability 10%; modelling capability and maturity 10%; intern learning curve and documentation 5%; licensing and dependencies 5%. Mandatory pass/fail checks apply regardless of score: exports a valid STEP solid, exchanges units correctly, preserves required assembly structure, reproduces geometry from a clean environment, acceptable open-source licence, fits the approved toolchain. A weighted score cannot compensate for a failed pass/fail check.

## 6. Authoritative Source and Exchange Formats

| Item | Policy |
|---|---|
| Native source (.scad, Python script, .FCStd, .SLDPRT/.SLDASM, KiCad project) | MUST be retained; authoritative |
| Neutral solid exchange | STEP (proposed) |
| STEP application protocol | OWNER-TBD pending interoperability tests |
| AP242 | Candidate for evaluation; not mandated |
| AP214 | Compatibility candidate |
| STL | Mesh only; MUST NOT be an authoritative solid source |
| 3MF | Mesh-based manufacturing exchange |
| DXF | 2D profiles |
| PDF | Released drawings |
| IDF | PCB mechanical exchange, subject to KiCad workflow validation |

A tool supporting STEP does not imply support for all AP242 capabilities (FreeCAD issue #19795 describes incomplete AP242 support). Before selecting a profile, a future paper-first test plan would cover CadQuery to FreeCAD, build123d to FreeCAD, FreeCAD to SolidWorks and back, and FreeCAD to Creo or NX where available, checking geometry, assembly hierarchy, names, colours, units and placements separately. Do not claim PMI, feature history, constraints or kinematics survive because a STEP file imports. Source-to-export traceability (each exchange file names source file, tool, version and revision) is required once CAD is authorized; the manifest format is deferred.

## 7. Engineering Units and Coordinate Systems

- Units: OWNER-TBD. Current feasibility documents work in mm, deg, kg, N, N.m, but that is not an approved standard.
- Robot coordinate convention: OWNER-TBD. No forward/left/up convention is proposed until the existing dual-arm and quadruped concept frames are reconciled. DA-02, DA-03 and QR-01 axis directions are recorded as assumed, and DA-02's side and top views use different frames.
- Dual-arm reference frames: OWNER-TBD.
- Quadruped reference frames: OWNER-TBD.

## 8. Component Identification and Revision

Reuse the existing A0/A1 hardware-version and P0/P1 phase conventions unchanged. A component ID format and revision scheme are not approved; any examples used in discussion are illustrative only.

## 9. Multi-CAD Exchange Workflow (future, not authorized)

1. Contributor works in their own tool and keeps native source.
2. Contributor exports STEP (and DXF/PDF as needed) with a source reference.
3. Integrator imports for inspection without overwriting the contributor's source.
4. A reviewer checks re-import fidelity; feature history is not expected to survive exchange.
5. Electrical/mechanical fit uses KiCad STEP or IDF exports reviewed by both disciplines.

## 10. Engineering Review and Verification

These are future implementation controls. They do not imply implementation has started or that any design is available for review or acceptance. Checks cover geometry validity, interface and dimension conformance, interoperability, unit and frame conformance, and traceability. Human engineering review is mandatory. Future automated validation cannot authorize or approve a design, and structural, clearance, actuator-compatibility and manufacturing judgments remain with engineers.

## 11. CAD Implementation Gate

- Default: HOLD.
- Feasibility completion is not implementation authorization. The study route is CP3 engineering review, CP4 final feasibility review and the G4 owner decision. CP3 PASS and CP4 completion do not release D-003.
- No activity may begin based solely on a checkpoint result, a merged PR, an intern recommendation, a passing CI run or a tool evaluation.
- CAD implementation may start only after a separate, explicit owner decision recorded in kritva-program that: identifies the architecture and implementation scope; explicitly authorizes CAD implementation; states which D-003 restrictions are lifted; and preserves every restriction not explicitly released. All other activities remain HOLD.
- The local record of such a decision is ROB-MECH-052 in planning/TASKS.md; recording it does not itself lift D-003. CAD tasks ROB-MECH-020 and 022 to 026 stay BLOCKED until a program decision reopens robot mechanical work.
- Decisions needed for the specifically authorized scope must be resolved or explicitly accepted as TBD. Unrelated decisions need not be closed first.

## 12. Repository and GitHub Workflow

Existing rules apply unchanged and are not restated or replaced here: AGENTS.md, `.github/PULL_REQUEST_TEMPLATE.md` (which already prohibits starting CAD under the hold) and `scripts/security/check_commit_format.py` (conventional commit, one Task/Tasks footer, no Claude-Session trailer). No parallel enforcement infrastructure is introduced.

## 13. Programme Governance

kritva-program is authoritative for decisions, approvals and gate records. This document links to them and creates no competing approval or task register.

## 14. Open Decisions

| Decision | Status |
|---|---|
| Primary code-CAD tool (CadQuery, build123d, other) | OWNER DECISION |
| Role of OpenSCAD | OWNER DECISION |
| FreeCAD integration workflow | PROPOSED |
| STEP application protocol profile | OWNER-TBD pending tests |
| Supported CAD tool versions | OWNER-TBD |
| Interoperability test requirements | PROPOSED |
| Standard units | OWNER-TBD |
| Dual-arm coordinate frame | OWNER-TBD |
| Quadruped coordinate frame | OWNER-TBD |
| Whether any tool familiarization with generated geometry is allowed before the gate lifts | OWNER DECISION (default: no) |
| CAD implementation authorization | HOLD |

Deferred until separately authorized: component manifest and schema, CODEOWNERS, new GitHub Actions or validation scripts, intern training documents and exercises, cad/ and integration/ directories. A follow-up `docs/CODE_CAD_TOOL_EVALUATION.md` is planned after this policy is reviewed.

## 15. References

- Repo: AGENTS.md, feasibility/STUDY_PLAN.md (sections 3 and 14), feasibility/INTERN_ASSIGNMENTS.md, feasibility/EVALUATION_CRITERIA.md, feasibility/reviews/CP3_ENGINEERING_REVIEW.md, PR template, scripts/security/check_commit_format.py.
- kritva-program: [v2/DECISIONS.md](https://github.com/KritvaOS/kritva-program/blob/main/v2/DECISIONS.md), rows D-003 (mechanical HOLD) and D-052 (actuator-only lift); D-053 (commit format).
- Repo: CONTRIBUTING.md, planning/TASKS.md (CAD tasks ROB-MECH-020, 022 to 026 are BLOCKED; ROB-MECH-052 records any owner decision on CAD/BOM follow-up).
- Public documentation to source-check before merge: OpenSCAD manual, CadQuery assembly/STEP docs, build123d import/export docs, FreeCAD OpenSCAD workbench and import/export docs, FreeCAD issue #19795, KiCad 3D export docs, SolidWorks STEP docs, prostep AP242 overview.
