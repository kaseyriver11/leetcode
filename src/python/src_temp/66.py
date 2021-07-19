"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        max_length = len(digits)
        for i in range(1, len(digits) + 1):
            if digits[-1 * i] < 9:
                digits[-1 * i] += 1
                break
            digits[-1 * i] = 0
            if i == len(digits):
                digits = [1] + digits
                break
        return digits
