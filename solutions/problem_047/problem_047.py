import math

def is_integer(n):
    if math.ceil(n) - math.floor(n) == 1:
         return False
    else:
        return True
    

def dist_factors(n):
    ls=[]
    for i in range(2,n+1):
        if i>n:
            break
        while is_integer(n/i):
            n=n/i
            if i not in ls:
                ls.append(i)
    return ls

def final(n):
    k=0
    for i in range(100000,200000):
        print(i)
        if len(dist_factors(i))==n:
            k+=1
        else:
            k=0
        if k==n:
            return i-k+1
    return 'insuficient range'
print(final(4))
