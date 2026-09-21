# Book

Manuscript, outline, and story bible for the book, versioned in git.

## Getting your existing docs in

If you have drafts sitting in a folder on your machine (the old Claude project
exports, a `novel` folder, a zip), put them here:

```bash
git clone https://github.com/akbok45/book.git
cd book
git checkout claude/serene-ramanujan-r6dhgc

# drop the files in, roughly:
cp ~/Downloads/novel/*.md manuscript/     # chapters and prose
unzip ~/Downloads/codex-book-one.zip -d /tmp/codex && cp -R /tmp/codex/* codex/

git add -A && git commit -m "Import existing manuscript and codex" && git push
```

Anything not obviously a chapter can land in `notes/` and get sorted later.
`.docx` files are fine to commit as-is; convert them to Markdown when you
actually start editing them.

## Layout

- `manuscript/` the book, one file per chapter
- `outline/` outline and beat sheets
- `codex/` characters, places, timeline, rules, glossary
- `notes/` ideas, open questions, revision lists
- `research/` source material
- `archive/` cut scenes and old drafts
- `tools/` helper scripts

## Word count

```bash
tools/wordcount.sh
```

## Working with Claude

`CLAUDE.md` holds the standing instructions: voice, POV, continuity rules, how
edits should be made. Keep the fields at the top filled in. That file is what
the old Claude project settings used to be.
