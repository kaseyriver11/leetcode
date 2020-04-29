
"""
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""

# ----- Solution #1
th, hu, te, on = dict(), dict(), dict(), dict()
th[0], th[1], th[2], th[3] = "", "M", "MM", "MMM"
hu[0], hu[1], hu[2], hu[3], hu[4] = "", "C", "CC", "CCC", "CD"
hu[5], hu[6], hu[7], hu[8], hu[9] = "D", "DC", "DCC", "DCCC", "CM"
te[0], te[1], te[2], te[3], te[4] = "", "X", "XX", "XXX", "XL"
te[5], te[6], te[7], te[8], te[9] = "L", "LX", "LXX", "LXXX", "XC"
on[0], on[1], on[2], on[3], on[4] = "", "I", "II", "III", "IV"
on[5], on[6], on[7], on[8], on[9] = "V", "VI", "VII", "VIII", "IX"


# Solution #1:
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        thousand, num = divmod(num, 1000)
        hundred, num = divmod(num, 100)
        ten, one = divmod(num, 10)

        return th[thousand] + hu[hundred] + te[ten] + on[one]

Solution().intToRoman(1200)


# -----
lth = ["", "M", "MM", "MMM"]
lhu = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
lte = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
lon = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


# Solution #2:
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        thousand, num = divmod(num, 1000)
        hundred, num = divmod(num, 100)
        ten, one = divmod(num, 10)

        return lth[thousand] + lhu[hundred] + lte[ten] + lon[one]

Solution().intToRoman(1200)