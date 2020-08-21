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
        
        half = run = head
        while run and run.next:
            half = half.next
            run = run.next.next
            
        prev = None
        while half:
            tmp = half.next
            half.next = prev
            prev, half = half, tmp
        
        run = res = None
        while head and prev:
            tmp = head
            head = head.next
            if run: run.next = tmp
            if not res: res = run
            run = tmp
            tmp = prev
            prev = prev.next
            run.next = tmp
            run = tmp
        if head:
            run.next = head
            run = run.next
        run.next = None
        return res