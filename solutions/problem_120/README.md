# Problem 120: Square Remainders

[Project Euler problem 120](https://projecteuler.net/problem=120)

For `3 <= a <= 1000`, find the maximum remainder of `(a - 1)^n + (a + 1)^n` divided by `a^2`, then sum those maximum remainders.

## Solution

The solution uses the simplified remainder pattern: even powers give a remainder of 2, while odd powers reduce to `2*n*a mod a^2`. It checks the relevant odd powers for each `a`, keeps the largest remainder, and sums those maxima.
