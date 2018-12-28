"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# ----- Solution #1 - 18.93%
def convert(a_list):
    a = str(a_list.val)
    next_node = a_list.next
    while next_node:
        a = a + str(next_node.val)
        next_node = next_node.next
    return int(a[::-1])


class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        int1 = convert(l1)
        int2 = convert(l2)

        final_int = int1 + int2

        return [int(x) for x in str(final_int)[::-1]]


# ----- Solution #2 - 15.23%
def convert(a_list):
    val = [a_list.val]
    while a_list.next:
        val = val + [a_list.next.val]
        a_list = a_list.next
    return sum([item * 10**i for i, item in enumerate(val)])

class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        int1 = convert(l1)
        int2 = convert(l2)
        final_int = int1 + int2
        return [int(x) for x in str(final_int)[::-1]]


# ----- Solution #3 - 30.60%
class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        v = 0
        a = []
        while l1 or l2:
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next

            a.append(v % 10)
            v //= 10

        if v != 0:
            a.append(v)

        return a


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node11 = ListNode(5)
node22 = ListNode(6)
node33 = ListNode(4)
node11.next = node22
node22.next = node33


l1 = node1
l2 = node11

Solution.addTwoNumbers(l1, l2)

# ----- Solution #4
class Solution(object):
    @staticmethod
    def addTwoNumbers(l1, l2):
        end_result = ListNode(0)
        result_tail = end_result
        carry = 0

        while l1 or l2 or carry:
            val1 = (carry + l1.val if l1 else carry)
            val2 = (val1 + l2.val if l2 else val1)
            carry, out = divmod(val2, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return end_result.next
