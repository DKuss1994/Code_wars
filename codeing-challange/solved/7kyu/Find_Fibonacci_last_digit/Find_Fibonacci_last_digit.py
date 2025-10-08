# Find Fibonacci last digit (7 kyu)

# https://www.codewars.com/kata/56b7251b81290caf76000978

# Sprache: Python
# Datum: 2025-10-07

# Task: The last number from the fibonacci.

# Skilled: The function from % in Python. If we work with % the result will be the rest from the division.
def get_last_digit(index):
    a, b = 0, 1

    for i in range(index):
        a, b = b % 10, (a + b) % 10
    string = str(a)[-1]
    value = int(string)
    return value
