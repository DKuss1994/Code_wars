# Friday the 13th Part 1 (7 kyu)

# https://www.codewars.com/kata/5831c5f8ac6a11e3380002de/solutions/python

# Sprache: Python
# Datum: 2025-10-12

# Complete the function. Two arguments will be given:
# arr: An array that contains some integers (positve,negative or zero).
# n: A positive integer. 1 <= n <= arr.length.
# Your task is to find the minimum value of each n adjacent elements in arr. Returns by a new array. For example:


# Skilled: Unterschied zwischen „Gruppen“ und „gleitenden Fenstern“
#
# Du hast verstanden, dass man Listen auf verschiedene Arten in Abschnitte teilt:
#
# Gruppenweise: [1,2], [3,4]
#
# Gleitend: [1,2], [2,3], [3,4] Das ist ein Grundkonzept in Datenverarbeitung, Statistik und KI-Vorbereitung (Sliding Windows).
def min_value(arr, n):
    min_list = []
    for i in range(len(arr)-n+1):
        window = arr[i:i+n]
        min_list.append(min(window))

    return min_list