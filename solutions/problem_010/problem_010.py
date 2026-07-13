# Solution note: I generate primes below two million and sum them.
def prime_gen(a):
	a=int(a)
	p=[2]
	for i in range(3,a+1):
		c=0
		for j in p:
			if j>i**.5:
				break
			if i%j==0:
				c+=1
				break
		if c==0:
			p.append(i)
	return p
p=prime_gen(2000000)
print(len(p))
print(sum(p))
