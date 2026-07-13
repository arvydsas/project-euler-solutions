# My solution note: I sum Euler totients for denominators up to one million.
def primes(n):
	primfac = []
	d = 2
	while d*d <= n:
		while (n % d) == 0:
			primfac.append(d)
			n/=d
		d+=1
	if n > 1:
		n=int(n)
		primfac.append(n)
	return primfac
def tot(n):
	ls=primes(n)
	ls1=[]
	prod=n
	for i in ls:
		if i in ls1:
			pass
		else:
			prod*=(1-1/i)
			ls1.append(i)
	return int(prod)

ss = -1
for i in range(1,(10**6)+1):
    ss += tot(i)
    if i%10**5 == 0:
        print(i)
print(ss)
    

