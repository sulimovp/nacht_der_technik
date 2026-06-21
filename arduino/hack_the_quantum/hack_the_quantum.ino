/*
 * Hack the Quantum — Wie aus Licht ein Bit wird
 * Nacht der Technik 2026, ZHAW TechLab.  Authors: P. Sulimov, C. Lehmann.
 *
 * A light sensor (LDR) turns light into a bit (0/1) through 3 encoding modes.
 * Level 1 (deterministic) -> easy to control.  Level 2 (hidden parity) -> tricky.
 * Level 3 (noise mixing) -> practically uncontrollable ("quantum-like").
 *
 * Works STANDALONE (RGB LED + piezo give feedback, buttons drive it) AND with the
 * Python screen UI in ../../software/quantum_ui/ over USB serial at 115200 baud.
 *
 * ---- Hardware (Arduino Starter Kit only) -------------------------------------
 *   LDR voltage divider:  5V -- LDR -- A0 -- 10k -- GND          (LDR_PIN = A0)
 *   RGB LED (common cathode, each leg via 220 ohm to a PWM pin):
 *        R = D9   G = D10   B = D11   common -> GND
 *   Piezo buzzer:         D6 -> piezo -> GND                     (BUZZER_PIN = 6)
 *   Button A (target):    D2 -> button -> GND  (uses INPUT_PULLUP)
 *   Button B (GO/measure):D3 -> button -> GND  (uses INPUT_PULLUP)
 *   (Common-anode RGB? set COMMON_ANODE true below.)
 *
 * ---- Serial protocol ---------------------------------------------------------
 *   Arduino -> PC (lines, '\n'):
 *     SIG <0..1023>                 live signal (throttled)
 *     STATE <level> <target>        after any state change
 *     RESULT <level> <bit> <target> <hit 0|1> <hits> <tries>
 *     LEVELDONE <level> <hits> <tries>
 *     READY
 *   PC -> Arduino (single chars or short tokens):
 *     L1 / L2 / L3   set level        C  calibrate (point sensor at ambient)
 *     T0 / T1        set target bit    G  measure now (same as button B)
 *     R              reset scores
 * ----------------------------------------------------------------------------*/

const uint8_t LDR_PIN    = A0;
const uint8_t PIN_R      = 9;
const uint8_t PIN_G      = 10;
const uint8_t PIN_B      = 11;
const uint8_t BUZZER_PIN = 6;
const uint8_t BTN_TARGET = 2;   // choose 0 or 1
const uint8_t BTN_GO     = 3;   // take the measurement

const bool COMMON_ANODE  = false;  // set true if your RGB LED is common-anode

// ---- tunables (calibrate on site, see TODO §1) -----------------------------
int   threshold      = 512;   // Level 1 split point; overwritten by calibration
const uint8_t  L3_SAMPLES = 64;    // Level 3: how many LSB samples to XOR-mix
const uint8_t  TRIES_PER_LEVEL = 10;

// ---- state ------------------------------------------------------------------
uint8_t level   = 1;    // 1..3
uint8_t target  = 1;    // bit the child is trying to force
uint8_t hits    = 0;
uint8_t tries   = 0;
unsigned long lastSig = 0;

void setup() {
  Serial.begin(115200);
  pinMode(PIN_R, OUTPUT); pinMode(PIN_G, OUTPUT); pinMode(PIN_B, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BTN_TARGET, INPUT_PULLUP);
  pinMode(BTN_GO, INPUT_PULLUP);
  randomSeed(analogRead(LDR_PIN));      // seed from sensor noise
  calibrate();
  Serial.println(F("READY"));
  sendState();
  showModeColor();
}

void loop() {
  // 1) stream the live signal (throttled to ~50 Hz)
  if (millis() - lastSig > 20) {
    Serial.print(F("SIG ")); Serial.println(analogRead(LDR_PIN));
    lastSig = millis();
  }

  // 2) handle PC commands
  if (Serial.available()) handleSerial();

  // 3) handle buttons (debounced)
  if (pressed(BTN_TARGET)) { target ^= 1; sendState(); blinkTarget(); }
  if (pressed(BTN_GO))     { measure(); }
}

