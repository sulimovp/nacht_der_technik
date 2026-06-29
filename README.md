# Nacht der Technik 2026 — Hack the Quantum

Interactive TechLab exhibit for **Nacht der Technik 2026** at ZHAW School of Engineering.
A child makes light on a sensor and tries to force the output to **0** or **1** — and discovers
that as the machine's rules get more complex, control fades from easy to impossible. That's the
hook for *why randomness matters for AI, security and quantum tech.* Motto: **Create Future!**

- **When:** Friday 3 July 2026, 18:00–23:00 (TechLab 18:00–22:00)
- **Where:** ZHAW SoE, building TP, ground floor — stand *InIT «Hack the Quantum»*, 3×2 m
- **Team:** Pavel Sulimov & Claude Lehmann (InIT)
- **Audience:** kids & teens, ages 6+, and a broad public

## Repo map

| Path | What |
|---|---|
| `CLAUDE.md` | Agent operating guide — read first if you're an AI working here |
| `NOTES.md` | Single source of truth: facts, decisions, open questions |
| `TODO.md` | Master checklist (owners + deadlines) |
| `docs/event-facts.md` | All facts from the factsheet / emails / floor plan |
| `docs/concept.md` | The exhibit concept |
| `docs/ideas-backlog.md` | Browser quantum games, polish, fallbacks, stretch ideas |
| `docs/poster-plan.md` | German poster content for the MINT template |
| `docs/guide/` | **Staff prep guide (EN+DE):** quantum basics, per-game principles/rules/scripts, cheat-sheet |
| `arduino/hack_the_quantum/` | UNO firmware — 3-mode light→bit encoder |
| `software/quantum_ui/` | Python screen UI (has a `--sim` mode to test without hardware) |
| `reference/organizer/` | Organizer factsheet + floor plan (source of truth) |
| `reference/poster_templates/` | ZHAW MINT `.potm` poster templates |

## Quick start

```bash
# test the screen UI without any hardware:
cd software/quantum_ui && pip install -r requirements.txt
python quantum_ui.py --sim --windowed     # keys: 1/2/3 level, 0/9 target, SPACE measure
```

Then flash `arduino/hack_the_quantum/hack_the_quantum.ino` to an Arduino UNO (Starter-Kit parts
only — see the pin map in the sketch header) and run `python quantum_ui.py`.

The next critical milestone is a working end-to-end Arduino→screen demo on real hardware — see
`TODO.md` §1.
