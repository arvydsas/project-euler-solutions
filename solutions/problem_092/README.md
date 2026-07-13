# Problem 92: Square Digit Chains

[Project Euler problem 92](https://projecteuler.net/problem=92)

Count how many starting numbers below ten million arrive at 89 when repeatedly replacing the number by the sum of the squares of its digits.

## Solution

The solution first determines which small square-digit sums end at 1 or 89. For every starting number below ten million, it computes the first square-digit sum and uses that precomputed classification to count the chains ending at 89.
