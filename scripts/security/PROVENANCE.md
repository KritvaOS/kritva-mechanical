# Provenance of vendored scripts

| File | Source | Source commit | SHA-256 of the copy | Modified |
|---|---|---|---|---|
| `check_commit_format.py` | `KritvaOS/kritva-program`, `scripts/security/check_commit_format.py` | `ff6d33afe26d14ddd29a949f50a97f8ee16331c8` (local clone; may be behind GitHub) | `aec47664e4bb65336d19bd5f4614c0877d1f09b2ed0e8876b96e859848df0a5d` | No, byte-for-byte copy |

Why vendored: the `commit-message-check` workflow must enforce the same program commit format (D-053) without a cross-repository checkout. The program script is the authority; if it changes, copy it again, update this table in the same pull request and add a changelog entry. Do not edit the copy here to make a commit pass.

The program script rejects AI session trailers and links, requires exactly one `Task:` or `Tasks:` footer, allows `Tasks: None (reason)` only on docs or chore commits, and skips merge commits. With `--registry` it also rejects task IDs that are not in the given list.
