#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

for private_path in arcrelay-mobile arcrelay-mobile-native docs/design; do
  if [[ -e "$private_path" ]]; then
    echo "private-only path is present: $private_path" >&2
    exit 1
  fi
done

if rg -n --hidden \
  --glob '!.git/**' \
  --glob '!target/**' \
  --glob '!ci/check-public-boundary.sh' \
  --glob '!Cargo.lock' \
  --glob '!package-lock.json' \
  --glob '!bun.lock' \
  '(gitea\.czbrcj\.cn|ci\.czbrcj\.cn|czbrcj|chenzibo|LinkGroup|SniptraGroup|BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY|github_pat_|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})'; then
  echo "public source contains an internal identifier or likely credential" >&2
  exit 1
fi

while IFS= read -r artifact; do
  echo "development image is present under documentation: $artifact" >&2
  exit 1
done < <(
  find . -path './.git' -prune -o -path '*/target' -prune -o \
    -type f -path '*/docs/*' \
    \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.webp' -o -iname '*.gif' \) \
    -print
)
