# INTERN-01 Week 3/4 — Research-backed scenario estimates

**Status:** PROPOSED paper feasibility estimates; authored 2026-11-28; D-003 remains HOLD. These are conditional engineering estimates, not an approved design, released BOM, supplier quotation, procurement budget, test result, or safety approval.

## 1. Scope and method

This report covers DA-01, QR-02, DA-04 and QR-04. It uses the concept-sheet values as CONCEPT_TARGETs, not requirements. Displayed mass rows round to 0.01 kg; totals use unrounded component masses. When the sheets omit a dimension, pose, part selection or duty cycle, the report makes a named scenario assumption and shows its effect. It does not silently substitute an artwork dimension, turn a peak rating into a continuous rating, or treat an optional sensor as part of the baseline.

Prices are planning snapshots, not quotes. INR 2,00,000 is the study comparison ceiling in EVALUATION_CRITERIA.md and FREQ-032, not authorization to spend. Imported-product totals use vendor list prices converted at the FBIL/RBI-reported 27-Nov-2026 rate of ₹92.9139 per USD; foreign shipping and customs duty are excluded because the tariff line and shipment are not specified. An 18% tax-only sensitivity is shown for imported actuator prices; it is not a customs calculation. ICEGATE requires product classification and shipment details for duty. No blanket import-duty rate is assumed.

The mass model has three configurations: an economy joint-module screen, a nominal packaging scenario, and a heavier actuator/sensor scenario. Where the L-family screen is shown, the high-mass case uses eight high-load sagittal joints plus four lower-demand hip-abduction joints; a strict literal “all hip and knee axes are L” case is shown separately. Battery capacity is a scenario input, not a runtime claim. The 8 Ah and 6 Ah battery cases are linearly scaled from a listed 10 Ah pack; those sizes are estimates, not listed products.

## 2. Sourced technical and price anchors

| Ref | Anchor | Sourced values used | Boundary |
|---|---|---|---|
| S01 | HEBI T-Series datasheet | T5-4: 4 Nm continuous, 7 Nm peak, 32 rpm, 0.450 kg. T8-16: 16 Nm continuous, 38 Nm peak, 15 rpm, 0.575 kg. 24–48 V. | T8-16 does not meet the proposed L continuous band of 25–40 Nm. Datasheet updated 2024. |
| S02 | Makiina medium actuator | 10 Nm rated continuous up to 75 rpm, 22 Nm burst, 117 rpm maximum, 0.240 kg, 24 V, USD 90. | Manufacturer page calls results preliminary lab tests; price excludes unlisted shipping/import costs. |
| S03 | CubeMars AK70-10 | 8.3 Nm rated, 24.8 Nm peak, 0.621 kg, USD 398.90–498.90. | Rated output is below the 10 Nm M reference; 24/48 V variants are shown. |
| S04 | CubeMars AK10-9 V3.0 KV60 | 18 Nm rated, 53 Nm peak, 0.940 kg, 48 V, USD 698.90–798.90. | Stronger than the M reference but still below the proposed 25–40 Nm L continuous band; 48 V conflicts with the 24 V concept direction. |
| S05 | IndiaMART AK80-8 KV60 listing | 10 Nm rated, 48 V, ₹113,980 per unit, seller marks price excluding taxes. | Seller listing; mass not published. Used for price sensitivity only, not mass. |
| S06 | Flowntro T25-40 profile | 40 Nm continuous, 80 Nm peak, 23 rpm, 1.5 kg, USD 4,500. | Third-party profile explicitly says HEBI has not claimed/confirmed it. Use only as a low-confidence L-class price/mass stress case, not a verified offer. |
| S07–S09 | Material data and market proxy | 6061 density 2,700 kg/m³; 20×20×2 mm tube calculates to 0.3888 kg/m; 40×40×3 mm calculates to 1.1988 kg/m. 6061 plate proxy ₹400–430/kg, ex-Mumbai and page reports 7% GST included. | Material price is a vendor-published planning proxy, not a quote for the exact tube/grade/quantity. No structural allowable is inferred from density or a generic datasheet. |
| S10 | CNC rate guide | ₹200–600/hour for turning/milling examples; higher rates for VMC/5-axis; underlying Ludhiana card dates to 2021. | ₹600/hour is the planning rate used here. Time per concept is an analyst allowance pending drawings. |
| S11–S12 | Battery and BMS | 22.2 V, 10 Ah 6S pack ₹6,899, listed mass 1.600 kg, no BMS; 6S 20 A BMS ₹629 and 0.045 kg. | 8 Ah and 6 Ah values are linear capacity-scaled scenarios. 20 A is a planning battery limit, not proof of peak-current suitability. |
| S13 | Higher-capacity battery reference | 22.2 V, 40 Ah, ₹73,559, 2.65 kg shipping weight. | Shipping mass is an upper packaging proxy, not bare pack mass. Not selected as a baseline. |
| S14 | OAK-D Lite camera | ₹36,799 including GST; 0.102 kg; 4 TOPS listed. | Optional sensor branch; not included in QR-02 or QR-04 baseline mass. |
| S15–S16 | Compute and currency | Raspberry Pi 5 4 GB manufacturer list price USD 110; USD/INR 92.9139 on 27-Nov-2026. Converted board-only planning cost: ₹10,220.53. | No kit, storage, heatsink, import, or tax premium is added; 0.20 kg assembled compute estimate is an analyst allowance. |
| S17 | DA-01 power supply | 24 V, 10 A, 240 W SMPS listed at ₹1,732. | Supplier list snapshot; not a tested power design. |
| S18 | DA-04 drive motor | 24 V, 100 W, 25 rpm, 2.050 kg and ₹11,664 excluding GST per motor/dual-driver listing. | Two listings are budgeted conservatively; they include duplicated dual-driver hardware. At 50 mm wheel radius, 25 rpm corresponds to 0.131 m/s. |
| S19–S20 | Light gripper | Robu kit mass 0.047 kg and ₹489; MG995 servo listing mass 0.030 kg and ₹304.27 including GST. | Two per DA-01 / DA-04. Grip force is not specified by these sources; this is a light demonstration gripper estimate, not a payload-certified end effector. |

