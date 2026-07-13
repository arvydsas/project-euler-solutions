# My solution note: I build amicable chains using divisor sums, pruning numbers as chains are classified.
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

def div_sum(n):
    return(sum(divisors(n)) - n)

max_length = 0
min_element = 0
ls_n = []

# Keep a removable list of candidates so chains already ruled out are not revisited.
for n in range(3,10**6):
    ls_n.append(n)

print('ls_n initialized')




for n in ls_n:
    chain = [n]
    if n%1000 == 0:
        print(n,len(ls_n))
    while True:
        n = div_sum(n)
        # Stop chains that leave the allowed range or hit a number already removed.
        if n >= 10**6 or n not in ls_n:
            for i in chain:
                ls_n.remove(i)
            break
        elif n in chain:
            # A repeated value means the tail of the current path is an amicable chain.
            chain = chain[chain.index(n):]
            if len(chain) > max_length:
                max_length = len(chain)
                min_element = min(chain)
                print(n, chain)
            for i in chain:
                ls_n.remove(i)
            break
        chain.append(n)




    
print(max_length, min_element)







