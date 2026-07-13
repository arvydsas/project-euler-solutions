# Solution note: I generate all powers in the requested range, sort them, and count distinct values.
pw=[]
for i in range(2,101):
	for j in range(2,101):
		pw.append(i**j)
pw.sort()
score=0
while len(pw)!=0:
	a=pw[0]
	pw.pop(0)
	if a in pw:
		pass
	else:
		score+=1
print(score)
