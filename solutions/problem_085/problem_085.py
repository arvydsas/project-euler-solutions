import math
import time


ss = 10000
super_n = 0
super_m = 0
laikas = time.time()

for m in range(2,2000):
    c = 8*(10**6)/(m*(m+1))
    d = math.sqrt(1 + 4*c)
    n1 = math.floor((-1+d)/2)
    n2 = math.ceil((-1+d)/2)
    if abs(n1*(n1+1)*m*(m+1) - (8*10**6)) < ss:
        ss = abs(n1*(n1+1)*m*(m+1) - (8*10**6))
        super_n = n1
        super_m = m
    if abs(n2*(n2+1)*m*(m+1) - (8*10**6)) < ss:
        ss = abs(n2*(n2+1)*m*(m+1) - (8*10**6))
        super_n = n2
        super_m = m

print(super_n * super_m)
print(laikas - time.time())
