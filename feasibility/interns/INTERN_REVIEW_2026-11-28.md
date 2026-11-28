# KRITVA Mechanical Feasibility — Consolidated Intern Review

**Review date:** 2026-11-28  
**Review scope:** INTERN-01 Amardeep, INTERN-02 Divagar and INTERN-03 Nishant; twelve assigned concepts in total.  
**Review status:** Consolidated technical review / feedback; **not an owner approval, checkpoint acceptance, design release or actuator selection**.  
**Governance:** D-003 HOLD remains active; paper feasibility only.

---

## 1. Executive summary

This document consolidates the mechanical feasibility reviews of all three interns:

| Intern | Assigned concepts | Overall evidence position |
|---|---|---|
| INTERN-01 — Amardeep | DA-01, QR-02, DA-04, QR-04 | Strongest quantitative progress of the three submissions reviewed, with joint-level torque/speed screens, mass/cost estimates and a partial comparison. Important calculation terminology, source-data, cost/mass reconciliation and actuator compatibility gaps remain. Task 044 acceptance is not claimed and remains subject to independent review. |
| INTERN-02 — Divagar | DA-02, DA-03, QR-01, QR-05 | Broad and systematic documentation foundation: proposed requirements, architecture/interfaces, estimated torque/speed and mass budgets, and open-question registers. However, cost is scope-only, actuator compatibility is not assessed, QR-05 interface/evidence remains incomplete, and claimed document completeness is not fully supported by repository branch/commit evidence. |
| INTERN-03 — Nishant | DA-05, QR-03, DA-06, QR-06 | Useful architecture definition and first-pass calculations for DA-05, DA-06 and QR-06. Several load models are incomplete or physically misapplied; QR-03 engineering report was absent from the submitted ZIP. |

**Consolidated conclusion:** all three interns have produced useful paper-feasibility progress, but none of the twelve concepts is demonstrated as fully ready for CP3 acceptance or actuator selection. CP3 remains pending for all three interns unless and until the authorized reviewer records a formal decision. The reviews identify different strengths and gaps; they do **not** establish a performance ranking of interns or a recommendation to select one concept over another.

The strongest next step is to converge on one controlled engineering evidence method across all twelve concepts: defined load cases, joint-axis-specific torque-speed-duty calculations, component-level mass and CoM budgets, controlled actuator data, reproducible cost assumptions, and traceable repository evidence.

### 1.1 Consolidated technical readiness

| Readiness area | INTERN-01 Amardeep | INTERN-02 Divagar | INTERN-03 Nishant |
|---|---|---|---|
| Architecture / DOF / interfaces | Good progress across four concepts | Broad draft coverage across four concepts | Good preliminary architecture for three; QR-03 engineering report absent |
| Torque / speed calculations | Expanded joint-level estimates; terminology and input reconciliation still need review | Estimates with formulas/assumptions; still preliminary and dependent on unresolved owner inputs | Payload-only or incomplete models; QR-06 joint model particularly incomplete |
| Mass model | Earlier status reports mass/cost reconciliation; current evidence review found mass UNKNOWN/incomplete beyond supported targets | Estimated mass bands and CoM; QR-01 and QR-05 exceed printed targets | Nominal mass assumptions but incomplete component-level budgets |
| Cost | Nominal estimates reported in status deck; source/reconciliation concerns remain; latest reviewed state does not support treating them as accepted comparison values | Scope-only; no cost values | Cost analysis absent/incomplete |
| Actuator S/M/L | Family screen only; compatibility blocked | Not assessed; controlled actuator data absent | Not demonstrated |
| Stability / structural | Partial; concept-specific gait/support, wrist, battery/wheel and mounting cases remain | Partial; tipping/support assumptions and unresolved interfaces remain | Partial or incomplete; QR-06 support polygon/gait analysis absent |
| Repository/evidence traceability | Branch and PR #18 contribution identified in status deck; Task 044 review pending | Claimed draft inventory needs branch/commit reconciliation; QR-05 gaps remain | ZIP alone does not establish repository branch/commit/acceptance; QR-03 report absent |
| CP3 recommendation | Pending | Pending | Pending |

### 1.2 Important interpretation

- A number shown in an intern deck is an **estimate**, unless its input data, load case, calculation and review status establish otherwise.
- A printed concept target is not an approved requirement.
- “Reviewed” or “resolved” artwork questions are not design approval.
- A family-level S/M/L screen is not actuator compatibility.
- Cost estimates cannot be treated as procurement quotes or authorization.
- This is not a ranking of interns. The concepts differ in architecture, complexity and available evidence.

---

## 2. Review rules, evidence basis and governance

### 2.1 Evidence categories

This review distinguishes:

- **Submitted evidence:** statements, tables, diagrams and calculations visible in the submitted weekly-status decks and concept files.
- **Repository evidence:** files, branch names, commits, pull requests and status records actually verified in the repository.
- **Calculation check:** arithmetic and dimensional consistency of a submitted calculation.
- **Engineering observation:** whether the chosen model represents the physical load case.
- **Reviewer recommendation:** additional work needed before a conclusion or checkpoint can be accepted.

Where a status deck claims that files or work products exist, that claim is not automatically treated as repository verification. Branch, commit, path and PR evidence are required.

### 2.2 D-003 boundary

The mechanical feasibility work remains subject to **D-003 HOLD**:

- Paper feasibility and analytical work may continue.
- This review does not authorize CAD release, detailed design, BOM finalization, supplier quotation commitments, procurement, fabrication, assembly or physical testing.
- A concept target, calculation assumption or intern recommendation is not an approved product requirement.
- Interns may prepare evidence and recommendations; checkpoint acceptance and design decisions remain with the owner/review authority.

No D-003 violation is established by the submitted status material reviewed here. Any later physical or procurement activity must be separately checked against the owner’s direction.

### 2.3 Common calculation language

All interns should distinguish the following quantities rather than combining them into one “torque” field:

1. Static gravity/holding torque.
2. Continuous operating torque.
3. Dynamic/acceleration torque.
4. Peak output torque and its permitted duration.
5. Required output speed under load.
6. Duty cycle and thermal constraints.
7. Planning/sizing factors and their rationale.

A dynamic allowance or planning factor selected by an intern is an assumption, not a validated safety factor. Calculations must state whether torque is at the motor shaft or gearbox output shaft and include gearbox ratio and efficiency where relevant.

---

## 3. INTERN-01 — Amardeep

**Assigned concepts:** DA-01, QR-02, DA-04 and QR-04.  
**Submitted status evidence:** `Amar_Updates.pptx`, identifying branch `feasibility/intern-01-week3`; it reports Week-2 architecture contribution merged upstream via PR #18 and Week-3 / early-Week-4 paper-feasibility progress.

### 3.1 Work reported

The weekly status deck reports:

- Architecture, joint/channel inventories, interfaces and mass framework for all four concepts.
- Week-2 contribution merged upstream via PR #18.
- Expanded joint-level torque/speed screens with formulas and assumptions.
- Mass and nominal cost models reconciled against a ₹2 lakh reference ceiling.
- Four paper-only SVG concept mockups, explicitly not to scale.
- An S/M/L actuator-family screen, explicitly **not compatibility evidence**.
- A partial four-concept comparison with 85% scored weight and 15% marked NOT SCORED.
- Task 044 acceptance explicitly **not claimed**; independent review remains pending.

### 3.2 Submitted estimate summary

The weekly status deck reports the following figures. They remain estimates, not approved requirements or validated actuator selections.

| Concept | Reported actuator count | Reported peak/continuous estimate (1.5× label in deck) | Nominal cost shown | Main open issue identified |
|---|---:|---:|---:|---|
| DA-01 | 6 | ≈3.2 N·m | ₹1.41 lakh | Wrist axis and pose |
| QR-02 | 12 | ≈8.3 N·m | ₹2.15 lakh | Joint axes, gait and support cases |
| DA-04 | 10 | ≈6.9 N·m | ₹2.40 lakh | Battery and wheel geometry |
| QR-04 | 12 | ≈12 N·m | ₹2.32 lakh | Long-leg, mounting and sensor questions |

