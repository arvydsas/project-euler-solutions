import math

def ff(n):
    for i in range(0,17,2):
        if int(str(n)[i]) - int(i/2 + 1) != 0:
            return(False)
    return(True)








n_min = 10203040506070809
n_max = 19293949596979899

for i in range(int(math.sqrt(n_min)/10),int(math.sqrt(n_max)/10)):
    n_min_3 = i*10 + 3
    n_min_7 = i*10 + 7
    if ff(n_min_3**2) or ff(n_min_7**2):
        print(n_min_3,n_min_7)
        break
    elif i%10**5 == 0:
        print(i)

