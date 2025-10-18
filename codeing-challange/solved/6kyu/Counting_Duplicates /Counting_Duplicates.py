# Counting Duplicates (6 kyu)

# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python
# Sprache: Python
# Datum: 2025-10-17

# Task: Write a function that will return
# the count of distinct case-insensitive alphabetic characters and numeric digits that occur more
# than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# example :
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# Ich hab gelernt, wie man Zeichen in einem String einmal zählt, wenn sie mehr als einmal drin vorkommen.

def duplicate_count(text):
    #1.Großbuchstaben zu Kleinbuchstaben machen damit die selben Buchstaben verglichen werden
    text = text.lower()
    # 2. der Stand der zurück geben wird.
    count = 0
    # Hier kommen zeichen rein die wir achon gezählt haben.
    liste_zeichen = []
    for i in text:
    # In der if Bedienung wird nur gepürft ob wir den Buchstaben schon einmal gezählt haben
        if i in liste_zeichen:
            continue
        elif text.count(i) > 1:
            liste_zeichen.append(i)
            count += 1
    return (count)