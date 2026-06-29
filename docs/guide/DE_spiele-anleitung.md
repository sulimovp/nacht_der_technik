# Spiel-Anleitung — Handbuch fürs Standteam (Deutsch)

> Für jedes Spiel: das **Prinzip**, die **echte Physik**, **Analogie vs. echt**, die **Regeln**, wie man
> es **je nach Alter erklärt**, **Beispiel-Dialoge** und **FAQ**. Englisch: `EN_games-guide.md`.
> Grundlagen: `DE_quanten-grundlagen.md`. Spickzettel: `DE_spickzettel.md`.

Der Stand hat **fünf** Spiele. Drei sind unsere (Web-Apps unter `arraxis.com/nachtdertechnik`):
**Hack the Light**, **Schlag die KI**, **Quanten-Elfmeter**. Zwei sind externe Browser-Spiele:
**Quanten-Schach** (q-chess.com) und **Quanten-Tic-Tac-Toe** (tiqtaqtoe.com). Dazu eine vom Team
gezogene **Quanten-Geschenk**-Verlosung.

Der ganze Stand erzählt **eine Geschichte**: *Manches kann man steuern, manches nicht — und die
tiefste Unvorhersehbarkeit (Quanten-Zufall) ist eine starke Ressource für die Zukunft.*

---

## 1. Hack the Light — "aus Licht wird ein Bit"

**Aufhänger:** Mach Licht auf die Kamera und versuche, das Ergebnis 0 oder 1 zu erzwingen.

**Gezeigtes Prinzip:** Wie aus einem physikalischen Signal digitale Information wird — und wie man
Zufall aus **physikalischem Rauschen** gewinnt, der Alltags-Verwandte eines Quanten-Zufallsgenerators.

**Die echte Physik:** Ein Lichtsensor macht aus Helligkeit eine Zahl. Drei "Codierer" machen daraus ein Bit:
- **Modus 1 – Hell/Dunkel (deterministisch):** `Bit = 1 wenn hell, sonst 0`. Volle Kontrolle.
- **Modus 2 – Versteckte Regel (Parität):** nur das *kleinste* Detail der Helligkeit zählt, grosse
  Änderungen kippen das Bit oft nicht. Die Kontrolle wird unzuverlässig.
- **Modus 3 – Zufall:** Die App mischt das **winzige Flacker-Rauschen** des Kamerasensors (thermisches
  + Schrotrauschen) aus vielen Pixeln und verknüpft es (XOR). Selbst bei ruhigem Licht ist das Ergebnis
  ~50/50 und praktisch nicht steuerbar.

**Analogie vs. echt:** Modus 3 ist eine *physikalische* Entropiequelle — echt, aber aus Elektronik,
**nicht** aus einzelnen Photonen. Eine ehrliche Analogie zum Quanten-Zufallsgenerator, der denselben
Trick mit einem Photon am halbdurchlässigen Spiegel macht. Sage "quanten-*ähnlich*".

**Regeln / Spielablauf:**
1. Ziel wählen (0 oder 1).
2. Mit der Handy-Kamera: abdecken, anleuchten, Hand bewegen — versuche dein Ziel zu erzwingen.
3. 10 Versuche pro Modus. Sieh, wie deine Trefferquote von Modus 1 → 2 → 3 **sinkt**.
4. Ein "Licht-Score" (Modus 1+2) kommt in die Bestenliste.

**Je nach Alter erklären:**
- **6–8:** "Hell macht 1, dunkel macht 0 — du bist der Chef! Jetzt wird die Maschine schlau… jetzt
  würfelt sie, und du kannst nicht gewinnen."
- **9–12:** "Zuerst ist die Regel einfach. Dann versteckt sie sich — nur ein winziges Detail zählt. Dann
  nutzt die Maschine ihr eigenes Rauschen, und niemand kann sie steuern."
- **13+:** "Das ist Entropie-Gewinnung: Wir ernten unvorhersehbares physikalisches Rauschen für
  Zufallsbits. Echte Quantengeneratoren machen das mit einzelnen Photonen — die Basis sicherer Schlüssel."

**Beispiel-Dialog:** "Mach mal eine 1 — easy, oder? Jetzt der blaue Modus, nochmal… frustrierend?
Genau das ist der Punkt: Manchen Zufall kann man nicht austricksen. Das ist Gold für Cybersicherheit."

**FAQ:**
- *"Ist das echtes Quanten?"* → "Es ist echter *physikalischer* Zufall aus dem Kamerarauschen — ein
  super Ersatz. Echte Quantengeneratoren nutzen einzelne Photonen; gleiche Idee, eine Stufe tiefer."
- *"Warum gehorcht es im blauen Modus nicht?"* → "Weil es Rauschen liest, das du nicht steuern kannst —
  genau das macht den Zufall vertrauenswürdig."