Full bibliographic details and links are in WEEK3_SOURCE_REGISTER.md.

## 3. Mass takeoffs

Aluminum tube mass is computed as (B² − (B − 2t)²) × 10⁻⁶ × 2,700 kg/m for B and t in mm. Plate mass is width × length × thickness × density. These are geometric material masses before holes, cutouts, welds, fasteners or finish. Bracket, enclosure, harness and compute allowances are explicitly estimated because the concept art is not dimensioned manufacturing geometry.

### DA-01

| Component | Low (kg) | Nominal (kg) | High (kg) | Basis |
|---|---:|---:|---:|---|
| Six joint modules | 1.44 | 2.04 | 2.70 | 6 × 0.240 / 0.340 / 0.450 kg; Makiina and HEBI T5-4 anchors, with 0.340 kg as midpoint estimate. |
| 300×250 mm base plate | 0.61 | 0.81 | 1.22 | 3 / 4 / 6 mm 6061 plate; nominal is 0.810 kg, not the earlier 0.80 kg low case. |
| Two 350 mm arm-link runs | 0.52 | 0.67 | 0.87 | 0.700 m total 20×20×2 tube = 0.272 kg bare, plus 0.25 / 0.40 / 0.60 kg link joints and fasteners. |
| Enclosure and mount structure | 0.80 | 1.20 | 1.80 | Explicit packaging allowance from the 300×250 mm base envelope. |
| Compute assembly | 0.15 | 0.20 | 0.25 | Board, heatsink/storage and mounting allowance; not a board datasheet mass. |
| PSU, wiring and safety | 0.40 | 0.60 | 0.80 | Estimate including the listed PSU and harness/protection. |
| Two light grippers and mounts | 0.30 | 0.40 | 0.50 | 2 × 0.077 kg sourced kit+servo plus mounting allowance. |
| Camera and mast | 0.30 | 0.40 | 0.60 | 0.102 kg camera plus 0.20 / 0.30 / 0.50 kg mast estimate. |
| **Total** | **4.53** | **6.33** | **8.74** | Nominal is inside the printed 5–8 kg target; low and high scenario endpoints straddle it. |

