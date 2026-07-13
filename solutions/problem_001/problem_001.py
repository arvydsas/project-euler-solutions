# Solution note: I loop through the numbers below 1000 and accumulate the ones divisible by 3 or 5.
sum=0
for i in range (1,1000):
	if i%3==0 or i%5==0:
		sum+=i
print(sum)