The status deck presents a preliminary ordering of DA-01 > QR-02 > QR-04 ≈ DA-04, while explicitly stating that it is not a final recommendation and that 15% of comparison weight is unscored.

### 3.3 Review observations

**Strengths**
- Of the three submitted weekly-status packages, Amardeep’s deck shows the most advanced quantitative comparison workflow: joint-level screening, mass/cost estimates, a visible actuator-family screen and an explicit partial-comparison status.
- The deck calls out unresolved concept-specific inputs instead of presenting the mockups as scale-accurate drawings.
- It explicitly avoids claiming Task 044 acceptance.

**Corrections and evidence gaps**
1. **Ranking is not ready for use as a decision.** The earlier audit found that the cost bands/source basis and comparison status did not reconcile cleanly with the latest repository evidence. The current defensible position is that the comparison is NOT SCORED / not decision-ready until the missing inputs and scoring basis are reconciled. The deck’s preliminary ordering must not be propagated as a program recommendation.
2. **Cost is not established merely by a nominal number.** Cost values require a traceable component list, quantity, source/date, currency, exclusions and estimate confidence. The ₹2 lakh value is a planning ceiling, not spending authority.
3. **Mass status must be evidence-based.** The earlier repository review found mass UNKNOWN/incomplete beyond the printed concept targets. Do not imply a validated mass budget unless the component-level roll-up and assumptions are present and reconciled.
4. **Torque terminology needs correction.** Static holding, continuous, dynamic peak, output torque and planning factors must be separately labelled. “Peak cont.” is ambiguous and should not combine distinct operating conditions.
5. **S/M/L is a family screen only.** Controlled data for torque, speed under load, thermal capability, price and maturity are still open. Compatibility cannot be claimed without matching each joint’s requirement to a revisioned actuator variant.
6. **Concept-specific blockers remain material:** DA-01 wrist axis/pose; QR-02 and QR-04 joint axes, gait and support; DA-04 battery and wheel geometry.
7. **Task 044 remains pending independent review.** Contribution of evidence is not acceptance.

### 3.4 CP3 assessment — Amardeep

| CP3 evidence area | Assessment | Reason |
|---|---|---|
| Architecture / joint inventory / interfaces | PARTIAL to GOOD | Broad four-concept baseline reported; mockups not to scale |
| Torque / speed | PARTIAL | Expanded formulas and assumptions, but terminology and input reconciliation required |
| Mass budget | INCOMPLETE / UNKNOWN where not supported | Earlier audit found no sufficiently evidenced mass roll-up beyond printed targets |
| Structural / stability | PARTIAL | Gait/support, wrist pose, mounting and wheel/battery inputs remain open |
| Actuator compatibility | BLOCKED | S/M/L family screen is not variant compatibility |
| Cost | NOT ACCEPTED / NOT COMPUTABLE as a decision basis | Nominal values require source and repository reconciliation |
| Comparative scoring | NOT SCORED for decision use | 15% unscored in deck; earlier repository audit found comparison status/source mismatch |
| Task 044 | REVIEW PENDING | Intern does not claim acceptance |

**Disposition:** retain as meaningful quantitative progress; request calculation/source reconciliation and independent Task 044 review. **CP3 remains pending.**

---

## 4. INTERN-02 — Divagar

**Assigned concepts:** DA-02, DA-03, QR-01 and QR-05.  
**Submitted status evidence:** `Divagar_Weekly_Status.pptx`, week ending 2026-11-27, under `KritvaOS/kritva-mechanical`.

### 4.1 Work reported

The weekly status deck reports:

- Earlier artwork audit and concept README creation.
- Draft requirements registers with 15–17 proposed requirements per concept; all marked PROPOSED.
- Architecture breakdown, DOF tables and interface notes for all four concepts.
- Torque/speed estimates with formulas and assumptions.
- Estimated mass budgets with bands and centres of mass, with printed concept targets kept separate.
- Cost models at **scope only**: categories listed, no cost values.
- Open-question registers with 11 questions and 5 owner decisions per concept.
- No actuator compatibility assessment because controlled `kritva-actuator` data had not been supplied.

The deck says each concept has eight draft artefacts (README, requirements, architecture, mechanical analysis, actuator analysis, mass budget, cost model and open questions). This is a reported inventory, not proof that all 32 files were present on the authoritative branch at review time.

### 4.2 Submitted estimate summary

| Concept | Reported actuator count | Highest reported joint need | Estimated mass | Printed concept target | Review note |
|---|---:|---:|---:|---:|---|
| DA-02 — Humanoid Torso Dual-Arm | 8 baseline (+1 with head) | ≈5.0 N·m shoulder pitch | ≈10.0 kg | 8–12 kg | Mass estimate lies in target range; shoulder spacing/base fixing remain open |
| DA-03 — Mobile Dual-Arm | 8 (6 arm, 2 drive channels) | ≈3.8 N·m wheel turning | ≈15.7 kg | 12–18 kg | Mass estimate lies in target range; battery and several artwork decisions remain open |
| QR-01 — Compact Quadruped | 8 | ≈11.6 N·m knee | ≈6.3 kg (reported range 3.4–9.2 kg) | 2.5–4 kg | Estimate exceeds printed target; mass and torque are coupled |
| QR-05 — Modular Quadruped | 8 or 12 | ≈22.6 N·m knee at 12 DOF | ≈10.4 kg at 12 DOF (8-DOF estimate ≈8.5 kg) | 4–6 kg | Estimate exceeds target; module interface D6 remains open |

The deck says the highest-joint estimates include a 2× dynamic allowance and 1.5× planning factor. These factors are intern assumptions, not validated margins. DA-03’s 3.8 N·m is wheel turning torque, not an arm-joint torque.

### 4.3 Concept-specific review observations

**DA-02 — Humanoid Torso Dual-Arm**
- Fixed-base architecture and torso/arm packaging are documented.
- The deck’s estimate table gives approximately 5.0 N·m for shoulder pitch, while its merits/demerits table separately cites approximately 2.6 N·m as the highest shoulder-pitch load. This is an internal numerical/label inconsistency that must be reconciled against the calculation file before either value is used.
- Shoulder spacing (D5) and base fixing remain open.
- The 8-actuator baseline versus 9 with head must remain explicit and tied to the owner decision; do not silently mix the two configurations.

**DA-03 — Mobile Dual-Arm**
- Wheeled-base, dual-arm, drive and battery architecture is described; the owner-resolved wheel configuration is four wheels with two drive channels.
- The ≈3.8 N·m estimate is for wheel turning at the output, not an arm joint.
- Battery, D3/D4/D5/D6 artwork questions and reach/width remain open.
- The reported ≈15.7 kg estimate is within the printed 12–18 kg target range, but does not by itself establish runtime, stability or drive feasibility.

**QR-01 — Compact Quadruped**
- Planar four-leg, two-DOF-per-leg architecture and crawl-stability analysis are reported.
- The ≈11.6 N·m knee estimate is preliminary; the load case, joint geometry, support configuration and mass assumptions need to be traceable in the calculation file.
- Estimated mass ≈6.3 kg exceeds the printed 2.5–4 kg target. The reported 42° tipping angle is an estimate under stated assumptions, not a validated gait stability result.
- Sensor baseline (D4/D6) remains open; no side-step capability is claimed.

**QR-05 — Modular Quadruped**
- Swappable leg modules and 2-DOF versus 3-DOF variants are considered; 8-DOF and 12-DOF configurations must be kept distinct.
- The 12-DOF case reports ≈22.6 N·m knee need and ≈10.4 kg mass; the 8-DOF case reports ≈8.5 kg. Both are above the printed 4–6 kg target.
- The module interface/sensor-module question D6 remains unresolved. The deck’s statement that the interface adds approximately 0.32 kg does not establish interface stiffness, load transfer, connector retention or repeatability.
- The earlier repository audit found QR-05 core documents/interface definition missing on main and calculation files not filed. The status deck’s claimed draft coverage therefore needs branch/commit/path reconciliation before completeness is accepted.