The “lower half of the target band” phrase is removed. The modeled low case is below the printed band; the nominal case is within it. Camera/gripper inclusion is now explicit.

### QR-02

| Component | Economy (kg) | Nominal, sensor-excluded (kg) | High L-class scenario (kg) | Basis |
|---|---:|---:|---:|---|
| Twelve joint modules | 2.88 | 2.88 | 12.96 | Economy/nominal: 12 × 0.240 kg Makiina. High: 8 × 1.50 kg T25-40 profile + 4 × 0.240 kg Makiina for low-torque abduction axes. |
| Body, links, feet and mounts | 1.48 | 1.60 | 2.33 | Two 350×260 mm plates at 1.5–2 mm, 0.880 m of 20×20×2 leg tube = 0.342 kg, plus feet/bracket allowance. |
| Battery plus BMS | 0.69 | 1.33 | 1.65 | 4 / 8 / 10 Ah scaled from listed 10 Ah pack and 45 g BMS. |
| Compute assembly | 0.15 | 0.20 | 0.25 | Analyst allowance. |
| Power and harness | 0.25 | 0.30 | 0.60 | Explicit estimated packaging allowance. |
| **Subtotal without camera** | **5.45** | **6.30** | **17.78** | High case is a torque-class sensitivity, not a recommended build. |
| Optional OAK-D Lite | +0.10 | +0.10 | +0.10 | Listed camera mass; sensor remains out of baseline. |

The 6.30 kg nominal load basis is sensor-excluded and reconciles to the mass budget. The camera variant is 6.40 kg. Both are compared with the printed 4–6 kg target. An 8 Ah battery is an interpolation, not a catalogued part.

### QR-04

| Component | Economy (kg) | Nominal, sensor-excluded (kg) | High L-class scenario (kg) | Basis |
|---|---:|---:|---:|---|
| Twelve joint modules | 2.88 | 2.88 | 12.96 | Economy/nominal: 12 × 0.240 kg Makiina. High: 8 × 1.50 kg T25-40 profile + 4 × 0.240 kg lower-torque abduction axes. |
| Body, long links, feet and mounts | 2.06 | 2.30 | 2.60 | Two 450×280 mm body plates at 1.5–2 mm, 1.120 m of 20×20×2 leg tube = 0.436 kg, plus bracket/foot allowance. |
| Battery plus BMS | 1.01 | 1.65 | 1.65 | 6 / 10 / 10 Ah scaled/listed pack cases. |
| Compute assembly | 0.15 | 0.20 | 0.25 | Analyst allowance. |
| Power and harness | 0.30 | 0.41 | 0.60 | Estimated. |
| **Subtotal without camera** | **6.39** | **7.43** | **18.06** | High case is a torque-class sensitivity, not a recommended build. |
| Optional OAK-D Lite | +0.10 | +0.10 | +0.10 | Listed camera mass; sensor remains out of baseline. |

The nominal 7.43 kg is the 10 Ah, sensor-excluded model; it is above the printed 5–7 kg target by 0.43 kg. Camera variant is 7.53 kg. The prior 7.5 kg load case is retained as a rounded upper planning case, and the calculation also reports the exact 7.43 kg scenario.

### DA-04

