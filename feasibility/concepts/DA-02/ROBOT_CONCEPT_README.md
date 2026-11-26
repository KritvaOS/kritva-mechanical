# DA-02 — Humanoid Torso Dual-Arm

| Property | Value |
|---|---|
| Document ID | KMECH-CONCEPT-DA-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Overview |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.4.0 |
| Last Updated | 2026-11-25 |
| Authority | Feasibility study; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `COST_MODEL.md`, `docs/images/ARTWORK_MANIFEST.json` |

This overview records the concept as printed on the two artwork sheets and the state of the preliminary paper work. All printed values are CONCEPT_TARGET (indicative, unapproved). All calculated values are ESTIMATES. Nothing here approves any value.

## 1. Concept Identification

- Concept ID: DA-02
- Concept name: Humanoid Torso Dual-Arm
- Family: Dual-arm
- Complexity: Medium (relative engineering category, not a validated assessment)
- Assigned intern: INTERN-02
- Assessment revision: Draft 1 (preliminary paper analysis, owner review pending)

## 2. Concept Summary

- **Intended configuration:** Two symmetric 4-DOF arms (shoulder yaw, shoulder pitch, elbow pitch, wrist pitch) on a fixed humanoid torso, mounted on a fixed base plate with no mobility. Optional one-axis pan head with a camera. Two-finger gripper on each arm (powered or passive, TBD). 8 baseline arm actuators, 9 when the head pan is fitted. Concept sheet: `docs/images/KMECH-CONCEPT-DA-02.png`; cross-section: `docs/images/KMECH-CROSS-SECTION-DA-02.png`.
- **Primary demonstration objective:** Kritva platform demonstration (manipulation, pick-and-place, research and development as printed on the concept sheet).
- **Key capabilities (as printed, CONCEPT_TARGET):**
  - Arm reach 350 mm each side (shoulder to gripper).
  - Target payload 0.1 – 0.2 kg per arm.
  - Indicative envelope 550 mm high, 800 mm overall width, 300 mm × 250 mm torso and base.
  - 24 V DC concept-level power with 5 V and 12 V rails inside the torso.
  - Medium-complexity step between a tabletop dual-arm (DA-01) and the mobile and 5-DOF concepts.
- **Major assumptions:**
  - Intern assumptions are listed in `ACTUATOR_ANALYSIS.md` (A1–A14), `MASS_BUDGET.md` (M1–M11) and `MECHANICAL_ANALYSIS.md` (S1–S7). Key ones: link split 175 / 100 / 75 mm; shoulder axes at 280 mm height on the torso centre plane; yaw axis vertical and pitch axes horizontal; torso height 300 mm; free-standing base for stability checks.
  - Printed weight (8 – 12 kg) and payload targets have no stated basis.
  - Upgrade to 5-DOF arms and a mobile base is a future path only, not part of the study baseline.
- **Known limitations:**
  - Only four DOF per arm: three-dimensional gripper position plus approach pitch, no gripper roll.
  - Not to scale and not CAD; no joint ranges, torque, speed, ratio, camera or battery data are printed.
  - Joint to S/M/L mapping has not been made.
  - Shoulder-to-shoulder spacing (600 mm) appears on the concept sheet only (D5).

## 3. Folder Contents

Drafted (preliminary, PROPOSED):

- `ARCHITECTURE.md` (KMECH-ARCH-DA-02)
- `MECHANICAL_ANALYSIS.md` (KMECH-MECH-DA-02)
- `ACTUATOR_ANALYSIS.md` (KMECH-ACT-DA-02)
- `MASS_BUDGET.md` (KMECH-MASS-DA-02)
- `COST_MODEL.md` (KMECH-COST-DA-02), categories and scope only, no cost values

Not yet created:

- `REQUIREMENTS.md`
- `INTERFACES.md`
- `OPEN_QUESTIONS.md`
- `calculations/` (CALC-DA02-01, -02, -03 are referenced and still to be filed)
- `references/`
- `reviews/`
- `sketches/`

There is no `cad/` folder while HOLD D-003 is active.

## 4. Current Assessment

- Overall status: PROPOSED. Preliminary paper drafts exist; owner review pending.
- Requirements completeness: INCOMPLETE. No `REQUIREMENTS.md` yet; payload, reach and mass remain UNKNOWN in the requirements register until the owner resolves them.
- Architecture assessment: Preliminary draft complete (`ARCHITECTURE.md`); torso packaging, shoulder axis arrangement and cable routing are not yet assessed in detail.
- Engineering assessment: Preliminary estimates only (`MECHANICAL_ANALYSIS.md`):
  - Shoulder pitch is the dominant load, 2.64 N·m holding per arm with 0.2 kg payload.
  - Link bending is negligible; joint compliance will govern stiffness.
  - Free-standing stability with arms extended has thin margins (about 1.3 – 1.7 against a 20 N assumed disturbance), so base fixing should be assumed.
  - Table-level picking reaches only about 58 – 85 mm beyond the base front edge.
  - The two arm workspaces overlap in a narrow lens about 100 mm wide on the midline.
- Actuator compatibility: NOT ASSESSED. No `kritva-actuator` data supplied and no S/M/L mapping.
- Cost assessment: Categories and scope listed only. No cost values estimated.
- Major risks:
  1. Torso packaging of Kritva Edge, drivers and power distribution in 300 mm × 250 mm.
  2. Shoulder arrangement, axis offset, workspace and singularities.
  3. Cable routing through four joints per arm and the head pan.
  4. Base loading and tipping with extended arms.
  5. Actuator mass and torque (largest mass uncertainty, about ±50%).
  6. Limited table-level reach and no gripper roll against the printed pick-and-place use.
  7. Printed weight and payload targets without stated basis.
  8. Power-off droop and pinch hazards (safeguards not defined).
- Evidence gaps: S/M/L data, joint ranges, link and module masses, gearbox stiffness, bearing data, shoulder height and torso height, base fixing method, interface list, collision envelopes, owner-supplied requirements.

## 5. Checkpoint Progress

| Checkpoint | Status | Review reference |
|---|---|---|
| CP2 | TBD | `reviews/` |
| CP3 | TBD | `reviews/` |
| CP4 | TBD | `reviews/` |

## 6. Open Decisions

1. **D5 (INCOMPLETE):** shoulder-to-shoulder 600 mm is on the concept sheet only and looks inconsistent with a 300 mm torso, 800 mm overall width and 350 mm reach. Owner to clarify what each width refers to. NOT VERIFIABLE FROM CURRENT ARTWORK.
2. Whether the optional head pan is fitted in the study configuration (D6 is settled: 8 baseline actuators, 9 when fitted). TBD.
3. Whether grippers are powered in the baseline configuration. TBD.
4. Payload, reach and mass targets remain UNKNOWN in the requirements register. BLOCKED on owner.
5. Joint to S/M/L actuator mapping and `kritva-actuator` source data. BLOCKED on owner input.
6. Joint ranges, shoulder height, torso height and base fixing method. TBD.
7. Whether S/M/L modules integrate motor drivers. UNKNOWN.
8. Kritva Edge cost basis, interface list and any EtherCAT provisions (not shown on the sheets). TBD.
9. Stale wording in the earlier README: references to a mast conflict with resolved D3 (head camera, no mast). Owner to confirm.

## 7. HOLD D-003

Paper feasibility work only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
