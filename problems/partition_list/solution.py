# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = less_t = ListNode(None)
        other = other_t = ListNode(None)
        run = head
        while run:
            if run.val < x: less_t.next, less_t = run, run
            else: other_t.next, other_t = run, run
            run = run.next
        less_t.next = None
        other_t.next = None
            
        if less != less_t:
            less_t.next = other.next
            return less.next
        return other.next