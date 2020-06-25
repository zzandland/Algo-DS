# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        h = t = head
        while h and h.next:
            h, t = h.next.next, t.next
            if h == t: break
        if not h or not h.next: return None
        t = head
        while h != t:
            h, t = h.next, t.next
        return h