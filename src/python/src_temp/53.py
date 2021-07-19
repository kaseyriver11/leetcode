"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
    and return its sum.

Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums: list()) -> int:
        if max(nums) < 1:
            return max(nums)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=min(nums)
        m=0
        for i in range(len(nums)):
            m=max(m+nums[i],nums[i])
            if(m>maximum):
                maximum=m
        return maximum
