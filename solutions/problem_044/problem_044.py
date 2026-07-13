# My solution note: I generate pentagonal numbers and search for a pair whose sum and difference are pentagonal.
def is_pentagonal(n):
    if ((1+24*n)**0.5)%6 == 5 :
        return True
    else:
        return False

ls=[1]
i=1
l=True

while l:
    ls.append(int(i*(3*i-1)/2))
    for j in range(1,i):
        if ls[i]-ls[j] in ls:
            if is_pentagonal(ls[i]+ls[j]):
                print(ls[i]-ls[j])
                l=False
    i+=1
            


