# My solution note: I compute continued-fraction periods for square roots and count odd periods.
import math

def root_per(n):
    if n**0.5 % 1 == 0:
        return 0 
    i = 0
    root = math.sqrt(n)
    ls_a = [math.floor(root)]
    ls_l = [1]
    ls_h = [1]
    ls_k = [math.floor(root)]
    frac = ls_l[i]/(ls_h[i]*root - ls_k[i])
    while True:
        ls_a.append(math.floor(frac))
        x = ls_l[i]*ls_h[i]
        y = ls_h[i]**2 * n - ls_k[i]**2
        z = ls_k[i]*ls_l[i]
        d = math.gcd(math.gcd(x,y),z)
        if d != 1:
            x = int(x/d)
            y = int(y/d)
            z = int(z/d)
        ls_l.append(y)
        ls_h.append(x)
        ls_k.append(-z+y*ls_a[i+1])
        i += 1
        frac = ls_l[i]/(ls_h[i]*root - ls_k[i])
        if ls_h[i] == ls_h[0] and ls_l[i] == ls_l[0] and ls_k[i] == ls_k[0]:
            break
    return len(ls_a)-1

ss = 0

for i in range(1,10001):
    if root_per(i) % 2 == 1:
        ss+=1

print(ss)

