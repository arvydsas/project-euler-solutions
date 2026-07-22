# Solution note: I use the odd-power remainder shortcut and sum the maximum
# remainder for each a from 3 through 1000.
def modulo_function_2(n, a):
    if n % 2 == 0:
        return 2
    else:
        return (2 * n * a) % (a**2)


def max_modulo(a):
    m = 0
    for k in range(1, a):
        temp = modulo_function_2(2 * k - 1, a)
        if temp > m:
            m = temp
    return m


ss = 0

for a in range(3, 1001):
    ss += max_modulo(a)

print(ss)
