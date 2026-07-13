# Solution note: I compute 2^1000 directly and sum its decimal digits.
a=2**1000
sum=0
for i in str(a):
	sum+=int(i)
print(sum)
