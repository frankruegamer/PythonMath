# PythonMath

Eine Sammlung verschiedene Python-Skripte für Mathematische Algorithmen

## eukld.py
#### Zweck
Berechnet für zwei übergebene Zahlen den erweiterten euklidischen Algorithmus und gibt diesen in Tabellenform aus.
Zusätzlich wird deren größter gemeinsamer Teiler ausgegeben.
Sehr nützlich ist dies auch für die Ermittlung des inversen Elements von `a` aus der Menge der Reste bei der Division durch `m`.
Diese Zahl befindet sich nach den Berechnungen als Zahl links unten in der Tabelle.

#### Verwendung
`eukld.py number1 number2`

Benötigt genau zwei Zahlen als Input.
Die Reihenfolge ist hierbei egal, denn die Zahlen werden automatisch sortiert.
Zu Beachten ist, dass die Zahlen natürliche Zahlen sein müssen.

## prime.py
#### Zweck
Prüft für übergebene Zahlen, ob diese Primzahlen sind.
Für Zahlen, die keine Primzahlen sind, wird deren Primfaktorzerlegung ermittelt.
Zusätzlich wird bei quadratfreien Zahlen die zugehörige Phi-Funktion berechnet.

#### Verwendung
`prime.py number1 [number2 ...]`

Benötigt mindestens eine Zahl als Input.
Weitere Zahlen können einfach als zusätzlicher Parameter übergeben werden.
Außerdem müssen die Zahlen Elemente der natürlichen Zahlenmenge sein.
Nicht unterstützte Parameter werden übersprungen.
