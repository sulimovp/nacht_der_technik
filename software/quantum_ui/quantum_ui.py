#!/usr/bin/env python3
"""
Hack the Quantum — screen UI for the Nacht der Technik 2026 TechLab stand.

Reads the Arduino over USB serial and shows a big, kid-friendly display:
the live light signal, the current rule (colour-coded), a giant 0/1, the target,
and the per-level score. The point kids should feel: control drops from
Level 1 (green, easy) -> Level 2 (yellow, sneaky) -> Level 3 (blue, random).

Run with hardware:   python quantum_ui.py --port COM5          (Windows)
                     python quantum_ui.py --port /dev/ttyACM0  (Linux/Mac)
Auto-detect port:    python quantum_ui.py
Test with NO Arduino:python quantum_ui.py --sim     (keys 1/2/3 set level, SPACE = measure)

Keys (always): 1/2/3 = level, 0/9 = target 0/1, SPACE = measure(G), c = calibrate,
               m = mute sound, ESC = quit.
Protocol matches arduino/hack_the_quantum/hack_the_quantum.ino.
"""
import argparse
import random
import sys
import time

import pygame

try:
    import serial
    import serial.tools.list_ports
    HAVE_SERIAL = True
except ImportError:
    HAVE_SERIAL = False

# ---- look & feel ------------------------------------------------------------
BG        = (12, 14, 22)
FG        = (235, 238, 245)
DIM       = (120, 128, 140)
LEVEL_COL = {1: (40, 200, 90), 2: (235, 195, 40), 3: (60, 130, 230)}
LEVEL_DE  = {
    1: ("STUFE 1 — Hell oder Dunkel", "Hell = 1, Dunkel = 0. Du hast die Kontrolle!"),
    2: ("STUFE 2 — Versteckte Regel", "Nur ein winziges Detail zaehlt. Tricky!"),
    3: ("STUFE 3 — Quanten-Modus", "Die Maschine mischt Zufall. Niemand kann es vorhersagen."),
}
HIT_COL  = (40, 200, 90)
MISS_COL = (230, 70, 70)


class State:
    def __init__(self):
        self.signal = 0       # 0..1023
        self.level = 1
        self.target = 1
        self.last_bit = None
        self.last_hit = None
        self.hits = 0
        self.tries = 0
        self.flash_until = 0.0
        self.level_summary = {}   # level -> (hits, tries)


def find_port():
    if not HAVE_SERIAL:
        return None
    for p in serial.tools.list_ports.comports():
        d = (p.description or "").lower()
        if "arduino" in d or "ch340" in d or "usb" in d or "acm" in d or "usbmodem" in d:
            return p.device
    ports = list(serial.tools.list_ports.comports())
    return ports[0].device if ports else None


