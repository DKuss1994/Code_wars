# Fruit string calculator (7 kyu)

# https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3

# Sprache: Python
# Datum: 2025-10-08

# You are given a string of words and numbers. Extract the expression including:
#
# the operator: either addition ("gains") or subtraction ("loses")
# the two numbers that we are operating on
# Return the result of the calculation.

# Skilled: I've learned to use terms like gains and loses as operators
def calculate(strng):
    strng_list = strng.split()
    a = int(strng_list[2])
    b = int(strng_list[-1])

    if "loses" in strng:
        value = a - b
        return value
    elif "gains" in strng:
        value = a + b
        return value