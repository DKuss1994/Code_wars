# Friend or Foe? (7 kyu)

# https://www.codewars.com/kata/55b42574ff091733d900002f/python

# Sprache: Python
# Datum: 2025-09-29

# Info: We get a list and we must return Person with exactly 4 letter

def friend(x):
    new = []
    for i in x:
        if len(i) == 4:
            new.append(i)
    return new
