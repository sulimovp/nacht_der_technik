# Per-game guide — staff handbook (English)

> For each game: the **principle**, the **real science**, **analogy vs. real**, the **rules**, how to
> **explain it by age**, **sample dialogue**, and **FAQs**. German: `DE_spiele-anleitung.md`.
> Background concepts: `EN_quantum-basics.md`. Quick reference: `EN_cheatsheet.md`.

The stand has **five** games. Three are ours (web apps at `arraxis.com/nachtdertechnik`):
**Hack the Light**, **Beat the AI**, **Quantum Penalty**. Two are external browser games:
**Quantum Chess** (q-chess.com) and **Quantum Tic-Tac-Toe** (tiqtaqtoe.com). Plus a staff-run
**Quantum gift** draw.

The whole stand tells **one story**: *some things you can control, some you can't — and the deepest
unpredictability (quantum randomness) is a powerful resource for the future.*

---

## 1. Hack the Light — "make light into a bit"

**Hook:** Shine light on the camera and try to force the result to be 0 or 1.

**Principle illustrated:** how a physical signal becomes digital information, and how randomness can be
**extracted from physical noise** — the everyday cousin of a quantum random-number generator.

**The real science:** A light sensor turns brightness into a number. Three "encoders" turn that number
into a bit:
- **Mode 1 – Bright/Dark (deterministic):** `bit = 1 if bright, else 0`. Total control.
- **Mode 2 – Hidden rule (parity):** only the *least significant* detail of the brightness counts, so
  big changes often don't flip the bit. Control becomes unreliable.
- **Mode 3 – Randomness:** the app mixes the **tiny flickering noise** of the camera sensor (thermal &
  shot noise) from many pixels and XORs it together. Even with perfectly steady light the output is
  ~50/50 and practically uncontrollable.

**Analogy vs. real:** Mode 3 is a *physical* entropy source — genuine, but from electronics, **not**
single photons. It's an honest analogy for a quantum RNG, which does the same trick with one photon at
a half-silvered mirror. Say "quantum-*like*" to guests.

**Rules / how to play:**
1. Pick a target (0 or 1).
2. Use the phone camera: cover it, shine a light, move your hand — try to force your target.
3. 10 tries per mode. Watch your success rate **drop** from Mode 1 → 2 → 3.
4. A "Licht-Score" (Modes 1+2) goes on the leaderboard.

**Explain it by age:**
- **6–8:** "Bright makes a 1, dark makes a 0 — you're the boss! Now the machine gets sneaky… now it
  rolls a dice you can't win."
- **9–12:** "First the rule is simple. Then the rule hides — only a tiny detail matters. Then the
  machine uses its own tiny noise, so nobody can steer it."
- **13+:** "This is entropy extraction: we harvest unpredictable physical noise to make random bits.
  Real quantum generators do the same with single photons — the basis of secure keys."

**Sample dialogue:** "Try to make a 1 — easy, right? Now switch to the blue mode and try again…
frustrating? That's the point: some randomness can't be cheated. That's gold for cybersecurity."

**FAQ:**
- *"Is this real quantum?"* → "It's real *physical* randomness from the camera's noise — a great
  stand-in. True quantum generators use single photons; same idea, deeper down."
- *"Why won't it obey me in blue mode?"* → "Because it's reading noise you can't control — that's what
  makes it trustworthy randomness."

**Tips:** Needs camera permission + HTTPS; if blocked it runs a "Demo ohne Kamera" mode. It
auto-calibrates to room light at start. Works best when the camera can see a light source.

---

## 2. Beat the AI — "be more random than a machine"

**Hook:** Tap left/right however you like; an AI tries to predict your next move — and usually wins.

**Principle illustrated:** **humans are terrible at being random**; AI is a pattern-finder; only *true*
randomness defeats prediction. This is the bridge from "why randomness matters" to "why we want
**quantum** randomness."

**The real science:** The predictor is an "Aaronson oracle" — it remembers short sequences of your
recent taps and bets you'll repeat your habits (we avoid repeats, we alternate, we fear long runs). On
patterned humans it scores ~80–99%; on truly random input it drops to ~50% (chance). No quantum
hardware — it's a neat AI/cognitive-science demo that *motivates* quantum randomness.

**Analogy vs. real:** This is **not** a quantum game; it's the "why" behind quantum randomness. The
honest tie-in: "to beat this AI you'd need a perfect coin — and the most perfect coins in nature are
quantum."

