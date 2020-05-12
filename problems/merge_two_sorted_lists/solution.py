# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        run = head = None
        while l1 and l2:
            if l1.val < l2.val: n, l1 = ListNode(l1.val), l1.next
            else: n, l2 = ListNode(l2.val), l2.next
            if run: run.next = n
            run = n
            if not head: head = n
        if l1:
            if not head: head = l1
            else: run.next = l1    
        elif l2:
            if not head: head = l2
            else: run.next = l2
        return head