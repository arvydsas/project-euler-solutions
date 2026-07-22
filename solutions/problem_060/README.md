# Problem 60: Prime Pair Sets

[Project Euler problem 60](https://projecteuler.net/problem=60)

Find the lowest sum for a set of five primes for which any two primes concatenate in either order to produce another prime.

## Solution

The solution generates primes up to 10000, records which prime pairs have the concatenation property, and then extends compatible groups from pairs to triples, quadruples, and finally quintuples. The first quintuple found gives the required minimum sum.
