# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        half = -1
        def reverseLatterHalf(n: ListNode, k: int) -> ListNode:
            nonlocal half
            if not n or not n.next: 
                half = k // 2
                return n
            p = reverseLatterHalf(n.next, k+1)
            if k <= half: 
                if k == half: n.next = None
                return p
            n.next.next = n
            n.next = None
            return p
        opp = reverseLatterHalf(head, 0)
        while head and opp:
            hn, on = head.next, opp.next
            head.next = opp
            opp.next = hn
            head, opp = hn, on