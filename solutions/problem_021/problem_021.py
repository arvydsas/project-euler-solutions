# My solution note: I use divisor sums to identify amicable pairs below 10000 and add the matching values.
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
def div_sum(a):
	divisors=[]
	for i in range(1,a//2+1):
		if (a/i)%1==0:
			divisors.append(i)
	return sum(divisors)
amicable=[]
for i in range(1,10001):
	print(i)
	if i!=div_sum(i) and i==div_sum(div_sum(i)):
		amicable.append(i)
print(sum(amicable))
print(amicable)
