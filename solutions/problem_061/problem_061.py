from itertools import permutations


# Solution note: I group four-digit figurate numbers by their first two digits,
# then join groups whose last two digits match the next first two digits.
def triangle(n):
    return n * (n + 1) / 2


def square(n):
    return n**2


def pentagonal(n):
    return n * (3 * n - 1) / 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return n * (5 * n - 3) / 2


def octagonal(n):
    return n * (3 * n - 2)


def four_digit_terms(function):
    ls = []
    i = 1
    while True:
        if function(i) < 10000 and function(i) > 999:
            ls.append(int(function(i)))
        i += 1
        if function(i) > 9999:
            break
    return ls


def ls_transform(ls):
    ls1 = []
    for i in range(0, 100):
        ls1.append([])
    for i in ls:
        s1, e1 = str(i)[0:2], str(i)[2:4]
        ls1[int(s1)].append([int(e1), i])
    return ls1


def ls_join(ls1, ls2):
    ls3 = []
    for i in range(0, 100):
        ls3.append([])
    for i in range(0, len(ls1)):
        if len(ls1[i]) == 0:
            pass
        else:
            for j in ls1[i]:
                if len(ls2[j[0]]) != 0:
                    for a in ls2[j[0]]:
                        ls3[i].append([a[0], a[1] + j[1]])
    return ls3


ls11 = ls_transform(four_digit_terms(triangle))
ls22 = ls_transform(four_digit_terms(square))
ls33 = ls_transform(four_digit_terms(pentagonal))
ls44 = ls_transform(four_digit_terms(hexagonal))
ls55 = ls_transform(four_digit_terms(heptagonal))
ls66 = ls_transform(four_digit_terms(octagonal))
ls_main = [ls11, ls22, ls33, ls44, ls55, ls66]

for p in permutations([0, 1, 2, 3, 4, 5]):
    ls_t = ls_join(ls_main[p[0]], ls_main[p[1]])
    ls_t = ls_join(ls_t, ls_main[p[2]])
    ls_t = ls_join(ls_t, ls_main[p[3]])
    ls_t = ls_join(ls_t, ls_main[p[4]])
    ls_t = ls_join(ls_t, ls_main[p[5]])
    for i in range(0, len(ls_t)):
        if len(ls_t[i]) != 0:
            for j in ls_t[i]:
                if j[0] == i:
                    print(j[1])
                    raise SystemExit
