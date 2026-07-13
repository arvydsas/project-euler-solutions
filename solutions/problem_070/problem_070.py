# Solution note: I compute phi(n), check digit permutations, and track the smallest n/phi(n) ratio.
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
def tot(n):
	ls=primes(n)
	ls1=[]
	prod=n
	for i in ls:
		if i in ls1:
			pass
		else:
			prod*=(1-1/i)
			ls1.append(i)
	return int(prod)

def n_list(n):
    ls = [0,0,0,0,0,0,0,0,0,0]
    for i in str(n):
        ls[int(i)] += 1
    return(ls)

def cc(l,k):
    for i in range(0,10):
        if l[i] != k[i]:
            return False
    return True

m = 1000

# Brute-force n and keep lowering the n / phi(n) ratio when phi(n) is a digit permutation.
for n in range(2,10**7):
    phi = tot(n)
    if cc(n_list(n),n_list(phi)):
        if m > n/phi:
            m = n/phi
            print(m, phi, n)
    


