"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    @staticmethod
    def twoSum(nums: list, target: int) -> list:
        """
        This problem tests the use of a map. We want to store the index of the matching value.
        For example, if the first number is 2 and the target is 9, the value we want to is 7.
        Store the key 7, with the index corresponding to 2. 
        """
        target_dict = dict()

        for index, number in enumerate(nums):
            if number in target_dict:
                return [target_dict[number], index]
            target_dict[target - number] = index

# ----- Test
nums = [2, 7, 11, 15]
target = 9
Solution.twoSum(nums, target)
