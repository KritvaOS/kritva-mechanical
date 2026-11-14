# Week 2 tools

Run from the repository root after copying this overlay.

```bash
python3 tools/validate_week2_overlay.py
python3 tools/apply_week2_readmes.py
```

The validator performs file/table/label smoke checks. It does not validate engineering accuracy, inspect PNG pixels, verify external links, prove mass/torque/stability, or approve CP2.

The README patcher requires the four existing concept READMEs. It replaces only numbered sections 11, 13, 14, 15 and 16, backs each original file up as `README.md.week2.bak`, and refuses to overwrite an existing backup. Review the diff before staging.
