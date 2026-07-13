# My solution note: I test candidate numbers against the sum of the fifth powers of their digits.
ls=[]
for i in range(2,1000000):
	a=str(i)
	sum=0
	for j in a:
		sum+=int(j)**5
	if i==sum:
		ls.append(i)
sum=0
for i in ls:
	sum+=i
print(sum)
