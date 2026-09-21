#!/usr/bin/env bash
# Word count per chapter plus a total. Author notes in [[ ]] are excluded.
set -euo pipefail

cd "$(dirname "$0")/.."

total=0
shopt -s nullglob
files=(manuscript/*.md)

if [ ${#files[@]} -eq 0 ]; then
  echo "No chapters in manuscript/ yet."
  exit 0
fi

for f in "${files[@]}"; do
  count=$(sed 's/\[\[[^]]*\]\]//g' "$f" | wc -w | tr -d ' ')
  total=$((total + count))
  printf '%-40s %8s\n' "$(basename "$f")" "$count"
done

printf '%-40s %8s\n' "TOTAL" "$total"
