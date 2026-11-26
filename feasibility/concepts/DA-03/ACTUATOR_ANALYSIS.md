# DA-03 — Actuator Analysis

| Property | Value |
|---|---|
| Document ID | KMECH-ACT-DA-03 |
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

- Concept ID: DA-03 (Mobile Dual-Arm)
- Supply direction: 24V DC investigation only (24 V Li-ion battery shown, capacity TBD)
- Motor direction: BLDC/PMSM
- Actuator architecture: S/M/L (no joint or wheel drive mapped yet)
- Joints in scope: shoulder yaw, elbow pitch, wrist pitch (per arm, symmetric) and the two wheel drive channels (left pair, right pair). Optional gripper actuation is not sized.
- Duty and operating assumptions: see below. Evidence type C; all values are **estimates**, nothing approved.

### 1.1 Inputs from the README (CONCEPT_TARGET)

Reach 350 mm; payload 0.1 – 0.2 kg per arm; weight 12 – 18 kg; base 400 mm × 450 mm; indoor flat terrain.

### 1.2 Intern assumptions

| ID | Assumption |
|---|---|
| A1 | g = 9.81 m/s² |
| A2 | Worst pose: arm fully extended horizontally; no shoulder pitch joint, so the upper arm is rigid and horizontal |
| A3 | Link split 175 / 100 / 75 mm |
| A4 – A8 | Upper arm link 0.15 kg at 87.5 mm; elbow module 0.35 kg at 175 mm; forearm 0.10 kg at 50 mm from the elbow; wrist module 0.20 kg at 100 mm from the elbow; gripper 0.15 kg, CoM 40 mm beyond the wrist |
| A9 | Payload 0.2 kg (worst) and 0.1 kg (low) at the tip |
| A10 | Yaw axis vertical; yaw module 0.45 kg on the axis |
| A11 | Arm joint speed 90 °/s (1.57 rad/s); acceleration 10 rad/s² |
| A12 | Planning factor 1.5 on required torque (not a validated margin) |
| A13 | Transit shock factor 2 on holding loads if the arm is not stowed |
| W1 | Moving mass 16.1 kg (15.7 kg estimate plus 0.4 kg payload) |
| W2 | Wheel diameter 100 mm (radius 0.05 m); four wheels as two driven pairs |
| W3 | Rolling resistance coefficient 0.03 (hard indoor floor, rubber tyre) |
| W4 | Slope 5° |
| W5 | Acceleration 0.3 m/s²; cruise speed 0.5 m/s |
| W6 | Lateral friction coefficient for scrub 0.5 |
| W7 | Wheel contact points ±190 mm (track 380 mm) and ±150 mm (wheelbase 300 mm) |
| W8 | Torque split equally between the two wheels of a pair |
| W9 | Electronics 20 W, arms 10 W and drive 10 W average; battery 6S4P, 10 Ah nominal 21.6 V (capacity not stated on the sheets) |

## 2. Per-Joint Assessment

Output-shaft torque, one arm or one drive channel (at the wheel). Static = gravity holding torque at A2. Peak = static + inertial (I·α, A11) for arm joints.

| Joint | Load case | Peak torque | Continuous torque | Speed | Range | Duty assumptions | Calculation reference | S/M/L compatibility | Margin | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Shoulder yaw (each arm) | Arm extended, rotating about the vertical axis; no gravity torque on the actuator. The output bearing carries a moment of about 2.64 N·m and about 11.3 N vertical load | ≈ 0.71 N·m (inertial, I ≈ 0.071 kg·m²) | ≈ 0 N·m static; friction and cable torque TBD | 1.57 rad/s (A11) | TBD | TBD | CALC-DA03-01 §3 | TBD | TBD | ESTIMATE |
| Elbow pitch (each arm) | Forearm horizontal, 0.2 kg at the tip | ≈ 0.91 N·m (0.80 static + 0.11 inertial) | ≈ 0.80 N·m | 1.57 rad/s | TBD | TBD | CALC-DA03-01 §1 | TBD | TBD | ESTIMATE |
| Wrist pitch (each arm) | Gripper horizontal, 0.2 kg at the tip | ≈ 0.22 N·m (0.21 + 0.01) | ≈ 0.21 N·m | 1.57 rad/s | TBD | TBD | CALC-DA03-01 §2 | TBD | TBD | ESTIMATE |
| Wheel drive channel (left or right pair) | Turning in place with scrub (W6, W7) | ≈ 2.5 N·m at the wheel (≈ 1.3 N·m per wheel) | ≈ 0.6 N·m at the wheel (straight, 5° slope, 0.3 m/s²) | ≈ 10 rad/s (95 rpm) at 0.5 m/s | n/a (continuous rotation) | TBD | CALC-DA03-01 §4 | TBD (gear ratio TBD) | TBD | ESTIMATE |
| Gripper (each arm, optional) | Not sized | TBD | TBD | TBD | TBD | TBD | none | TBD | TBD | NOT STARTED |

### 2.1 Required with planning factor (A12, 1.5×), for comparison with S/M/L data once supplied

| Joint | Peak × 1.5 | Continuous × 1.5 |
|---|---|---|
| Shoulder yaw | ≈ 1.1 N·m | TBD (friction-dominated) |
| Elbow pitch | ≈ 1.4 N·m | ≈ 1.2 N·m |
| Wrist pitch | ≈ 0.33 N·m | ≈ 0.31 N·m |
| Wheel drive channel (at wheel) | ≈ 3.8 N·m | ≈ 0.9 N·m |

