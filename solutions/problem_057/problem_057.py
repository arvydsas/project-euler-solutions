import math

def is_prime(n): # checks if the number n is prime -- OPTIMISED USING 6K OPTIMISATION
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i**2 <= n:
        if (n % i == 0) or (n % (i+2) == 0):
            return False
        i+=6
    return True

def is_palindrome(n): # checks if the number n is a palindrome USES MATH 
    number=str(n)
    for i in range(0,math.floor(len(number)/2)):
        if number[i] != number[-1-i]:
            return False
    return True

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
    
def prime_fac(n): #returns prime factors of a number n -- NOT OPTIMISED
    ls=[]
    for i in range(2,n+1):
        while n%i == 0:
            ls.append(i)
            n=int(n/i)
    return ls

def bin_push(ls): #used in divisors
    if len(ls) == sum(ls):
        return ls
    k=0
    for i in ls:
        if i == 0:
            ls[k] = 1
            return ls
        else:
            ls[k] = 0
            k+=1
                
def is_prime(n): # checks if the number n is prime -- OPTIMISED USING 6K OPTIMISATION
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i**2 <= n:
        if (n % i == 0) or (n % (i+2) == 0):
            return False
        i+=6
    return True

def is_palindrome(n): # checks if the number n is a palindrome USES MATH 
    number=str(n)
    for i in range(0,math.floor(len(number)/2)):
        if number[i] != number[-1-i]:
            return False
    return True

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
    
def prime_fac(n): #returns prime factors of a number n -- NOT OPTIMISED
    ls=[]
    for i in range(2,n+1):
        while n%i == 0:
            ls.append(i)
            n=int(n/i)
    return ls

def bin_push(ls): #used in divisors
    if len(ls) == sum(ls):
        return ls
    k=0
    for i in ls:
        if i == 0:
            ls[k] = 1
            return ls
        else:
            ls[k] = 0
            k+=1
                

def divisors(n):  # Returns divisors of a number n , does not use recursion -- NOT OPRIMISED
    ls2 =[1]      # USES prime_fac bin_push
    ls1 = prime_fac(n)
    ls3 = []
    for i in range(1, len(ls1)+1):
        ls3.append(0)
    while sum(ls3) != len(ls1):
        ls3 = bin_push(ls3) 
        divisor = 1
        for i in range(0,len(ls1)):
            if ls3[i] == 1:
                divisor*=ls1[i]
        if divisor not in ls2:
            ls2.append(divisor)
    return ls2

def divisors(n):  # Returns divisors of a number n , does not use recursion -- NOT OPRIMISED
    ls2 =[1]      # USES prime_fac bin_push
    ls1 = prime_fac(n)
    ls3 = []
    for i in range(1, len(ls1)+1):
        ls3.append(0)
    while sum(ls3) != len(ls1):
        ls3 = bin_push(ls3) 
        divisor = 1
        for i in range(0,len(ls1)):
            if ls3[i] == 1:
                divisor*=ls1[i]
        if divisor not in ls2:
            ls2.append(divisor)
    return ls2

ss = 0
b = 1
c = 1

for i in range(1,1001):
    b = b + 2*c
    c = b - c
    if len(str(b)) > len(str(c)):
        ss+=1
        print(i, 'YES')
print(ss)