// ---- the three encoders -----------------------------------------------------
uint8_t encodeBit() {
  if (level == 1) {                       // deterministic: bright = 1
    return (analogRead(LDR_PIN) > threshold) ? 1 : 0;
  }
  if (level == 2) {                       // hidden rule: least-significant bit
    return analogRead(LDR_PIN) & 0x01;
  }
  // level 3: mix many fast LSB samples (entropy extraction) + Von Neumann debias
  uint8_t mixed = 0;
  for (uint8_t i = 0; i < L3_SAMPLES; i++) {
    mixed ^= (analogRead(LDR_PIN) & 0x01);
    delayMicroseconds(137);               // odd interval to decorrelate samples
  }
  // Von Neumann debiasing: compare two fresh bits to kill residual bias
  while (true) {
    uint8_t a = analogRead(LDR_PIN) & 0x01;
    uint8_t b = analogRead(LDR_PIN) & 0x01;
    if (a != b) { mixed ^= a; break; }
  }
  return mixed & 0x01;
}

void measure() {
  uint8_t bit = encodeBit();
  uint8_t hit = (bit == target) ? 1 : 0;
  tries++; if (hit) hits++;
  feedback(hit);

  Serial.print(F("RESULT ")); Serial.print(level); Serial.print(' ');
  Serial.print(bit);  Serial.print(' '); Serial.print(target); Serial.print(' ');
  Serial.print(hit);  Serial.print(' '); Serial.print(hits);   Serial.print(' ');
  Serial.println(tries);

  if (tries >= TRIES_PER_LEVEL) {
    Serial.print(F("LEVELDONE ")); Serial.print(level); Serial.print(' ');
    Serial.print(hits); Serial.print(' '); Serial.println(tries);
    tries = 0; hits = 0;                   // ready for next round
  }
}

// ---- feedback ---------------------------------------------------------------
void feedback(uint8_t hit) {
  if (hit) { setRGB(0, 255, 0); tone(BUZZER_PIN, 880, 120); }   // green + high beep
  else     { setRGB(255, 0, 0); tone(BUZZER_PIN, 220, 200); }   // red + low beep
  delay(250);
  showModeColor();
}

void showModeColor() {                     // 1=green 2=yellow 3=blue
  if (level == 1) setRGB(0, 120, 0);
  else if (level == 2) setRGB(120, 90, 0);
  else setRGB(0, 60, 160);
}

void blinkTarget() {                       // quick flash to confirm target change
  for (uint8_t i = 0; i < target + 1; i++) { setRGB(80,80,80); delay(80); showModeColor(); delay(80); }
}

void setRGB(int r, int g, int b) {
  if (COMMON_ANODE) { r = 255 - r; g = 255 - g; b = 255 - b; }
  analogWrite(PIN_R, r); analogWrite(PIN_G, g); analogWrite(PIN_B, b);
}

// ---- calibration ------------------------------------------------------------
void calibrate() {                         // sample ambient, set threshold above it
  long sum = 0; const int N = 200;
  for (int i = 0; i < N; i++) { sum += analogRead(LDR_PIN); delay(2); }
  int ambient = sum / N;
  threshold = constrain(ambient + 120, 80, 940);   // "brighter than now" = 1
  Serial.print(F("# calibrated ambient=")); Serial.print(ambient);
  Serial.print(F(" threshold=")); Serial.println(threshold);
}

// ---- input helpers ----------------------------------------------------------
bool pressed(uint8_t pin) {                // simple debounce, active-low
  static unsigned long last[20] = {0};
  if (digitalRead(pin) == LOW && millis() - last[pin] > 200) {
    last[pin] = millis();
    return true;
  }
  return false;
}

void handleSerial() {
  String cmd = Serial.readStringUntil('\n');
  cmd.trim();
  if (cmd == "L1") { level = 1; tries = hits = 0; }
  else if (cmd == "L2") { level = 2; tries = hits = 0; }
  else if (cmd == "L3") { level = 3; tries = hits = 0; }
  else if (cmd == "T0") { target = 0; }
  else if (cmd == "T1") { target = 1; }
  else if (cmd == "C")  { calibrate(); }
  else if (cmd == "G")  { measure(); return; }
  else if (cmd == "R")  { tries = hits = 0; }
  sendState();
  showModeColor();
}

void sendState() {
  Serial.print(F("STATE ")); Serial.print(level); Serial.print(' ');
  Serial.println(target);
}
