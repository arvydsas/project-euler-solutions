# Problem 33: Digit Cancelling Fractions

[Project Euler problem 33](https://projecteuler.net/problem=33)

Find the denominator of the product of the four non-trivial digit-cancelling fractions, when the product is written in lowest terms.

## Solution

The solution searches two-digit numerator/denominator pairs and keeps the non-trivial cases where cancelling a shared digit preserves the value of the fraction. It then multiplies those fractions together and reduces the product.
