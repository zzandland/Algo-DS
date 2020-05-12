# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lft, head, n = 0, None, None
        while l1 or l2:
            v1 = v2 = 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            s = v1 + v2 + lft
            lft, s = divmod(s, 10)
            nxt = ListNode(s)
            if n: n.next = nxt
            n = nxt
            if not head: head = n
        if lft: n.next = ListNode(lft)        
        return head    