**Tipps:** Braucht Kamera-Erlaubnis + HTTPS; sonst läuft ein "Demo ohne Kamera". Kalibriert sich beim
Start auf das Raumlicht. Klappt am besten, wenn die Kamera eine Lichtquelle sieht.

---

## 2. Schlag die KI — "sei zufälliger als eine Maschine"

**Aufhänger:** Tippe links/rechts, wie du willst; eine KI versucht, deinen nächsten Tipp vorherzusagen —
und gewinnt meistens.

**Gezeigtes Prinzip:** **Menschen sind schlecht im Zufälligsein**; KI ist ein Mustererkenner; nur
*echter* Zufall schlägt die Vorhersage. Das ist die Brücke von "warum Zufall wichtig ist" zu "warum wir
**Quanten**-Zufall wollen".

**Die echte Physik (bzw. Informatik):** Der Vorhersager ist ein "Aaronson-Orakel" — er merkt sich kurze
Folgen deiner letzten Tipps und wettet, dass du deine Gewohnheiten wiederholst (wir vermeiden
Wiederholungen, wir wechseln ab, wir fürchten lange Serien). Bei Mustern trifft er ~80–99 %; bei echtem
Zufall fällt er auf ~50 % (Zufallsniveau). Keine Quanten-Hardware — eine schöne KI-Demo, die den
*Bedarf* an Quanten-Zufall **motiviert**.

**Analogie vs. echt:** Dies ist **kein** Quantenspiel; es ist das "Warum" hinter dem Quanten-Zufall.
Ehrlicher Bezug: "Um diese KI zu schlagen, bräuchtest du eine perfekte Münze — und die perfektesten
Münzen der Natur sind quantenmechanisch."

**Regeln / Spielablauf:**
1. 25 Runden. Pro Runde **LINKS** oder **RECHTS** tippen (auch wischen / Pfeiltasten).
2. Du punktest, wenn die KI **falsch** rät (du hast sie ausgetrickst); die KI punktet, wenn sie richtig liegt.
3. Endstand + Bestenliste (deine "Treffer").

**Je nach Alter erklären:**
- **6–8:** "Überrasche den Roboter! Er liest deine Gedanken. Kannst du tricksen?"
- **9–12:** "Der Computer lernt deine Gewohnheiten in Sekunden. Zum Gewinnen musst du echt zufällig
  sein — und das ist für Menschen richtig schwer."
- **13+:** "Es ist ein Markov-Vorhersager. Menschen verraten Muster, darum gewinnt die KI. Kryptografie
  braucht Zufall, den keine KI vorhersagen kann — darum gibt es Quanten-Zufallsgeneratoren."

**Beispiel-Dialog:** "Wette, du schlägst die KI nicht… siehst du? Sie hat dein Muster erkannt. Witzig:
Gewinnen kann man nur, wenn man perfekt zufällig ist — und das können Menschen kaum. Darum machen
Computer — und vor allem die Quanten-Physik — die Zufallszahlen, die deine Passwörter schützen."

**FAQ:**
- *"Liest sie meine Gedanken?"* → "Nur deine Gewohnheiten — sie merkt sich deine letzten Züge."
- *"Wie gewinne ich?"* → "Sei unvorhersehbar. Manche werfen im Kopf eine Münze. Selbst dann ist es schwer!"

**Tipps:** Ideal für Warteschlange / Wettbewerb. Bei Frust betonen: *Verlieren* ist die Lektion, fast
alle verlieren.

---

## 3. Quanten-Elfmeter — die Überlagerung schiesst

**Aufhänger:** Triff gegen einen Torhüter, der deine Gedanken liest — oder nimm den **Quantenschuss**,
der in zwei Ecken gleichzeitig ist.

**Gezeigtes Prinzip:** **Überlagerung** und **Messung/Kollaps**, kombiniert mit der Vorhersage-Lektion.
Der Torhüter ist dieselbe musterlesende KI; der **Quantenschuss** bringt den Ball in eine Überlagerung
zweier Ecken, bis die "Messung" ihn kollabieren lässt.

**Die echte Physik:**
- **Normaler Schuss:** Du wählst Links/Mitte/Rechts; der KI-Torhüter sagt dich voraus und hechtet.
  Vorhersehbare Schützen werden gehalten.
- **Quantenschuss:** Der Ball ist in **Überlagerung** aus Links **und** Rechts. Der Torhüter kann nur
  einen Ort decken. Im **Moment des Aufpralls (Messung)** **kollabiert** der Ball zufällig (echt 50/50)
  in eine Ecke. Hechtet der Torhüter zur *anderen* Seite — oder in die Mitte — ist es ein Tor.

