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
- **2026-06-28** — **Pivot to an all-software stand (no Arduino needed).** Stand = four browser
  games: **Quanten-Schach** (q-chess.com) + **Quanten-Tic-Tac-Toe** (tiqtaqtoe.com) + our own
  **Schlag die KI** (swipe/guess; teaches "humans are predictable, only true randomness wins") +
  **Hack the Light** (phone camera → bit, the no-Arduino version of the original 3-mode experiment).
  Our two games are self-contained mobile web pages in `software/web/`, deployed static to
  arraxis.com, opened via a **QR on the poster**. Arduino is now an **optional fallback**, not the hero.
- **2026-06-28** — Deployment: static (no backend) on arraxis.com; players use their **own phones**.
  Camera game needs **HTTPS** (has a no-camera demo fallback).
- **2026-06-28** — Added **Quanten-Elfmeter** (World-Cup tie-in): a penalty shootout where the
  goalkeeper is the same AI predictor (reads your pattern) + a **Quantenschuss** (superpose two
  corners; measurement collapses 50/50). Controls: buttons + swipe + motion-flick. Lesson = same as
  Schlag die KI (randomness beats prediction) plus superposition/measurement.
- **2026-06-28** — Leaderboard = **shared online** (`software/web/backend/`: Cloudflare Worker
  recommended, plain Node alternative), with a **localStorage fallback** so nothing breaks offline.
  Used by Quanten-Elfmeter (board `penalty`). Must set `LB_API_BASE` in the game after deploying.
- **2026-06-28** — **Quanten-Geschenk** prize page (`prize.html`): true-random (crypto) draw, staff
  triggers it for top players → they take a sweet from the box. Prize list editable in the file.
- **2026-06-28** — UX fixes: added a **"‹ Menü"** return button to our own games; **removed the
  manual "Kalibrieren"** in Hack the Light — it now **auto-calibrates** the mode-1 threshold on start.
- **2026-06-28** — **Load is a non-issue:** all our games are 100% client-side (each phone runs its
  own copy). The only shared piece is the leaderboard endpoint (a Worker handles far more than a
  kids' stand), and it degrades to a local board if unreachable.
- **2026-06-29** — **Games moved into the Arraxis website** (`triangulo-site`, Flask) and deploy at
  **https://arraxis.com/nachtdertechnik/**. Canonical source is now
  `triangulo-site/frontend/nachtdertechnik/` (the earlier `software/web/` copies are the dev origin).
  Added **Quanten-Elfmeter** as a 5th game. Styling matched to Arraxis (Inter, dark pink/teal theme,
  site nav/footer on the landing).
- **2026-06-29** — **Leaderboard now in every custom game** (boards `penalty`, `beat-ai`, `light`),
  backed by the **Arraxis Flask backend** (`/api/ndt/scores`, new `ndt_scores` table). Keeps each
  player's **best score + attempt count** (fixes the "score didn't update on retry" bug); name saved
  on the device, auto-submits on each replay; local fallback if offline. Cloudflare Worker is no
  longer needed (kept in `software/web/backend/` only as an alternative).
- **2026-06-29** — Penalty **motion control** reworked into a clear on/off toggle ("Bewegung: Aus/Ein")
  that fully removes the listener when off.
- **2026-06-29** — **Tests added:** 22 Node/jsdom (logic, encoders, leaderboard client, DOM flows) +
  6 pytest (leaderboard API). Run: `node --test` in the games folder; `pytest tests/test_ndt_leaderboard.py`.
- **2026-06-29** — **Poster refactored** to feature all 5 games + a real **QR** to
  arraxis.com/nachtdertechnik (`poster/Hack_the_Quantum_Poster_DE.pptx/.pdf`, `poster/qr_nachtdertechnik.png`).
- **2026-07-01** — Big feature batch on the Arraxis games:
  - **Mobile fixes** (penalty glove/ball depth + responsive sizing; motion = tilt-to-aim + shake-to-shoot; landing nav overlap).
  - **Quanten-Geschenk award system:** device id + `ndt_awards` table; rule = 1 sweet first-play + 1 for top-3, **max 2/device**, redeemed tracked (re-entry safe); medals 🥇🥈🥉 + tie-break; `prize.html` draws a **Lindt Lindor** flavour; games show a 🎁 button when unlocked; **admin panel** (list/delete/reset) at /admin. 6 new pytest pass.
  - **Penalty upgrades:** pre-game **team (flags) + role** pick (⚽ Schiessen / 🧤 Halten, same mechanic).
  - **Hack the Light:** clearer target ("Mach eine 0/1") + explicit "heller = eher 1" tip.
  - **Quantum-World slider** (`quantum-world.html`): 9 animated slides, Prev/Next + fullscreen, linked from landing.
  - **German i18n** added to the Arraxis site (backend + `i18n.js` allow `de`; per-key **English fallback**; `de.json` covers nav/footer/hero; deeper content falls back to English).
  - **Operating manual** (`docs/guide/operating-manual.md`) + physical-experiment idea + bilingual glossary + print PDFs.
  - ⚠️ Sandbox mount truncates freshly-edited large files, so penalty/beat-ai/hack-light/htq-lb JS could only be edited (not re-run) here — **test on a real phone after deploy.**

## Open questions (need an answer)

- [ ] Screen: use the provided one or bring our own monitor? What connector (HDMI)? Cable length?
- [ ] How many power sockets are actually at the stand?
- [ ] Guest Wi-Fi for browser games, or must everything run offline/local? (our games also run
      offline from the laptop; external chess/ttt need internet unless we cache them)
- [ ] Service Center poster print cost + lead time → set the print deadline.
- [ ] Confirm arraxis.com serves **HTTPS** (needed for the camera game) + final deploy URL for the QR.
- [ ] Replace the poster's placeholder QR with the real arraxis.com link.

## Pointers

- Agent guide: `CLAUDE.md` · Concept: `docs/concept.md` · Facts: `docs/event-facts.md`
- Checklist: `TODO.md` · Ideas/games/fallbacks: `docs/ideas-backlog.md` · Poster: `docs/poster-plan.md`
- Firmware: `arduino/hack_the_quantum/` · Screen UI: `software/quantum_ui/`
