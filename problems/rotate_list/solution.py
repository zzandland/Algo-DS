# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        # get len of list first O(N)
        ln = 1
        run = head
        while run.next:
            ln += 1
            run = run.next
        tail, run = run, head
        
        # k modulus by length, then move upto one before that O(k)
        k %= ln
        if k == 0: return head
        for _ in range(ln - k - 1):
            run = run.next
        res = run.next
        run.next = None
        tail.next = head
        return res