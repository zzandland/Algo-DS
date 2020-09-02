# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
            if not head or not head.next: return head
            pre, slow, fast = None, head, head
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            pre.next = None
            left, right = self.sortList(head), self.sortList(slow)
            return self.merge(left, right)
            
    def merge(self, n1: ListNode, n2: ListNode) -> ListNode:
        dummy = tail = ListNode(None)
        while n1 and n2:
            if n1.val < n2.val: tail.next, tail, n1 = n1, n1, n1.next
            else: tail.next, tail, n2 = n2, n2, n2.next
        tail.next = n1 or n2
        return dummy.next