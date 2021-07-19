"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List
import numpy as np

class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return len(np.where(np.array(nums) < target)[-1])



# Tests
Solution.searchInsert(nums = [1,3,5,6], target = 5)
Solution.searchInsert(nums = [1,3,5,6], target = 2)
