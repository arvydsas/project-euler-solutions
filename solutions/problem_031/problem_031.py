import math

def ways(n):
    ls = [200,100,50,20,10,5,2,1]
    s = 0 
    if n[0] == 0:
        return 1
    if len(ls) == n[1]:
        return 0
    if ls[n[1]] <= n[0]:
        for i in range(1,math.floor(n[0]/ls[n[1]])+1):
            s += ways((n[0]-i*ls[n[1]],n[1]+1))
    s+=ways((n[0],n[1]+1))
    return s


print(ways((200,0)))

