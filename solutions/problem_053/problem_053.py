# Solution note: I build factorials up to 100 and count combinations larger than one million.
ls = [1]
for i in range(1, 101):
    ls.append(max(ls) * i)

ss = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        c = int(ls[n] / (ls[r] * ls[n - r]))
        if c > 1000000:
            ss += 1

print(ss)
