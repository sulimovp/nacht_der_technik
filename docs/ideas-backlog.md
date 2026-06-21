# Ideas backlog, browser games & fallbacks

> Ranked by our prime directive: **minimal effort, maximal outcome.** 🟢 = high value / low effort,
> 🔵 = nice, ⚪ = stretch. Hardware ceiling = Arduino Starter Kit + a laptop + the provided screen.

## A. Quantum games for the screen corner — curated catalog 🟢

A broader, vetted shortlist drawn from the **Awesome Quantum Games** master list
(https://github.com/HuangJunye/Awesome-Quantum-Games) — not just Tic-Tac-Toe. Tagged by
audience and whether it's truly **browser-ready** (drop-in) vs **needs a build/download**.
**Golden rule: test every pick live AND offline during prep** (TODO §2). Many quantum games are
hackathon prototypes — links rot, and some old hosts (e.g. IBM Bluemix) are retired.

### A1. Top picks — on-theme, browser, drop-in 🟢

| Game | Audience | Why it's a top pick | Link |
|---|---|---|---|
| **Quantum Game / Virtual Lab** (Quantum Flytrap, P. Migdał et al.) | all ages, staff-driven | **Our single best thematic match** — drag lasers/photons, see superposition & **measurement** of light. It *is* the "light becomes information" idea our Arduino station teaches. Real QM underneath. | https://quantumgame.io · https://lab.quantumflytrap.com |
| **Quantum Tic-Tac-Toe** | 8+, 2-player | Easy pick-up-and-play; superposition + collapse with almost no text. Our default 2-player game. | https://tiqtaqtoe.com · https://quantum-ttt.com · https://vickynititi.itch.io/quantum-tic-tac-toe |
| **Quantum Moves 2** (ScienceAtHome) | all ages | "Slosh" a quantum atom into place — pure visual intuition, no reading needed, satisfying in 30 s. Citizen-science pedigree. | https://www.scienceathome.org/games/quantum-moves-2/ |

### A2. For older kids, teens, parents & the chess crowd 🔵

| Game | Notes | Link |
|---|---|---|
| **Q-Chess — quantum chess online** | Browser, play a "Baby Robot" or a human, no install. Split/merge moves put a piece in **superposition** across squares until observed. Longer per turn → best for teens/adults, not 6-year-olds. | https://q-chess.com |
| **Quantum Chess** (C. Cantwell — the Paul Rudd vs Hawking one) | The famous polished version, but it's a **paid desktop game (Steam)**, not browser. Reference/“did you know” talking point, not a stand activity. | https://store.steampowered.com/app/453870/ |
| **Hello Quantum** (IBM) | Qubit-logic puzzle. ⚠️ Original Bluemix host is likely **dead** — verify a working mirror before relying on it. | (search “Hello Quantum IBM” for current host) |

### A3. Younger kids & “true randomness” tie-ins 🔵

| Game / app | Notes | Link |
|---|---|---|
| **Quantum Cats** (IQC, U. Waterloo) | Kid-friendly “rescue the kittens with spooky quantum laws.” Verify it still runs in-browser. | http://quantumcats.ca |
| **Universe Splitter** | Uses a **real** quantum device (single-photon split) to make a decision — a lovely, honest demo of *genuine* quantum randomness vs our *simulated* Level-3 noise. Phone app, not browser; could run on a staffer’s phone. | http://cheapuniverses.com/universesplitter/ |
| **Quantum Grove** (browser) | Ambient, browser-playable art piece — better as an **idle/attract visual** on the screen than an active game. | https://quantum-kittens.itch.io/quantum-grove |

### A4. Fun but **needs a build/download** — only if we want to invest ⚪

From the Awesome list, mostly GitHub/itch hackathon projects (not drop-in browser): **QPong**
(quantum Pong), **Quantum Cat-sweeper** (Minesweeper), **Schrödinger's Cat** (superposition/gates),
**Quantum Othello**, **QTetris**, **FlappyQat**, **Hunt the Quantpus**. Treat as stretch — each needs
setup/testing we probably can't justify for a 4-hour stand.

### Recommendation (don't overload the corner)

Run **two** things on the screen: the **Quantum Flytrap photon game** as the headline — because it
literally mirrors our Arduino "light → bit → measurement" story — and **Quantum Tic-Tac-Toe** as the
easy 2-player pick-up game. Keep **Q-Chess** bookmarked for chess-savvy older visitors, and have the
**Universe Splitter** phone app ready as the "this one uses a *real* quantum device" punchline that
ties straight into our honesty note (our Level 3 is an analogy, not a true quantum RNG).

> ⚠️ Verify each link is **live + works offline** during prep (TODO §2). Have a fully-offline
> fallback ready (a downloaded HTML build of Tic-Tac-Toe) in case there's no guest Wi-Fi.

## B. Engagement polish for the Arduino demo 🔵

- **Streak / high-score** display ("longest controlled streak") — kids queue to beat it.
- **Attract / idle animation** on the screen so the stand pulls people in when empty.
- **Sound toggle** — a piezo beeping for 4 hours is rough; let staff mute it.
- **Big colour-coded mode banner** (🟢🟡🔵) so a passer-by reads the story in 2 seconds.
- **Takeaway slip:** print "your personal quantum-random number: 0110…" — cheap, memorable, on-brand.

## C. Concept extensions (only if time) ⚪

From Pavel's original write-up — keep as stretch, none are needed for a great stand:

- **Multi-sensor entropy:** mix light + temperature + tilt for Level 3 (more "real" entropy).
  *Cost:* needs sensors possibly beyond the Starter Kit — check before committing.
- **Human vs AI prediction:** a simple model tries to predict the child's next bit; show it
  succeeding in Level 1 and failing in Level 3. Strong "AI needs patterns" message.
- **Live entropy meter:** a bar showing how unpredictable the stream is, rising across levels.
- **Two-player competitive Arduino mode:** two sensors, race to force a target bit.
- **Integration into a broader "Quantum Games Lab"** theme for future events.

## D. Fallbacks & risk busters 🟢

Plan for things going wrong at a loud, crowded, kids-everywhere event:

- **Arduino dies / flakes out:** have the **browser games** ready as the primary activity, plus a
  printed "paper version" of the 3 modes (a flip card: bright=1 → hidden rule → coin-flip).
- **No guest Wi-Fi:** pre-download all games to run locally/offline.
- **Laptop issues:** the Arduino can give standalone feedback via the RGB LED + piezo even with no
  screen (firmware works without the Python UI). Keep that path working.
- **Sensor drift as room light changes** (evening → dark): include an **auto-calibration** button
  and re-run it a few times during the night.
- **Spare parts:** bring a 2nd LDR, RGB LED, buttons and jumper wires — they're cheap and they fail.

## E. Explicitly out of scope (to protect the prime directive)

- No custom PCB, no 3D printing, no soldering beyond breadboard.
- No real quantum hardware / cloud QPU (overkill, fragile, not kid-legible).
- No app install for guests; everything runs on our screen.
