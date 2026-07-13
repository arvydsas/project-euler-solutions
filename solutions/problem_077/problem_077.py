# My solution note: I recursively count representations of 71 as a sum of primes.
import math

def budai(n,ls):
    if n == 0:
        return 1
    elif len(ls) == 0:
        return 0
    ls1 = []
    for i in range(0,len(ls)-1):
        ls1.append(ls[i])
    den = ls[-1]
    n1 = n
    ss = 0
    for i in range(0,math.floor(n1/den) + 1):
        ss += budai(n1 - i*den,ls1)
    return ss

def prime_gen(a): #returns a list of primes less than or equal to a. -- NOT OPTIMISED  
	a=int(a)
	p=[2]
	for i in range(3,a+1):
		c=0
		for j in p:
			if j>i**.5:
				break
			if i%j==0:
				c+=1
				break
		if c==0:
			p.append(i)
	return p



print(budai(71,prime_gen(71)))

    