**Rules / how to play:**
1. 25 rounds. Each round tap **LINKS** or **RECHTS** (also swipe / arrow keys).
2. You score when the AI guesses **wrong** (you fooled it); the AI scores when it's right.
3. Final tally + leaderboard (your "wins").

**Explain it by age:**
- **6–8:** "Try to surprise the robot! It's reading your mind. Can you be tricky?"
- **9–12:** "The computer learns your habits in seconds. To win you must be truly random — and that's
  really hard for people."
- **13+:** "It's a Markov predictor. Humans leak patterns, so AI wins. Cryptography needs randomness no
  AI can predict — which is why quantum RNGs exist."

**Sample dialogue:** "Bet you can't beat the AI… see? It caught your pattern. Funny thing: the only way
to win is to be perfectly random, and humans basically can't. That's why computers — and especially
quantum physics — make the random numbers that protect your passwords."

**FAQ:**
- *"Is it reading my mind?"* → "Just your habits — it remembers your last few moves."
- *"How do I win?"* → "Be unpredictable. Some people imagine flipping a coin in their head. Even then
  it's hard!"

**Tips:** Great for a queue / competition. If a kid is frustrated, point out that *losing* is the
lesson and almost everyone loses.

---

## 3. Quantum Penalty — superposition takes a shot

**Hook:** Score against a goalkeeper who reads your mind — or take a **quantum shot** that's in two
corners at once.

**Principle illustrated:** **superposition** and **measurement/collapse**, combined with the
predictability lesson. The keeper is the same pattern-reading AI; the **quantum shot** puts the ball in
a superposition of two corners until the "measurement" collapses it.

**The real science:**
- **Normal shot:** you pick Left/Centre/Right; the AI keeper predicts you and dives. Predictable
  shooters get saved.
- **Quantum shot:** the ball is in a **superposition** of Left **and** Right. The keeper can cover only
  one place. At the **moment of impact (measurement)** the ball **collapses** randomly (true 50/50) to
  one corner. If the keeper dived to the *other* wing — or to the centre — it's a goal.

**Analogy vs. real:** Quantum-*inspired*. The superposition and random collapse are faithful to how a
qubit behaves on measurement; the implementation is ordinary code + a cryptographic coin flip, not
quantum hardware.

**Rules / how to play:**
1. 10 penalties. Choose **Links / Mitte / Rechts** (buttons, swipe, or the on/off **motion** toggle —
   flick the phone).
2. Or hit **Quantenschuss**: ball superposed Left+Right, collapses 50/50.
3. Goals go on the leaderboard. 8+ goals → a "Quanten-Geschenk" prompt.

**Explain it by age:**
- **6–8:** "The goalie guesses where you'll shoot! But the magic ball goes BOTH ways at once — he can't
  catch both."
- **9–12:** "A good keeper reads your pattern. The quantum shot is in two corners at the same time —
  only when the ball arrives does it 'decide' which corner, totally at random."
- **13+:** "The quantum shot is a superposition of two states; the keeper is a which-path detector;
  impact is the measurement that collapses it 50/50. Predictability vs. genuine randomness, on a pitch."

**Sample dialogue:** "Shoot normally a few times… the keeper's learning you, right? Now try the quantum
shot — the ball is in two corners at once, and only 'decides' when it arrives. The keeper can't read
what hasn't been decided yet."

**FAQ:**
- *"Is the ball really in two places?"* → "In the game it represents a qubit's superposition — two
  possibilities at once until measured. Real particles genuinely do this."
- *"Why did my quantum shot still get saved?"* → "It collapses 50/50 — if the keeper happened to dive
  to that wing, bad luck. Quantum guarantees *unpredictability*, not always winning."

**Tips:** The motion control is a clear ON/OFF toggle — turn it off if a kid finds it fiddly; buttons
and swipe always work.

---

## 4. Quantum Chess (q-chess.com) — superposition & entanglement on a board

**Hook:** Normal chess, but pieces can be in **two squares at once** and become **entangled**.

**Principle illustrated:** **superposition** (a "split" move puts one piece on two squares),
**entanglement** (linked pieces), and **measurement** (a capture/collision forces reality to "pick").

**The real science (as a faithful metaphor):**
- A **split move** sends a piece to two destinations simultaneously — it now exists in superposition
  across both squares, each with some probability.