### 4.4 Review observations across Divagar’s four concepts

**Strengths**
- Broad and consistent document structure across the four assigned concepts.
- Requirements, architecture, analysis, mass and open-question work are separated rather than collapsed into one slide.
- Estimates are labelled as estimates and concept targets are kept separate.
- The deck explicitly avoids ranking concepts and does not claim actuator compatibility or approval.

**Corrections and evidence gaps**
1. **Repository completeness is not established.** The 32-document claim must be reconciled to an exact branch, commit and file list. In particular, QR-05 core documents and calculation files were not evidenced on main in the earlier repository audit.
2. **QR-05 module interface is a blocker.** Define load transfer, alignment, retention/locking, electrical/sensor interface, harness routing, stiffness and serviceability at paper level before treating module mass as sufficient evidence.
3. **DA-02 torque inconsistency must be resolved.** The ≈5.0 N·m and ≈2.6 N·m shoulder-pitch figures cannot both be used as the same “highest load” without explaining different load cases or factors.
4. **Cost remains scope-only.** This is acceptable as an explicit status, but it is not a cost estimate or comparison.
5. **Actuator compatibility remains unassessed.** Do not map S/M/L until controlled actuator data and complete joint requirements exist.
6. **Traceability needs strengthening.** Requirement, function, unknown, risk, assumption, mass and calculation IDs should link from each concept README to the supporting analysis and review record.
7. **Mass estimates above target are feasibility signals, not automatic rejection.** QR-01 and QR-05 need a controlled mass roll-up and sensitivity analysis; actuator mass can create a feedback loop with joint torque.

### 4.5 CP3 assessment — Divagar

| CP3 evidence area | Assessment | Reason |
|---|---|---|
| Architecture / DOF / interfaces | PARTIAL to GOOD | Draft coverage reported across four concepts |
| Requirements | DRAFT / PROPOSED | 15–17 per concept; none should be treated as approved requirements |
| Torque / speed | PARTIAL | Formula-based estimates; assumptions and load cases require review |
| Mass budget | PARTIAL | Estimates and CoM bands; QR-01 and QR-05 exceed printed targets |
| Structural / stability | PARTIAL | Static/tipping screens only; gait and interface cases need further evidence |
| Actuator compatibility | BLOCKED | No controlled S/M/L matching |
| Cost | SCOPE ONLY | Categories listed, no values |
| QR-05 interface | OPEN / BLOCKING | D6 unresolved; interface definition and calculation files not evidenced on main |
| Repository traceability | INCOMPLETE | 32-file claim requires branch/commit/path reconciliation |

**Disposition:** retain as a useful documentation and analysis foundation; prioritize QR-05 evidence/interface closure, DA-02 torque reconciliation and repository traceability. **CP3 remains pending.**

---

## 5. INTERN-03 — Nishant

**Assigned concepts:** DA-05, QR-03, DA-06 and QR-06.  
**Submitted evidence:** ZIP `Kritva Robotics-20261128T090914Z-1-001.zip`, containing engineering presentations for DA-05, DA-06 and QR-06, and concept-overview PDFs for DA-05, QR-03, DA-06 and QR-06.

**Summary:** useful architecture definition and first-pass calculations for DA-05, DA-06 and QR-06. Several load models are incomplete or physically misapplied; QR-03 engineering report was absent from the submitted ZIP. CP3 remains pending.

## 6. INTERN-03 — detailed technical review

The following detailed concept-by-concept analysis expands the summary above for Nishant's four assigned concepts.

---

## 7. Detailed concept review --- DA-05

### 3.1 Submitted architecture

The deck describes a compact tabletop dual-arm robot with:

-   Two symmetric serial arms, each with 3 baseline actuated DOFs:
    shoulder, elbow and wrist.
-   One continuously rotating 360° base DOF.
-   Seven baseline actuated DOFs in total, excluding optional grippers.
-   A fixed table/base plate, rotary bearing, rotating base, central
    torso/enclosure, two arms and optional two-finger grippers.
-   A concept-level 24 V DC supply, with 5 V and 12 V rails shown.
-   A proposed use case covering manipulation, pick-and-place,
    inspection, teleoperation and research/platform demonstration.

The proposed mechanical interfaces are usefully identified:
table-to-base, base-to-bearing, base-to-slip-ring, rotary-base-to-torso,
torso-to-shoulder, joint-to-link, cable path and wrist-to-gripper.

**Assessment:** the architecture is coherent as a first-pass concept.
Treating the rotary interface as a separate serviceable module is a good
architectural decision to investigate. The deck also correctly
identifies bearing capacity, slip-ring specification, actuator
packaging, mass properties and cable fatigue as dependencies.

### 3.2 Concept targets recorded in the deck

  ------------------------------------------------------------------------
  Parameter                          Submitted value Review interpretation
  --------------------- ---------------------------- ---------------------
  Overall arm-to-arm                          800 mm Packaging target; not
  width                                              computed workspace

  Base                                  300 × 250 mm Preliminary envelope

  Overall height                              400 mm Concept target

  Reach per arm                               350 mm Target; geometry and
                                                     joint limits not
                                                     fixed

  Base rotation                      360° continuous Requires rotary
                                                     interface and cable
                                                     strategy

  Payload                        0.2--0.5 kg per arm Estimated concept
                                                     target

  Target mass                              15--25 kg Estimated; no
                                                     component mass
                                                     roll-up

  Supply                                     24 V DC Concept-level
  ------------------------------------------------------------------------

These values are not design-approved requirements.

### 3.3 Arm torque calculation check

The deck uses:

-   Payload mass: 0.5 kg
-   Reach: 0.35 m
-   Gravity: 9.81 m/s²
-   Dynamic factor: 2.0
-   Sizing margin: 1.5

Payload force:

\[ F = mg = 0.5 `\times 9.81`{=tex} = 4.905 `\mathrm{N}`{=tex} \]

Payload-only static shoulder moment:

\[ T = Fr = 4.905 `\times 0.35`{=tex} = 1.71675 `\mathrm{N\,m}`{=tex} \]

Screening value after the stated factors:

\[ T\_{screen} = 1.71675 `\times 2.0`{=tex} `\times 1.5`{=tex}
`\approx 5.15`{=tex} `\mathrm{N\,m}`{=tex} \]

The arithmetic is correct for the stated payload-only model. The deck
also gives approximately 2.57 N·m for the elbow using an illustrative
175 mm + 175 mm link split.

**Important limitation:** these values do not include upper-arm/forearm
mass, motor and gearbox mass, wrist and gripper mass, cable forces,
joint friction, gearbox efficiency, acceleration/inertia torque, gravity
at other postures or the effect of the arm's own centre of mass. The
elbow result is also only an illustrative geometry-based split, not a
complete elbow free-body calculation.

The labels "M class / verify" and "S/M boundary / verify" should
therefore remain preliminary screening annotations, not actuator
selections.

### 3.4 Rotary-base calculation

The deck illustrates a 20 kg rotating assembly approximated at a 0.25 m
radius:

\[ I `\approx `{=tex}mr\^2 = 20 `\times 0.25`{=tex}\^2 =
1.25 `\mathrm{kg\,m^2}`{=tex} \]

For an assumed angular acceleration of 0.5 rad/s²:

\[ T = I`\alpha `{=tex}= 1.25 `\times 0.5`{=tex} =
0.625 `\mathrm{N\,m}`{=tex} \]

The arithmetic is correct for the simplified point-mass/ring
approximation. It is **not a base actuator requirement** because the
model does not establish:

-   Actual distribution of torso, arms, actuators, electronics and
    payload around the rotation axis.
