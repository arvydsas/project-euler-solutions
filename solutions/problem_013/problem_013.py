# My solution note: I read the provided large numbers from the local data file, print the running additions, and output the final sum.
from pathlib import Path


file1=open(Path(__file__).with_name('b.txt'),'r')
line='00'
sum=0
while line != 'X':
	line=file1.readline()
	if line=='X\n' or line=='X':
		break
	line=int(line[0:len(line)])
	print(line)
	sum+=line
	print (sum)
print(sum)

