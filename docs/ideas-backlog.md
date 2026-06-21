# Ideas backlog, browser games & fallbacks

> Ranked by our prime directive: **minimal effort, maximal outcome.** 🟢 = high value / low effort,
> 🔵 = nice, ⚪ = stretch. Hardware ceiling = Arduino Starter Kit + a laptop + the provided screen.

## A. Free browser quantum games (PC corner) — zero build 🟢

Use one or two of these on the provided screen for 2-player play and to absorb the queue.
**Test offline first** — confirm each works without guest Wi-Fi (download/cache or run locally).

| Game | Why it fits | Link |
|---|---|---|
| **Quantum Tic-Tac-Toe** (everthemore / "TiqTaqToe") | Pavel's reference; "turn up the quantumness", 2-player, intuitive superposition | https://everthemore.itch.io/tiqtaqtoe · https://tiqtaqtoe.com/ |
| **Quantum Tic-Tac-Toe** (quantum-ttt.com) | Clean browser version, 2-player or vs AI; entanglement + measurement | https://quantum-ttt.com/ |
| **Quantum Tic-Tac-Toe** (V. Sánchez Muñoz) | Has an "instructor" mode with less text / more visuals — good for kids | https://vickynititi.itch.io/quantum-tic-tac-toe |
| **TiqTaqToe @ QPlayLearn** | Curated educational framing, age-friendly | https://qplaylearn.com/game-tiqtaqtoe |
| **Quantum Flytrap Virtual Lab / Photonic Trail** | Drag-and-drop photons, light → measurement; ties directly to our "light becomes a bit" story | https://qplaylearn.com (Photonic Trail) |
| **Awesome Quantum Games** (curated list) | Backup source if we want more options | https://github.com/HuangJunye/Awesome-Quantum-Games |

**Recommendation:** default to **one** Quantum Tic-Tac-Toe (2-player, low-text) as the headline
game, with the Quantum Flytrap photon lab as a "wow" demo a staffer drives. Don't overload the corner.

> ⚠️ Verify each link + offline behaviour during prep (TODO §2). Itch.io games may need a download
> to run offline. Have a fully-offline fallback ready (e.g. a downloaded HTML build).

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
