'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        node_1 = head
        node_2 = head
        for _ in range(n):
            node_2 = node_2.next
            
        if node_2 is None:
            return head.next
            
        while True:
            if node_2.next is not None:
                node_2 = node_2.next
                node_1 = node_1.next
            else:
                break
                
        node_1.next = node_1.next.next
        return head