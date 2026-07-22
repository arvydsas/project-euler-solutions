# Problem 61: Cyclical Figurate Numbers

[Project Euler problem 61](https://projecteuler.net/problem=61)

Find the sum of the only ordered set of six cyclic four-digit numbers, where each number is a different figurate type from triangle through octagonal.

## Solution

The solution builds four-digit values for each figurate type and groups them by their first two digits. It then tries every order of the six figurate types, repeatedly joining chains where the ending two digits of one number match the starting two digits of the next, and prints the sum when the chain closes cyclically.
