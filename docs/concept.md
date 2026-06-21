# Concept — Hack the Quantum: Wie aus Licht ein Bit wird

> The committed exhibit concept. Distilled from Pavel's original write-up and the submitted
> proposal, trimmed to what we can actually build with an Arduino Starter Kit + laptop + screen.

## One-sentence pitch

A child makes light on a sensor and tries to force the output to **0** or **1** — and discovers
that as the machine's hidden rules get more complex, control slips away until the outcome becomes
genuinely unpredictable. That's the doorway to *why randomness matters for AI, security and quantum tech*.

## The experience (30–90 s per child)

1. Child shines a phone flashlight / waves a hand / covers the **light sensor (LDR)**.
2. A big **0/1** and a live signal bar show on the screen (and an RGB LED + a beep give instant feedback).
3. Child picks a target ("make a 1") and gets 10 tries per level.
4. Three levels, each harder to control. The **visible drop in their success rate is the whole point.**

## The three encoding modes

| Level | Name | Rule (kid-facing words) | Colour | Typical success |
|---|---|---|---|---|
| 1 | **Deterministic** | "Bright = 1, dark = 0." Direct, obvious control. | 🟢 Green | 8–10 / 10 |
| 2 | **Hidden rule (Parity)** | Only a hidden detail of the signal counts, so big changes may do nothing. | 🟡 Yellow | ~5–7 / 10 |
| 3 | **Quantum-like (Noise mixing)** | The machine mixes tiny, uncontrollable flickers — even steady light gives random results. | 🔵 Blue | ~50 / 50 |

- Level 1 = threshold: `bit = signal > threshold`.
- Level 2 = parity: `bit = signal & 1` (least-significant bit; magnitude barely matters).
- Level 3 = entropy: XOR many fast LSB samples, with optional Von Neumann debiasing →
  practically uncontrollable. **Honesty note for staff:** this is a *physical-noise* entropy
  source used as an analogy, **not** a true quantum RNG. Say "quantum-like" to guests.

## What it teaches (without any maths)

- Simple rules → you can control the system.
- Encoding can hide structure → magnitude isn't everything.
- Mixing enough noise → effectively unpredictable.
- Some processes (real quantum physics) are *fundamentally* unpredictable.
- Randomness is a building block for AI, cryptography and quantum computing → "Create Future".

## Age-adaptive one-liners (for staff + poster)

- **6–8:** "First you control the machine. Then it gets sneaky. Then nature wins."
- **9–12:** "Some rules are simple. Some hide information. Some things just can't be predicted."
- **13–15:** "AI finds patterns in data. If there's no pattern, prediction fails — that's where quantum randomness lives."

## Two stations on the 3×2 m stand

1. **Arduino station** (the hero): LDR sensor, RGB LED, piezo, two buttons, laptop driving the screen UI.
2. **PC / screen corner:** free browser quantum games for 2-player / waiting guests
   (e.g. Quantum Tic-Tac-Toe). Zero build. See `docs/ideas-backlog.md` for the vetted list.

## Hardware — all from the Arduino Starter Kit

| Part | Role | In Starter Kit? |
|---|---|---|
| Arduino UNO R3 | brain, reads sensor, drives feedback | ✅ |
| Photoresistor (LDR) + 10 kΩ resistor | the light sensor (voltage divider) | ✅ |
| RGB LED (+ 220 Ω resistors) | colour feedback + mode colour | ✅ |
| Piezo buzzer | correct/incorrect beeps | ✅ |
| 2× pushbutton | choose target bit / confirm | ✅ |
| Breadboard + jumper wires | wiring | ✅ |
| Laptop (Pavel's) | runs Python UI, drives the screen | own |

Nothing here needs buying. The clever, cheap trick is using **LDR analog noise as the entropy
source** in Level 3 — no extra hardware for "quantum-like" randomness.

## Software

- **Arduino firmware** (`arduino/hack_the_quantum/`): reads LDR, runs the 3 modes, sends bits over
  serial, drives LED + buzzer.
- **Python screen UI** (`software/quantum_ui/`): reads serial, shows the big 0/1, live bar, current
  rule, score per level, and the final "control dropping" summary screen.

## Success criteria for the night

- A child can complete all 3 levels in under ~2 minutes and *get* the "I lost control" moment.
- The stand runs unattended-ish: robust to abuse, recovers from unplugging, no laptop babysitting.
- A second, no-Arduino activity (browser game) absorbs the queue.
