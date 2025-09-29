# Two Sum (6 kyu)

**Link:** https://www.codewars.com/...

## Problem
Gegeben ein Array von Zahlen und ein Zielwert. Finde zwei Indizes, deren Werte die Summe ergeben.

## Ansatz
- Brute-Force: O(n^2) → zu langsam
- Optimiert: Hashmap für O(n)
- Schritte:
  1. Iteriere durch Array
  2. Prüfe, ob (target - arr[i]) schon gesehen wurde
  3. Falls ja, gib beide Indizes zurück
  4. Sonst füge arr[i] in Hashmap ein

## Komplexität
- Zeit: O(n)
- Platz: O(n)

## Tests
- Standardfall: [2,7,11,15], target=9 → [0,1]
- Kein Ergebnis → None
- Negative Zahlen → funktioniert auch

## Lessons Learned
- Hashmaps sind perfekt für Lookup-Probleme
- Refactor hat Code kürzer + effizienter gemacht
