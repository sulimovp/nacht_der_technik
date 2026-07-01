# Operating manual — running the stand, game by game

> The hands-on runbook: exact setup, step-by-step run flow, **verbatim staff lines** (the German is
> what you say to kids; English notes are for you), troubleshooting, and reset/admin. Pair with the
> concepts in `EN_quantum-basics.md` / `DE_quanten-grundlagen.md` and the quick `*_cheatsheet`.

Everything lives at **https://arraxis.com/nachtdertechnik/**. Games: Quanten-Elfmeter, Schlag die KI,
Hack the Light (ours) + Quanten-Schach and Quanten-Tic-Tac-Toe (external) + the Quantum-World slider
and the Quanten-Geschenk prize page.

---

## 0. Before the event (once)

1. **Deploy** the Arraxis site so `/nachtdertechnik/` is live over **HTTPS** (camera game needs it).
2. On every stand device, open `https://arraxis.com/nachtdertechnik/` and confirm:
   - all six tiles open; the games run; the leaderboard shows and updates.
   - the camera game asks for camera permission and, if denied, offers "Demo ohne Kamera".
3. **Print** the poster (A1) + the A3 sign; put the A3 QR where kids can scan it.
4. Fill the **prize box** with Lindt Lindor (Milch/Dunkel/Weiss/Haselnuss). The prize page draws a flavour.
5. Decide devices: 1 laptop/tablet per game station is ideal; kids also play on **their own phones** via the QR.
6. Do a **full dry-run**: play each game to the end on a real iPhone + Android; earn a gift; reset via admin.

**Reset before doors open:** Admin → "Nacht der Technik" panel → **Alles zurücksetzen** (clears scores + gifts).

---

## 1. Quanten-Elfmeter (`quantum-penalty.html`)

**Goal it teaches:** superposition (the quantum shot) + "you can't beat a mind-reader unless you're random."
**Devices:** phone or tablet (portrait). Works with buttons, swipe, or phone motion.

**Run flow**
1. Setup screen appears: kid **picks a team** (flag) and a **role** — ⚽ *Schiessen* (shoot) or 🧤 *Halten* (save) — and can type a name. Tap **Los geht's!**
2. **Shoot mode:** 10 penalties. Kid picks Links / Mitte / Rechts (button, swipe, or tilt+shake). The AI keeper predicts them. Or tap **⚛ Quantenschuss** (ball in two corners at once, collapses 50/50).
3. **Save mode:** kid is the keeper; picks a corner to dive; the AI shoots at random. Count the saves.
4. End screen: score → leaderboard (medals for top-3) → if a gift is unlocked, a 🎁 button appears.

**What you say (DE to the kid):**
- "Wähle dein Team und ob du **schiessen** oder **halten** willst."
- Shoot: "Der Torhüter liest dein Muster – sei unberechenbar! Oder nimm den **Quantenschuss**: der Ball ist in **zwei Ecken gleichzeitig**, der Torhüter kann nur eine halten."
- Save: "Jetzt bist **du** im Tor. Der Schütze schiesst zufällig – kannst du es erraten? … Schwer, oder? Gegen echten Zufall gewinnt niemand immer."

**Motion control:** tap **📱 Bewegung: Aus → Ein**. Tilt the phone to aim (the target button lights up; **flat = Mitte**), then **shake** to shoot. Tap again to turn it off. If a kid struggles, just use the buttons.

**Troubleshooting**
- Motion does nothing on iPhone → it needs the one-time permission prompt after tapping the toggle; if declined, use buttons.
- Ball/keeper look cramped → it's responsive; fine on phones. On a big screen it's just larger.

---

## 2. Schlag die KI (`beat-the-ai.html`)

**Goal it teaches:** humans can't be random; AI finds patterns; that's *why* we want quantum randomness.
**Devices:** anything; tap/swipe/arrow keys.

**Run flow**
1. 25 rounds. Kid taps **LINKS** or **RECHTS** each round.
2. Kid scores when the AI guesses **wrong**; AI scores when right.
3. End → leaderboard + possible gift.

**What you say (DE):**
- "Tippe links oder rechts, wie du willst. Die KI versucht, deinen nächsten Tipp zu erraten."
- After: "Siehst du? Sie hat dein Muster geknackt. **Nur echter Zufall** schlägt die KI – und den liefert die Physik, sogar die Quanten-Physik."

**Note:** almost everyone loses — that *is* the lesson. Frame losing as the point.

---

## 3. Hack the Light (`hack-the-light.html`)

**Goal it teaches:** light → a bit; control fades from steerable → hidden rule → pure randomness.
**Devices:** phone/tablet **with camera** (HTTPS). Falls back to a no-camera demo.

**Run flow**
1. On start it **auto-calibrates** to room light (~1 s).
2. Kid picks a goal: **Mach eine 0** / **Mach eine 1**. The tip shows the relationship ("heller = eher 1").
3. Three modes (tabs): **Hell/Dunkel** (steerable) → **Versteckte Regel** (tricky) → **Zufall** (uncontrollable). 10 tries each.
4. Tap **🏆 Licht-Score & Bestenliste** to submit (modes 1+2) and see the board + possible gift.

