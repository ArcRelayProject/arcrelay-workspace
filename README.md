# ArcRelay

ArcRelay is a local-first desktop collaboration system for clipboard sharing,
nearby file transfer, cross-screen input, printer sharing, remote files, and
local automation.

This repository is the integration workspace for the open-source desktop
client. Each Rust or Tauri component is pinned as a Git submodule so releases
can be reproduced from an exact set of source revisions.

The official ArcRelay mobile application and its native bridge are proprietary
products distributed separately. Their source code, build system, product
design material, development QA artifacts, and internal test reports are not
part of this repository.

## Clone and verify

```sh
git clone --recurse-submodules https://github.com/ArcRelayProject/arcrelay.git
cd arcrelay
./ci/check-public-boundary.sh
python3 ci/check-dependency-pins.py
cargo fmt --all -- --check
cargo test --workspace --all-targets
cd arcrelay-desktop
npm ci
npm run check
npm test
```

See [arcrelay-desktop](arcrelay-desktop/) for development and community build
instructions. Screenshot capture and OCR are optional proprietary components in
official builds; the open-source desktop client builds and runs without them.

## Repository map

| Area | Repositories |
| --- | --- |
| Desktop application | `arcrelay-desktop` |
| Wire and transport | `arcrelay-wire`, `arcrelay-transport`, `arcrelay-network` |
| Trust and permissions | `arcrelay-peer` |
| Features | `arcrelay-content`, `arcrelay-input`, `arcrelay-transfer`, `arcrelay-print`, `arcrelay-files` |
| Application services | `arcrelay-core`, `arcrelay-protocol`, `arcrelay-automation`, `arcrelay-web-gateway` |

## License and branding

The source code is licensed under the GNU Affero General Public License,
version 3 only. See [LICENSE](LICENSE). Commercial licensing is available from
Shenzhen Changning Technology Co., Ltd. at
[chenzibo@nbhive.com](mailto:chenzibo@nbhive.com) for products that cannot
comply with the AGPL.

The software license does not grant rights to the ArcRelay name, logos, or
trade dress. See [TRADEMARKS.md](TRADEMARKS.md).
