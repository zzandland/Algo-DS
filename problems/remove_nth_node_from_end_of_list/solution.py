# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next or not n: return None
        f = s = cpy = head
        for _ in range(n):
            if not f.next: return head.next
            f = f.next
        while f.next:
            f, s = f.next, s.next    
        s.next = s.next.next    
        return cpy