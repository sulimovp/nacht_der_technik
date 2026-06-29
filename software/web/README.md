# Hack the Quantum — web games

Three self-contained, mobile-first web pages (no backend, no build step). Designed to be opened
on visitors' **own phones** via a QR code on the poster, and to run offline on the stand laptop.

| File | What it is | Needs |
|---|---|---|
| `index.html` | Landing page (German). QR target. Links to all four activities. | nothing |
| `beat-the-ai.html` | **Schlag die KI** — tap/swipe 0/1; an in-page predictor (Aaronson-style oracle) guesses your next move and usually wins. Teaches: humans are predictable, only true randomness beats prediction. | nothing |
| `hack-the-light.html` | **Hack the Light** — the phone camera turns light into a bit through 3 modes (control → hidden rule → random). The no-Arduino version of the original experiment. | **camera + HTTPS** |

External games linked from the landing page: **Quanten-Schach** (q-chess.com) and
**Quanten-Tic-Tac-Toe** (tiqtaqtoe.com).

## Run locally (to test)

```bash
cd software/web
python3 -m http.server 8000
# open http://localhost:8000/  (camera works on localhost without HTTPS)
```

## Deploy to arraxis.com (or any static host)

Just upload the four files (`index.html`, `beat-the-ai.html`, `hack-the-light.html`, plus this
README is optional) to a folder, e.g. `https://arraxis.com/quantum/`. No server code needed.

**Important — the camera game needs HTTPS.** `getUserMedia` only works on `https://` (or
`localhost`). arraxis.com must serve the page over HTTPS, otherwise `hack-the-light.html` falls
back to its built-in **"Demo ohne Kamera"** mode (still playable, just simulated light).

## QR code for the poster

Point the poster's QR at the deployed landing page, e.g. `https://arraxis.com/quantum/`.
Generate the QR with any tool (e.g. a CLI: `qrencode -o quantum-qr.png "https://arraxis.com/quantum/"`,
or any web QR generator) and drop it into the poster's QR circle.

## Notes / robustness

- All pages are German, mobile-first, big touch targets, work in portrait.
- `beat-the-ai.html` also accepts **arrow keys** and **swipes** — good for a touchscreen or the
  stand laptop. Personal best is stored in `localStorage`.
- `hack-the-light.html` requests the **rear** camera; if denied/unavailable it offers a demo mode,
  so the stand never has a dead screen.
- Honesty note (for staff, not on screen): the camera "Zufall" mode uses real image-sensor noise —
  a genuine physical entropy source, but an *analogy* to quantum randomness, not a true quantum RNG.
- Test on a few real phones before the event (iOS Safari + Android Chrome), and confirm camera
  permission + HTTPS on arraxis.com.
