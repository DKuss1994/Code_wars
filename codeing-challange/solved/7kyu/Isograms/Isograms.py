# Isograms (7 kyu)

# https://www.codewars.com/kata/54ba84be607a92aa900000f1/python
# Sprache: Python
# Datum: 2025-10-08

# Task: An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains
# only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# example :
# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

# Ich hab die Funktion count genutzt um in der for schleife zu prüfen ob es ein Buchstabe mehr als einmal vorkommt.
def is_isogram(string):
    string = string.lower()
    for buchstabe in string:
        x = string.count(buchstabe)
    if x > 1:
        return False
    return True
