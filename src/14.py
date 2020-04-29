"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: ["flower", "flow", "flight"]
Output: "fl"

Input: ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

# Solution #1
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        m = min([len(item) for item in strs])
        for value in range(m, 0, -1):
            if all(x[0:value] == strs[0][0:value] for x in strs):
                return strs[0][0:value]
        if len(strs) == 1:
            return strs[0]
        else:
            return ""

strs = ["flower", "flow", "flight"]
Solution().longestCommonPrefix(strs)
