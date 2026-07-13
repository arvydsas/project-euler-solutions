# Solution note: I compute the central binomial coefficient through factorials and write the answer to the local side-output file.
from pathlib import Path


def fac(x):
	prod=1
	for x in range(1,x+1):
		prod*=x
	return prod
g=Path(__file__).with_name('a.txt')
a=fac(40)
b=fac(20)
c=a/b**2
c=int(c)
print(c)
file=open(g,'w')
file.write(str(c))
file.close()

