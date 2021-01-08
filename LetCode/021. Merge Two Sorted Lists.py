'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        if l1.val <= l2.val:
            head = temp = l1
            l1 = l1.next
        else:
            head = temp = l2
            l2 = l2.next
        
        while True:
            if l1 is None:
                temp.next = l2
                break
        
            if l2 is None:
                temp.next = l1
                break
            
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
				
            temp = temp.next

        return head