**Analogie vs. echt:** Quanten-*inspiriert*. Überlagerung und zufälliger Kollaps sind dem Verhalten eines
Qubits bei der Messung treu nachgebildet; technisch ist es normaler Code + ein kryptografischer
Münzwurf, keine Quanten-Hardware.

**Regeln / Spielablauf:**
1. 10 Elfmeter. Wähle **Links / Mitte / Rechts** (Knöpfe, Wischen oder der **Bewegungs**-Schalter Ein/Aus —
   Handy schwingen).
2. Oder drücke **Quantenschuss**: Ball in Überlagerung Links+Rechts, kollabiert 50/50.
3. Tore kommen in die Bestenliste. 8+ Tore → Hinweis aufs Quanten-Geschenk.

**Je nach Alter erklären:**
- **6–8:** "Der Torhüter rät, wohin du schiesst! Aber der Zauberball geht in BEIDE Ecken gleichzeitig —
  beide kann er nicht halten."
- **9–12:** "Ein guter Torhüter liest dein Muster. Der Quantenschuss ist in zwei Ecken zugleich — erst
  wenn der Ball ankommt, 'entscheidet' er sich für eine Ecke, völlig zufällig."
- **13+:** "Der Quantenschuss ist eine Überlagerung zweier Zustände; der Torhüter ist ein
  Welcher-Weg-Detektor; der Aufprall ist die Messung, die 50/50 kollabiert. Vorhersagbarkeit vs. echter
  Zufall, auf dem Platz."

**Beispiel-Dialog:** "Schiess ein paar Mal normal… der Torhüter lernt dich, oder? Jetzt der
Quantenschuss — der Ball ist in zwei Ecken zugleich und 'entscheidet' sich erst beim Ankommen. Der
Torhüter kann nicht lesen, was noch nicht entschieden ist."

**FAQ:**
- *"Ist der Ball wirklich an zwei Orten?"* → "Im Spiel steht er für die Überlagerung eines Qubits — zwei
  Möglichkeiten zugleich, bis gemessen wird. Echte Teilchen machen das tatsächlich."
- *"Warum wurde mein Quantenschuss trotzdem gehalten?"* → "Er kollabiert 50/50 — hechtete der Torhüter
  zufällig dorthin, Pech. Quanten garantiert *Unvorhersehbarkeit*, nicht immer ein Tor."

**Tipps:** Die Bewegungssteuerung ist ein klarer Ein/Aus-Schalter — bei Bedarf ausschalten; Knöpfe und
Wischen gehen immer.

---

## 4. Quanten-Schach (q-chess.com) — Überlagerung & Verschränkung auf dem Brett

**Aufhänger:** Normales Schach, aber Figuren können in **zwei Feldern zugleich** sein und **verschränkt** werden.

**Gezeigtes Prinzip:** **Überlagerung** (ein "Split"-Zug setzt eine Figur auf zwei Felder),
**Verschränkung** (verbundene Figuren) und **Messung** (ein Schlagzug/Zusammenstoss zwingt die Realität
zur Wahl).

**Die echte Physik (als treue Metapher):**
- Ein **Split-Zug** schickt eine Figur gleichzeitig auf zwei Zielfelder — sie ist nun in Überlagerung
  über beide Felder, jedes mit einer gewissen Wahrscheinlichkeit.
- Figuren können **verschränkt** werden, sodass das Auflösen der einen die andere beeinflusst.
- Eine **Messung** (z. B. ein Schlagversuch) lässt die Überlagerung **kollabieren**: Die Figur stellt
  sich als wirklich auf einem Feld heraus, die andere Möglichkeit verschwindet.

**Analogie vs. echt:** Ein quanten-*inspiriertes* Brettspiel — ideal für *Jugendliche/Erwachsene/Schach-Fans*.
Keine Quanten-Hardware. Am besten vom Team begleitet oder für zwei sichere Spieler; tiefer als Tic-Tac-Toe.

**Regeln / Spielablauf (q-chess.com):** Normales Schach plus "Split"/"Merge"-Züge, die Überlagerungen
erzeugen; wenn ein Zug eine eindeutige Antwort braucht (Schlagen, Schach), werden die betroffenen Figuren
**gemessen** und die Stellung kollabiert. Lass die Leute experimentieren — ein, zwei Split-Züge, und der
Groschen fällt. Gegen den "Baby Robot" oder zu zweit.

**Je nach Alter erklären:**
- **6–8:** (wohl zu komplex) "Diese Figuren können Geister in zwei Feldern sein — schau, wie sie echt
  werden, wenn sie zusammenstossen." Kurz halten; Jüngere besser zu Tic-Tac-Toe lenken.
- **9–12:** "Dein Springer kann auf zwei Felder zugleich springen und 'vielleicht-hier, vielleicht-dort'
  bleiben, bis jemand nachschaut — dann muss er sich für eines entscheiden."