**What you say (DE):**
- "Mach eine 1 – halte die Kamera ins Licht. Einfach, oder? **Heller = eher 1.**"
- Switch to blue mode: "Jetzt mischt die Kamera ihr eigenes **Rauschen** – jetzt kannst du **nicht** mehr steuern. Genau solchen echten Zufall braucht die Technik für Sicherheit."

**Troubleshooting**
- No camera / black preview → tap "Demo ohne Kamera"; it simulates light so the lesson still works.
- Mode 1 feels off in a very dark/bright corner → it re-calibrates on load; reload the page to recalibrate.

---

## 4. Quanten-Schach (q-chess.com) — external, for older visitors

**Run flow:** open q-chess.com; play "Baby Robot" or two players. A **split move** puts a piece in two
squares (superposition); captures/checks **measure** and collapse it; pieces can **entangle**.
**What you say (DE, 9+):** "Deine Figur kann in **zwei Feldern gleichzeitig** sein, bis jemand nachschaut –
dann muss sie sich für eines entscheiden." Steer under-8s to Tic-Tac-Toe instead.

## 5. Quanten-Tic-Tac-Toe (tiqtaqtoe.com) — external, best for families

**Run flow:** each move places your mark in **two cells at once**; when marks form a loop they **collapse**
into real cells; first real three-in-a-row wins. Use the site's low-text "instructor" mode for kids.
**What you say (DE):** "Setz dein X in **zwei Kästchen zugleich** – ein Geist! Wenn sich die Geister
verheddern, springen sie in ein echtes Kästchen. Das ist **Verschränkung** und **Messung**."

## 6. Die Quantenwelt (`quantum-world.html`) — the explainer slider

Nine slides with animations: quantum world → Bausteine → Photonen → Überlagerung → Messung → Zufall →
Verschränkung → Qubits → warum wichtig. **Weiter/Zurück** buttons, swipe, or arrow keys; **⛶ Vollbild**
for a screen. Great for waiting kids or a curious parent; end slide links back to the games.

---

## 7. Leaderboard & Quanten-Geschenk (how the sweets work)

**The rule (built in):** a device earns **1 Lindor the first time it plays any game**, and **1 more for
reaching the top-3** of any game. **Max 2 per device.** Each is claimable once; after claiming it's marked
redeemed, so re-entering the top-3 later does **not** give another.

- **Medals:** top-3 rows show 🥇🥈🥉 and gold/silver/bronze tint. **Ties** break by fewer attempts, then earlier time.
- **Empty board:** the first player is automatically top-3, so they qualify.
- **How a kid claims:** at a game's end screen a 🎁 "Du hast ein Quanten-Geschenk frei!" button appears →
  it opens the prize page → they press **Zufall messen** → a random Lindor flavour is drawn → **hand them
  that flavour** from the box. If they have two entitlements, the page lets them draw again.
- **No button?** They've already used their 2, or aren't in the top-3 yet — that's correct behaviour.

**What you say (DE):** "Top 3! Tipp auf **Quanten-Geschenk**, drück den Knopf – der **Zufall** wählt deine
Lindor. Nimm die, die erscheint, aus der Box."

**Material budget:** with max 2 per device the box lasts; if it runs low, tell the team to switch the rule
to "Top-3 only" (ask the developer to flip it) or simply hand out the on-screen result while stock lasts.

---

## 8. Admin — reset & manage (arraxis.com/admin)

1. Go to **/admin**, log in.
2. The **"Nacht der Technik — Leaderboard & Geschenke"** panel is at the top. Click **Aktualisieren** to load.
3. You see every entry per board + a count of redeemed gifts. **✕** deletes a single entry.
4. Buttons: **Scores löschen** (clear leaderboards), **Geschenke zurücksetzen** (let devices earn again),
   **Alles zurücksetzen** (both). Each asks to confirm.
5. **Do "Alles zurücksetzen" before doors open** (clears any test data) and optionally at the start of a new night.

---

## 9. Language (site chrome)

The main Arraxis site now offers **Deutsch** in the language switcher (🇩🇪) alongside English/Español. The
navigation, footer and homepage hero are translated; deeper marketing/story pages currently fall back to
English until more of `backend/translations/de.json` is filled in. The **games** at `/nachtdertechnik/` are
German throughout.

---

## 10. Troubleshooting matrix

| Symptom | Fix |
|---|---|
| A game page is blank/half-loaded | Reload. Check the site is deployed over HTTPS. |
| Camera game shows black / no permission | Grant camera permission, or use "Demo ohne Kamera". Keep a **tablet** you control as the camera station. |
| Leaderboard not updating across phones | Needs internet to reach the API; if offline it shows a **local** board only. Check Wi-Fi / cellular. |
| No 🎁 button after a good game | Device already claimed its 2 gifts, or not top-3 yet. Correct behaviour. Verify in admin. |
| Motion/tilt not working (penalty) | iOS needs the permission prompt after tapping the toggle; otherwise use buttons. |
| Someone gamed the board with silly names | Delete the entry via admin (✕) or reset scores. |
| External game (chess/ttt) won't load | Needs internet. Have it bookmarked; if the venue Wi-Fi is down, focus on our three games. |

---

## 11. Close-down

- Optional: screenshot the final leaderboard for fun/records.
- **Alles zurücksetzen** in admin if you don't want to keep the data.
- Pack devices, cables, the prize box, the poster + A3 sign.
