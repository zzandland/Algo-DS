# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s = l = head
        while l:
            if not l.next: return s
            s = s.next
            l = l.next.next
        return s    