"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # establish the head as the lower value
        if (not l1) or (not l2):
            return l1 or l2
        
        if l1.val < l2.val:
            node1, node2 = (l1, l2)
        else:
            node1, node2 = (l2, l1)

        head = node1
        prev = node1
        node1 = node1.next
       
        while node1 and node2:
            if node1.val < node2.val:
                prev.next = node1
                node1 = node1.next
            else:
                prev.next = node2
                node2 = node2.next
            prev = prev.next
        prev.next = node1 or node2
        return head


Solution().mergeTwoLists(l1, l2)

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = l1