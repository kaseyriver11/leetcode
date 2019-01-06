"""

Given two arrays, write a function to compute their intersection.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


"""

nums1 = [4, 5, 9]
nums2 = [9, 4, 9, 8, 4]


# ----- Solution #1
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        s1 = set(nums1)
        s2 = set(nums2)

        return [item for item in s1 if item in s2]


# ----- Solution #2
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        return list(set(nums1).intersection(set(nums2)))
