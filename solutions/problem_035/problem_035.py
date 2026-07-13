from p_euler import prime_gen, is_prime

def circ(n):
    a=str(n)
    if len(a)>1:
        if a[1]=='0':
            return 0
    return int(a[1:]+a[0])
print('Generating primes')
ls = prime_gen(1000000)
k = 0
print('Checking if primes are circular')
for i in ls:
    n = i
    for j in range(0,len(str(i))+2):
        n = circ(n)
        if not is_prime(n):
            n = 0
            break
    if n != 0:
        print(i)
        k += 1

print(k,' Circular primes encountered')

        
    
    