class Link:
    """Serial link to the Arduino, or a built-in simulator for testing."""
    def __init__(self, port, sim):
        self.sim = sim
        self.ser = None
        if not sim:
            if not HAVE_SERIAL:
                print("pyserial not installed; falling back to --sim. (pip install pyserial)")
                self.sim = True
            else:
                port = port or find_port()
                if not port:
                    print("No serial port found; falling back to --sim.")
                    self.sim = True
                else:
                    self.ser = serial.Serial(port, 115200, timeout=0)
                    time.sleep(2)   # let the UNO reset
                    print(f"Connected to {port}")
        self._buf = ""
        self._sim_level = 1
        self._sim_target = 1

    def send(self, token):
        if self.ser:
            self.ser.write((token + "\n").encode())
        elif token in ("L1", "L2", "L3"):
            self._sim_level = int(token[1])
        elif token in ("T0", "T1"):
            self._sim_target = int(token[1])

    def readlines(self):
        """Yield protocol lines from hardware, or synthesize them in sim mode."""
        if self.ser:
            try:
                self._buf += self.ser.read(4096).decode(errors="ignore")
            except Exception:
                return
            while "\n" in self._buf:
                line, self._buf = self._buf.split("\n", 1)
                line = line.strip()
                if line:
                    yield line
        else:
            # simulator: drift the signal a bit so the bar looks alive
            yield f"SIG {random.randint(200, 800)}"

    def sim_measure(self):
        """Produce a RESULT line in sim mode matching the firmware's odds."""
        lvl, tgt = self._sim_level, self._sim_target
        if lvl == 1:
            bit = tgt                      # deterministic: you win
        elif lvl == 2:
            bit = tgt if random.random() < 0.65 else 1 - tgt
        else:
            bit = random.randint(0, 1)     # ~50/50
        hit = int(bit == tgt)
        return lvl, bit, tgt, hit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", default=None)
    ap.add_argument("--sim", action="store_true")
    ap.add_argument("--windowed", action="store_true")
    args = ap.parse_args()

    link = Link(args.port, args.sim)

    pygame.init()
    pygame.display.set_caption("Hack the Quantum")
    flags = 0 if args.windowed else pygame.FULLSCREEN
    screen = pygame.display.set_mode((1280, 720), flags)
    W, H = screen.get_size()
    clock = pygame.time.Clock()
    f_huge  = pygame.font.SysFont("Arial Black,Arial", int(H * 0.42), bold=True)
    f_big   = pygame.font.SysFont("Arial", int(H * 0.075), bold=True)
    f_mid   = pygame.font.SysFont("Arial", int(H * 0.045))
    f_small = pygame.font.SysFont("Arial", int(H * 0.032))

    st = State()
    muted = False
    sim_hits = sim_tries = 0

    def text(s, font, col, cx, cy):
        img = font.render(s, True, col)
        screen.blit(img, img.get_rect(center=(cx, cy)))

    running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN:
                k = ev.key
                if k == pygame.K_ESCAPE:
                    running = False
                elif k in (pygame.K_1, pygame.K_2, pygame.K_3):
                    lvl = k - pygame.K_0
                    link.send(f"L{lvl}"); st.level = lvl; st.hits = st.tries = 0
                    sim_hits = sim_tries = 0
                elif k == pygame.K_0:
                    link.send("T0"); st.target = 0
                elif k == pygame.K_9:
                    link.send("T1"); st.target = 1
                elif k == pygame.K_c:
                    link.send("C")
                elif k == pygame.K_m:
                    muted = not muted
                elif k == pygame.K_SPACE:
                    link.send("G")
                    if link.sim:
                        lvl, bit, tgt, hit = link.sim_measure()
                        sim_tries += 1; sim_hits += hit
                        _apply_result(st, lvl, bit, tgt, hit, sim_hits, sim_tries)
                        if sim_tries >= 10:
                            st.level_summary[lvl] = (sim_hits, sim_tries)
                            sim_hits = sim_tries = 0

        # read protocol lines
        for line in link.readlines():
            parts = line.split()
            if not parts:
                continue
            tag = parts[0]
            try:
                if tag == "SIG":
                    st.signal = int(parts[1])
                elif tag == "STATE":
                    st.level, st.target = int(parts[1]), int(parts[2])
                elif tag == "RESULT":
                    lvl, bit, tgt, hit, hh, tt = map(int, parts[1:7])
                    _apply_result(st, lvl, bit, tgt, hit, hh, tt)
                elif tag == "LEVELDONE":
                    lvl, hh, tt = int(parts[1]), int(parts[2]), int(parts[3])
                    st.level_summary[lvl] = (hh, tt)
            except (ValueError, IndexError):
                pass  # ignore comment/partial lines

        # ---- draw ----------------------------------------------------------
        screen.fill(BG)
        col = LEVEL_COL[st.level]
        title, sub = LEVEL_DE[st.level]
        text(title, f_big, col, W // 2, int(H * 0.10))
        text(sub, f_mid, FG, W // 2, int(H * 0.18))

        # giant bit (flashes hit/miss colour briefly)
        now = time.time()
        bit_col = FG
        if now < st.flash_until and st.last_hit is not None:
            bit_col = HIT_COL if st.last_hit else MISS_COL
        text(str(st.last_bit) if st.last_bit is not None else "?",
             f_huge, bit_col, W // 2, int(H * 0.50))

        # live signal bar
        bar_w = int(W * 0.6); bx = (W - bar_w) // 2; by = int(H * 0.74)
        pygame.draw.rect(screen, (40, 44, 54), (bx, by, bar_w, 26), border_radius=13)
        fill = int(bar_w * min(st.signal, 1023) / 1023)
        pygame.draw.rect(screen, col, (bx, by, fill, 26), border_radius=13)
        text("Dein Lichtsignal", f_small, DIM, W // 2, by - 22)

        # target + score
        text(f"Ziel: mach eine  {st.target}", f_mid, FG, int(W * 0.27), int(H * 0.88))
        text(f"Treffer: {st.hits} / {st.tries}", f_mid, FG, int(W * 0.73), int(H * 0.88))

        # mini level summary (control dropping)
        if st.level_summary:
            parts = []
            for lv in (1, 2, 3):
                if lv in st.level_summary:
                    h, t = st.level_summary[lv]
                    parts.append(f"S{lv}: {h}/{t}")
            text("   ".join(parts), f_small, DIM, W // 2, int(H * 0.96))

        if muted:
            text("ton aus (m)", f_small, DIM, int(W * 0.93), int(H * 0.04))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


def _apply_result(st, lvl, bit, tgt, hit, hh, tt):
    st.level = lvl
    st.last_bit = bit
    st.target = tgt
    st.last_hit = bool(hit)
    st.hits, st.tries = hh, tt
    st.flash_until = time.time() + 0.4


if __name__ == "__main__":
    main()