- Pieces can become **entangled**, so resolving one affects the other.
- A **measurement** (e.g. trying a capture) **collapses** the superposition: the piece turns out to be
  really on one square, and the other possibility vanishes.

**Analogy vs. real:** A quantum-*inspired* board game — excellent for *teens/adults/chess players*. Not
quantum hardware. Best run by a staffer or for two confident players; it's deeper than Tic-Tac-Toe.

**Rules / how to play (q-chess.com):** Standard chess plus "split"/"merge" moves that create
superpositions; when a move would require a definite answer (a capture, a check), the relevant pieces
are **measured** and the position collapses. Let players experiment — a couple of split moves makes the
idea click. Play vs. the "Baby Robot" or two players.

**Explain it by age:**
- **6–8:** (probably too complex) "These chess pieces can be ghosts in two squares — watch them turn
  real when they bump." Keep it short; steer younger kids to Tic-Tac-Toe.
- **9–12:** "Your knight can jump to two squares at once and stay 'maybe-here, maybe-there' until
  someone checks — then it has to pick one."
- **13+:** "Split = create a superposition across squares; captures/checks act as measurements that
  collapse it; pieces can entangle. It's chess with the three core quantum rules."

**FAQ:**
- *"How can a piece be in two places?"* → "Same as a qubit: a blend of possibilities until something
  forces a definite answer."

**Tips:** This is the "wow, that's deep" station for older visitors. Keep a 1-line rule summary handy.

---

## 5. Quantum Tic-Tac-Toe (tiqtaqtoe.com) — superposition you can grasp in 30 seconds

**Hook:** Three-in-a-row, but your mark goes in **two cells at once**, and marks get **entangled** and
**collapse**.

**Principle illustrated:** the *easiest* hands-on demo of **superposition**, **entanglement** and
**measurement** — perfect for kids and families.

**The real science (as a faithful metaphor):**
- A **quantum mark** is placed in **two cells at once** (superposition), labelled with the move number.
- When marks form a **loop** of shared cells (entanglement), a **measurement** happens: the loop
  **collapses** and each ghost mark becomes real in exactly one cell.
- Then you check for three-in-a-row as usual.

**Analogy vs. real:** Quantum-*inspired*, 2-player, very low text. The single best family game on the
stand for *feeling* superposition and collapse.

**Rules / how to play (tiqtaqtoe.com):**
1. On your turn you place your symbol in **two** empty cells (a "spooky" mark in superposition).
2. When the entangled marks form a closed loop, a **collapse** occurs and each mark settles into one
   real cell.
3. First to a real three-in-a-row wins. (The site has an "instructor" mode with less text for kids.)

**Explain it by age:**
- **6–8:** "Put your X in TWO boxes at once — it's a ghost! When the ghosts get tangled, they pop into
  one real box."
- **9–12:** "Each move lives in two boxes at the same time. When they form a loop they're 'entangled'
  and have to choose — that choosing is a measurement."
- **13+:** "Superposition (mark in two cells), entanglement (a cyclic dependency), and collapse
  (measurement resolves the cycle). Tic-Tac-Toe is just the scaffolding."

**Sample dialogue:** "Your X goes in two squares at once — it's in superposition. See how it links with
mine? When the links make a loop, everything 'collapses' and each X or O lands in one real square. That
loop is entanglement; the collapse is a measurement."

**FAQ:**
- *"Why did my mark jump?"* → "It was in two cells until the collapse forced it into one — exactly like
  measuring a quantum particle."

**Tips:** Default 2-player game for the screen corner; pair it with the simple verbal script above.

---

## The quantum gift (staff-run) — true-random reward

A `prize.html` page draws a winner using the browser's cryptographic randomness (a stand-in for a
quantum draw). Use it for top leaderboard players: open the page, let them press the button, and hand
out the sweet the "Quanten-Zufall" picks. Ties the whole randomness theme together with a treat.

---

## Running the stand — practical flow

1. **Greet:** "Want to try to beat a quantum machine?"
2. **Hook with one game** (Beat the AI or Penalty are fastest).
3. **Land the lesson:** point out control vs. no-control.
4. **Bridge:** "That unpredictability is what keeps your data safe and powers future computers."
5. **Offer the others** + the leaderboard + a chance at the Quanten-Geschenk.
6. Keep each turn **30–90 s**; the queue is absorbed by phones (everyone can play their own).
