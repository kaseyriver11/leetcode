"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer,
the decimal digits are truncated and only the integer part of the result is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i**2 <= x:
            i += 1
        return i - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        return int(x ** (1/2))