# My solution note: I generate primes and scan consecutive prime sums, printing prime sums found with long run lengths.
from p_euler import *

primes=prime_gen(1000000)

for i in range(99,1001,2):
    for j in range(0,len(primes)-i):
        if sum(primes[j:j+i])> 1000000:
            break
        if is_prime(sum(primes[j:j+i])):
            print(sum(primes[j:j+i]),i)