-   Arm configuration and the inertia change with arm pose.
-   Required angular speed, acceleration/deceleration profile or cycle
    time.
-   Bearing friction, preload, seal drag and overturning load.
-   Slip-ring drag and cable/harness torque.
-   External manipulation reaction loads and disturbance torque.
-   Required holding torque, duty cycle and thermal limits.

**Required follow-up:** provide an inertia estimate by component and
radius, identify representative arm configurations, define base
speed/acceleration/duty requirements, and list bearing/slip-ring/cable
torque contributions separately. The work can remain analytical at this
stage.

### 3.5 Stability calculation

The deck uses a 20 kg robot, centred CoM and the shortest base
half-dimension of 125 mm:

\[ M\_{restore} = 20 `\times 9.81`{=tex} `\times 0.125`{=tex}
`\approx 24.5`{=tex} `\mathrm{N\,m}`{=tex} \]

It compares this with the payload moment of approximately 1.72 N·m and
reports a ratio of about 14.3×.

The arithmetic is correct for the stated assumptions. However, the ratio
is not a verified tipping safety factor. It assumes the CoM is centred,
uses a simplified restoring arm, and compares against one payload moment
without resolving the actual tipping edge and the geometry of the loaded
arm.

**Required follow-up:**

-   Define the tabletop tipping edge for each relevant arm orientation.
-   Use the actual base support polygon and the combined
    robot-plus-payload CoM.
-   Include both arms, unequal payload cases and maximum-reach poses.
-   Include base rotation and arm motion cases where dynamic effects
    matter.
-   State whether the table attachment is assumed to be
    friction-supported, bolted or otherwise constrained; these are
    different boundary conditions.

### 3.6 Workspace, mass and structural status

The deck correctly states that 350 mm reach and 360° base rotation do
not establish a computed 3D workspace. The 800 mm arm-to-arm envelope is
a packaging target. Exact workspace needs link lengths, joint limits,
shoulder spacing and a defined wrist convention.

The mass section gives a 15--25 kg target and uses 20 kg as a nominal
calculation assumption. It does not provide a component-level mass
budget. Link/joint masses, battery/electronics, bearing/slip-ring and
final mass properties remain TBD.

The structural load cases listed are relevant: shoulder and elbow
bending, rotary-bearing radial/axial and overturning loads, tabletop
mounting plate and local joint/fastener stresses. FEA is correctly
deferred until geometry, material properties and actual loads exist. For
this paper-feasibility phase, analytical free-body and beam/plate
screening can be prepared without claiming FEA completion.

### 3.7 DA-05 verdict

**Architecture: GOOD preliminary definition.**\
**Quantitative feasibility: PARTIAL.**\
**Actuator selection: NOT READY.**\
**CP3: PENDING.**

Priority corrections are complete arm self-weight/inertia torque basis,
rotary-base inertia and loss model, actual tipping-edge stability model,
mass budget and speed/duty requirements.

------------------------------------------------------------------------

## 8. Detailed concept review --- QR-03

### 4.1 Evidence received

The ZIP contains `QR-03/QR 03.pdf` and its extracted text, which is a
concept-overview document. It does **not** contain a dedicated QR-03
engineering presentation or report comparable to the DA-05, DA-06 and
QR-06 engineering decks.

The concept overview describes:

-   Low-profile quadruped.
-   Four legs.
-   Two DOFs per leg: hip and knee flexion.
-   Eight baseline actuators.
-   Body envelope approximately 400 × 350 × 180 mm.
-   Overall envelope approximately 480 × 520 mm.
-   Target mass 3--5 kg.
-   Payload target 0.5--1.0 kg.
-   Concept-level 24 V DC.

These are concept-level statements only.

### 4.2 What cannot be concluded

The available QR-03 overview does not provide sufficient engineering
evidence to assess:

-   Week 1 reference architecture and requirements traceability.
-   Joint-axis orientation, joint limits and DOF rationale.
-   Link lengths, leg geometry and mechanical configuration.
-   Body-to-leg, hip, knee, foot and harness interfaces.
-   Representative standing and walking postures.
-   Hip and knee torque-speed requirements.
-   Ground reaction forces and load distribution.
-   Support polygon and dynamic gait stability.
-   Component-level mass budget and centre of mass.
-   Actuator S/M/L compatibility.
-   Structural load cases and cost model.

The QR-06 analysis must not be reused as if it were QR-03 analysis: a
four-legged robot has different support polygons and gait load cases
from a six-legged robot.

### 4.3 QR-03 verdict

**Concept overview: PRESENT.**\
**Intern engineering report: NOT PROVIDED IN THE REVIEW ZIP.**\
**Technical assessment: NOT ASSESSED.**\
**CP3: NOT EVIDENCED / PENDING.**

**Required action:** Nishant should provide the QR-03 engineering report
and repository evidence (branch, commit and changed file paths). Until
then, do not mark QR-03 engineering deliverables complete or infer
acceptance from the concept overview.

------------------------------------------------------------------------

## 9. Detailed concept review --- DA-06

### 5.1 Submitted architecture

The deck describes a fixed tabletop, vision-integrated dual-arm system
with:

-   Two symmetric arms, each with 4 DOFs.
-   Eight baseline arm actuators: shoulder yaw, shoulder pitch, elbow
    pitch and wrist pitch on each arm.
-   Optional two-finger servo grippers.
-   Top RGB-D/stereo camera and left/right cameras.
-   Adjustable camera mast.
-   24 V input with 5 V and 12 V rails.
-   Base, torso, arms, mast, camera mounts and cable routing as major
    assemblies.

The deck recommends centralizing heavy electronics, using modular joint
cartridges, providing a positive mast lock, maintaining cable service
loops and making camera mounts repeatable. These are useful architecture
recommendations.

### 5.2 Concept targets

  Parameter              Submitted value Review interpretation
  ---------------- --------------------- -----------------------------------------
  Overall width                   800 mm Packaging target
  Overall height                  500 mm Includes mast/camera provision
  Base                      300 × 250 mm Preliminary envelope
  Reach per arm                   350 mm Target; not computed workspace
  Payload            0.2--0.5 kg per arm Estimated target
  Target mass                  20--30 kg Estimate; not supported by mass roll-up
  Arm DOF                      4 per arm Architecture baseline

The deck calls the concept "Vision-Integrated Dual-Arm Robot." The
assignment context identifies DA-06 as a humanoid
upper-body/head-provision work item. The exact scope/name and priority
should be reconciled by the owner/program register; this is a governance
issue, not an intern-level unilateral change.

### 5.3 Shoulder pitch and elbow torque calculation

The deck uses a 0.5 kg payload at 0.35 m:

\[ T\_{payload}=0.5 `\times 9.81`{=tex} `\times 0.35`{=tex}
=1.71675 `\mathrm{N\,m}`{=tex} \]

Applying the stated 2.0 dynamic factor and 1.5 sizing margin gives:

\[ T\_{screen}=1.71675 `\times 2.0`{=tex} `\times 1.5`{=tex}
`\approx 5.15`{=tex} `\mathrm{N\,m}`{=tex} \]

The elbow estimate of approximately 2.57 N·m follows the illustrative
175 mm + 175 mm link split.

As with DA-05, this is a payload-only lower-bound screen. It excludes
arm/link/gripper/cable self-weight, motor/gearbox mass, inertia,
friction and actual motion profiles.

### 5.4 Material issue: shoulder yaw torque

The deck assigns ≥5.2 N·m to both shoulder yaw and shoulder pitch, and
labels both M/L.

This is not justified by the calculation shown. The 5.15 N·m calculation
is a gravity moment from a payload at horizontal reach. It is relevant
to a joint axis that must resist that gravity moment, such as a
horizontal shoulder-pitch axis in the assumed posture.

