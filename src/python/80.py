"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to
0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        current_value = nums[0]
        nums_length = 1
        current_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                current_count += 1
                if current_count > 2:
                    continue
                nums[nums_length] = nums[i]
                nums_length += 1
            else:
                nums[nums_length] = nums[i]
                nums_length += 1
                current_count = 1
        return nums_length


Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3])
