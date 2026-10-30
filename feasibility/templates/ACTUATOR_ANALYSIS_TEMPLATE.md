# [Concept ID] — Actuator Analysis

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-XXX |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Joint and Actuator Feasibility Analysis |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | TBD |
| Version | 0.1.0 |
| Last Updated | 2026-10-30 |
| Authority | Preliminary paper analysis; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `feasibility/DESIGN_GUIDELINES.md` |

## 1. Scope and Assumptions

- Concept ID: TBD
- Supply direction: 24V DC investigation only
- Motor direction: BLDC/PMSM
- Actuator architecture: S/M/L
- Duty and operating assumptions: TBD

## 2. Per-Joint Assessment

| Joint | Load case | Peak torque | Continuous torque | Speed | Range | Duty assumptions | Calculation reference | S/M/L compatibility | Margin | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

Use explicit units. Mark calculated values and estimates clearly. Derive requirements independently for every joint.

## 3. Reference Limitations

The elbow discussion reference of 24V, 10 N·m continuous and 20 N·m peak is not a universal specification. Do not copy it to other arm or leg joints.

## 4. Actuator Source Traceability

For any input from `kritva-actuator`, record:

- Source repository and path: TBD
- Revision / commit: TBD
- Source document or specification: TBD
- Maturity: UNKNOWN (prototype / preliminary / released / other, if established)
- Verification status and limitations: TBD

Do not treat preliminary repository values as validated specifications.

## 5. Findings and Open Items

- Torque/speed feasibility: TBD
- S/M/L mapping rationale: TBD
- Margin interpretation: TBD
- Missing inputs and risks: TBD

## 6. HOLD D-003

Paper calculations and compatibility assessment only. No actuator purchase, detailed CAD, final BOM, fabrication, assembly or physical testing. All require explicit owner decision under HOLD D-003.
