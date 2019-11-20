"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
    and return its sum.
"""


class Solution(object):
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if max(nums) < 1:
            return max(nums)



Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

nums =  [-2, 1, -3, 4, -1, 2, 1, -5, 4]

negs = [i for i, item in enumerate(nums) if item < 0]

for i in negs:



s = 0
e = 1
for item in nums:
    total = input[0]

sum(nums[4:])

max(nums)
min(nums)


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
