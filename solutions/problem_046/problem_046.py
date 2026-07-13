# Solution note: I test odd composite numbers against Goldbach's other conjecture until one fails.
def primes(n):
	ps, sieve = [], [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			ps.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return ps
k=1
while True:
	Bool=False
	k+=2
	prime=primes(k)
	if k in prime:
		pass
	else:
		for i in prime:
			z=((k-i)/2)**0.5
			if z.is_integer():
				Bool=True
		if not Bool:
			break
print(k)
