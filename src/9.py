"""

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Could you solve it without converting the integer to a string?
"""
import math


# ----- Solution #1:
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True

        digits = int(math.log10(x))
        tests = (digits + 1) // 2
        l1 = [x // 10 ** digits]
        new_val = x - l1[0] * 10**digits

        for i in range(digits - 1):
            l1.append(new_val // 10 ** (digits - i - 1))
            new_val = new_val - l1[i+1] * 10 ** (digits - i - 1)
        l1.append(new_val)

        for i in range(tests):
            if l1[i] != l1[-i - 1]:
                return False
        return True


# ----- Solution #2:
class Solution:
    def isPalindrome(self, x):
        a = str(x)
        return a == a[::-1]


# ----- Solution #3:
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True

        digits = int(math.log10(x))
        tests = (digits + 1) // 2
        l1 = [x // 10 ** digits]
        new_val = x - l1[0] * 10**digits

        for i in range(digits - 1):
            l1.append(new_val // 10 ** (digits - i - 1))
            new_val = new_val - l1[i+1] * 10 ** (digits - i - 1)
        l1.append(new_val)

        for i in range(tests):
            if l1[i] != l1[-i - 1]:
                return False
        return True


Solution().isPalindrome(
    12345678999999999999999999999999999999999999999999999999999999999999999999999999999999987654321)
