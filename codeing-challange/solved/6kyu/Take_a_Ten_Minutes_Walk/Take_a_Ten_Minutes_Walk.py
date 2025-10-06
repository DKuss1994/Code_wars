# Take a Ten Minutes Walk (6 kyu)

# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc

# Sprache: Python
# Datum: 2025-10-06

# Info:
# You need to write a function that checks if a given walk:
# lasts exactly 10 minutes (the array has 10 directions), and
# returns you to your starting point (the same number of steps north/south and east/west).
# If both conditions are true, return true; otherwise, return false.

def is_valid_walk(walk):
    n = walk.count("n")
    s = walk.count("s")
    w = walk.count("w")
    e = walk.count("e")
    if len(walk) == 10:
        if n != s:
            return False
        elif w != e:
            return False
        else:
            return True
    else:
        return False
