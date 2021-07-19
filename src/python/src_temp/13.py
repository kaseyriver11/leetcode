"""

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together.
12 is written as, XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999

"""

d = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
st = dict(I=None, V="I", X="I", L="X", C="X", D="C", M="C")


# ----- Solution #1
class Solution:
    def romanToInt(self, s):
        left = len(s) - 1
        val = 0
        while left >= 0:
            if (st[s[left]] == s[left - 1]) and left - 1 >= 0:
                val += d[s[left]] - d[st[s[left]]]
                left -= 2
                print(val)
                print("top")
            else:
                val += d[s[left]]
                left -= 1

        return val


# ----- Solution #2
d = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
st = dict(I=["V", "X"], X=["L", "C"], C=["D", "M"], V=[], L=[], D=[], M=[])


class Solution:
    def romanToInt(self, s):
        place = len(s) - 1
        val = 0
        while place >= 0:
            if (s[place] in st[s[place - 1]]) and place - 1 >= 0:
                val += d[s[place]] - d[s[place - 1]]
                place -= 2
            else:
                val += d[s[place]]
                place -= 1

        return val


Solution().romanToInt("CXXIII")
Solution().romanToInt("MCMXCIX")
Solution().romanToInt("LVIII")
