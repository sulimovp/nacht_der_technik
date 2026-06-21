# CLAUDE.md — Agent operating guide

> Read this first. It tells you (the AI agent) what this repo is, what we're building,
> the hard constraints, and how to work here. Humans: see `README.md`.

## What this project is

We are building an interactive exhibit for **Nacht der Technik 2026** at ZHAW School of
Engineering (Winterthur), in the **TechLab** (for kids & teens, ages 6+).

- **Exhibit title:** *Hack the Quantum — Wie aus Licht ein Bit wird*
- **Stand ID on the floor plan:** `InIT «Hack the Quantum»`, TP ground floor (EG), 3×2 m
- **Owners:** Pavel Sulimov (`suli`) and Claude Lehmann (`lehl`), both InIT, ZHAW.
- **Event date:** Friday **3 July 2026**, 18:00–23:00 (TechLab open 18:00–22:00).

The core idea: a child makes a light signal (flashlight / hand) on an Arduino light
sensor and tries to force the output bit to 0 or 1. Three encoding modes make control
progressively harder — deterministic → hidden rule → physical-noise randomness — so kids
*feel* the difference between a controllable system and a fundamentally unpredictable one.
This is the bridge to why randomness matters for AI, security and quantum tech.

## The prime directive: minimal effort, maximal outcome

Every decision is judged against this. Pavel owns an **Arduino Starter Kit** and that is
essentially our whole hardware budget. Prefer, in order:

1. **Free browser quantum games** on a screen (zero build) — see `docs/ideas-backlog.md`.
2. **One small Arduino build** using only Starter-Kit parts (LDR + RGB LED + piezo + buttons).
3. Only then anything that needs buying or fabricating.

If a proposed feature can't be reached with the Starter Kit + a laptop + a screen, flag it
as "stretch" rather than committing to it.

## Hard constraints (do not violate)

- **Audience is children 6+ and a broad public.** No jargon, no formulas on anything public-facing.
  The organizer factsheet explicitly requires simple, abbreviation-free language.
- **Public text must be German** (event website + poster). Working docs are English.
- **Stand footprint is 3×2 m.** Provided by organizer: 2 tables, 3 chairs, power, back walls,
  poster wall, A3 stand, 1 screen. Don't design for more space than that.
- **Power:** plan for 1× 230 V socket (laptop/USB for Arduino); a 2nd socket is optional for
  a monitor/2nd laptop. Keep power needs low.
- **Interaction must be short:** 30–90 s per child. Things must survive hundreds of sticky-hand cycles.
- **No student helper, no Bachelor thesis attached** (we said "Nein" in the proposal). Just the two of us.
- **Poster must use the provided MINT templates** in `reference/poster_templates/` (new ZHAW
  corporate design). Do not invent a layout.

## Repo layout

```
CLAUDE.md                  ← you are here (agent guide)
README.md                  ← human overview + quick start
NOTES.md                   ← single source of truth: facts, decisions, open questions
TODO.md                    ← master checklist (owners + deadlines)
docs/
  event-facts.md           ← everything extracted from factsheet / emails / floor plan
  concept.md               ← the exhibit concept, cleaned and committed
  ideas-backlog.md         ← extra ideas, browser games, fallbacks, extensions
  poster-plan.md           ← German poster content mapped to the MINT template
arduino/
  hack_the_quantum/
    hack_the_quantum.ino   ← 3-mode encoder firmware (Starter-Kit only)
software/
  quantum_ui/
    quantum_ui.py          ← Python screen UI (serial → live bit + score)
    requirements.txt
reference/
  organizer/               ← factsheet PDF, floor plan PDF (read-only source of truth)
  poster_templates/        ← MINT .potm templates (use these for the poster)
```

## How to work in this repo

- **Treat `NOTES.md` as the source of truth.** When you learn or decide something, record it
  there (and update `TODO.md`). Don't let facts live only in chat.
- **When facts conflict,** the organizer PDFs in `reference/organizer/` win, then emails, then
  our own proposal. (Note: the original proposal blurb mis-stated the date as well as "3. Juli";
  the factsheet confirms **Friday 3 July 2026** — use that everywhere.)
- **Keep public-facing content child-simple and German.** Working notes stay English.
- **Prefer editing the real files** over pasting long content into chat.
- **Document creation:** for the poster use the `pptx` skill with the `.potm` templates; for any
  Word/PDF deliverables use the `docx`/`pdf` skills. Do research first, then read the skill.
- **Hardware reality check:** before adding a component to the Arduino sketch, confirm it's in the
  Arduino Starter Kit. If unsure, mark it as "needs purchase" in `TODO.md`.

## Quick status

See `TODO.md` for the live checklist. The single most important early milestone is a working
end-to-end Arduino→screen demo of all three modes on Pavel's own kit.
