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

Before a contribution can be merged, every human author must execute the
[individual contributor license agreement](CLA-INDIVIDUAL.md). If an employer
or another organization owns the contribution, an authorized representative
must also execute the [corporate contributor license agreement](CLA-CORPORATE.md).
The agreements keep copyright with its owner while granting Shenzhen Changning
Technology Co., Ltd. the rights needed to distribute the contribution under
the AGPL and under separate commercial terms.

Send the completed agreement from the signer's email address to
[chenzibo@nbhive.com](mailto:chenzibo@nbhive.com). Do not commit a signed
agreement or personal details to a public repository. The company keeps signed
agreements in private records. After verification, a maintainer applies the
`cla: signed` label to the pull request. Each additional human co-author must
complete the same process.

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
