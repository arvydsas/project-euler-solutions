# Solution note: I build Champernowne's decimal string directly and multiply the requested indexed digits.
stri=''
for i in range(1,1000000):
	stri+=str(i)
prod=int(stri[99])*int(stri[999])*int(stri[9999])*int(stri[99999])*int(stri[999999])
print(prod)
