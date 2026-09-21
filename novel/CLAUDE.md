# The Codex Trilogy, Book One

Caribbean, 1690. First person, narrated by Jigsaw, plain sailor's voice. Tonal register after *Gideon the Ninth*: sardonic, raunchy, genuinely dark, pathos buried under comedy.

Aydin writes this book. Claude drafts, line edits, and checks continuity on request. Claude does not decide plot, kill characters, or invent backstory without being asked.

---

## The prose laws (non negotiable)

These override every craft note in `reference/craft/`. If a craft doc and this section disagree, this section wins.

1. **No filler words.** Every word carries weight or comes out.
2. **Never use the word "thing"** except inside dialogue where a character would say it.
3. **Every comparison comes from their world.** Ocean, fish, weather, hide, stone, rope, rot, powder, animals, the hunt. No modern referent, no abstraction dressed as an image.
4. **Two commas a sentence, maximum.** Exception one: a list. Exception two: a short appositive dropped between commas does not count against the pair, as in `scabbard, clean, the hand dropping with the hilt still in its grip`. The rule exists to kill runoff sentences, not to ban rhythm.
5. **1690 is locked.** Only objects, words, foods, weapons, and ideas that existed. No anachronism, ever.
6. **Show feeling in behavior, never state it.** Hands, jaw, where the eyes go, what gets reached for. A man who says it is fine and means it does not say it.

## The voice ladder

| Character | Register | Volume |
|---|---|---|
| **Bonesy** | High, raspy, drawn out. Common words only, he was a peasant, not a wit. Short lines. Pauses. Pries with questions, never theses. Comma loose. Bawdy and bodily, of its century. | Loudest |
| **Crumble** | Terse, controlled, a man sitting at his own wake. Grief in the hands and the jaw, never in a speech. Says it is fine and reaches for a task. Maya softening only the trusted hear. | Middle |
| **Jigsaw** | Plain sailor's mouth, dry. Quietest in the room, loudest on the page, because we live in his head. Narration observes, withholds, then leaks personal when the wound is touched. | A notch under Crumble |

Rhythm test for Bonesy. Wrong, too built: *"I'm only watching the two of you not want things. It's hard labor to watch."* Right: short line, pause, then he just asks. *"You had a woman."* ... *"What was her name."*

## Ban list, search and destroy

okay, OK, guys, yeah, yep, nope, hi, hey, cool, awesome, fine (as in "I'm fine"), deal with it, no problem, I guess, kind of, sort of, focus, contact (as a verb), teenager, boyfriend, girlfriend, definitely, basically, actually, obviously, thing.

Also banned as period errors: **gun** for a hand weapon (gun means cannon, use pistol, musket, piece), **maroon** for Jigsaw's father's people (it means escaped African captives, a different people), **guerrilla** (not a word until the 1800s), **"Arrr"** and all Hollywood pirate speech.

---

## Where everything lives

```
manuscript/          the book itself, one file per scene, in reading order
  ch01-the-temple/
  ch02-tortuga/
  ch03-the-cay/
  OUTLINE.md         scene index, word counts, what happens where
reference/
  character-bible.md the leads, the antagonist, the dead, the timeline
  story-so-far.md    plain recap of book one to date
  world-1690.md      buccaneer Caribbean research: history, ships, code, language
  craft/             the fourteen craft guides, 00 to 14
notes/
  style-rules.md     the prose laws expanded, with worked examples
  continuity-flags.md contradictions and draft artifacts awaiting a decision
  open-threads.md    plot and character questions still unsettled
_raw/                the original single file exports, kept as a backup. Do not edit.
```

## Working rules

**Read before you write.** Before drafting or editing any scene, read `reference/character-bible.md` and the scene files on either side of the one being worked. Voice drift comes from writing a scene in isolation.

**Edit in place, in the full passage.** Never present an edited line on its own. Rewrites go back into the scene file being worked, so the surrounding rhythm is visible.

**One scene per file.** New scenes get a new numbered file in the right chapter folder, with the same front matter block as its neighbours. Renumber neighbours if a scene is inserted between two others.

**Never touch `_raw/`.** It is the backup of the original drafts.

**Flag, do not fix, a contradiction.** If a new line conflicts with the bible or an earlier scene, say so and add it to `notes/continuity-flags.md`. Aydin decides which version is true.

**Do not smooth the draft.** Odd punctuation, a lowercase name, a half sentence left standing: leave it unless asked. Some of it is deliberate.

**Do not summarize the emotion after a scene lands it.** If the behavior did the work, no line explaining it follows.

## What Claude does when asked to draft

1. Read the bible section for whoever is in the scene.
2. Read the previous scene file, whole.
3. Draft into a new or existing scene file, in the voice ladder above.
4. Run the check in `.claude/commands/linecheck.md` on the new prose before handing it back.
5. Report what was written in two sentences. No recap of the content Aydin just asked for.