A vertical shoulder-yaw axis does not experience the same static gravity
moment about its own axis. Yaw sizing instead needs an analysis of
rotational inertia about the yaw axis, angular acceleration, friction,
cable forces, external loads and any geometry-dependent coupling. The
yaw axis may still require substantial torque, but it cannot be assigned
the pitch result without a separate calculation.

**Required correction:** separate yaw and pitch load cases. For pitch,
include the mass and CoM of all downstream links and payload. For yaw,
calculate the relevant inertia and dynamic torque about the vertical
axis, and include friction/cable/external disturbance terms. Do not
retain "≥5.2 N·m" as a yaw requirement unless a distinct calculation
supports it.

### 5.5 Base stability

The deck uses a 25 kg nominal mass, centred CoM and 125 mm half-base:

\[ M\_{restore}=25 `\times 9.81`{=tex} `\times 0.125`{=tex}
`\approx 30.7`{=tex} `\mathrm{N\,m}`{=tex} \]

It compares this with the same 1.72 N·m payload-only moment and reports
approximately 17.8×.

The arithmetic is correct under the simplified assumptions, but the
ratio is not a verified stability margin. It does not account for actual
arm extension and shoulder location, both arms and unequal loads,
mast/camera mass and CoM, base attachment boundary conditions or dynamic
arm motion.

### 5.6 Mast and camera stability

The deck identifies a relevant coupling:

**arm motion → mast vibration → camera pose movement/image blur →
degraded vision accuracy.**

It also correctly identifies that numerical analysis cannot be completed
without mast section, material, camera mass and boundary conditions.

This is a significant system-level risk and should be quantified
analytically before any detailed design decision. A paper beam model can
estimate static deflection and first-order stiffness/frequency
sensitivity using explicitly labelled assumptions. It should consider:

-   Mast free length and support condition.
-   Section geometry and material modulus.
-   Camera and bracket masses and their offsets.
-   Arm-motion disturbance assumptions.
-   Camera pose/deflection tolerance linked to the vision requirement.
-   Resonance separation from dominant arm-motion frequencies.

The deck also identifies camera occlusion, hand-eye calibration versus
mast height, cable fatigue/pinch and actuator sizing risks. These are
appropriate open risks, but they need traceable IDs, severity/likelihood
rationale and closure evidence.

### 5.7 Workspace, mass and structural status

The exact 3D workspace is not calculated because link geometry and joint
limits are not finalized. The 800 mm width is a packaging target, not a
reachable-workspace result.

The 20--30 kg mass range is an estimate. No component-level mass budget
or CoM roll-up is supplied. Structural load cases include shoulder,
elbow, wrist, base/tabletop, fasteners/plates and mast. FEA is correctly
deferred pending geometry, material and load inputs.

### 5.8 DA-06 verdict

**Architecture: GOOD preliminary definition.**\
**Quantitative feasibility: PARTIAL.**\
**Yaw/pitch actuator classification: CORRECTION REQUIRED.**\
**Actuator selection: NOT READY.**\
**CP3: PENDING.**

The yaw/pitch torque-axis issue is the most important technical
correction in this deck. The mast/camera stiffness risk should also be
carried as a first-class system risk.

------------------------------------------------------------------------

## 10. Detailed concept review --- QR-06

### 6.1 Submitted architecture

The deck describes a six-legged hexapod with:

-   Six legs arranged as front, middle and rear bilateral pairs.
-   Two actuated DOFs per leg: Hip Yaw and Knee Pitch.
-   Twelve baseline actuators/DOFs.
-   Rigid central body, interchangeable leg assemblies and replaceable
    feet.
-   Optional six-axis force sensing, RGB-D camera and IMU.
-   Concept-level 24 V power/control architecture.
-   Body-to-leg, hip-to-link, knee-to-lower-link, foot-to-ground,
    body-to-sensor and body-to-harness interfaces.

The modular leg concept, replaceable foot pads and protected cable paths
are useful design directions.

### 6.2 Concept targets

  Parameter              Submitted value Review interpretation
  -------------------- ----------------- -----------------------
  Body length                     400 mm Concept target
  Body width                      280 mm Concept target
  Body height                     220 mm Concept target
  Overall length                  520 mm Concept target
  Overall width                   480 mm Concept target
  Target mass                    3--5 kg Concept target
  Payload                    0.5--1.0 kg Concept target
  Baseline actuators                  12 Two per leg
  Leg DOF                              2 Hip yaw + knee pitch

### 6.3 Payload torque calculation

The deck uses:

-   Payload: 1.0 kg
-   Provisional moment arm: 0.26 m
-   Dynamic factor: 2.0
-   Sizing margin: 1.5

Payload force:

\[ F=1.0 `\times 9.81`{=tex}=9.81 `\mathrm{N}`{=tex} \]

Static payload moment:

\[ T=9.81 `\times 0.26`{=tex}=2.55 `\mathrm{N\,m}`{=tex} \]

After the stated factors:

\[ T\_{screen}=2.55 `\times 2.0`{=tex} `\times 1.5`{=tex}
`\approx 7.65`{=tex} `\mathrm{N\,m}`{=tex} \]

The arithmetic is correct. The deck explicitly calls this a payload-only
screening result and leaves knee torque TBD.

However, the 0.26 m provisional arm is not shown to be the perpendicular
distance from the payload/load line to the Hip or Knee joint axis for a
defined posture. The same arm cannot automatically represent both
joints. The deck also does not establish how the payload is mounted, how
many legs share the load, what the leg posture is, or what the ground
reaction forces are.

**Conclusion:** 7.65 N·m is an illustrative payload moment with a factor
multiplier, not a derived Hip actuator requirement and not a basis for
selecting M/L actuators.

### 6.4 Required joint-load methodology

The next analysis should define representative static and gait cases,
for example:

1.  Six-leg static stance, no payload.
2.  Six-leg static stance, maximum payload.
3.  Tripod support phase with three stance legs.
4.  Swing-leg transition and load transfer.
5.  Uneven terrain or one-foot contact variation, if within intended
    use.
6.  Payload centre-of-mass offset and worst-case body/leg orientation.

For each case, calculate or estimate the ground reaction forces and
resolve moments about the actual Hip and Knee axes using defined link
lengths, joint positions and posture. Include leg/link/actuator
self-weight, payload location, acceleration assumptions and a clear
load-sharing model. The Hip Yaw and Knee Pitch axes need separate torque
derivations.

### 6.5 Stability calculation

The deck uses:

-   Nominal robot mass: 4 kg
-   Body half-width: 0.14 m
-   Gravity: 9.81 m/s²

\[ M=4 `\times 9.81`{=tex} `\times 0.14`{=tex}
`\approx 5.49`{=tex} `\mathrm{N\,m}`{=tex} \]

This is a body-level static moment screen. It omits the 1 kg payload and
does not calculate the combined robot-plus-payload CoM.

More importantly, hexapod stability must be evaluated against the
**support polygon of the feet currently in contact with the ground**.
During tripod gait, the relevant support region is a triangle formed by
the stance feet, not simply half the body width. The projected combined
CoM must be checked against that support polygon, with a stated support
margin. Foot-ground reactions and load distribution must also be
considered.

**Required correction:** provide foot contact coordinates for
representative stance configurations, support polygons for six-leg
stance and tripod stance, combined CoM projections with and without
payload, and the minimum support margin through the gait cycle. Do not
report 5.49 N·m as a dynamic walking stability margin.

### 6.6 Mass, structure, workspace and actuator status

The 3--5 kg target and 4 kg calculation midpoint are not a
component-level mass budget. With twelve actuators, actuator/gearbox
mass is a significant architecture variable and can create a feedback
loop: heavier actuators increase leg/body mass, which raises joint loads
and may require larger actuators.

The deck appropriately lists body/leg structural analysis, workspace,
gait stability and actuator sizing as unresolved. It also identifies
cable routing and body interface questions. These need to be translated
into traceable requirements, assumptions, risks and calculation
evidence.

### 6.7 QR-06 verdict

