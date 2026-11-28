# INTERN-01 — Four-concept comparison matrix (Week 3/4 estimate)

| Property | Value |
|---|---|
| Document ID | KMECH-CMP-INTERN-01 |
| Status | PROPOSED — paper comparison; not CP4 acceptance |
| Version | 0.4.0 |
| Last Updated | 2026-11-28 |
| Assigned Intern | INTERN-01 |
| HOLD | D-003 active |

This matrix covers the four INTERN-01 concepts only. All scores are provisional ESTIMATE/C evidence, based on the linked mass, cost, mechanical and actuator screens. The complete 12-concept study is not represented here.

## 1. Criteria and weights

Weights are copied from [EVALUATION_CRITERIA.md](../../EVALUATION_CRITERIA.md) and remain proposed. No weights are changed here.

| ID | Criterion | Weight |
|---|---|---:|
| EC-01 | Mechanical feasibility | 20% |
| EC-02 | Actuator availability and compatibility | 15% |
| EC-03 | Hardware cost | 20% |
| EC-04 | Fabrication simplicity | 10% |
| EC-05 | Kritva platform demonstration value | 20% |
| EC-06 | Modularity and upgrade potential | 10% |
| EC-07 | Mechanical safety | 5% |
| | **Total** | **100%** |

## 2. Provisional scorecard

| Criterion | Weight | DA-01 | QR-02 | DA-04 | QR-04 | Evidence level and reference | Score rationale |
|---|---:|---:|---:|---:|---:|---|---|
| EC-01 Mechanical feasibility | 20% | 4 | 3 | 2 | 2 | C / ESTIMATE; see evidence map below. Component geometry is assumed where artwork is schematic. | DA-01 fixed tabletop path is simplest; QR-02 has conventional legs but static-only contact basis; DA-04 adds tall mobile base/arms; QR-04 adds long-leg moment and target-mass pressure. No structure or gait validation. |
| EC-02 Actuator availability and compatibility | 15% | 4 | 2 | 3 | 2 | C / ESTIMATE; see evidence map below. Product listings compared with proposed family roles. | DA-01 10 Nm reference clears modeled screens; QR-02 10 Nm load case conflicts with L role; DA-04 1 kg arm case requires a 48 V upgrade; QR-04 10 Nm misses high hip-flexion scenario. No variant is qualified. |
| EC-03 Hardware cost | 20% | 3 | 2 | 2 | 1 | ESTIMATE; see evidence map below. Foreign landing/conditioning excluded. | Economy cases are below ₹2 lakh, but role/load-compatible alternatives exceed it for the quadrupeds and high-payload DA-04. |
| EC-04 Fabrication simplicity | 10% | 4 | 3 | 2 | 2 | ESTIMATE; see evidence map below. Qualitative part/interface count only. | Fixed tabletop assembly has fewer moving subsystems; repeated leg joints, long links and mobile arm/base integration add alignment and routing. No fabrication trial. |
| EC-05 Kritva platform demonstration value | 20% | 3 | 4 | 5 | 4 | ESTIMATE; see evidence map below. Program value is qualitative. | DA-04 combines mobility/manipulation; quadrupeds add locomotion; DA-01 is a controlled manipulation platform. Owner/program scoring remains needed. |
| EC-06 Modularity and upgrade | 10% | 3 | 3 | 3 | 4 | ESTIMATE; see evidence map below. Indicated interface patterns are not load-rated. | QR-04 shows the clearest module/body interface; the mount remains illustrative. Other concepts show modular joint intent without verified interface loads. |
| EC-07 Mechanical safety | 5% | 3 | 2 | 2 | 2 | ESTIMATE; see evidence map below. Static tipping/contact sensitivities only. | DA-01 has an optimistic support-edge estimate; quadrupeds add gait/contact hazards; DA-04 adds tall mobile/tipping exposure; QR-04 adds long-leg dynamic risk. No formal hazard or physical safety validation. |
| **Weighted total (out of 5)** | **100%** | **3.45** | **2.80** | **2.85** | **2.40** | Weighted sum; all seven proposed criteria scored on estimates. | Provisional only. |

## Evidence map

