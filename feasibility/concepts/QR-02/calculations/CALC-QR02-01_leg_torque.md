# CALC-QR02-01 — QR-02 Leg Joint Torque Estimates

**Status:** PROPOSED / ESTIMATE | 2026-11-27 | INTERN-01

## Purpose
Transparent quasi-static + planning dynamic torque for one leg of QR-02 under single-leg support.

## Inputs (from ACTUATOR_ANALYSIS)
- Robot mass 5.5 kg → single-leg vertical force ≈ 54 N
- Leg length 220 mm, equal segments 110 mm
- Planning factor 1.5×
- α = 15 rad/s² for inertial allowance

## Static moments (critical flexed pose)
Approximate moment arm for hip flexion ≈ 0.07–0.09 m at mid-stance flexed posture →  
τ_hip_flex ≈ 54 N × 0.08 m ≈ 4.3 N·m (before dynamic).  
Working continuous value used in matrix: 3.8 N·m (conservative geometry variation).

Knee: shorter distal lever → ≈ 2.1 N·m continuous.

## Peak
Static + Iα allowance + ground transient planning margin → values shown in parent ACTUATOR_ANALYSIS.

## Limitations
No measured gait, no force-plate data, no multi-body model. Results are order-of-magnitude planning estimates only.
