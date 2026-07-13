def non_bouncy(n):
    a = str(n)[0]
    bool_a = True
    bool_b = True
    for i in str(n):
        if i > a:
            bool_a = False
        elif i < a:
            bool_b = False
        a = i
    return bool_a or bool_b

ss = 0

for i in range(0,10**6+6*10**5):
    if not non_bouncy(i):
        ss += 1
    if i > 10**6:
        if ss/i == 0.99:
            print(ss, i, ss/i)
            break





