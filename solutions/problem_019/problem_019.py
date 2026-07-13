# My solution note: I simulate calendar days from 1901 through 2000 and count Sundays that land on the first of a month.
year = 1901
month = 1
day = 1
weekday = 2

def not_leap(year):
    if year % 4 == 0:
        if (year % 100!=0) or (year % 400 == 0):
            return False
    return True

def time(year, month, day, weekday):
    if weekday != 7:
        weekday += 1
    else:
        weekday = 1
    if day < 28:
        day += 1
    elif day == 28 and month == 2 and not_leap(year):
        month += 1
        day = 1
    elif day == 28 and ((month == 2 and not not_leap(year)) or month != 2):
        day+=1
    elif day == 29 and month == 2:
        day = 1
        month += 1
    elif day == 29:
        day+=1
    elif day == 30 and month in [4,6,9,11]:
        day = 1
        month += 1
    elif day == 30:
        day += 1
    elif day == 31 and month != 12:
        day = 1
        month += 1
    else:
        day = 1
        month = 1
        year += 1

    return [year, month, day, weekday]

ls=[year, month, day, weekday]
s=0

while ls[0] != 2001:
    if ls[3] == 7 and ls[2] == 1:
        s+=1
    ls=time(ls[0],ls[1],ls[2],ls[3])
    if ls[0] % 2000 ==0:
        print(ls)
print(s)

