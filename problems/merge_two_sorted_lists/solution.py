# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        run = res = None
        while l1 and l2:
            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next
            if run: run.next = tmp
            run = tmp
            if not res: res = run
        if l1: run.next = l1
        elif l2: run.next = l2
        return res