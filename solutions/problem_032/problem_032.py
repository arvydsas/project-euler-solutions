# Solution note: I test factor/product identities whose concatenated digits are 1 to 9 pandigital.
def is_pandigital(num_str, n):
    if len(num_str) != n:
        return False
    ls = ['0']
    for i in num_str:
        if i not in ls:
            ls.append(i)
        else:
            return False
    return True


sum = 0
ls = []

for i in range(1, 10000):
    for j in range(1, i):
        if len(str(i) + str(j)) > 5:
            break
        if is_pandigital(str(i) + str(j), len(str(i) + str(j))):
            if is_pandigital(str(i) + str(j) + str(i * j), 9):
                if i * j not in ls:
                    sum += i * j
                    ls.append(i * j)

print(sum)
