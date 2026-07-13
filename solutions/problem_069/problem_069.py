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
max=(0,0)
for i in range(1,1000001):
	if i%100000==0:
		print(i)
	a=i/tot(i)
	if a>max[0]:
		max=[a,i]
print(max)
	