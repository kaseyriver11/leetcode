"""

Given a string, find the length of the longest substring without repeating characters.


Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

# ----- Solution #1
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0:
            d = {}
            max_d = {}
            for i, letter in enumerate(s):
                val = s[(i + 1):].find(letter)
                if val == -1:
                    d[i] = len(s)
                elif val == 0:
                    d[i] = i + 1
                else:
                    d[i] = val + i + 1

            for i in d:
                max_d[i] = d[i] - i

            for item in d:
                for i in range(item + 1, d[item]):
                    if d[item] > d[i]:
                        max_d[item] = min(d[i] - item, max_d[item])
            return max([max(max_d.values()), 1])
        return 0


# ----- Solution #2:
class Solution:
    def lengthOfLongestSubstring(self, string):
        """
        Time:  O(n)
        Space: O(k)
        [k = length of the longest substring w/o repeating characters]
        """
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(string[left])
                left += 1
        return longest


# ----- Solution #3:
class Solution:
    def lengthOfLongestSubstring(self, string):
        max_d = 0
        left_place, right_place = 0, 0
        letters = set()

        while right_place < len(string):
            if string[right_place] not in letters:
                letters.add(string[right_place])
                right_place += 1
                max_d = max(max_d, right_place - left_place)
            else:
                letters.remove(string[left_place])
                left_place += 1

        return max_d


Solution().lengthOfLongestSubstring("cdd")
Solution().lengthOfLongestSubstring("abcabcbb")
Solution().lengthOfLongestSubstring("au")
Solution().lengthOfLongestSubstring(" ")
Solution().lengthOfLongestSubstring("jlygy")
Solution().lengthOfLongestSubstring("uqinntq")

