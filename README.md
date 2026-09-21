# The Codex Trilogy, Book One

Working repository for the novel. Caribbean, 1690. First person, narrated by Jigsaw.

## Getting started

```
git clone https://github.com/akbok45/book.git
cd book
claude
```

Claude reads `CLAUDE.md` on start, so the prose laws, the voice ladder, and the file map are loaded before you ask for anything.

Try `/status` first. It reports word counts, gaps, and what is worth working on next.

## Commands

| Command | What it does |
|---|---|
| `/draft <scene>` | Reads the bible and the previous scene, then drafts in voice into a scene file |
| `/linecheck <file>` | Line edit pass against the ban list, the comma rule, the comparison rule, stated feeling, anachronism |
| `/continuity <file>` | Checks a scene against the bible and its neighbours. Reports, never fixes |
| `/status` | Word counts, gaps, open flags, what to do next |

## Layout

```
CLAUDE.md              the prose laws and working rules. Read on every session
.claude/commands/      the four slash commands below
manuscript/            the book, one file per scene, in reading order
  OUTLINE.md           scene index with word counts and beats
reference/
  character-bible.md   the authority on the cast, the wounds, the timeline
  story-so-far.md      plain recap of book one. Superseded by the bible where they disagree
  world-1690.md        buccaneer Caribbean research: history, ships, the code, language
  craft/               the fourteen craft guides
notes/
  style-rules.md       the prose laws with worked examples from the draft
  continuity-flags.md  contradictions and draft artifacts awaiting a decision
  open-threads.md      plot and character questions still unsettled
_raw/                  the original single file exports. Backup. Do not edit
tools/wordcount.sh     words per scene, chapter subtotals, stale front matter
```

## Why this shape

The whole point of moving off one long document is that an edit no longer costs the whole draft. A scene file is small enough to load, work, and check on its own, and `CLAUDE.md` carries the rules that used to have to be restated every session.

Two habits keep it working:

- Update the word count in a scene's front matter when the scene changes.
- Put decisions into `notes/`, not into the chat. The chat ends. The files do not.

## Version control

This is a git repository, at https://github.com/akbok45/book.

Every session's edits are a diff you can read and undo. Commit when a scene
lands or a pass finishes, not at the end of the night:

```
git add -A
git commit -m "2.4 the escape, first draft"
git push
```

`git diff` before committing shows exactly what changed in the prose. `git
checkout -- <file>` throws a bad pass away.
