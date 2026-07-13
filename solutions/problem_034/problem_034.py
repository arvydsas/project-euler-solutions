# Solution note: I compare each candidate number with the sum of precomputed digit factorials.
def factorialise(a):
	b=str(a)
	g=[1,1,2,6,24,120,720,5040,40320,362880]
	sum=0
	for i in b:
		j=int(i)
		sum+=g[j]
	return sum
sum=0
n=[]
for i in range(11,4000000):
	if i==factorialise(i):
		sum+=i
		n.append(i)
print(sum)
print(n)
