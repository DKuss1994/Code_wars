# Find Fibonacci last digit (7 kyu)

# https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e

# Sprache: Python
# Datum: 2025-10-09

# Task: Those numbers for which this process ends in 1 are happy numbers,
# while those that do not end in 1 are unhappy numbers (or sad numbers) (Wikipedia).
# Write a function that takes n as parameter and return true if and only if n is an happy number, false otherwise.

# example n = 7: 7, 49, 97, 130, 10, 1. Is happy
# example n = 3: 3, 9, 81, 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, 58, 89, 145, 42, 20, 4, 16, 37,... is not Happy

# Skilled: Ich habe gelernt Zahlen zu formatieren in eine Liste einzufügen um sie mit sich selbst mal zu nehmen.
# Zu prüfen wann man eine while schleife sinnvoll beenden kann.
def is_happy(n):
    n_value_list = []

    while n != 1:
        if n in n_value_list:
            return False
        n_value_list.append(n)
        value = 0
        str_list = n_too_list(n)
        for hoch in str_list:
            value += hoch*hoch
        n = value

        print(n)
    if n == 1:
        print(n_value_list)
        return True


def n_too_list(n):
    str_n = str(n)
    len_str_n = len(str_n)
    str_list = []
    index = 0
    for x in range(len_str_n):
        str_list.append(int(str_n[index]))
        index += 1
    return str_list