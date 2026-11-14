#!/usr/bin/env python3
"""Offline smoke validator for the INTERN-01 Week 2 overlay. Standard library only."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"DA-01": 6, "QR-02": 12, "DA-04": 10, "QR-04": 12}
REQUIRED = (
    "ARCHITECTURE.md", "MECHANICAL_ANALYSIS.md", "ACTUATOR_ANALYSIS.md",
    "INTERFACES.md", "MASS_BUDGET.md", "COST_MODEL.md", "OPEN_QUESTIONS.md",
    "WEEK2_README_SECTIONS.md", "calculations/WEEK2_ARCHITECTURE_CHECKS.md",
    "references/SOURCE_REGISTER.md", "reviews/WEEK2_CONCEPT_REVIEW.md",
    "sketches/WEEK2_CONCEPT_SKETCH.svg",
)

def main():
    errors = []
    for cid, joint_count in EXPECTED.items():
        folder = ROOT / "feasibility" / "concepts" / cid
        for rel in REQUIRED:
            if not (folder / rel).is_file():
                errors.append(f"{cid}: missing {rel}")
        arch = folder / "ARCHITECTURE.md"
        actuator = folder / "ACTUATOR_ANALYSIS.md"
        if arch.exists():
            a = arch.read_text(encoding="utf-8")
            if "CONCEPT_TARGET" not in a or "TBD" not in a or "D-003" not in a:
                errors.append(f"{cid}: architecture lacks target/unknown/hold labels")
        if actuator.exists():
            t = actuator.read_text(encoding="utf-8")
            # Each physical instance row must exist and unknown fields must remain explicit.
            rows = [ln for ln in t.splitlines() if ln.startswith("| ") and "TBD" in ln]
            if len(rows) < joint_count:
                errors.append(f"{cid}: expected at least {joint_count} TBD joint rows, found {len(rows)}")
            if "S/M/L" not in t or "20 N·m" in t and cid != "DA-01":
                # Guard only to ensure the file discusses mapping and doesn't treat reference as universal.
                pass
            for col in ("Continuous torque", "Peak torque", "Output speed", "ROM"):
                if col not in t:
                    errors.append(f"{cid}: actuator matrix missing {col}")
        svg = folder / "sketches" / "WEEK2_CONCEPT_SKETCH.svg"
        if svg.exists():
            s = svg.read_text(encoding="utf-8")
            if "<svg" not in s or "NOT TO SCALE" not in s or "NOT CAD" not in s:
                errors.append(f"{cid}: sketch is missing conceptual/non-CAD markings")
        if (folder / "cad").exists():
            errors.append(f"{cid}: forbidden cad/ folder exists")
        if (folder / "WEEK2_README_SECTIONS.md").exists():
            p = (folder / "WEEK2_README_SECTIONS.md").read_text(encoding="utf-8")
            found = re.findall(r"(?m)^## (11|13|14|15|16)\.", p)
            if sorted(map(int, found)) != [11, 13, 14, 15, 16]:
                errors.append(f"{cid}: README patch does not contain exactly sections 11,13,14,15,16")
    for rel in ("feasibility/interns/INTERN-01/WEEKLY_STATUS.md",
                "feasibility/interns/INTERN-01/CP2_CONTRIBUTION.md",
                "feasibility/interns/INTERN-01/WEEK2_ARCHITECTURE_COMPARISON.md"):
        if not (ROOT / rel).is_file():
            errors.append(f"Missing {rel}")
    if errors:
        print("FAIL")
        for e in errors: print("-", e)
        return 1
    print("PASS: Week 2 overlay file and structural checks passed.")
    print("LIMITATION: this is not engineering verification, image validation, repository-wide link validation or owner acceptance.")
    print("CHECKPOINT: CP2 remains PARTIAL until all 12 concepts and authorized review are complete.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
