# My solution note: I generate primes by trial division until reaching the requested prime index.
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
a=prime_gen(1000000)
c=a[10000]
file=open('a.txt','w')
file.write(str(c))
file.close()
print(c)