| Component | 24 V economy (kg) | 18 Nm arm-module scenario (kg) | High packaging case (kg) | Basis |
|---|---:|---:|---:|---|
| Eight arm modules | 1.92 | 7.52 | 7.52 | 8 × 0.240 kg Makiina, or 8 × 0.940 kg AK10-9; these are different voltage/torque scenarios. |
| Two drive motors | 4.10 | 4.10 | 4.10 | 2 × listed 2.050 kg motor modules. |
| Base plate, rails and brackets | 8.32 | 8.32 | 9.50 | 500×600×4 mm plate = 3.24 kg; 3.40 m 40×40×3 tube = 4.08 kg; brackets 1.00 kg nominal. |
| Torso/head structure | 2.44 | 2.44 | 3.00 | Two 400×600×1.5 mm panels = 1.94 kg plus 0.50 kg structure allowance. |
| Arm links and mounts | 0.85 | 0.85 | 1.40 | 0.900 m total 20×20×2 tube = 0.350 kg plus mounts. |
| Battery plus BMS | 1.65 | 1.65 | 1.65 | Listed 10 Ah pack plus 45 g BMS; all three mass cases use this pack. |
| Compute, camera, harness and grippers | 1.31 | 1.31 | 1.75 | 0.20 kg compute, 0.102 kg camera, 0.60 kg harness and 0.404 kg grippers nominal; high allowance is larger packaging. |
| **Total** | **20.59** | **26.19** | **28.92** | Economy case is below the printed 25–35 kg target; higher-module scenario is within it. |

The 18 Nm mass case uses a 48 V product and is a sensitivity only. The concept’s printed 24 V direction is not met by that actuator without redesign; this is a compatibility penalty, not an assumed converter mass. The high mass case uses the same 10 Ah pack as the other cases; the 40 Ah product is not treated as a complete system option because its source does not identify a matching high-current BMS.

## 4. Torque and actuator screens

All results are static/paper screens. The 1.5 multiplier is an explicit 50% headroom sensitivity applied to the stated static or point-mass sum; it is not a safety factor, validated dynamic peak or duty rating. Speeds and inertial acceleration inputs are named assumptions. No product is selected.

| Concept | Joint screen and load basis | Product comparison | Finding |
|---|---|---|---|
| DA-01 | Updated point-mass screen: elbow 1.33 Nm, wrist pitch 0.31 Nm, shoulder-yaw inertial 1.03 Nm; conditional shoulder-pitch at 0.20 kg/350 mm is 4.77 Nm. | HEBI T5-4 provides 4 Nm continuous; Makiina provides 10 Nm rated continuous at 24 V. | Makiina clears modeled branches; T5-4 does not clear conditional 4.77 Nm pitch branch. Wrist/shoulder-axis branches remain explicit alternatives. |
| QR-02 | 6.30 kg × 9.81 = 61.80 N on one leg. Whole robot on one leg is deliberately conservative static load-sharing. Hip-flexion d⊥ 70–90 mm gives 4.33–5.56 Nm static and 6.49–8.34 Nm at 1.5×. Hip-yaw uses 17.8–26.7 mm sensitivity: 1.10–1.65 Nm static. Knee uses 31.1–46.7 mm: 1.92–2.89 Nm static. | Makiina 10 Nm rated continuous clears the 8.34 Nm upper static-only screen. Proposed family role still labels hips/knees as L (25–40 Nm continuous); that is a program-role mismatch, not a measured load shortfall. | Static screen supports a low-cost 10 Nm candidate; it does not qualify walking, impact, thermal duty or a proposed L-class role. |
| QR-04 | 7.43 kg × 9.81 = 72.89 N one-leg conservative static case. For comparison with the reviewer’s rounded 7.5 kg case, force is 73.58 N. Moment arms are consistently rounded to 0.1 mm: hip yaw 23.5, hip flexion 86.2, knee 47.0 mm. ±20% moment-arm sensitivity produces hip-flexion 1.5× screen up to 11.31 Nm at 7.43 kg or 11.42 Nm at 7.50 kg. | 10 Nm Makiina does not clear the high hip-flexion sensitivity; 18 Nm AK10-9 clears that torque screen but uses 48 V and is below proposed L continuous torque. T25-40 profile is the only 40 Nm anchor found, but is unconfirmed third-party data. | Load-compatible hip-flexion hybrid and literal L-role alternatives exceed the ₹2 lakh ceiling; the high-L mass scenario also overwhelms the 5–7 kg target. |
| DA-04 | 450 mm reach, 0.5–1.0 kg payload, estimated links/joints/gripper, 10 rad/s² angular acceleration and 1.5 headroom. Shoulder-pitch screen 9.81–14.64 Nm; elbow 3.28–5.32 Nm; wrist 0.68–1.28 Nm; shoulder-yaw inertial screen 2.76–4.28 Nm. Wheel screen at 25–35 kg, 50 mm radius, 5° slope and 0.5 m/s²: 1.27–1.78 Nm per wheel after 1.5×. | 10 Nm Makiina clears the 0.5 kg shoulder case but not the 1.0 kg case. 18 Nm AK10-9 clears the modeled torque but is 48 V. Robokits 24 V/100 W/25 rpm drive listing’s 280 kg·cm rated torque is above the wheel screen; its 0.131 m/s speed is a slow-mobility scenario. | The 1 kg payload branch and 24 V supply direction conflict with the current low-cost actuator scenario. Wheel torque is not the limiting calculation; speed, braking, tipping and duty still matter. |

