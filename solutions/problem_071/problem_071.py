# My solution note: I scan denominators up to one million and keep the best fraction immediately left of 3/7.
import math

ss = 0

for n in range(100,10**6):
    x = math.floor(3*n/7)/n
    if x > ss and x != 3/7:
        ss = x
        a = n

print(ss, a, math.floor(3*a/7))

