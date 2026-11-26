# QR-01 — Compact Quadruped

| Property | Value |
|---|---|
| Document ID | KMECH-CONCEPT-QR-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Overview |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.4.1 |
| Last Updated | 2026-11-26 |
| Authority | Feasibility study; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `COST_MODEL.md`, `OPEN_QUESTIONS.md`, `docs/images/ARTWORK_MANIFEST.json` |

This overview records the concept as printed on the two artwork sheets and the state of the preliminary paper work. Printed values are CONCEPT_TARGET (indicative, unapproved). Calculated values are ESTIMATES. Nothing here approves any value.

## 1. Concept Identification

- Concept ID: QR-01
- Concept name: Compact Quadruped
- Family: Legged
- Complexity: Low (relative engineering category, not a validated assessment)
- Assigned intern: INTERN-02
- Assessment revision: Draft 1 (preliminary paper analysis, owner review pending)

## 2. Concept Summary

- **Intended configuration:** Four symmetric legs on a rigid central body, two DOF per leg (hip and knee flexion/extension, all in one plane), 8 actuators in total, replaceable rubber or TPU foot pads, optional top sensor module. Sheets: `docs/images/KMECH-CONCEPT-QR-01.png`, `docs/images/KMECH-CROSS-SECTION-QR-01.png`.
- **Primary demonstration objective:** Kritva platform demonstration: standing, sitting, slow walking and basic locomotion on indoor and outdoor flat terrain.
- **Key capabilities (as printed, CONCEPT_TARGET):** body 300 mm × 250 mm × 200 mm; overall 420 mm × 400 mm with leg extension; target weight 2.5 – 4 kg (est.); target payload 0.3 – 0.8 kg (est.); 24 V DC with 5 V and 12 V rails.
- **Major assumptions:** Listed in `ACTUATOR_ANALYSIS.md` (A1 – A10), `MASS_BUDGET.md` (M1 – M10) and `MECHANICAL_ANALYSIS.md` (S1 – S7). Key ones: thigh 130 mm and shank 150 mm; hip height 220 mm; leg planes 190 mm either side of the centreline; feet at ±190 mm × ±180 mm; battery 6S 5 Ah (capacity and placement are not drawn on the sheets).
- **Known limitations:** Planar legs cannot move sideways, so no side-stepping or lateral balance. Not to scale, not CAD. No joint ranges, link lengths, torque, speed, battery or sensor data are printed. No S/M/L mapping.

## 3. Folder Contents

Drafted (preliminary, PROPOSED): `REQUIREMENTS.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `COST_MODEL.md` (categories and scope only, no cost values), `OPEN_QUESTIONS.md`.

Not yet created: `INTERFACES.md`, `calculations/` (CALC-QR01-01, -02, -03 are referenced and still to be filed), `references/`, `reviews/`, `sketches/`. No `cad/` folder while HOLD D-003 is active.

## 4. Current Assessment

- Overall status: PROPOSED. Preliminary paper drafts exist; owner review pending.
- Requirements completeness: INCOMPLETE. Weight, payload and size remain UNKNOWN until the owner resolves them.
- Architecture assessment: Preliminary draft complete; body packaging, battery placement (not drawn) and cooling (not drawn) not yet assessed.
- Engineering assessment (estimates):
  - Worst static joint loads for a 7.1 kg robot (6.3 kg estimate plus 0.8 kg payload) on two feet: knee about 3.9 N·m, hip about 2.1 N·m; about 7.7 and 4.2 N·m with a 2× dynamic allowance.
  - Estimated mass 6.26 kg (range about 3.4 – 9.2 kg), well above the printed 2.5 – 4 kg; the printed target lies mostly below the estimate range (it overlaps only between 3.4 and 4 kg).
  - A statically stable crawl gait needs a fore-aft body shift of about 41 mm for a 30 mm margin, because planar legs cannot shift the body sideways.
  - Static tipping angle is about 42°; foot friction is more likely to limit slopes (about 27° at friction 0.5).
- Actuator compatibility: NOT ASSESSED. No `kritva-actuator` data supplied.
- Cost assessment: Categories and scope listed only. No cost values estimated.
- Major risks: printed weight target versus estimated mass and actuator size (they feed each other); no lateral motion and awkward turning; power-off collapse and falls; unknown battery, cooling and sensor baseline; foot impact and traction.
- Evidence gaps: S/M/L data, leg link lengths, joint ranges, battery capacity, thermal data, foot and ground data, interface list.

## 5. Checkpoint Progress

| Checkpoint | Status | Review reference |
|---|---|---|
| CP2 | TBD | `reviews/` |
| CP3 | TBD | `reviews/` |
| CP4 | TBD | `reviews/` |

## 6. Open Decisions

1. **D6 (OPEN):** which optional sensors (IMU, LiDAR, camera) are in the baseline.
2. **D4 (NOT VERIFIABLE):** weight and payload appear on the concept sheet only; targets remain UNKNOWN until the owner resolves them.
3. Size targets (overall 420 mm × 400 mm versus a 250 mm body width) and the leg mounting that gives them: TBD.
4. Joint to S/M/L actuator mapping and `kritva-actuator` source data: BLOCKED.
5. Battery capacity and placement, cooling, joint ranges and link lengths: TBD.
6. Stale wording in the earlier README (hip abduction and a 3-DOF leg are mentioned although D1 resolved to 2 DOF): owner to confirm.

## 7. HOLD D-003

Paper feasibility work only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
