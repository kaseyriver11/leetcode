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
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        """Instead of turning into a string, reversing, and then creating a new ListNode,
        let's try creating the ListNode as we go using mod to keep track of any value greater than 10 
        that need to be carried to the next value.
        """

        count = 0
        leftover = 0
        final_ln = ListNode(0)
        temp_ln = final_ln

        while l1 or l2:
            # We dont want errors
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)

            count = l1.val + l2.val + leftover
            leftover, count = divmod(count, 10)
            temp_ln.next = ListNode(count)
            temp_ln = temp_ln.next
            l1 = l1.next
            l2 = l2.next
        if leftover > 0:
            temp_ln.next = ListNode(leftover)

        return final_ln.next

# Create an example
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l2 = ListNode(9)
l2.next = ListNode(8)
l2.next.next = ListNode(7)

Solution().addTwoNumbers(l1, l2)


# ----- Original solution using strings
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

