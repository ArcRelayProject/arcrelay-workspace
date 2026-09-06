# Contributing to ArcRelay

Thank you for considering a contribution to the ArcRelay desktop project.

## Scope

Contributions must stay within the public desktop and shared-library boundary.
Do not submit proprietary mobile source, mobile build scripts, private service
implementation, credentials, internal URLs, product design sources, QA capture
images, or internal test reports.

Use Conventional Commit prefixes such as `feat:`, `fix:`, `docs:`, `test:`,
`refactor:`, and `chore:`. Open a focused pull request against the component
repository that owns the change. Update this integration repository only after
the component commit has landed.

## Contributor license agreement

Before a contribution can be merged, its authors must complete the ArcRelay
Contributor License Agreement. The agreement keeps copyright with the author
while granting the project owner the rights needed to distribute the
contribution under the AGPL and under separate commercial terms. Pull requests
from contributors who have not completed the agreement remain unmerged.

By submitting a contribution, you confirm that you have the right to submit it
and that it does not contain confidential or third-party material you are not
authorized to disclose.

## Checks

Run the checks that apply to the changed component. For integration changes,
run:

```sh
./ci/check-public-boundary.sh
python3 ci/check-dependency-pins.py
cargo fmt --all -- --check
cargo test --workspace --all-targets
```

For desktop frontend changes, also run `npm ci`, `npm run check`, and `npm test`
inside `arcrelay-desktop`.
