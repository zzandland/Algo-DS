from collections import deque

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
        if not head: return None
        q = deque()
        run = head
        while run:
            q.append(run)
            run = run.next
        res = run = None
        while q:
            tmp = q.popleft()
            if run: run.next = tmp
            if not res: res = run
            run = tmp
            if q: tmp = q.pop()
            run.next = tmp
            run = tmp
        run.next = None
        return res