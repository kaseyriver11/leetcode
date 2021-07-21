"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def listNodeToVal(ln):
        value = 0
        count = 0
        while ln.next:
            value += ln.val * 10**count
            count +=1
            ln = ln.next
        value += ln.val * 10**count
        return value

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """List nodes are a newer concept to me. Here are the steps I took.

        1. Convert the list node to a value
        2. Convert this value to its reverse
        3. Create a new ListNode to output
        """
        v3 = self.listNodeToVal(l1) + self.listNodeToVal(l2)
        final_list = [int(x) for x in str(v3)[::-1]]
        final_ln = ListNode(final_list[0])
        if len(final_list) > 0:
            temp_ln = final_ln
            for val in final_list[1:]:
                temp_ln.next = ListNode(val)
                temp_ln = temp_ln.next
        return final_ln

# Create an example
example_list = [1, 2, 3]
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

%timeit -n 100 Solution().addTwoNumbers(l1, l1)


# Profile list node to string
def listNodeToInt(listNode):
    s1 = ""
    while listNode.next:
        s1 += str(listNode.val)
        listNode = listNode.next
    s1 += str(listNode.val)
    return int(s1[::-1])
%timeit -n 100 listNodeToInt(l1)

# What about keeping it as an integer
def listNodeToVal(ln):
    value = 0
    count = 0
    while ln.next:
        value += ln.val * 10**count
        count +=1
        ln = ln.next
    value += ln.val * 10**count
    return value
