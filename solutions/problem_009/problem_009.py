# Solution note: I search possible triples until the Pythagorean condition and the required total are both met.
for i in range(1,1001):
	for j in range(1,1001):
		if (i**2+j**2)**0.5+i+j==1000:
			a=i
			b=j
			break
			break
print(a,b)
			
