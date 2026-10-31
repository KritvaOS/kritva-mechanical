# Concept Variation Audit (DA-01 to DA-06, QR-01 to QR-06)

| Property | Value |
|---|---|
| Document | Concept Variation Audit |
| Repository | `KritvaOS/kritva-mechanical` |
| Version | 0.2.0 |
| Last Updated | 2026-10-31 |
| Status | DRAFT, PROPOSED (drafted by Claude; owner review pending) |
| Evidence | Type C, maturity L0. Built only from the concept READMEs v0.3.0 and the 24 artwork sheets; all numbers are `CONCEPT_TARGET`, and every derived number is marked `ESTIMATE` |
| Related | `feasibility/STUDY_PLAN.md`, `feasibility/concepts/*/README.md`, `docs/images/ARTWORK_INDEX.md`, `feasibility/EVALUATION_CRITERIA.md` |

## 1. Question

Do the 12 concepts vary in a way that makes a comparative feasibility study meaningful? That means each concept should change something that matters, the changes should be separable, and the study should be able to say why one concept scores differently from another. This audit does not judge any design.

## 2. Result in short

1. The dual-arm set is a reasonable grid (arm DOF × base type) with one gap and one near-duplicate.
2. The legged set varies body size and DOF per leg, but the two things the names promise (QR-04 "long-leg", QR-05 "modular") are not visible in any printed number.
3. Several target values (weight, payload, arm reach) do not move with the variation, or move without a stated reason. Any scoring that uses them will reward the artwork, not the concept.
4. After the DA-04 and DA-06 redefinition (CL-025, approved by the owner on 2026-10-31) no concept has arms above 4 DOF, so the study cannot test whether wrist roll or a 5th DOF is needed.

Findings F1 to F10 below are numbered for reference in owner decisions.

## 3. Dual-arm variation matrix

| Concept | Arm DOF | Base | Head / vision | Width × height (mm) | Reach (mm) | Payload / arm (kg) | Weight (kg) | Actuators |
|---|---|---|---|---|---|---|---|---|
| DA-01 | 3 | Fixed | Optional mast | 700 × 400 | 350 | 0.1–0.2 | 5–8 | 6 |
| DA-02 | 4 | Fixed | Torso, optional head | 800 × 550 | 350 | 0.1–0.2 | 8–12 | 8 (+1 head) |
| DA-03 | 3 | Differential drive | Mast | 800 × 650 | 350 | 0.1–0.2 | 12–18 | 8 |
| DA-04 | 4 | Differential drive | Torso, head | 1200 × 1200 | 450 | 0.5–1.0 | 25–35 | 10 |
| DA-05 | 3 | Rotating (1 DOF) | Mast / top mount | 800 × 400 | 350 | 0.2–0.5 | 15–25 | 7 |
| DA-06 | 4 | Fixed | Multi-camera mast | 800 × 500 | 350 | 0.2–0.5 | 20–30 | 8 |

Reading: the intended axes are arm DOF (3 or 4) and base (fixed, rotating, mobile). Covered cells: 3-DOF fixed (DA-01), 3-DOF rotating (DA-05), 3-DOF mobile (DA-03), 4-DOF fixed (DA-02, DA-06), 4-DOF mobile (DA-04).

### Findings

