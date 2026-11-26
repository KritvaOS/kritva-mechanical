# QR-01 — Actuator Analysis

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-QR-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Joint and Actuator Feasibility Analysis |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Preliminary paper analysis; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `feasibility/DESIGN_GUIDELINES.md` |

## 1. Scope and Assumptions

- Concept ID: QR-01 (Compact Quadruped)
- Supply direction: 24V DC investigation only
- Motor direction: BLDC/PMSM
- Actuator architecture: S/M/L (no joint mapped yet)
- Joints in scope: hip and knee of each leg (4 each, symmetric, so one leg is analysed). Evidence type C; all values are **estimates**, nothing approved.

### 1.1 Inputs from the README (CONCEPT_TARGET)

Target weight 2.5 – 4 kg; payload 0.3 – 0.8 kg; body 300 × 250 × 200 mm; overall 420 × 400 mm; slow walking on flat terrain.

### 1.2 Intern assumptions

| ID | Assumption |
|---|---|
| A1 | g = 9.81 m/s² |
| A2 | Moving mass 7.06 kg: 6.26 kg estimate (`MASS_BUDGET.md`) plus 0.8 kg worst payload; weight 69.3 N |
| A3 | Planar leg: thigh 130 mm, shank 150 mm, knee pointing backward, hip at body mid-height; standing hip height 220 mm; stride foot offset ±60 mm; crouch hip height 120 mm |
| A4 | Load cases: 4-leg stance, F = W/4 = 17.3 N per foot; two-foot support (trot or worst crawl) as a bounding case, F = W/2 = 34.6 N per foot |
| A5 | Dynamic allowance 2× on static torque for peak (acceleration, touchdown; no impact is modelled) |
| A6 | Planning factor 1.5 on peak (not a validated margin) |
| A7 | Peak joint speed 5 rad/s (about 48 rpm) for slow walking |
| A8 | Module masses: hip 0.30 kg, knee 0.35 kg; thigh 0.06 kg, shank 0.05 kg, foot pad 0.02 kg |
| A9 | Average power 60 W (electronics 15 W, joints 45 W); battery 6S2P of 2.5 Ah cells, 5 Ah nominal 21.6 V (capacity not stated on the sheets); 80% usable |
| A10 | Foot support points ±190 mm × ±180 mm |

## 2. Per-Joint Assessment

Output-shaft torque, one leg. Static = bounding load case. Peak = 2 × static (A5).

| Joint | Load case | Peak torque | Continuous torque | Speed | Range | Duty assumptions | Calculation reference | S/M/L compatibility | Margin | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Hip (each leg) | Two-foot support, foot 60 mm from the hip line, F = 34.6 N | ≈ 4.2 N·m (2.1 static) | ≈ 0 N·m standing (foot under hip); walking RMS TBD | 5 rad/s (A7) | TBD | TBD | CALC-QR01-01 §2 | TBD | TBD | ESTIMATE |
| Knee (each leg) | Two-foot support, foot 60 mm forward, knee back; knee–foot horizontal distance 111 mm | ≈ 7.7 N·m (3.85 static) | ≈ 1.5 N·m (4-leg stand, h = 220 mm); walking RMS TBD | 5 rad/s | TBD | TBD | CALC-QR01-01 §1 | TBD | TBD | ESTIMATE |

### 2.1 Required with planning factor (A6, 1.5× on peak)

| Joint | Peak × 1.5 | Continuous × 1.5 |
|---|---|---|
| Hip | ≈ 6.2 N·m | TBD |
| Knee | ≈ 11.6 N·m | ≈ 2.2 N·m (standing) |

### 2.2 Other cases

- Low payload (0.3 kg): total 6.56 kg; knee ≈ 3.6 N·m, hip ≈ 1.9 N·m static.
- Sit-to-stand (crouch h = 120 mm, four feet): knee ≈ 2.2 N·m static (knee–foot distance 125 mm).
- Swing leg held horizontal: hip ≈ 0.64 N·m (leg weight), knee ≈ 0.07 N·m.
- Sensitivity: every +0.1 kg on each of the 8 modules adds 0.8 kg (about 11%) and raises the joint torques by about the same share. If the modules were 0.5 kg (about 0.2 kg heavier on average), the mass rises about 1.4 kg and the torques about 20%.

