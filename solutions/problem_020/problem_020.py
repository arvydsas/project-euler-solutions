# Solution note: I compute 100! with a small factorial helper and sum the digits.
def fac(x):
	prod=1
	for i in range(1,x+1):
		prod*=i
	return prod
a=str(fac(100))	
sum=0
for i in a:
	sum+=int(i)
print(sum)
