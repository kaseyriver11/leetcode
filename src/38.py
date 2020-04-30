"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Input: 1
Output: "1"

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        v = "1"
        for i in range(2, n+1):
            j = 1
            count = 1
            new_v = ""
            while j < len(v):
                if v[j-1] == v[j]:
                    count += 1
                else:
                    new_v += str(count) + str(v[j-1])
                    count = 1
                j += 1
            new_v += str(count) + str(v[j-1])
            v = new_v
        return v

Solution().countAndSay(4)
