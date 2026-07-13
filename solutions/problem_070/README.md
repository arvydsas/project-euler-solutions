# Problem 70: Totient Permutation

[Project Euler problem 70](https://projecteuler.net/problem=70)

Find the value of `n < 10,000,000` for which `phi(n)` is a digit permutation of `n` and `n / phi(n)` is minimized.

## My Solution

I compute phi(n), check digit permutations, and track the smallest n/phi(n) ratio.
