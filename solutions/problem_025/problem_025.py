# Solution note: I iterate Fibonacci numbers until the current term reaches 1000 digits.
x=1
y=2
k=3
while True:
	k+=1
	if x>y:
		y+=x
		d=str(y)
	else:
		x+=y
		d=str(x)
	if len(d)==1000:
		break
print(k)
