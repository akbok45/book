#!/usr/bin/env bash
# Words per scene, chapter subtotals, and a flag where front matter `words:`
# no longer matches the file. Front matter and <!-- BEAT --> notes excluded.
set -euo pipefail

cd "$(dirname "$0")/.."

shopt -s nullglob
total=0
mismatches=0
current_chapter=""
chapter_total=0

print_chapter_total() {
  if [ -n "$current_chapter" ]; then
    printf '%-52s %7s\n' "  subtotal" "$chapter_total"
    echo
  fi
}

for f in manuscript/ch*/*.md; do
  chapter=$(dirname "$f")
  if [ "$chapter" != "$current_chapter" ]; then
    print_chapter_total
    current_chapter="$chapter"
    chapter_total=0
    echo "$(basename "$chapter")"
  fi

  actual=$(awk 'NR==1 && $0=="---" {fm=1; next} fm && $0=="---" {fm=0; next} !fm' "$f" \
    | sed 's/<!--[^>]*-->//g' | wc -w | tr -d ' ')
  declared=$(awk -F': *' 'NR==1 && $0=="---" {fm=1; next} fm && $0=="---" {exit} fm && $1=="words" {print $2; exit}' "$f")

  flag=""
  if [ -n "$declared" ] && [ "$declared" != "$actual" ]; then
    flag="  <- front matter says $declared"
    mismatches=$((mismatches + 1))
  fi

  printf '  %-50s %7s%s\n' "$(basename "$f")" "$actual" "$flag"
  chapter_total=$((chapter_total + actual))
  total=$((total + actual))
done

print_chapter_total
printf '%-52s %7s\n' "TOTAL" "$total"

if [ "$mismatches" -gt 0 ]; then
  echo
  echo "$mismatches scene(s) out of date in front matter."
fi
