def fac(a):
	b=1
	if a==0 or a==1:
		return 1
	if a==2:
		return 2
	if a==3:
		return 6
	if a==4:
		return 24
	if a==5:
		return 120
	if a==6:
		return 720
	if a==7:
		return 5040
	if a==8:
		return 40320
	if a==9:
		return 362880
a2=[]
for i in range(1,1000001):
	b=i
	a1=[i]
	while len(a1)<=60:
		sum=0
		for j in str(b):
			sum+=fac(int(j))
		if sum in a1:
			if len(a1)==60:
				a2.append(i)
				print(i)
			break
		a1.append(sum)
		b=sum
print(a2)
print(len(a2))		