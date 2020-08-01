# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lift = 0
        run = root = None
        while l1 or l2:
            sm = lift
            if l1:
                sm += l1.val
                l1 = l1.next
            if l2:
                sm += l2.val
                l2 = l2.next
            if sm >= 10:
                sm -= 10
                lift = 1
            else: lift = 0
            tmp = ListNode(sm)
            if run: run.next = tmp
            run = tmp
            if not root: root = run
        if lift == 1: run.next = ListNode(lift)
        return root