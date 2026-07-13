def square_sum(a):
	sum=0
	for i in range(1,a+1):
		sum+=i**2
	return sum
c=(101*50)**2-square_sum(100)
file=open('a.txt','w')
file.write(str(c))
file.close()