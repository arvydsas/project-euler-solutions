from p_euler import is_prime, prime_gen

def is_trunc_prime(n):
    if n < 10:
        return False
    for i in range(1,len(str(n))):
        if not(is_prime(int(str(n)[i:])) and is_prime(int(str(n)[:i]))):
            return False
    return True

print('Generating primes')
ls = prime_gen(1000000)
k = 0
s = 0
print('Checking for truncatable primes')
for i in ls:
    if is_trunc_prime(i):
        s += i
        k += 1
        print(i,' is a truncatable prime')
        if k==11:
            break
print('Sum of 11 truncatable primes is: ',s)
