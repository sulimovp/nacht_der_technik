# NOTES — single source of truth

> Living document. Record facts, decisions, and open questions here as they happen.
> Detailed extracts live in `docs/`; this is the at-a-glance index + decision log.

## The one-liner

**Hack the Quantum — Wie aus Licht ein Bit wird.** A hands-on TechLab stand where kids make light
on a sensor and try to force a 0/1; three encoding modes make control fade from easy → impossible,
teaching why randomness matters for AI / security / quantum tech. Minimal hardware (Arduino Starter
Kit) + a screen with free browser quantum games.

## Who / where / when

- **Team:** Pavel Sulimov (suli) + Claude Lehmann (lehl), InIT, ZHAW. Both staff the stand.
- **When:** Fri **3 July 2026**, 18:00–23:00 (TechLab 18:00–22:00). Setup from 12:00, done by 17:15.
- **Where:** ZHAW SoE, building TP, ground floor, stand "InIT «Hack the Quantum»", 3×2 m.

## Key facts (see `docs/event-facts.md` for the full extract)

- Organizer provides: 2 tables, 3 chairs, power, back walls, poster wall, A3 stand, a screen.
- Poster: must use MINT templates (`reference/poster_templates/`), German, child-simple, **we print
  it ourselves** via the Service Center (confirm cost + lead time → drives our print deadline).
- Catering provided if we register staff names in advance to events.engineering@zhaw.ch.
- PSP hours: only 18:00–23:00 counts; report PSP persons by Mon 6 July; log hours by end July.

## Decisions log

- **2026-06-21** — Repo organized for agent work (CLAUDE.md + docs/ + arduino/ + software/ +
  reference/). Working docs in English; public text in German.
- **2026-06-21** — Hardware scope locked to the Arduino Starter Kit only (LDR + RGB LED + piezo +
  2 buttons). Level-3 "quantum-like" randomness = LDR analog noise (no extra hardware). Honesty
  note: it's a physical-noise entropy source, an analogy, not a true quantum RNG.
- **2026-06-21** — Second activity = free **browser** quantum games on the provided screen (zero
  build), to absorb the queue. Shortlist in `docs/ideas-backlog.md`.
- **2026-06-21** — Starter Arduino sketch + Python UI skeleton drafted (need to flash & test on
  Pavel's real kit).

## Open questions (need an answer)

- [ ] Screen: use the provided one or bring our own monitor? What connector (HDMI)? Cable length?
- [ ] How many power sockets are actually at the stand?
- [ ] Guest Wi-Fi for browser games, or must everything run offline/local?
- [ ] Service Center poster print cost + lead time → set the print deadline.
- [ ] Do we want bilingual (DE/EN) screen text, or German only?

## Pointers

- Agent guide: `CLAUDE.md` · Concept: `docs/concept.md` · Facts: `docs/event-facts.md`
- Checklist: `TODO.md` · Ideas/games/fallbacks: `docs/ideas-backlog.md` · Poster: `docs/poster-plan.md`
- Firmware: `arduino/hack_the_quantum/` · Screen UI: `software/quantum_ui/`
