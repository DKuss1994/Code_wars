# String ends with? (7 kyu)

# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
# Sprache: Python
# Datum: 2025-10-17

# Task: Complete the solution so that
# it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# example :
# Inputs: "abc", "bc"
# Output: true
#
# Inputs: "abc", "d"
# Output: false

# Gelernt wie man in einem String prüft ob etwas am Ende gleich ist wie die Eingabe
def solution(text, ending):
    if ending in text[len(ending)*-1:]:
        return True
    return False