"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        v = s.split()
        try:
            return len(s.split()[-1])
        except IndexError:
            return 0


# Tests

Solution.lengthOfLastWord("temp")
Solution.lengthOfLastWord(" ")