**Architecture: GOOD preliminary definition.**\
**Quantitative feasibility: INCOMPLETE.**\
**Hip/Knee actuator sizing: NOT READY.**\
**Dynamic stability: NOT DEMONSTRATED.**\
**CP3: PENDING.**

The 7.65 N·m result must remain a provisional payload-only screen. The
next critical work is geometry-based joint loading and support-polygon
analysis.

------------------------------------------------------------------------

## 11. Nishant concept-set findings and required corrections

  -------------------------------------------------------------------------------------------------
  Finding ID     Concept(s)     Finding                    Severity       Required evidence /
                                                                          closure
  -------------- -------------- -------------------------- -------------- -------------------------
  N-01           QR-03          Dedicated engineering      Critical       Submit report,
                                report is absent from the                 branch/commit and
                                submitted ZIP; only                       changed-file evidence
                                concept overview is                       
                                available                                 

  N-02           DA-05, DA-06   Arm torque calculations    High           Free-body diagrams and
                                are payload-only and omit                 joint torque calculations
                                link/joint/gripper/cable                  including downstream
                                mass and inertia                          mass/CoM and motion cases

  N-03           DA-06          Same gravity-derived       High           Separate yaw-axis
                                torque is assigned to                     inertia/dynamic
                                shoulder yaw and shoulder                 calculation from
                                pitch                                     pitch-axis gravity
                                                                          calculation

  N-04           DA-05          Rotary-base inertia/torque High           Component inertia model,
                                model is illustrative and                 arm-pose cases,
                                omits mass distribution                   speed/acceleration and
                                and interface losses                      bearing/slip-ring/cable
                                                                          torque assumptions

  N-05           DA-05          Stability ratio assumes    High           Combined CoM and
                                centred CoM and does not                  tipping-edge moment cases
                                resolve actual tipping                    for relevant arm
                                edge/arm poses                            configurations

  N-06           QR-06          7.65 N·m is based on a     Critical       Geometry-based Hip and
                                provisional arm not tied                  Knee free-body
                                to a defined joint                        calculations for defined
                                axis/posture                              load cases

  N-07           QR-06          Static body-level          Critical       Six-leg and tripod
                                restoring moment is not                   support polygons, CoM
                                support-polygon or gait                   projection and foot
                                stability analysis                        reaction/load cases

  N-08           All            No complete                High           Mass budget by subsystem,
                                component-level mass                      estimated/known status,
                                budget or mass-property                   CoM and inertia basis
                                roll-up                                   

  N-09           All            Actuator S/M/L             High           Candidate
                                classifications are not                   motor/gearbox/encoder
                                backed by complete                        data and
                                torque-speed-duty                         torque-speed/duty
                                compatibility                             comparison

  N-10           DA-06          Concept name/priority      Medium         Owner/program
                                differs between assignment                reconciliation of concept
                                context and submitted                     scope, name and priority
                                deck/concept description                  

  N-11           All            Submission ZIP does not    High           Provide canonical branch,
                                establish repository                      commit SHA, PR or merged
                                branch, commit, review                    commit, and file paths
                                state or accepted-file                    
                                status                                    

  N-12           All            Cost model and comparative Medium         Cost assumptions, sourced
                                feasibility evidence are                  component estimates,
                                absent or incomplete                      exclusions and common
                                                                          comparison basis
  -------------------------------------------------------------------------------------------------

Severity describes the impact on technical readiness, not intern
performance.

------------------------------------------------------------------------

## 12. CP3 evidence-readiness matrix

The following matrix evaluates the evidence visible in the submitted
material. "Partial" means some relevant work exists but is not
sufficient for acceptance. "Not evidenced" means the submitted files do
not establish completion.

  --------------------------------------------------------------------------------------
  CP3 evidence     DA-05             QR-03           DA-06             QR-06
  area                                                                 
  ---------------- ----------------- --------------- ----------------- -----------------
  Architecture /   Partial-to-good   Concept         Partial-to-good   Partial-to-good
  DOF                                overview only                     

  Mechanical       Partial           Not evidenced   Partial           Partial
  configuration /                                                      
  assembly                                                             

  Interfaces /     Partial           Not evidenced   Partial           Partial
  serviceability                                                       

  Torque           Partial;          Not evidenced   Partial; yaw      Incomplete; arm
  derivation       payload-only                      error             basis unverified

  Speed /          Not evidenced     Not evidenced   Not evidenced     Not evidenced
  acceleration /                                                       
  duty                                                                 

  Actuator S/M/L   Blocked           Not evidenced   Blocked           Blocked
  compatibility                                                        

  Structural       Load cases        Not evidenced   Load cases        Load cases
  loading          identified; not                   identified; mast  identified; not
                   calculated                        model pending     calculated

  Static/dynamic   Simplified static Not evidenced   Simplified static Incomplete;
  stability        screen only                       screen only       support polygon
                                                                       absent

  Workspace /      Target reach only Not evidenced   Target reach only Not evidenced
  kinematics                                                           quantitatively

  Mass budget /    Incomplete        Not evidenced   Incomplete        Incomplete
  CoM                                                                  

  Cost model       Not evidenced     Not evidenced   Not evidenced     Not evidenced

  Risks / unknowns Partial           Concept-level   Partial           Partial
                                     only                              

  Repository       Not established   Not established Not established   Not established
  traceability     by ZIP            by ZIP          by ZIP            by ZIP
  --------------------------------------------------------------------------------------

**Checkpoint recommendation: CP3 remains PENDING for DA-05, QR-03, DA-06
and QR-06.** This is a review recommendation, not a checkpoint decision.
The owner/review authority must record any formal status change.

------------------------------------------------------------------------

## 13. Recommended correction plan for Nishant

The following order is recommended so that calculations are based on
controlled inputs rather than repeatedly changing assumptions.

### Priority 0 --- Evidence and assignment integrity

1.  Provide the QR-03 engineering report; do not use the concept
    overview as a substitute.
2.  Publish or identify the exact INTERN-03 branch and commit SHA.
3.  Ensure each concept folder contains the current engineering
    evidence, assumptions, calculation files and open issues.
4.  Reconcile DA-06 concept name/scope and priority with the assignment
    register through the owner/program process.
5.  Update the weekly status record with dates, work completed,
    blockers, deliverable links and commit references. Do not mark a
    checkpoint passed unless the authorized reviewer has done so.

### Priority 1 --- Freeze calculation inputs on paper

For each concept, provide a controlled input table with:

-   Geometry and link lengths.
-   Joint-axis directions and joint limits.
-   Payload mass and payload CoM.
-   Link, gripper, actuator and gearbox mass assumptions.
-   Estimated component CoM locations.
-   Required joint speed, acceleration and duty cycle.
-   Gravity and environmental assumptions.
-   Dynamic/load factors and their rationale.
-   Known values versus estimates versus unknowns.

Every assumption should have an ID and source or rationale. Do not mix a
target value with a measured or verified value.

### Priority 2 --- Complete concept-specific calculations

**DA-05** - Shoulder, elbow and wrist free-body calculations including
link and end-effector mass. - Rotary-base component inertia and torque
estimate. - Bearing radial, axial and overturning load cases. -
Slip-ring/cable torque and rotation-life assumptions. - Tipping-edge
stability cases for extended arms and asymmetric payloads.

**QR-03** - Complete architecture and joint-axis definition. - Link
geometry and representative postures. - Hip/knee torque-speed estimates
for standing and gait cases. - Four-leg support polygon and CoM
projection for relevant gait phases. - Mass and actuator packaging
budget.

**DA-06** - Separate shoulder-pitch gravity sizing from shoulder-yaw
dynamic sizing. - Include downstream link, wrist, gripper and
camera/cable mass as applicable. - Establish mast
beam/deflection/stiffness screening model and camera-pose tolerance. -
Check camera field-of-view/occlusion and hand-eye calibration
assumptions. - Revisit stability with mast and camera masses included.

