from typing import Dict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        node_map = self.generate_map(lists)
        head, first = None, None
        for _, lst in sorted(node_map.items()):
            for node in lst:
                if head is not None:
                    head.next = node
                head = node
                if first is None:
                    first = head
        return first            
    
    def generate_map(self, lists: List[ListNode]) -> Dict[int, List[ListNode]]:
        node_map = {}
        for lstNode in lists:
            while lstNode is not None:
                if lstNode.val not in node_map:
                    node_map[lstNode.val] = [lstNode]
                else:
                    node_map[lstNode.val].append(lstNode)    
                lstNode = lstNode.next    
        return node_map        