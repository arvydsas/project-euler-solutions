# Solution note: I brute-force reduced fractions between 1/3 and 1/2 with denominators up to 12000.
import math
from math import gcd


def coprime(a,b):
    if gcd(a,b) == 1:
        return True
    else:
        return False


k = 12000
ss = 0

for n in range(4,k+1):
    for i in range(math.ceil(n/3), math.ceil(n/2)):
        if coprime(n, i):
            ss+=1
print(ss)