**QR-06** - Define leg link lengths, joint axes, joint limits and
representative postures. - Derive Hip and Knee loads separately from
actual joint geometry. - Calculate ground reactions and load sharing for
six-leg and tripod support. - Evaluate support polygon and combined CoM
projection with payload. - Check the actuator mass feedback effect
against the 3--5 kg target.

### Priority 3 --- Actuator and cost comparison

Only after torque-speed-duty requirements are sufficiently defined:

-   List candidate motor, gearbox and encoder combinations.
-   Compare continuous torque, peak torque, speed, duty/thermal
    capability, backlash, efficiency, mass and supply compatibility.
-   Distinguish motor-shaft torque from gearbox-output torque.
-   Include gearbox ratio and efficiency explicitly.
-   Identify whether each requirement is continuous, intermittent peak,
    holding or dynamic.
-   Record data sources and date of retrieval.
-   Prepare a cost model with quantity, source, currency, estimate
    status, exclusions and contingency assumptions.

Do not convert a preliminary "S/M/L" label into an approved actuator
selection.

### Priority 4 --- Common review and cross-check

Use a common review sheet for all four concepts so that torque, mass,
stability, actuator and cost evidence is comparable. Have another intern
or reviewer independently check equations, units, load cases and
assumptions. Cross-review does not constitute owner approval.

------------------------------------------------------------------------

## 14. Suggested common calculation/evidence format

For each calculation, use the following structure:

1.  **Calculation ID and title**
2.  **Requirement or question being answered**
3.  **Concept and subsystem**
4.  **Load case / posture / operating condition**
5.  **Diagram or free-body representation**
6.  **Inputs table** --- value, unit, source, status
    (known/estimated/assumed/TBD)
7.  **Equations and derivation**
8.  **Result with units**
9.  **Sensitivity to uncertain inputs**
10. **Limitations and excluded effects**
11. **Engineering conclusion** --- what the result does and does not
    establish
12. **Reviewer and review status**
13. **Repository path and commit SHA**

For actuator sizing, include a separate row for each joint and each
relevant load case. At minimum distinguish:

-   Gravity/holding torque.
-   Continuous operating torque.
-   Peak/dynamic torque.
-   Required output speed.
-   Acceleration/inertia torque.
-   Duty cycle and thermal constraint.

For legged robots, include support configuration and foot contact
assumptions with every stability or joint-load result.

------------------------------------------------------------------------

## 15. Final review disposition

### 11.1 Disposition

-   **DA-05:** retain as useful architecture and preliminary calculation
    evidence; corrections required; CP3 pending.
-   **QR-03:** concept overview received, engineering report not
    received; assessment not possible; CP3 not evidenced.
-   **DA-06:** retain as architecture and preliminary calculation
    evidence; correct the yaw/pitch torque treatment; CP3 pending.
-   **QR-06:** retain as architecture and preliminary screening
    evidence; rebuild joint-load and gait-stability basis; CP3 pending.

### 11.2 Overall conclusion

The submission demonstrates a reasonable start on architecture
definition and identification of engineering unknowns. The work is not
yet at the level needed to close quantitative feasibility or select
actuators. The most important next step is not to add more concept
slides, but to establish controlled geometry and mass assumptions,
derive joint-specific torque-speed requirements, and validate stability
using the correct physical support/load model.

**No concept is approved for detailed design or hardware realization by
this review. D-003 HOLD remains unchanged.**

------------------------------------------------------------------------

## 16. Cross-intern comparison — evidence maturity, not intern ranking

This section compares the nature of submitted work and evidence maturity. It must not be interpreted as a performance ranking: the concepts differ in architecture and complexity, and the evidence packages are not identical.

| Dimension | INTERN-01 Amardeep | INTERN-02 Divagar | INTERN-03 Nishant |
|---|---|---|---|
| Main strength | Most advanced quantitative comparison workflow; joint-level screens and cost/mass framework | Broadest structured documentation baseline; requirements and open-question registers | Clear architecture/interface decomposition and identification of unresolved technical risks |
| Main weakness | Quantitative comparison/cost/mass basis not fully reconciled; torque terminology and actuator matching unresolved | Claimed document completeness not fully verified; cost only scope; QR-05 interface/evidence incomplete | Load calculations often payload-only or use incomplete physical models; QR-03 engineering report missing |
| Cost readiness | Estimates shown in status deck, but not accepted as decision-grade pending source reconciliation | Scope only; no values | Not evidenced / incomplete |
| Mass readiness | Incomplete/unknown where not supported by component roll-up | Estimated bands and CoM; QR-01/QR-05 exceed printed target | Incomplete component-level mass budgets |
| Actuator readiness | S/M/L family screen only | Not assessed | Not demonstrated |
| Checkpoint status | Task 044 review pending; CP3 pending | CP3 pending | CP3 pending |

### 16.1 Cross-intern findings

| Finding ID | Scope | Consolidated finding | Required closure |
|---|---|---|---|
| CI-01 | All 12 concepts | No complete, reviewed torque-speed-duty evidence package supports actuator selection across the programme | Joint-specific load cases, formulas, inputs, speed, duty and reviewer sign-off |
| CI-02 | All 12 concepts | S/M/L family labels are not compatibility evidence | Revisioned actuator variant data and joint-by-joint compatibility matrix |
| CI-03 | All 12 concepts | Mass budgets are at different levels of maturity and are not consistently closed | Standard component mass categories, estimated/known status, CoM and inertia roll-up |
| CI-04 | All 12 concepts | Torque terminology and planning factors are not yet consistently controlled | Common glossary and calculation template; separate continuous, holding, dynamic peak and output torque |
| CI-05 | All 12 concepts | Stability analyses use differing simplified assumptions and are not consistently tied to support/contact geometry | Common static and dynamic load-case definitions; support polygon/contact model for legged concepts |
| CI-06 | All 12 concepts | Cost evidence is not comparable: some values are estimates with source/reconciliation issues, some are scope-only, and some are absent | Common cost model with quantities, source/date, currency, exclusions and estimate confidence |
| CI-07 | All 12 concepts | Requirement and calculation traceability is not uniformly demonstrated | Link CREQ/FREQ/U/RISK/A/M/S IDs to calculations, source files and review evidence |
| CI-08 | All 12 concepts | Repository evidence must be distinguished from slide claims | Record canonical repo, branch, commit SHA, paths, PR/merge status and reviewer |
| CI-09 | QR-05 | Module interface remains an unresolved feasibility dependency | Interface definition and load/retention/stiffness/serviceability analysis |
| CI-10 | QR-03 | Dedicated engineering report absent from Nishant's submitted ZIP | Submit and review the engineering report before crediting engineering deliverables |

### 16.2 Common calculation and data standards

Adopt one common template across all twelve concepts:

**Torque and motion**
- Joint ID, axis direction and reference frame.
- Load case and posture.
- Downstream link/actuator/gripper/payload masses and CoM.
- Gravity torque, inertia/acceleration torque, friction/cable/external torque.
- Continuous torque, peak torque and permitted duration.
- Required output speed, acceleration and duty.
- Gear ratio, efficiency and motor-side/output-side distinction.
- Formula, units, assumptions, sensitivity and limitations.

**Mass and stability**
- Component mass by subsystem.
- Status: known, estimated, assumed or TBD.
- Component CoM and total CoM calculation.
- Inertia estimate where rotary motion matters.
- Support polygon/contact set for legged robots.
- Tipping edge and combined CoM for fixed-base systems.
- Static and dynamic load cases kept distinct.

**Actuator data**
- Controlled actuator variant/revision.
- Continuous and peak output torque.
- Output speed under load.
- Thermal/duty capability.
- Gear ratio, efficiency and backlash.
- Mass, dimensions, encoder and electrical requirements.
- Price/source/date and maturity.
- Requirement-to-variant compatibility result with rationale.

