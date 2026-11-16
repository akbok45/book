# Start here: where the current book is

Read this first in any new chat about the book.

## The current book

- **The year is 1670.** Any text set in 1690, with a chapter 2 called
  "Tortuga", a girl named Ixmal in the prose as final, or Domingo and Balam
  as "boys together", is an old version. Ignore it.
- **The manuscript** is the scene files in `manuscript/`, one file per scene.
  `manuscript/OUTLINE.md` lists every drafted scene with word counts.
- **The full reading copy** is `exports/book-one-working-draft.pdf` and
  `.docx`, rebuilt from the scene files with
  `python3 tools/working_draft.py . exports/book-one-working-draft.docx`
  (then convert to PDF with LibreOffice).
- **The plan for the whole book** is the Claude Doc "Book One: The Story"
  (https://claude.ai/artifact/AupjVzBfAcARa3aqaK9BJC). A plain export of it
  with the manuscript is `exports/book-one-2026-10-21.md`.

## The structure, as of 2026-11-15

Eleven chapters, about 115,000 words planned.

1. The Temple, drafted
2. Petit-Goâve, drafted
3. The Cay, drafted
4. The Half Moon, drafted
5. The Hidden Village, drafted through 5.4 The Sign
6. The Road Under the Lilies (the ceremony), not drafted
7. The Patrol, drafted ahead, to revise
8. The Singing Shrine
9. The Hold
10. The Fort
11. Florida

## Decisions and history

- `reference/character-bible.md`: who everyone is. The latest rulings are in
  the "Village arc" blocks near the end of the living cast section.
- `notes/village-arc-development.md`: the plan for chapters 5 to 7 and every
  ruling on it.
- `notes/continuity-flags.md`: what is invented and open to veto.
- `notes/conversation-*.md`: saved chat logs.

## Git

`main` holds the current book. Work happens on a branch and comes back to
`main` through a pull request. Pull request akbok45/book#1 brought everything
up to 5.4 into `main` on 2026-11-16.
