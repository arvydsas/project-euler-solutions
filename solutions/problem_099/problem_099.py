import math
from pathlib import Path

#Reading the file
file = open(Path(__file__).with_name("a.txt"), "r")

mm = 0

for n in range(0,1000):
    
    words = file.readline()

    snumber = ''
    ls = []

    for i in words:
        if i != ',':
            snumber += i
        else:
            ls.append(int(snumber))
            snumber = ''
    ls.append(int(snumber))
    if(math.log10(ls[0])*ls[1]) > mm:
        mm = math.log10(ls[0])*ls[1]
        l_number = n

print(l_number + 1,mm)

