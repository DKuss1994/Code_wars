def dig_pow(n, p):
    value_x = 0
    n_list = []
    n_str = str(n)

#Hier werden die zahlen separiert in eine Liste gepackt.
    for index in range(len(n_str)):
        n_list.append(int(n_str[index]))
    for zahl in n_list:
        value_x += zahl ** p
        p += 1
    if value_x % n == 0:
        k = value_x / n
        return int(k)
    else:
        return -1

# k = value_x /n or k*n = value_x, value_x = A¹+B²