- **F1. Gap: 4-DOF rotating base.** It is the only empty cell. It may be deliberately skipped; the plan should say so.
- **F2. DA-02 and DA-06 are close to duplicates.** Both are 4-DOF arms on a fixed 300 × 250 mm base, 800 mm wide, 350 mm reach. They differ in head versus camera mast. Yet DA-06 targets 20–30 kg and 0.2–0.5 kg payload against DA-02's 8–12 kg and 0.1–0.2 kg. A sensor mast does not explain doubling the weight and payload. If the vision suite is the variable, change only that.
- **F3. Weight and payload targets are not tied to the variation.** DA-05 (3-DOF, 400 mm tall, 300 × 250 mm base) targets 15–25 kg, three times DA-01 (5–8 kg) with the same arms and base. DA-05 and DA-06 payload (0.2–0.5 kg) is higher than DA-01, DA-02 and DA-03 with the same 350 mm reach and no stated change in actuator size. No target states how it was derived.
- **F4. Arm reach is not a variable.** Five of six concepts use 350 mm. Only DA-04 changes it (450 mm), together with scale, payload and weight. The study cannot separate the effect of reach from that of size.
- **F5. Payload is below a gripper's likely mass.** A 0.1–0.2 kg payload for a two-finger gripper-equipped arm is small enough that the gripper itself may be heavier. A static payload-only check at full reach gives `ESTIMATE` shoulder torques of about 0.7 N·m (0.2 kg at 350 mm), 1.7 N·m (0.5 kg at 350 mm) and 4.4 N·m (1.0 kg at 450 mm), before arm and gripper mass and any dynamic or safety factor. The real demand is higher; the S/M/L mapping (CP3-04) should start from this.
- **F6. Arm DOF limits what the concepts can show.** The 3-DOF arms (shoulder yaw, elbow pitch, wrist pitch) and 4-DOF arms (add shoulder pitch) have no wrist roll. They suit top-down pick-and-place but cannot orient a gripper freely. DA-02 and DA-04 name a 5-DOF upgrade path, which the proposed redefinition removed as a concept. State the task scope (for example top-down pick-and-place) so the DOF variation can be judged against it.
- **F7. DA-05 stacks a base yaw on a shoulder yaw.** Both arms already have shoulder yaw; the base rotation rotates both arms together. The benefit (workspace sweep without arm yaw, or shared yaw) is not stated and should be an intern analysis (README section 11).

## 4. Legged variation matrix

| Concept | Legs | DOF / leg | Actuators | Body L × W × H (mm) | Overall L × W (mm) | Extension L / W (mm, derived) | Weight (kg) | Payload (kg) |
|---|---|---|---|---|---|---|---|---|
| QR-01 | 4 | 2 | 8 | 300 × 250 × 200 | 420 × 400 | 120 / 150 | 2.5–4 | 0.3–0.8 |
| QR-02 | 4 | 3 | 12 | 350 × 260 × 250 | 520 × 480 | 170 / 220 | 4–6 | 0.5–1.0 |
| QR-03 | 4 | 2 | 8 | 400 × 350 × 180 | 520 × 480 | 120 / 130 | 3–5 | 0.5–1.0 |
| QR-04 | 4 | 3 | 12 | 450 × 280 × 320 | 620 × 520 | 170 / 240 | 5–7 | 0.5–1.0 |
| QR-05 | 4 | 2 or 3 | 8 or 12 | 420 × 260 × 250 | 560 × 520 | 140 / 260 | 4–6 (12 DOF) | 0.5–1.0 |
| QR-06 | 6 | 2 | 12 | 400 × 280 × 220 | 520 × 480 | 120 / 200 | 3–5 | 0.5–1.0 |

Extension is overall minus body, derived by this audit (`ESTIMATE`, not printed on any sheet).

### Findings

- **F8. QR-04 "long-leg" is not visible in the numbers.** Its length extension (170 mm) equals QR-02's, and no sheet gives leg link lengths. The body is taller (320 mm against 250 mm) and wider overall, but leg length, the defining variable, is undefined. The same applies to stride, which the concept names as its purpose. Define thigh and shank length for QR-02 and QR-04 so the comparison tests leg length, not just body size.
- **F9. QR-05 "modular" carries no modular cost.** In its 12-DOF mode it targets the same weight (4–6 kg) and payload as QR-02, with similar body size. Interchangeable leg modules need an interface (the cross-section draws 4 × M5 and 2 × Ø5 dowels as "indicative concept"), which adds mass and joints. No target reflects it, and the interface is not on the concept sheet. Either add the interface mass to the target or record it as unknown.
- **F10. The 2-DOF legs cannot move sideways.** QR-01, QR-03 and QR-06 use hip and knee flexion only: each leg moves in a plane. QR-01 and QR-03 are quadrupeds with no abduction, so lateral foot placement, turning in place and side-step balance are open questions; the concept lists "turning" and "stable walking" as uses. This is a feasibility question for those three, not an artwork error. QR-06 reaches lateral coverage with six legs and a coxa joint (its joint definition is already an owner item).

Other observations:

- Actuator count is the strongest cost proxy and clusters at 12 for QR-02, QR-04, QR-05 (12-DOF mode) and QR-06, with 8 for QR-01, QR-03 and QR-05 (8-DOF mode). The budget check (CP4-09) will compare almost the same count across four concepts, so cost differences will come from leg and body structure, not from actuators.
- Terrain: QR-02 and QR-04 name uneven terrain; the others name flat terrain only. QR-05 (modular) names flat terrain only although its purpose is configurable testing.
- QR-01 and QR-03 differ cleanly (compact against wide and low); QR-06 is a clean topology change (six legs).

