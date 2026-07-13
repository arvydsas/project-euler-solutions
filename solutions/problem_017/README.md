# Problem 17: Number Letter Counts

[Project Euler problem 17](https://projecteuler.net/problem=17)

Count how many letters are used when writing the numbers from 1 to 1000 inclusive in words, ignoring spaces and hyphens and using British "and".

## Solution

The solution builds one long string containing the written form of every number from 1 through 1000, then prints the string length. The teen numbers are handled separately because names such as `fourteen`, `sixteen`, `seventeen`, and `nineteen` are not formed by simply joining `ten` with the unit word.
