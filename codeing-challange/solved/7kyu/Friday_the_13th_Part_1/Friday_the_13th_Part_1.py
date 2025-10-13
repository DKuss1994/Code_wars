# Friday the 13th Part 1 (7 kyu)

# https://www.codewars.com/kata/5925acf31a9825d616000e74

# Sprache: Python
# Datum: 2025-10-09

# t's Friday the 13th, and Jason is ready for his first killing spree!
#
# Create a function, killcount, that accepts two arguments: an array of array pairs
# (the conselor's name and intelligence - ["Chad", 2]) and an integer representing Jason's intellegence.


# Skilled: Mit mehreren variabeln in einer for Schleife zu arbeiten
def kill_count(counselors, jason):
    jason_kill_list =[]
    for name,smart in counselors:
        if smart<jason:
            jason_kill_list.append(name)
    return jason_kill_list