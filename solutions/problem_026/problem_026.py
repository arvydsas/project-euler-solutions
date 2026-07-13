# Solution note: I track long-division remainders to find the recurring cycle length.
def rep_cycle(n):
    ls = []
    dividend = 1
    remainder = 0
    divisor = n
    buffer = 0
    while True:
        if dividend / divisor == 1 or dividend == 0:
            return 0
        remainder = dividend % divisor
        buffer = dividend // divisor
        dividend = remainder * 10
        if (buffer, remainder) not in ls:
            ls.append((buffer, remainder))
            buffer = 0
            remainder = 0
        else:
            return len(ls) - ls.index((buffer, remainder))


max_cycle = (0, 0)

for i in range(1, 1000):
    cycle = rep_cycle(i)
    if cycle > max_cycle[0]:
        max_cycle = (cycle, i)

print(max_cycle[1])
