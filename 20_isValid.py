"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false
"""



left_items = dict()
left_items['('] = ')'
left_items['{'] = '}'
left_items['['] = ']'
left_items['0'] = '0'

# ----- Solution #1
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        current_open = ['0']

        for value in s:
            if value in left_items.keys():
                current_open.append(value)
            elif left_items[current_open[-1]] == value:
                current_open = current_open[0:len(current_open) - 1]
            else:
                return False
        if len(current_open) > 1:
            return False
        return True


Solution().isValid("()")



# ----- Solution #2
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return True
        s_map = {']': '[', '}': '{', ')': '('}
        items = [None]
        for letter in s:
            if letter in ['(', '{', '[']:
                items.append(letter)
            elif letter in s_map:
                if s_map[letter] == items[-1]:
                    items.pop()
                else:
                    items.append(letter)
            else:
                return False
        return len(items) == 1

# ----- Solution #2 based on:
class Solution:
    def isValid(self, s):
        if not s:
            return True
        mapping = {']':'[','}':'{',')':'('}
        stack = [None]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif i in mapping:
                if mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                return False
        return len(stack) == 1

Solution().isValid("{([])}")
