"""
Given a 32-bit signed integer, reverse digits of an integer.
"""
import numpy as np


# ----- Solution #1
class Solution:
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)
        if x < 0:
            a = a.replace("-", "")
            a = -1 * int(a[::-1])
        else:
            a = int(a[::-1])

        if abs(a) > 2147483647:
            return 0
        else:
            return a

Solution.reverse(15)


# ----- Solution #2
class Solution:
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            a = -1 * int(str(abs(x))[::-1])
        else:
            a = int(str(x)[::-1])

        if abs(a) > 2147483647:
            return 0
        else:
            return a

Solution.reverse(15)