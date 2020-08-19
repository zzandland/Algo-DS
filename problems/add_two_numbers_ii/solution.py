# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        nxt = None
        lft = 0
        while st1 or st2 or lft:
            v1, v2 = st1.pop() if st1 else 0, st2.pop() if st2 else 0
            run = ListNode(v1 + v2 + lft)
            if nxt: run.next = nxt
            if run.val > 9:
                run.val -= 10
                lft = 1
            else: lft = 0
            nxt = run
        return nxt