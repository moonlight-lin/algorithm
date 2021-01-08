'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output_header = ListNode()
        temp_node = output_header
        incremental = 0        
        temp_l1 = l1
        temp_l2 = l2
        
        while temp_l1 is not None and temp_l2 is not None:
            temp_node.next = ListNode()
            temp_node = temp_node.next
            temp_result = temp_l1.val + temp_l2.val + incremental
            incremental = 1 if temp_result >= 10 else 0
            temp_node.val = temp_result - 10 if incremental != 0 else temp_result
            temp_l1 = temp_l1.next
            temp_l2 = temp_l2.next
            
        while temp_l1 is not None:
            temp_node.next = ListNode()
            temp_node = temp_node.next
            temp_result = temp_l1.val + incremental
            incremental = 1 if temp_result >= 10 else 0
            temp_node.val = temp_result - 10 if incremental != 0 else temp_result
            temp_l1 = temp_l1.next
        
        while temp_l2 is not None:
            temp_node.next = ListNode()
            temp_node = temp_node.next
            temp_result = temp_l2.val + incremental
            incremental = 1 if temp_result >= 10 else 0
            temp_node.val = temp_result - 10 if incremental != 0 else temp_result
            temp_l2 = temp_l2.next
            
        if incremental != 0:
            temp_node.next = ListNode()
            temp_node.next.val = incremental
            
        return output_header.next