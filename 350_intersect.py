"""
Given two arrays, write a function to compute their intersection.

Ex: 1
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Ex: 2
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

# ----- Solution #1:
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        intersection = list(set(nums1).intersection(set(nums2)))
        list_of_lists = [[item] * min(nums1.count(item), nums2.count(item)) for item in intersection]
        return [item for sublist in list_of_lists for item in sublist]

Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])


# ----- Solution #2:
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        seen = {}

        if len(nums1) >= len(nums2):
            l1 = nums1
            l2 = nums2
        else:
            l1 = nums2
            l2 = nums1

        for element in l1:
            if element in seen.keys():
                seen[element] += 1
            else:
                seen[element] = 1
        for element in l2:
            if element in seen.keys() and seen[element] > 0:
                result.append(element)
                seen[element] -= 1
        return result


Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
