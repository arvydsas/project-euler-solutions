from math import gcd


# Solution note: I find the four non-trivial digit-cancelling fractions, then reduce their product.
num_prod = 1
den_prod = 1

for i in range(10, 100):
    b = i % 10
    a = int((i - b) / 10)
    for j in range(i + 1, 100):
        d = j % 10
        c = int((j - d) / 10)
        if d == b and d != 0 and a / c == i / j:
            num_prod *= i
            den_prod *= j
        if c == b and d != 0:
            if a / d == i / j:
                num_prod *= i
                den_prod *= j
        if d == a and b / c == i / j:
            num_prod *= i
            den_prod *= j
        if c == a and d != 0:
            if b / d == i / j:
                num_prod *= i
                den_prod *= j

print(den_prod // gcd(num_prod, den_prod))
