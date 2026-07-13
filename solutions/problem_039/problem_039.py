max=0
sols=[]
for p in range(1,1001):
	sol=[]
	for i in range(1,p):
		for j in range(1,p):
			if i**2+j**2==(p-i-j)**2 and p-i-j>0:
				sol.append([i,j,p-i-j])
	if len(sol)>max:
		max=len(sol)
		print(p)

					