### 2.2 Other cases

- Low payload (0.1 kg): elbow ≈ 0.62 N·m, wrist ≈ 0.13 N·m, yaw bearing moment ≈ 2.30 N·m.
- Transit with arms not stowed (A13): elbow ≈ 1.6 N·m, wrist ≈ 0.41 N·m, yaw bearing moment ≈ 5.3 N·m. Stowing the arms in transit is preferred.
- Wheel scrub sensitivity: with lateral friction 0.8 the turning torque rises to about 4.0 N·m per channel.

### 2.3 Hand calculation (CALC-DA03-01 summary; CALC-DA03-01 is to be filed)

- **§1 Elbow:** Σ m·d = 0.10(0.050) + 0.20(0.100) + 0.15(0.140) + 0.20(0.175) = 0.0810 kg·m; T = 0.0810 × 9.81 = **0.795 N·m**; inertia I ≈ 0.0113 kg·m², I·α = 0.11 N·m.
- **§2 Wrist:** Σ m·d = 0.15(0.040) + 0.20(0.075) = 0.0210 kg·m; T = **0.206 N·m**; I·α = 0.014 N·m.
- **§3 Shoulder yaw:** I = Σ m·d² about the yaw axis ≈ 0.0714 kg·m² (distances 0.0875, 0.175, 0.225, 0.275, 0.315, 0.350 m); I·α = **0.71 N·m**. Moment on the output bearing = 0.2691 kg·m × 9.81 = **2.64 N·m**.
- **§4 Wheels:** F_roll = 0.03 × 16.1 × 9.81 × cos 5° ≈ 4.7 N; F_slope = 16.1 × 9.81 × sin 5° ≈ 13.8 N; F_acc = 16.1 × 0.3 ≈ 4.8 N; total ≈ 23.3 N; wheel torque total = 23.3 × 0.05 ≈ 1.17 N·m, so ≈ **0.58 N·m** per channel. Turning in place: r = √(0.19² + 0.15²) = 0.242 m; scrub moment M = μ·m·g·r = 0.5 × 157.9 × 0.242 ≈ 19.1 N·m; each side force = M ÷ (2 × 0.19) ≈ 50 N; wheel torque = 50 × 0.05 ≈ **2.5 N·m** per channel.
- **§5 Power:** straight, 5° slope, 0.5 m/s: 23.3 N × 0.5 ≈ 12 W mechanical; flat cruise ≈ 2.4 W; turning in place at 0.785 rad/s ≈ 15 W.

### 2.4 Energy and runtime (paper estimate)

Assumed 40 W average (electronics 20 W + arms 10 W + drive 10 W, W9). Battery 6S4P at 10 Ah nominal 21.6 V ≈ 216 Wh, with 80% usable ≈ 173 Wh, giving about **4 h**. At 80 W the runtime halves to about 2 h. Battery capacity is UNKNOWN on the sheets, so runtime is TBD. Protection and charging are not assessed.

## 3. Reference Limitations

The elbow discussion reference of 24V, 10 N·m continuous and 20 N·m peak is not a universal specification. It is **not** used here. Every joint and wheel drive above is derived independently from DA-03 geometry and the stated assumptions.

## 4. Actuator Source Traceability

No input from `kritva-actuator` has been supplied for DA-03.

- Source repository and path: TBD (none supplied)
- Revision / commit: TBD
- Source document or specification: TBD
- Maturity: UNKNOWN
- Verification status and limitations: None. The concept sheet calls the actuators Kritva S/M/L compatible, but no joint or wheel drive has been mapped. Preliminary repository values, when received, must not be treated as validated specifications.

## 5. Findings and Open Items

- **Torque/speed feasibility:** Not assessable without S/M/L data. Arm joint loads are small (elbow about 0.8 N·m, wrist about 0.2 N·m). Wheel turning torque (about 2.5 N·m per channel at the wheel) is the largest actuator demand and depends on the floor and tyre.
- **S/M/L mapping rationale:** NOT STARTED. Arm joints and wheel drives differ greatly in speed and torque, so one size is unlikely to suit both; this is an observation, not a mapping.
- **Margin interpretation:** TBD. Margin = rating ÷ required torque (Section 2.1) once ratings are supplied.
- **Missing inputs and risks:**
  1. Link, module and payload masses are assumed.
  2. Joint ranges, speeds, duty, wheel size, tyre, floor friction and gear ratio are not printed.
  3. The upper arm is a fixed cantilever, so the yaw output bearing must carry about 2.64 N·m moment; this is a bearing question, not an actuator torque.
  4. Wheel torque depends on turning strategy (in place or arc) and friction; paired wheels scrub.
  5. Battery capacity, discharge limit, protection and charging are UNKNOWN; peak current at 24 V is not assessed.
  6. Gearbox type, efficiency and backdrive (arm droop, base roll-away on slopes) are not assessed.
- **Next steps (paper only):** get S/M/L data with traceability; replace assumed masses with the mass budget; add joint ranges and duty; sweep turning cases; file CALC-DA03-01.

## 6. HOLD D-003

Paper calculations and compatibility assessment only. No actuator purchase, detailed CAD, final BOM, fabrication, assembly or physical testing. All require explicit owner decision under HOLD D-003.
