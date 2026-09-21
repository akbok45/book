---
description: Word counts, gaps, open flags, and what is worth working on next
---

Report the state of the draft. Be brief, this is a dashboard, not an essay.

1. Run `tools/wordcount.sh`. It prints words per scene, the chapter subtotals,
   the total, and flags any scene whose front matter `words:` no longer matches
   the file. Report the mismatches, they mean a scene changed and the outline
   was not updated.
2. Compare the scene files on disk against `manuscript/OUTLINE.md`. Report any
   scene marked MISSING, and any file on disk with no row in the outline.
3. Count the unstruck items in `notes/continuity-flags.md`, split into hard
   contradictions and mechanical slips. Name the hard ones in one line each.
4. List the open items in `notes/open-threads.md` by heading, count only,
   except any that block a scene the outline says is next.
5. Close with what is worth doing next and why, at most three options, ordered.
   A gap in the manuscript outranks a polish pass.

Do not draft anything. Do not fix anything. This command only reports.
