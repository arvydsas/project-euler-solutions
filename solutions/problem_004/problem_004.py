# Solution note: I brute-force products of three-digit numbers and keep the largest one that reads the same backwards.
b=0
pol=[]
for i in range(100,1000):
	for j in range(100,1000):
		a=i*j
		if a>900000:
			a1=a%10
			a2=int((a%100-a1)/10)
			a3=int((a%1000-a1-10*a2)/100)
			a4=int((a%10000-a1-10*a2-100*a3)/1000)
			a5=int((a%100000-a1-10*a2-100*a3-1000*a4)/10000)
			a6=int((a-a1-10*a2-100*a3-1000*a4-10000*a5)/100000)
			if a1==a6 and a2==a5 and a3==a4:
				if a>b:
				 b=a
				 pol.append(b)
print (b,pol)
