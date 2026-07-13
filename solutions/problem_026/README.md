# Problem 26: Reciprocal Cycles

[Project Euler problem 26](https://projecteuler.net/problem=26)

Find the value of `d < 1000` for which `1/d` contains the longest recurring cycle in its decimal fraction part.

## Solution

The solution simulates long division for each denominator and stores the seen quotient/remainder pairs. When a pair repeats, the distance back to its first occurrence is the recurring cycle length.
