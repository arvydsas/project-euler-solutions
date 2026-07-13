# Problem 53: Combinatoric Selections

[Project Euler problem 53](https://projecteuler.net/problem=53)

Count how many values of `nCr`, for `1 <= n <= 100`, are greater than one million.

## Solution

The solution precomputes factorials up to 100, evaluates each relevant combination value directly, and counts the ones above one million.