| Criterion | Per-concept references | Shared basis |
|---|---|---|
| EC-01 | [DA-01](../../concepts/DA-01/MECHANICAL_ANALYSIS.md), [QR-02](../../concepts/QR-02/MECHANICAL_ANALYSIS.md), [DA-04](../../concepts/DA-04/MECHANICAL_ANALYSIS.md), [QR-04](../../concepts/QR-04/MECHANICAL_ANALYSIS.md); mass values in the [central method](WEEK3_ESTIMATE_METHOD.md) | [Estimate method](WEEK3_ESTIMATE_METHOD.md), published artwork targets. |
| EC-02 | [DA-01](../../concepts/DA-01/ACTUATOR_ANALYSIS.md), [QR-02](../../concepts/QR-02/ACTUATOR_ANALYSIS.md), [DA-04](../../concepts/DA-04/ACTUATOR_ANALYSIS.md), [QR-04](../../concepts/QR-04/ACTUATOR_ANALYSIS.md); corresponding CALC files | [Source register](WEEK3_SOURCE_REGISTER.md), proposed family specification. |
| EC-03 | [DA-01](../../concepts/DA-01/COST_MODEL.md), [QR-02](../../concepts/QR-02/COST_MODEL.md), [DA-04](../../concepts/DA-04/COST_MODEL.md), [QR-04](../../concepts/QR-04/COST_MODEL.md) | [EVALUATION_CRITERIA.md, EC-03](../../EVALUATION_CRITERIA.md), [REQUIREMENTS_REGISTER.md, FREQ-032](../../REQUIREMENTS_REGISTER.md), [Source register](WEEK3_SOURCE_REGISTER.md). |
| EC-04 | Four concept architecture and mechanical-analysis records; see [DA-01](../../concepts/DA-01/ARCHITECTURE.md), [QR-02](../../concepts/QR-02/ARCHITECTURE.md), [DA-04](../../concepts/DA-04/ARCHITECTURE.md), [QR-04](../../concepts/QR-04/ARCHITECTURE.md) | [Estimate method](WEEK3_ESTIMATE_METHOD.md); paper-only qualitative assumptions. |
| EC-05 | [DA-01](../../concepts/DA-01/README.md), [QR-02](../../concepts/QR-02/README.md), [DA-04](../../concepts/DA-04/README.md), [QR-04](../../concepts/QR-04/README.md) | [EVALUATION_CRITERIA.md, EC-05](../../EVALUATION_CRITERIA.md); proposed program value. |
| EC-06 | [DA-01](../../concepts/DA-01/INTERFACES.md), [QR-02](../../concepts/QR-02/INTERFACES.md), [DA-04](../../concepts/DA-04/INTERFACES.md), [QR-04](../../concepts/QR-04/INTERFACES.md) | [Estimate method](WEEK3_ESTIMATE_METHOD.md); indicative interfaces are not load-rated. |
| EC-07 | [DA-01](../../concepts/DA-01/MECHANICAL_ANALYSIS.md), [QR-02](../../concepts/QR-02/MECHANICAL_ANALYSIS.md), [DA-04](../../concepts/DA-04/MECHANICAL_ANALYSIS.md), [QR-04](../../concepts/QR-04/MECHANICAL_ANALYSIS.md) | [EVALUATION_CRITERIA.md, HG-03](../../EVALUATION_CRITERIA.md); no physical safety validation. |

## 3. Partial ordering

All seven criteria contribute their proposed weights, for 100% scored weight among the four assessed concepts. The calculation is sum(score × weight) / 100, yielding a 0–5 weighted contribution. The paired-AK10 L-role prices below assume ideal additive torque and load sharing; no coupler or mechanical arrangement is validated. The ordering is partial because only 4 of 12 concepts are included, not because a criterion was silently removed. Estimates do not constitute CP4 acceptance or a final recommendation.

| Partial rank within assigned set | Concept | Weighted contribution / 5 | Scored weight |
|---:|---|---:|---:|
| 1 | DA-01 | 3.45 | 100% |
| 2 | DA-04 | 2.85 | 100% |
| 3 | QR-02 | 2.80 | 100% |
| 4 | QR-04 | 2.40 | 100% |

## 4. Cost and load scenario check (INR)

The ₹2,00,000 study ceiling is from EVALUATION_CRITERIA.md, EC-03, and FREQ-032; it is not a procurement budget. Values below are component-price scenarios, not quotes. Foreign actuator freight/customs are excluded.

| Concept | Economy estimate | Load/role-related alternative | Interpretation |
|---|---:|---:|---|
| DA-01 | ₹112,773 | ₹746,480 using six local AK80-8 listings | Economy case clears modeled torque screens and ceiling; local listed alternative exceeds ceiling. |
| QR-02 | ₹166,503 | ₹1,138,605 load-only hybrid; ₹1,624,657 paired AK10-9 on all 12 L joints; ₹5,083,507 T25-40 sensitivity | Economy case clears static screen but not proposed L role; T25-40 is unconfirmed third-party data. |
| DA-04 | ₹175,052 | ₹288,202 with two 18 Nm shoulder modules | Economy case misses 1 kg shoulder screen; voltage changes to 48 V for upgrade. |
| QR-04 | ₹170,584 | ₹396,885 load-only four-hip-flexion upgrade; ₹1,628,738 paired AK10-9 on all 12 L joints; ₹5,087,588 T25-40 sensitivity | Economy case misses upper hip-flexion screen; alternative remains 48 V and below proposed L torque band. |

An 18% import-tax-only sensitivity is itemized in COST_MODEL.md for Makiina modules; it is not a landed-cost estimate. QR-02/QR-04 camera price is included in the scenario subtotal but sensor mass is kept as a separate branch.

## 5. Independent hard gates

| Gate | DA-01 | QR-02 | DA-04 | QR-04 |
|---|---|---|---|---|
| HG-01 Cost against ₹2 lakh | PASS for modeled economy scenario; local listing exceeds | NOT PASSED — literal L-role component lower bound exceeds ceiling | CONDITIONAL; economy passes, load-compatible shoulder upgrade exceeds | NOT PASSED — load-compatible upgrade exceeds ceiling |
| HG-02 Actuator compatibility | CONDITIONAL — paper torque pass; no selected variant | NOT PASSED — L role and load-only economy do not align | NOT PASSED — 1 kg case requires a voltage/price change | NOT PASSED — high hip-flexion load exceeds economy candidate |
| HG-03 Mechanical safety | NOT PASSED — tipping/fixture verification absent | NOT PASSED — gait/contact/stability verification absent | NOT PASSED — tall mobile stability/hazard validation absent | NOT PASSED — long-leg gait/mount validation absent |
| HG-04 D-003 respected | PASS — no build or procurement | PASS — no build or procurement | PASS — no build or procurement | PASS — no build or procurement |

A hard-gate outcome is separate from the weighted score. No concept is represented as ready for implementation. No final recommendation is made before CP4, owner decisions and the remaining eight concept assessments.