# TODO — Hack the Quantum @ Nacht der Technik 2026

> Master checklist. **P** = Pavel, **CL** = Claude Lehmann, **AI** = can be done with the agent.
> Guiding rule: *minimal effort, maximal outcome.* Do the 🟢 "must-haves" first; 🔵 are
> nice-to-haves; ⚪ are stretch ideas. Event day: **Fri 3 July 2026**.

## 0. Admin & deadlines (cheap, don't forget) 🟢

- [ ] Email events.engineering@zhaw.ch with **stand staff names** (Pavel + Claude L.) for catering — *(P)*
- [ ] Confirm **PSP-number persons** report by **Mon 6 July 2026**; log event hours by end July — *(P)*
- [ ] Ask organizer the open questions in `NOTES.md` (screen/connector, sockets, Wi-Fi) — *(P)*
- [ ] Confirm Service Center **poster print cost + lead time** → set our print deadline — *(P)*

## 1. The hero: Arduino → screen demo 🟢

This is the single most important milestone. Get an end-to-end working demo on Pavel's own kit early.

- [ ] Flash `arduino/hack_the_quantum/hack_the_quantum.ino` to the UNO — *(P, AI to help debug)*
- [ ] Wire per the pin map in the sketch header (LDR divider, RGB LED, piezo, 2 buttons) — *(P)*
- [ ] Run `software/quantum_ui/quantum_ui.py`, confirm serial connection + live bar + big 0/1 — *(P/AI)*
- [ ] **Calibrate Level 1 threshold** to the room's actual light (auto-calibrate routine in sketch) — *(P)*
- [ ] **Tune Level 2 parity** so big brightness changes sometimes don't flip the bit (feels "sneaky") — *(P/AI)*
- [ ] **Tune Level 3 entropy** (sample count N, debiasing) so success ≈ 50% even with steady light — *(P/AI)*
- [ ] Test the "feel": does a real person experience control dropping across levels? — *(P+CL)*
- [ ] Robustness: survives unplug/replug, sticky hands, mashed buttons; auto-recovers — *(P/AI)*

## 2. Second activity: browser quantum games 🟢

Zero build — absorbs the queue and gives a 2-player option.

- [ ] Pick 1–2 games from `docs/ideas-backlog.md` (default: Quantum Tic-Tac-Toe) — *(P+CL)*
- [ ] Test on the actual screen resolution; check they work **offline** if no guest Wi-Fi — *(P)*
- [ ] Make a 1-page "how to play" card (German, kid-simple) for the screen corner — *(AI)*
- [ ] Decide browser kiosk/fullscreen setup so kids can't wander off the page — *(P/AI)*

## 3. Poster (must use MINT template, German, child-simple) 🟢

- [ ] Confirm portrait vs landscape (poster wall = portrait likely) — *(P)*
- [ ] Fill the MINT template from `docs/poster-plan.md` content using the `pptx` skill — *(AI)*
- [ ] Keep it jargon-free; add the big "🟢🟡🔵 control drops" visual — *(AI)*
- [ ] Internal review for CD compliance + readability from 2 m — *(P+CL)*
- [ ] Send to print with enough lead time before 3 July — *(P)*

## 4. Stand build & logistics 🔵

- [ ] A3 stand: short "How to play" + safety/hygiene note (German) — *(AI draft, P print)*
- [ ] Pack list: laptop + charger, UNO + USB cable, breadboard (pre-wired + spare), spare LDR/LED/
      wires, monitor cable (HDMI?), power strip, tape, cable ties, hand sanitiser/wipes — *(P)*
- [ ] **Pre-wire and hot-glue** the breadboard at home so setup on-site is plug-and-play — *(P)*
- [ ] Bring a printed copy of the pin map + this TODO — *(P)*
- [ ] Setup rehearsal: full stand assembled once before the event — *(P+CL)*

## 5. Polish / engagement 🔵

- [ ] Sound on/off toggle (a beeping stand for 4 h can get old) — *(AI)*
- [ ] "High score" / streak display to pull kids in — *(AI)*
- [ ] Simple attract-mode animation when idle — *(AI)*
- [ ] Optional bilingual (DE/EN) screen text — *(AI)* — pending decision in `NOTES.md`

## 6. Stretch ideas (only if time) ⚪

See `docs/ideas-backlog.md` for the full backlog (multi-sensor entropy, human-vs-AI prediction,
live entropy meter, two-player Arduino mode, takeaway "your random number" slip).

## Status snapshot

- ✅ Repo organized; concept + facts + notes committed.
- ✅ Arduino sketch + Python UI **first drafts** written (untested on hardware).
- ✅ Poster content outline drafted (`docs/poster-plan.md`).
- ⏭️ **Next critical step:** flash + wire + test the end-to-end demo on Pavel's kit (section 1).
