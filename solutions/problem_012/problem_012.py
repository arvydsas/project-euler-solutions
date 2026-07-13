# My solution note: I factor consecutive triangular-number components to count divisors until the threshold is exceeded.
from pathlib import Path


def fac(a):
	f=[]
	for i in range(1,int(a/2+1)):
		if (a/i)%1==0:
			f.append(i)
	f.append(a)
	return f
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
n=0
d=0
p=1
for i in range (5,100000000000000000):
	a=primes(i)
	b=primes(i+1)
	a+=b
	a.sort()
	a.pop(0)
	c=1
	prod=1
	while c<=len(a):
		j=a[c-1]
		b=a.count(j)
		prod=prod*(b+1)
		c+=b
	if prod>500:
		break
print(prod)
print(int(i*(i+1)/2))

# Keep the original side-output beside this solution file.
file=open(Path(__file__).with_name('a.txt'),'w')
file.write(str(prod))
file.write('    ')
file.write(str(int(i*(i+1)/2)))
file.close()

