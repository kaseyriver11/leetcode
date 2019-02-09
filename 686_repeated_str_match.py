"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it;
B is not a substring of A repeated two times ("abcdabcd").

The length of A and B will be between 1 and 10000.

"""


class Solution(object):
    def repeatedStringMatch(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        l1 = len(s1)
        l2 = len(s2)
        s = s1

        for i in range(1, l2 // l1 + 2):
            if s.find(s2) != -1:
                return i
            else:
                s = s + s1
        return -1

Solution().repeatedStringMatch("abcd", "cdabcdab")

s1 = "abcd"

s2 = "cdabcdab"

l1 = len(s1)
l2 = len(s2)
s = s1

for i in range(1, l2 // l1 + 2):
    if s.find(s2) != -1:
        print(i)
    else:
        s = s + s1

s1 = "abc"
s2 = "cabcabca"

s1 + s1 + s1 + s1