## 5. Cross-cutting findings

- Every concept targets 24 V DC and the same internal rails; battery capacity is not stated for any mobile or legged concept, so run time cannot be compared. Fixed-base concepts do not state their power source.
- Weight, payload and reach targets are the study's main comparison inputs but have no derivation (F3, F4, F5). The study should either mark them `CONCEPT_TARGET` and exclude them from scoring, or derive them from the leg or arm geometry.
- The 12 concepts vary several things at once. A cleaner design for the matrix is to list for every pair what changes. The pairs that already vary one thing and are good comparators: QR-01 against QR-03 (size and profile), QR-02 against QR-04 (leg length, once defined), DA-01 against DA-02 (arm DOF and torso), DA-03 against DA-04 (scale).

## 6. Decisions for the owner

1. F1: add a 4-DOF rotating-base concept, or record that the gap is deliberate.
2. F2: keep DA-06 as a vision variant of DA-02 with the same weight and payload, or state why it differs.
3. F3, F4: accept the weight, payload and reach targets as unscored `CONCEPT_TARGET` values, or ask for a derivation.
4. F6: state the task scope for arm DOF (top-down pick-and-place or general grasp), and whether a 5-DOF option should remain on DA-04.
5. F8: define leg link lengths for QR-02 and QR-04.
6. F9: decide whether the QR-05 interface mass is part of its target.
7. F10: note that 2-DOF legs have no abduction and add a lateral-motion check to the QR-01 and QR-03 feasibility activities.

## 7. What this audit did not do

It did not assess any structure, actuator, mass, cost or kinematics beyond the static torque indication in F5. The `ESTIMATE` values are for orientation only and are not requirements. It is a paper review under HOLD D-003, and it is not design approval.

## 8. Cross-check with the independent ChatGPT audit (2026-10-31)

The owner ran a similar audit in the ChatGPT planning session (repository snapshot at commit `acb10061`, PR #12). The two audits agree on the main points and differ in emphasis.

| Topic | ChatGPT audit | This audit | Outcome |
|---|---|---|---|
| Overall verdict | Architectural variation passes; not ready for ranking | Same, with F1 to F10 | Aligned |
| DA-04 and DA-06 definitions | Study plan wording is outdated | Same (open item 14) | Done: owner approved both as baseline; STUDY_PLAN, INTERN_ASSIGNMENTS, feasibility README and READMEs updated (CL-028) |
| DA-02 head pan | 8 arm + 1 optional, 9 when fitted | F-series noted the count only | Done: recorded as owner decision; DA-02 cross-section now `REVIEWED` |
| DA-04 head pan | Excluded from the 10 baseline | Same | Done in README; cross-section label added to the next-round fix list |
| DA-03 and DA-04 drivetrain | Two drive channels for four wheels | Not flagged | Done: the READMEs said "one drive motor per wheel" with 2 actuators, which contradicted each other; corrected to one channel per side |
| DA-05 slip ring | Select slip ring, drop cable loop | D3 was open | Done in README; concept-sheet wording added to the next-round fix list |
| QR-06 joints | Define coxa and femur/tibia actuated joints | Same | Still open; owner defines the two joints and axes |
| QR-04 long-leg, QR-05 modular | Leg lengths and interface undefined | F8, F9 | Aligned; still open |
| Weight and payload targets | Not covered | F2, F3, F5 (DA-02 against DA-06, DA-05 weight, payload against gripper mass) | Only in this audit; owner decision 3 |
| Empty DA cell (4-DOF rotating) and DA-05 yaw stacking | Not covered | F1, F7 | Only in this audit |
| Dimension convention (pose and datums) | Recommended | F4 on reach | Added to the functional comparison matrix, section 4 |
| Two-level study (all 12 first-pass, shortlist deeper) | Recommended | Not covered | Open: needs an owner decision on STUDY_PLAN scope |
| Family comparison dimensions | Recommended | Not covered | Done: `feasibility/FUNCTIONAL_COMPARISON_MATRIX.md` |

Remaining owner decisions: items 1, 3, 4, 5, 6, 7 of section 6, the QR-06 joint definition, and whether to adopt the two-level study.