**Traceability**
- CREQ/FREQ requirement IDs.
- U unknowns and RISK IDs.
- A assumptions, M mass IDs and S source IDs.
- CALC IDs and repository paths.
- Reviewer name/role, review date and status.
- Exact commit SHA and PR/merge reference.

### 16.3 Consolidated CP3 recommendation

| Intern | Concepts | Recommendation | Formal status |
|---|---|---|---|
| INTERN-01 Amardeep | DA-01, QR-02, DA-04, QR-04 | Retain quantitative progress; reconcile calculation terminology, cost/mass sources, comparison status and actuator evidence; complete independent Task 044 review | CP3 PENDING |
| INTERN-02 Divagar | DA-02, DA-03, QR-01, QR-05 | Retain documentation foundation; reconcile DA-02 torque discrepancy; verify repository artefacts; close QR-05 interface and calculation evidence; cost remains scope-only | CP3 PENDING |
| INTERN-03 Nishant | DA-05, QR-03, DA-06, QR-06 | Retain architecture work; correct physical load models; submit QR-03 report; complete mass, actuator and stability evidence | CP3 PENDING |

**No PASS recommendation is made for any intern or concept in this consolidated review.** Only the authorized owner/reviewer may change checkpoint status.

---

## 17. Consolidated action plan

### Priority 0 — Repository and evidence integrity
1. For each intern, record exact repository, branch, commit SHA, file paths and PR/merge state.
2. Reconcile Amardeep's comparison/cost/mass claims against the latest authoritative repository state.
3. Reconcile Divagar's claimed 32 artefacts against the authoritative branch; explicitly identify missing QR-05 files and calculation files.
4. Obtain Nishant's QR-03 engineering report and repository evidence.
5. Ensure weekly status records distinguish work drafted, committed, merged, reviewed and accepted.

### Priority 1 — Common calculation baseline
1. Publish the common torque/speed/duty terminology and template.
2. Recompute or reconcile all joint screens using actual joint axes and representative load cases.
3. Keep static holding, continuous, dynamic peak and output speed separate.
4. Document the basis for every dynamic allowance and planning factor.
5. Do not classify actuator families until controlled actuator data is available.

### Priority 2 — Mass, stability and structural evidence
1. Use one component-level mass taxonomy across all concepts.
2. Include actuator/gearbox mass feedback in mass and torque estimates.
3. Revisit legged-robot support polygons and gait load sharing.
4. Revisit fixed-base tipping edges and combined CoM.
5. Complete paper analytical structural checks where geometry and material assumptions permit; do not claim FEA or physical validation when not performed.

### Priority 3 — Cost and comparison
1. Reconcile Amardeep's nominal cost estimates with sourced line items and the current repository state.
2. Keep Divagar's cost status as SCOPE ONLY until values are supported.
3. Add cost models for Nishant's concepts only when the scope and component assumptions are defined.
4. Compare concepts only after the scoring criteria, weights, data completeness and unscored items are controlled.
5. Treat ₹2 lakh as a planning ceiling, not spending authority.

### Priority 4 — Review and acceptance
1. Cross-review calculations across interns using the common template.
2. Record comments, corrections and evidence closure in the repository.
3. Keep all checkpoints pending until the authorized reviewer records acceptance.
4. Preserve D-003 HOLD unless explicitly changed by the owner.

---

## 18. Final consolidated disposition

- **INTERN-01 Amardeep:** strongest quantitative progress in the submitted status package, but comparison, mass/cost reconciliation, torque terminology and S/M/L compatibility remain open. Task 044 acceptance is not claimed. CP3 pending.
- **INTERN-02 Divagar:** strong documentation foundation and broad draft coverage, but cost is scope-only, QR-05 interface/evidence is incomplete, and repository completeness needs verification. CP3 pending.
- **INTERN-03 Nishant:** useful architecture work and initial calculations, but key load models need correction/completion and QR-03 engineering report is absent from the submitted ZIP. CP3 pending.

**Programme-level conclusion:** the three submissions provide a useful paper-feasibility baseline, not a completed feasibility closure. No concept is approved for detailed design or hardware realization by this review. **D-003 HOLD remains unchanged.**

---

## Appendix C — Consolidated submitted evidence inventory

| Intern | Submitted evidence reviewed | Evidence limitation |
|---|---|---|
| INTERN-01 Amardeep | `Amar_Updates.pptx` | Weekly status deck identifies branch `feasibility/intern-01-week3` and PR #18 contribution; underlying calculation/source files and current repo state still require independent reconciliation |
| INTERN-02 Divagar | `Divagar_Weekly_Status.pptx` | Weekly status deck reports 8 draft artefacts per concept; exact branch/commit/path inventory requires reconciliation, especially QR-05 |
| INTERN-03 Nishant | `Kritva Robotics-20261128T090914Z-1-001.zip` containing DA-05, DA-06, QR-06 engineering PPTX files and DA-05, QR-03, DA-06, QR-06 concept PDFs | QR-03 engineering report absent; ZIP does not establish repository branch/commit/acceptance |

## Appendix D — Repository and governance references

- [Mechanical feasibility concepts](https://github.com/KritvaOS/kritva-mechanical/tree/main/feasibility/concepts)
- [Intern assignments](https://github.com/KritvaOS/kritva-mechanical/blob/main/feasibility/INTERN_ASSIGNMENTS.md)
- [Study plan](https://github.com/KritvaOS/kritva-mechanical/blob/main/feasibility/STUDY_PLAN.md)
- [INTERN-03 weekly status](https://github.com/KritvaOS/kritva-mechanical/blob/main/feasibility/interns/INTERN-03/WEEKLY_STATUS.md)

These references are provided for repository verification. This consolidated document does not claim that all three intern branches and every underlying artefact were independently re-fetched during preparation of this revision.

## Appendix E — INTERN-03 submitted evidence inventory

The review ZIP contains:

  --------------------------------------------------------------------------
  Concept           File                 Type              Use in this
                                                           review
  ----------------- -------------------- ----------------- -----------------
  DA-05             `DA-05/DA-05.pptx`   Engineering       Primary
                                         presentation      engineering
                                                           evidence

  DA-05             `DA-05/DA 05.pdf`    Concept overview  Concept reference
                                         PDF               

  DA-06             `DA-06/DA-06.pptx`   Engineering       Primary
                                         presentation      engineering
                                                           evidence

  DA-06             `DA-06/DA 06.pdf`    Concept overview  Concept reference
                                         PDF               

  QR-03             `QR-03/QR 03.pdf`    Concept overview  Concept baseline
                                         PDF               only; no
                                                           engineering
                                                           report

  QR-06             `QR-06/QR-06.pptx`   Engineering       Primary
                                         presentation      engineering
                                                           evidence

  QR-06             `QR-06/QR 06.pdf`    Concept overview  Concept reference
                                         PDF               
  --------------------------------------------------------------------------

**Evidence limitation:** the ZIP does not, by itself, establish
repository branch names, commit SHAs, pull-request state, merged status
or formal checkpoint acceptance. Those must be verified against the
repository and its review records before the work is treated as an
accepted program deliverable.

## Appendix F — Source and governance references used for INTERN-03

The following repository references should be used to verify assignment
and process status:

-   [Intern
    assignments](https://github.com/KritvaOS/kritva-mechanical/blob/main/feasibility/INTERN_ASSIGNMENTS.md)
-   [Study
    plan](https://github.com/KritvaOS/kritva-mechanical/blob/main/feasibility/STUDY_PLAN.md)
-   [INTERN-03 weekly
    status](https://github.com/KritvaOS/kritva-mechanical/blob/main/feasibility/interns/INTERN-03/WEEKLY_STATUS.md)
-   [Mechanical feasibility
    concepts](https://github.com/KritvaOS/kritva-mechanical/tree/main/feasibility/concepts)

These links are references for repository verification; this review does
not claim that the current branch contents were independently re-fetched
as part of preparing this Markdown artifact.
