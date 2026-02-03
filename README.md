# Kaffeeverbrauchs-Tracker 

Dieses Repository enthält ein Python-Modul (kein vollständiges UI), das den täglichen
Kaffeeverbrauch erfasst und einfache Statistiken liefert.

## Funktionen
- Kaffee-Eintrag erfassen (Menge, Tag, Art)
- Tagesstatistik: Anzahl, Gesamtsumme (ml), Durchschnitt
- Grenzwertprüfung (Tageslimit nach Anzahl)
- Wochenübersicht: Totals pro Tag (7 Tage)
- Häufigste Kaffee-Art eines Tages

## Projektstruktur
- `src/` Implementierung
- `tests/` Unit-Tests (PyUnit)

## Tests ausführen
```bash
python -m unittest discover
