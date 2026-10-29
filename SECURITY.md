# Security Policy

This repository holds robot-level mechanical planning and, later, design data for the Kritva robot. The reporting route below is PROPOSED and must be confirmed by the owner before this file is relied on.

## Reporting a vulnerability or safety concern

Do not open a public issue or pull request that describes an unfixed vulnerability, a leaked secret or an unresolved safety hazard.

Report it privately:

1. Use GitHub private vulnerability reporting for this repository (the "Report a vulnerability" button on the Security tab), if it is enabled.
2. If that button is not shown, contact the repository owner, Dinesh (Kritvaos Security Owner), through the contact route published on the `KritvaOS` organisation profile, and ask for a private channel before sending details.

Include what you found, where, and how to reproduce it, without attaching real secrets or personal data. Expect an acknowledgement from the owner; no response time is promised until the owner sets one.

## What counts

- A committed credential, token, key or personal data.
- A weakness in repository automation, such as a workflow that could leak a secret or run untrusted code.
- A mechanical or safety hazard in a published design, such as a wrong limit, an unsafe assumption or a missing guard. Safety concerns about physical hardware are handled with the same private route.

## Supported versions

There are no releases. The `main` branch is the only maintained version.

## If you committed a secret

Tell the owner at once. Deleting it in a later commit does not make it safe; the credential must be revoked or rotated.

## Disclosure

The owner decides when and how a fixed issue is disclosed.
