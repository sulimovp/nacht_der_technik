# TODO — Hack the Quantum @ Nacht der Technik 2026

> Master checklist. **P** = Pavel, **CL** = Claude Lehmann, **AI** = can be done with the agent.
> Event day: **Fri 3 July 2026**, 18:00–22:00 (TechLab). Setup from 12:00, done by 17:15.
> The digital build is essentially done — what's left is **deploy, test, print, and stand logistics.**

## 0. Admin & deadlines (cheap emails, don't forget) 🟢

- [ ] Email events.engineering@zhaw.ch with **stand staff names** (Pavel + Claude L.) for catering — *(P)*
- [ ] Ask organizer the open questions in `NOTES.md`: provided screen + connector (HDMI?), number of
      power sockets, guest Wi-Fi — *(P)*
- [ ] Confirm Service Center **poster print cost + lead time** → set the print deadline — *(P)*
- [ ] Report **PSP-number persons** by **Mon 6 July 2026**; log event hours by end July — *(P)*

## 1. Deploy & test the games (digital — only P can do) 🟢

Games live in the **Arraxis site**: `triangulo-site/frontend/nachtdertechnik/` (5 games + landing).
Leaderboard is built into the **Arraxis Flask backend** (`/api/ndt/scores`, same-origin — no separate
service, no `LB_API_BASE` to set). Reachable at **https://arraxis.com/nachtdertechnik/**.

- [ ] Review + commit the Arraxis edits (`backend/app.py`, `backend/database.py`, `frontend/nachtdertechnik/`) — *(P)*
- [ ] **Deploy** the site so `/nachtdertechnik/` is live over **HTTPS** (needed for the camera game) — *(P)*
- [ ] Test all 3 custom games on a real **iPhone (Safari) + Android (Chrome)**:
      Quanten-Elfmeter (buttons/swipe/motion, quantum shot, leaderboard), Schlag die KI, Hack the Light
      (camera permission + venue lighting + the no-camera demo fallback) — *(P+CL)*
- [ ] Confirm the **leaderboard** writes/reads across devices (boards: penalty, beat-ai, light) — *(P)*
- [ ] Check the external games are live + decide offline handling if no Wi-Fi: **q-chess.com**,
      **tiqtaqtoe.com** — *(P)*
- [ ] Edit the `PRIZES` list in `prize.html` to match the sweets actually in the box — *(P/AI)*
- [ ] Decide kiosk/fullscreen on the stand laptop/tablet so kids can't wander off the page — *(P)*

## 2. Physical / on-site 🟢

- [ ] **Print the poster** (`poster/Hack_the_Quantum_Poster_DE.pdf`, A1 portrait) via the Service
      Center — mind the lead time; make sure the site is deployed before the event so the QR works — *(P)*
- [ ] **Print the A3 sign** (`poster/A3_Anleitung_DE.pdf`) for the A3 stand — *(P)*
- [ ] **Buy sweets** for the "Quanten-Geschenk" box — *(P)*
- [ ] **Pack:** stand laptop + charger, a **tablet** for the camera game, phone/tablet **stand**,
      **HDMI cable** for the provided screen, power strip, tape, hand sanitiser/wipes — *(P)*
- [ ] Bring a printed copy of this TODO + the deploy URL — *(P)*
- [ ] **Setup rehearsal:** assemble the full stand once before the event — *(P+CL)*
- [ ] **Event day:** build 12:00–17:15 · staff 18:00–22:00 · teardown after 22:00 — *(P+CL)*

## 3. Optional fallback: Arduino physical demo ⚪

Not needed — everything runs without it. Bring only if we want a physical exhibit too.
Code drafted in `arduino/` + `software/quantum_ui/` (untested on hardware).

- [ ] (Optional) Flash the sketch, wire per the pin map, calibrate the 3 modes on Pavel's kit — *(P)*

## 4. Nice-to-have polish ⚪

- [ ] Sound on/off toggle in the games (optional) — *(AI)*
- [ ] Idle/attract animation on the stand screen — *(AI)*
- [ ] Bilingual (DE/EN) toggle — pending decision in `NOTES.md` — *(AI)*
- [ ] More backlog ideas in `docs/ideas-backlog.md`.

## Status snapshot

- ✅ Repo organized; concept + facts + notes committed.
- ✅ **5 web games built & themed to Arraxis**, in `triangulo-site/frontend/nachtdertechnik/`
  (Quanten-Elfmeter, Schlag die KI, Hack the Light, + links to Quanten-Schach & Tic-Tac-Toe), plus the
  `prize.html` Quanten-Geschenk draw.
- ✅ **Leaderboard** (best score + attempts) wired into the Arraxis Flask backend.
- ✅ **Tests pass:** 22 Node/jsdom + 6 pytest.
- ✅ **Poster** (`poster/Hack_the_Quantum_Poster_DE.pdf`) + **A3 sign** (`poster/A3_Anleitung_DE.pdf`),
  with real QR, game icons, quantum motifs, Arraxis + Quantum Lab logos, LinkedIn contact QRs.
- ⏭️ **Next:** deploy the Arraxis site (HTTPS) → test on phones → print poster + A3 → sweets + gear → rehearse.
