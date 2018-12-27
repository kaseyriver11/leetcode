"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import time

n = range(2000)
t = 2500


# ----- Solution #1: First attempted solution
class Solution:
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, value in enumerate(nums):
            for j, value2 in enumerate(nums):
                if value + value2 == target:
                    if i != j:
                        return [i, j]


ts = time.time()
[Solution.twoSum(n, t) for item in range(10)]
print((time.time() - ts)*1000)


# ----- Final Solution Used
class Solution:
    @staticmethod
    def twoSum(nums, target):
        c_map = {}
        for i, value in enumerate(nums):
            if value in c_map:
                return [c_map[value], i]
            c_map[target - value] = i


ts = time.time()
[Solution.twoSum(n, t) for item in range(1000)]
print((time.time() - ts)*1000)
