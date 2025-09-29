# Find the next perfect square! (7 kyu)

# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python

# Sprache: Python
# Datum: 2025-09-29

# Task: We must find the next square. If the next square not perfect we must return -1
def find_next_square(sq):
    # We take a root from sq
    root = sq ** 0.5
    # We go up for the next perfect square
    if root.is_integer():
        root += 1
        root *= root
        return int(root)
    # We check the type from root sq and if it not a float we return -1
    else:
        return -1
