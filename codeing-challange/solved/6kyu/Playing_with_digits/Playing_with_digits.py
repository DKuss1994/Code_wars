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

# k = value_x /n or k*n = value_x, value_x = A¹+B²