### QR one-leg and hip-yaw conservatism

For both quadrupeds, the full robot weight is assigned to one stance leg as a conservative static load-share screen. It is not asserted to be a normal gait load or a dynamic impact bound. Hip-yaw uses a force-times-offset sensitivity about the yaw axis; because no axis geometry is approved, it is an intentionally conservative bound rather than a validated torque requirement. Moment arms are displayed to 0.1 mm and torque to 0.01 Nm throughout.

## 5. Cost model and ceiling comparison

The baseline includes joint modules, computer, structural material, estimated machine time, a sourced PSU/battery branch, basic harness/safety allowance, DA-04 drive motors and the listed light grippers/camera where applicable. Optional camera price is shown in the component tables; the QR-02/QR-04 mass baselines exclude it. Material cost uses ₹430/kg; machining uses ₹600/hour; allowances are described in the concept COST_MODEL files. Taxes on Indian list prices are treated as shown by the source; an 18% import-tax sensitivity is shown separately for foreign actuators. Freight and customs duty are excluded from all foreign-import subtotals, so these are not landed quotations. Battery scenarios use a 22.2 V nominal pack while several actuator/drive listings specify 24 V; direct compatibility and any voltage conditioning are not established or priced.

| Concept | Economy 10 Nm price case (INR) | 18% actuator-tax sensitivity (INR) | Load-/L-class alternative before couplers and import costs | ₹2 lakh reading |
|---|---:|---:|---:|---|
| DA-01 | 112,773 | 121,804 | 746,480 using six local AK80-8 listings at ₹113,980 each, pre-tax | Economy scenario is below ceiling; local-price case is not. |
| QR-02 | 166,503 | 184,565 | 1,138,605 load-only hybrid (eight sagittal axes paired with AK10-9 plus four Makiina abduction units); full 12-axis L-role paired AK10-9 lower bound ₹1,624,657; 12 T25-40 profiles ₹5,083,507, low confidence | Static-load 10 Nm option is below ceiling; paired 18 Nm modules per L joint exceed it before couplers. T25-40 price is an unconfirmed third-party sensitivity. |
| DA-04 | 175,052 | 187,093 | 288,202 with two 18 Nm AK10-9 shoulder modules replacing the 10 Nm parts | Budget case is below ceiling but fails the 1 kg shoulder screen; the torque-upgraded scenario exceeds it. |
| QR-04 | 170,584 | 188,646 | 396,885 load-only hip-flexion upgrade; full 12-axis L-role paired AK10-9 lower bound ₹1,628,738; 12 T25-40 profiles ₹5,087,588, low confidence | Economy case is below ceiling but misses high hip-flexion screen; load-upgraded and L-role cases exceed it. |

These are scenario comparisons, not one averaged price. Where a low-cost candidate fails the load screen or the proposed family role, it is not described as an affordable feasible design. The AK80-8 local price is a seller listing; T25-40 is a low-confidence third-party profile; CubeMars/Makiina prices are foreign product-page prices. Customs tariff and shipment are not guessed. The study criterion is the ₹2,00,000 ceiling in EVALUATION_CRITERIA.md / FREQ-032.

## 6. Comparison scorecard update

