# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev, curr, runner = None, head, None
        while curr:
            runner = curr.next
            curr.next = prev
            prev = curr
            curr = runner
        return prev    