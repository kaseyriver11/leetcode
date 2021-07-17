"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        # Each letter could be the center
        winner = s[0]
        for i, l in enumerate(s):
            left = i - 1
            right = i + 1
            best = l
            while (left >= 0) & (right < len(s)):
                if s[left] == s[right]:
                    best = s[left:(right + 1)]
                    left -= 1
                    right += 1
                else:
                    left = -1
            if len(best) > len(winner):
                winner = best
        # A Pair of letters could be the center
        for i in range(0, len(s) - 1):
            if s[i] == s[i+1]:
                left = i - 1
                right = i + 2
                best = s[i:(i+2)]
                while (left >= 0) & (right < len(s)):
                    if s[left] == s[right]:
                        best = s[left:(right + 1)]
                        left -= 1
                        right += 1
                    else:
                        left = -1
                if len(best) > len(winner):
                    winner = best
        return winner

Solution().longestPalindrome(s="adcdddd")
