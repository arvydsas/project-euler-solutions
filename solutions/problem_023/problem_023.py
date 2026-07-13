# Solution note: I generate abundant numbers, mark sums of pairs, and add the values that never appear as such a sum.
def prime_fac(n):
    ls=[]
    for i in range(2,n+1):
        while n%i == 0:
            ls.append(i)
            n=int(n/i)
    return ls

def bin_push(ls):
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
                

def divisors(n):
    ls2 =[1]
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

ls=[]
ls1=[]

# First collect the abundant numbers below the known upper bound.
for i in range(2,28124):
    if sum(divisors(i)) > 2*i:
        ls.append(i)
        print(i)

# Then record every value that can be written as a sum of two abundant numbers.
for i in range(0,len(ls)):
    print(ls[i])
    for j in range(i,len(ls)):
        if ls[i]+ls[j]>28123:
            break
        elif ls[i]+ls[j] not in ls1:
            ls1.append(ls[i]+ls[j])

sum=0

# Anything never marked in ls1 contributes to the final answer.
for i in range(1,28124):
    if i not in ls1:
        sum+=i
print(sum)

#runtime ~45 min
    

