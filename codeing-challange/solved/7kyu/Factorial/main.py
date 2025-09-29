# Factorial (7 kyu)

# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

# Sprache: Python
# Datum: 2025-09-29

# Info:
# Wir sollen die Factorial berechnen von input n. als n!
# Beispiel 5! = 5 * 4 * 3 * 2 * 1 = 120.
# Wenn n größer 12 oder kleiner 0 ist soll ein Value Error kommen.
# Noch ein zusatzt bei 0! soll 1 rauskommen

def factorial(n: int) -> int:
    # Wir starten mit dem abfangen vom Fehler
    # Hier wird geprüft ob n größer 12 ist.
    if n > 12:
        raise ValueError("Input to larg")
    #Hier wird geprüft ob n kleiner 0 ist
    if n < 0:
        raise ValueError("Input to low")
    #Hier prüfen wir ob n = 0 ist um es auf 1 zusetzten
    if n == 0:
        n = 1
        return n
    else:
        x = 1
        for i in range(n):
            i += 1
            x *= i
        return x


