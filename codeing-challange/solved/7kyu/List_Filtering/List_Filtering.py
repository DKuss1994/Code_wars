# List Filtering (7 kyu)

# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/python

# Sprache: Python
# Datum: 2025-09-29

# In this kata you will create a function
# that takes a list of non-negative integers and strings and returns a new
# list with the strings filtered out.

def filter_list(l):
    new = []
    for zahl in l:
        if type(zahl) == int:
            new.append(zahl)
    return new
