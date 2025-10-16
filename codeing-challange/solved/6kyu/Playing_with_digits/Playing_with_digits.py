# Playing with digits (6 kyu)

# https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e

# Sprache: Python
# Datum: 2025-10-09

# Task: Given n and p, raise each digit of n to successive powers starting from p.
# If the sum equals k * n for some integer k, return k; otherwise, return -1.

# example :
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# Skilled: Ich habe gelernt Zahlen zu formatieren in eine Liste einzufügen um sie mit sich selbst mal zu nehmen.
# Zu prüfen wann man eine while schleife sinnvoll beenden kann.
def dig_pow(n, p):
    value_x = 0
    n_list = []
    n_str = str(n)

#Hier werden die zahlen separiert in eine Liste gepackt.
    value_x = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n)))
    if value_x % n == 0:
        k = value_x / n
        return int(k)
    else:
        return -1





