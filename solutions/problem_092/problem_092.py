# Solution note: I classify small square-digit chains, then use those classes for every number below ten million.
def dig_sq(n):
    ss = 0
    for i in str(n):
        ss += int(i) ** 2
    return ss


ls_1 = []
ls_89 = []

for i in range(1, 1000):
    a = i
    while True:
        if a == 1:
            ls_1.append(i)
            break
        elif a == 89:
            ls_89.append(i)
            break
        else:
            a = dig_sq(a)

ss_89 = 0

for i in range(1, 10**7):
    c = dig_sq(i)
    if c in ls_1:
        pass
    else:
        ss_89 += 1

print(ss_89)
