'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        all_values = []
        for list_node in lists:
            while list_node is not None:
                all_values.append(list_node.val)
                list_node = list_node.next
                
        all_values.sort()
        
        node = ListNode()
        header = node
        
        for value in all_values:
            node.next = ListNode(value)
            node = node.next
            
        return header.next