- **13+:** "Split = Überlagerung über Felder erzeugen; Schlagzüge/Schach wirken als Messungen, die
  kollabieren; Figuren können verschränken. Schach mit den drei Quanten-Grundregeln."

**FAQ:**
- *"Wie kann eine Figur an zwei Orten sein?"* → "Wie ein Qubit: eine Mischung aus Möglichkeiten, bis
  etwas eine eindeutige Antwort erzwingt."

**Tipps:** Die "Wow, das ist tief"-Station für ältere Gäste. Halte eine 1-Zeilen-Regel bereit.

---

## 5. Quanten-Tic-Tac-Toe (tiqtaqtoe.com) — Überlagerung in 30 Sekunden verstanden

**Aufhänger:** Drei gewinnt, aber dein Zeichen kommt in **zwei Felder zugleich**, Zeichen werden
**verschränkt** und **kollabieren**.

**Gezeigtes Prinzip:** Die *einfachste* handfeste Demo für **Überlagerung**, **Verschränkung** und
**Messung** — perfekt für Kinder und Familien.

**Die echte Physik (als treue Metapher):**
- Ein **Quanten-Zeichen** wird in **zwei Feldern zugleich** gesetzt (Überlagerung), markiert mit der Zugnummer.
- Bilden die Zeichen eine **Schleife** geteilter Felder (Verschränkung), passiert eine **Messung**: Die
  Schleife **kollabiert** und jedes Geister-Zeichen wird in genau einem Feld real.
- Dann prüft man wie gewohnt auf drei in einer Reihe.

**Analogie vs. echt:** Quanten-*inspiriert*, 2 Personen, sehr wenig Text. Das beste Familienspiel am
Stand, um Überlagerung und Kollaps zu *spüren*.

**Regeln / Spielablauf (tiqtaqtoe.com):**
1. Im Zug setzt du dein Symbol in **zwei** leere Felder (ein "spukendes" Zeichen in Überlagerung).
2. Bilden die verschränkten Zeichen eine geschlossene Schleife, gibt es einen **Kollaps**, und jedes
   Zeichen landet in einem echten Feld.
3. Wer zuerst drei echte in einer Reihe hat, gewinnt. (Die Seite hat einen "Instructor"-Modus mit
   weniger Text für Kinder.)

**Je nach Alter erklären:**
- **6–8:** "Setz dein X in ZWEI Felder zugleich — es ist ein Geist! Wenn sich die Geister verheddern,
  springen sie in ein echtes Feld."
- **9–12:** "Jeder Zug lebt in zwei Feldern zugleich. Bilden sie eine Schleife, sind sie 'verschränkt'
  und müssen sich entscheiden — dieses Entscheiden ist eine Messung."
- **13+:** "Überlagerung (Zeichen in zwei Feldern), Verschränkung (zyklische Abhängigkeit) und Kollaps
  (Messung löst den Zyklus). Tic-Tac-Toe ist nur das Gerüst."

**Beispiel-Dialog:** "Dein X kommt in zwei Felder zugleich — es ist in Überlagerung. Siehst du, wie es
sich mit meinem verbindet? Bilden die Verbindungen eine Schleife, 'kollabiert' alles, und jedes X oder O
landet in einem echten Feld. Die Schleife ist Verschränkung; der Kollaps ist eine Messung."

**FAQ:**
- *"Warum ist mein Zeichen gesprungen?"* → "Es war in zwei Feldern, bis der Kollaps es in eines zwang —
  genau wie beim Messen eines Quantenteilchens."

**Tipps:** Standard-2-Personen-Spiel für die Bildschirm-Ecke; mit dem kurzen Sprech oben kombinieren.

---

## Quanten-Geschenk (vom Team) — Belohnung mit echtem Zufall

Eine `prize.html`-Seite zieht eine Gewinnerin/einen Gewinner mit dem kryptografischen Zufall des
Browsers (Ersatz für eine Quanten-Ziehung). Für Top-Spieler:innen der Bestenliste: Seite öffnen, Knopf
drücken lassen, und die Süssigkeit ausgeben, die der "Quanten-Zufall" wählt. Verbindet das Zufalls-Thema
mit einem Leckerli.

---

## Stand betreiben — praktischer Ablauf

1. **Begrüssen:** "Willst du eine Quantenmaschine schlagen?"
2. **Mit einem Spiel ködern** (Schlag die KI oder Elfmeter gehen am schnellsten).
3. **Lektion landen:** Steuern vs. Nicht-Steuern aufzeigen.
4. **Brücke:** "Diese Unvorhersehbarkeit schützt deine Daten und treibt zukünftige Computer an."
5. **Andere anbieten** + Bestenliste + Chance aufs Quanten-Geschenk.
6. Jede Runde **30–90 s**; die Schlange spielt am eigenen Handy weiter.
