# Problem 32: Pandigital Products

[Project Euler problem 32](https://projecteuler.net/problem=32)

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital number.

## Solution

The solution checks factor pairs, first filtering pairs with distinct nonzero digits and then checking whether the concatenation of the two factors and their product is 1 to 9 pandigital. Products are stored so duplicate identities do not get counted twice.