### 2.3 Hand calculation (CALC-QR01-01 summary; CALC-QR01-01 is to be filed)

- **Geometry (§1):** foot below the hip at h = 220 mm: knee height y = (L2² − L1² − h²) ÷ (2h) = (22,500 − 16,900 − 48,400) ÷ 440 = −97.3 mm; knee offset x = √(130² − 97.3²) = 86 mm. Foot forward 60 mm: hip–foot distance D = √(60² + 220²) = 228.0 mm; hip angle α = acos[(130² + 228.0² − 150²) ÷ (2 × 130 × 228.0)] = 38.5°; thigh angle from vertical = 15.3° − 38.5° = −23.2°; knee x = −51 mm; knee–foot horizontal distance = 60 + 51 = **111 mm**.
- **Knee (§1):** T = F × 0.111 = 34.6 × 0.111 ≈ **3.85 N·m**; standing 4-leg: 17.3 × 0.086 ≈ **1.49 N·m**.
- **Hip (§2):** T = F × 0.060 = 34.6 × 0.060 ≈ **2.08 N·m** (zero when the foot is directly under the hip).
- **Swing leg (§3):** hip Σ m·d = 0.06(0.065) + 0.35(0.130) + 0.05(0.205) + 0.02(0.280) = 0.0653 kg·m, T = **0.64 N·m**.
- **Power (§4):** peak knee 3.85 N·m × 5 rad/s ≈ 19 W and hip 2.08 × 5 ≈ 10 W per joint (not simultaneous peaks).

### 2.4 Energy and runtime (paper estimate)

Assumed 60 W average (A9). Battery 108 Wh nominal; 80% usable gives 86 Wh and about **1.4 h**. At 100 W the runtime falls to about 0.9 h. Battery capacity is UNKNOWN on the sheets, so runtime is TBD; protection and charging are not assessed.

## 3. Reference Limitations

The elbow discussion reference of 24V, 10 N·m continuous and 20 N·m peak is not a universal specification. It is **not** used here. Hip and knee are derived independently from the QR-01 leg geometry and the stated assumptions.

## 4. Actuator Source Traceability

No input from `kritva-actuator` has been supplied for QR-01.

- Source repository and path: TBD (none supplied)
- Revision / commit: TBD
- Source document or specification: TBD
- Maturity: UNKNOWN
- Verification status and limitations: None. The concept sheet calls the actuators Kritva S/M/L compatible, but no joint has been mapped. Preliminary repository values, when received, must not be treated as validated specifications.

## 5. Findings and Open Items

- **Torque/speed feasibility:** Not assessable without S/M/L data. The knee is the most loaded joint (about 3.9 N·m static, about 11.6 N·m with allowance and factor). Whether the assumed module masses (0.30 – 0.35 kg) can deliver that is open, and the answer feeds back into the mass.
- **S/M/L mapping rationale:** NOT STARTED. Hip and knee loads differ by about a factor of two, so one size for both may be wasteful; this is an observation, not a mapping.
- **Margin interpretation:** TBD. Margin = rating ÷ required torque (Section 2.1) once ratings are supplied.
- **Missing inputs and risks:**
  1. Link lengths, hip height, joint ranges, module and body masses are assumed.
  2. Impact at touchdown is only covered by the 2× allowance, not by a model.
  3. Walking RMS torque and thermal limits at standing (knee holds about 1.5 N·m continuously) are not assessed.
  4. Battery capacity, peak current and discharge limit at 24 V are UNKNOWN.
  5. Gearbox type and backdrive (power-off collapse) not selected.
- **Next steps (paper only):** get S/M/L data with traceability; iterate mass and torque; add joint ranges and a gait cycle; file CALC-QR01-01.

## 6. HOLD D-003

Paper calculations and compatibility assessment only. No actuator purchase, detailed CAD, final BOM, fabrication, assembly or physical testing. All require explicit owner decision under HOLD D-003.
