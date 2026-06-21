# Quantum UI — screen display

Reads the Arduino (`arduino/hack_the_quantum/`) over USB serial and shows the kid-facing screen.

## Run

```bash
pip install -r requirements.txt

# with the Arduino plugged in (auto-detect the port):
python quantum_ui.py

# specify a port:
python quantum_ui.py --port COM5          # Windows
python quantum_ui.py --port /dev/ttyACM0  # Linux / Mac

# no Arduino yet? test the screen in simulation mode:
python quantum_ui.py --sim --windowed
```

## Keys

| Key | Action |
|---|---|
| 1 / 2 / 3 | set Level (also sent to Arduino) |
| 0 / 9 | set target bit to 0 / 1 |
| SPACE | take a measurement (same as the Arduino GO button) |
| c | recalibrate the sensor to ambient light |
| m | mute (UI flag; firmware also has its own beeps) |
| ESC | quit |

On the night, the **buttons on the Arduino** drive it; the keyboard is just a backup / for testing.
See the protocol description in the `.ino` header. Start in `--windowed` while testing, drop the
flag for fullscreen kiosk mode on the stand.
