# Solution note: I build prime-concatenation compatibility lists and extend
# compatible prime groups until a set of five is found.
def prime_gen(a):
    a = int(a)
    p = [2]
    for i in range(3, a + 1):
        c = 0
        for j in p:
            if j > i**0.5:
                break
            if i % j == 0:
                c += 1
                break
        if c == 0:
            p.append(i)
    return p


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i**2 <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True


def con_prime(prime1, prime2):
    return is_prime(int(str(prime1) + str(prime2))) and is_prime(int(str(prime2) + str(prime1)))


primes = prime_gen(10**4)
prime_n = len(primes)

ls = []
for i in range(0, prime_n):
    ls.append([0] * prime_n)

for i in range(0, prime_n):
    for j in range(0, prime_n):
        if con_prime(primes[i], primes[j]):
            ls[i][j] = 1

ls2 = []
for i in range(0, prime_n):
    ll = []
    for j in range(0, prime_n):
        if ls[i][j] == 1:
            ll.append(primes[j])
    ls2.append(ll)

ls3 = []
for i in range(0, prime_n):
    for j in ls2[i]:
        for k in range(0, prime_n):
            if primes[i] in ls2[k] and j in ls2[k]:
                ls3.append((primes[i], j, primes[k]))

ls4 = []
for i in ls3:
    for j in range(0, prime_n):
        if i[0] in ls2[j] and i[1] in ls2[j] and i[2] in ls2[j]:
            ls4.append([i[0], i[1], i[2], primes[j]])

ls5 = []
for i in ls4:
    for j in range(0, prime_n):
        if i[0] in ls2[j] and i[1] in ls2[j] and i[2] in ls2[j] and i[3] in ls2[j]:
            ls5.append([i[0], i[1], i[2], i[3], primes[j]])

print(sum(ls5[0]))