EVALUATION_CRITERIA.md permits provisional scores supported by traceable ESTIMATE evidence. These scores use all seven proposed weights, but cover only four of twelve concepts and remain a partial four-concept comparison, not CP4 or a final recommendation.

| Criterion (weight) | DA-01 | QR-02 | DA-04 | QR-04 | Reason for score |
|---|---:|---:|---:|---:|---|
| EC-01 Mechanical feasibility (20%) | 4 | 3 | 2 | 2 | Fixed base is simplest; quadrupeds carry long-link and contact assumptions; DA-04 has mobile/tall tipping exposure. |
| EC-02 Actuator compatibility (15%) | 4 | 2 | 3 | 2 | DA-01 torque screen fits 10 Nm; QR-02 static screen fits but L role conflicts; DA-04 1 kg shoulder branch needs >10 Nm; QR-04 high hip-flexion case exceeds 10 Nm. |
| EC-03 Hardware cost (20%) | 3 | 2 | 2 | 1 | Economy scenario is under the ceiling, but compatible higher-torque/L alternatives exceed it for QR-04 and the high-payload DA-04 branch. |
| EC-04 Fabrication simplicity (10%) | 4 | 3 | 2 | 2 | Fixed tabletop packaging is simplest; long legs, moving base and alignment add work. |
| EC-05 Platform demonstration value (20%) | 3 | 4 | 5 | 4 | DA-04 combines mobility and arms; quadrupeds demonstrate locomotion; DA-01 is a controlled manipulation platform. |
| EC-06 Modularity and upgrade (10%) | 3 | 3 | 3 | 4 | QR-04 has the clearest modular body/leg interface concept, still only an indicative interface. |
| EC-07 Mechanical safety (5%) | 3 | 2 | 2 | 2 | Pinch/overturning, gait/contact and mobile-base hazards remain paper-assessed, not validated. |
| **Weighted total (out of 5)** | **3.45** | **2.80** | **2.85** | **2.40** | Weights sum to 100%; provisional estimate-only scores. |

Partial ordering among the four assigned concepts is DA-01 (3.45), DA-04 (2.85), QR-02 (2.80), QR-04 (2.40). This replaces the earlier 85%-weighted ordering because the new research supports an explicit provisional EC-02 estimate. It does not rank the other eight concepts, and does not satisfy CP4. Hard gates remain separate: D-003 is respected; the budget/actuator/safety gates are conditional or not passed where the load-compatible scenario exceeds budget or stability is unvalidated.

## 7. Scope branches replacing placeholders

- DA-01 shoulder yaw vs shoulder pitch and wrist rotation vs wrist pitch are represented as separate calculation branches. Neither is silently declared owner-approved.
- QR-02 baseline excludes optional sensors; the OAK-D Lite is an explicit +₹36,799 / +0.102 kg camera branch. Optional sensor differences are not counted in the 12 joints.
- QR-04 body interface is costed as a light adapter/bracket allowance around the printed 4×M5 / 2×Ø5 indicator; no structural capacity or approval is claimed. Sensor branch is separate.
- DA-04 battery is modeled as a 10 Ah, 22.2 V pack plus a 20 A BMS price/mass anchor. A listed 40 Ah/888 Wh pack is shown only as a pack-price reference; no current-matched BMS is included, so it is not a complete costed configuration. The source artwork’s 24 V remains a concept direction.
- Decision-log check: no decision-log file or matching decision ID exists in the tracked paths reviewed. The DA-04 10-actuator baseline is reported as the source README’s current statement; this report does not repeat “approved 2026-10-31” as a verified approval or assign a decision ID.
- Week 2 architecture references and FREQ-012/013, FREQ-019/020, FREQ-031/032/033 are restored in the handoff. Estimates do not change D-003, fabricate a final BOM, quote, CAD or procurement record.

## 8. Reference files

See WEEK3_SOURCE_REGISTER.md for all external and project source links. Per-concept calculations, costs, masses, actuator screens, and comparison scorecards link back to this report and that register. The results are paper evidence only; no simulation, bench or physical validation is claimed.