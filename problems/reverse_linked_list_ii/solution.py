# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur, prev1 = head, None
        i = 1
        while cur:
            if i == m:
                run, prev2 = cur, None
                while i <= n:
                    nxt = run.next
                    run.next = prev2
                    run, prev2 = nxt, run
                    i += 1
                cur.next = run
                if not prev1: return prev2
                prev1.next = prev2
                return head
            cur, prev1 = cur.next, cur
            i += 1