# My solution note: I use Decimal square roots and sum the first 100 digits for irrational roots below 100.
from __future__ import print_function

from math import sqrt
from decimal import Decimal, getcontext


getcontext().prec = 102

total = 0
for a in range(100):
    if not sqrt(a) % 1 == 0:
        ans = str(Decimal(a).sqrt()).replace('.', '')[:100]
        digits = map(int, ans)
        '''print(a, sum(digits), "--------", sep='\n')'''
        total += sum(digits)



print(total)

