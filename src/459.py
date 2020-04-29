"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies
of the substring together.

You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

Input: "aba"
Output: False
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        checks = [item for item in range(1, l) if l % item == 0]
        for v in checks:
            splits = [s[i:i + v] for i in range(0, l, v)]
            items = set(splits)
            if len(items) == 1:
                if list(items)[0] == s[0:v]:
                    return True
        return False

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not str:
            return False

        ss = s[1:] + s[:-1]
        return ss.find(s) != -1
