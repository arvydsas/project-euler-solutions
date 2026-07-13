# Problem 69: Totient Maximum

[Project Euler problem 69](https://projecteuler.net/problem=69)

Find the value of `n <= 1,000,000` that maximizes `n / phi(n)`.

## Solution

I compute Euler totients by factoring each n, then track the largest n/phi(n) ratio.
