# My solution note: I generate spiral diagonal values layer by layer and track the prime ratio.
def is_prime(n): # checks if the number n is prime -- OPTIMISED USING 6K OPTIMISATION
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i**2 <= n:
        if (n % i == 0) or (n % (i+2) == 0):
            return False
        i+=6
    return True


n_primes = 0
i = 1

while True:
    side_length = 2*i + 1
    ls = [(2*i+1)**2 -6*i,(2*i+1)**2 -4*i, (2*i+1)**2 -2*i]
    for j in ls:
        if is_prime(j):
            n_primes += 1
    if n_primes/(4*i + 1) < 0.1: break
    i+=1 

print(2*i+1)

