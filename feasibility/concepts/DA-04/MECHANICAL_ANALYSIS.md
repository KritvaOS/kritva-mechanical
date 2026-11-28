# DA-04 — Mechanical feasibility screen

**Status:** PROPOSED / ESTIMATE; no structural verification. D-003 remains active.

## Load path and mass geometry

The proposed path is payload → gripper/wrist → arm links → shoulder frame → torso → mobile base → wheels. At 2,700 kg/m³, a 500×600×4 mm 6061 plate is 3.24 kg; 3.40 m of 40×40×3 tube at 1.199 kg/m is 4.08 kg; estimated brackets add 1.00 kg. Two 400×600×1.5 mm torso panels are 1.94 kg plus a 0.50 kg frame allowance. A 0.900 m 20×20×2 arm tube is 0.350 kg bare plus 0.50 kg joints/mounts. These inputs produce a modeled mass rather than a selected construction.

## Static tip sensitivity

For a 30 kg robot centered over a 600 mm wheelbase, with the full mass COM assumed at the base center, the restoring moment at a wheel edge is 30×9.81×0.300 = 88.29 Nm. The 1.0 kg horizontal arm screen is 6.90 Nm gravity torque per arm at the shoulder; two symmetric arms produce a 13.81 Nm combined pitch moment in this simplified case, 16% of the upper-bound restoring moment. This calculation assumes the entire robot mass is centered and does not include drive acceleration, slope, unequal wheel support, COM shift or arm/base collision. It is not a tip-over pass or operational permission. At the 5° slope case, stability still requires actual COM and wheel-contact geometry.

## Drive and serviceability

The listing title gives 25 rpm and its description elsewhere says 35 rpm; using the lower 25 rpm yields 0.131 m/s at a 50 mm wheel radius. The modeled wheel torque is 1.27–1.78 Nm per driven side with 1.5× planning headroom; the listing reports 27.46 Nm after unit conversion. The torque excess does not settle speed, braking, traction or thermal fit. The base needs cable routing, emergency-stop access and battery restraint; these are design criteria, not verified layouts. A two-channel driver appears in each listing, so two combos are conservatively costed and may duplicate electronics.

## Evidence boundary

The centered COM, 600 mm wheelbase, 30 kg nominal, 0.45 m reach, symmetric arm loading, 5° slope, wheel radius and acceleration are scenario inputs. No structural, tipping, traction, braking, collision, thermal or physical validation is claimed. The study remains paper-only.