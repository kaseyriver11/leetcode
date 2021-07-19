"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def deleteDuplicates(head: ListNode) -> ListNode:
        if head:
            if head.next == None:
                return head
    
            current = head.next
            prev = head
            while current != None:
                if prev.val == current.val:
                    prev.next = current.next
                else:
                    prev=current
                current = current.next
            return head
        return head

ln = ListNode(1)
ln.next = ListNode(1)
ln.next = ListNode(2)


Solution.deleteDuplicates(ln)

