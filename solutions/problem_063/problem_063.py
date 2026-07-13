# Solution note: I count nth powers that have exactly n digits using a direct formula-driven loop.
import math
ss = 0
for n in range(1,1000):
    ss += math.floor(10*(1-10**(-1/n)))
    if math.floor(10*(1-10**(-1/n))) < 1:
        break
print(ss)

