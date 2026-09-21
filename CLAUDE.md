# Working on this book

This repo is the single source of truth for the book. It replaced a Claude
project, so the standing instructions that used to live in project settings
live here instead.

## Fill this in

These fields drive every drafting and editing decision. Keep them current.

- **Working title:** TBD
- **Genre / comps:** TBD
- **POV and tense:** TBD (e.g. third limited, past)
- **Target length:** TBD words across TBD chapters
- **Status:** TBD (outlining / drafting / revising)
- **Voice in one line:** TBD

## Layout

| Path | What lives there |
| --- | --- |
| `manuscript/` | The book itself. One file per chapter, `ch01-slug.md`. |
| `outline/` | Outline, beat sheets, structure docs. |
| `codex/` | Story bible: characters, places, timeline, rules, glossary. |
| `notes/` | Ideas, open questions, revision lists, scratch thinking. |
| `research/` | Source material and reference. Not the author's prose. |
| `archive/` | Cut scenes and superseded drafts. Never delete, move here. |
| `tools/` | Small scripts, e.g. word counts. |

## Rules when drafting or editing

1. **Read before writing.** Before touching a chapter, read the chapter before
   and after it, plus the relevant `codex/` entries. Continuity beats speed.
2. **Match the voice, do not impose one.** Sample the existing prose and write
   inside it. If no prose exists yet for a section, ask which register to use.
3. **No wholesale rewrites without being asked.** Default to targeted edits.
   If a passage needs structural surgery, say so and propose it first.
4. **Preserve the author's lines.** When editing, keep the original sentence
   wherever it works. Flag what changed and why.
5. **Update the codex as facts are established.** A new character name, a date,
   a rule of the world, a place: it goes in `codex/` in the same change.
6. **Track open questions.** Anything unresolved goes in `notes/questions.md`
   rather than being invented and quietly committed.
7. **Never invent citations.** Anything in `research/` that is claimed as fact
   needs a real source noted with it.

## Conventions

- Markdown, one sentence per line is fine but not required. Do not reflow a
  file wholesale, it destroys the diff.
- Scene breaks: a line containing only `***`.
- Chapter files start with `# Chapter N: Title`.
- Inline author notes use `[[ note to self ]]` so they are greppable and
  obviously not prose.
- Commit per meaningful unit of work (a scene, a pass over a chapter), with a
  message that says what changed in the story, not just "update".

## Useful commands

```bash
tools/wordcount.sh            # words per chapter plus total
grep -rn "\[\[" manuscript/   # every open author note
```
