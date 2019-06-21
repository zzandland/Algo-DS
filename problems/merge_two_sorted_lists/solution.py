# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        output = runner = None
        while l1 is not None and l2 is not None:    
            if l1.val > l2.val:
                tmp = l2
                l2 = l2.next
            else:
                tmp = l1    
                l1 = l1.next
            if runner is not None:
                runner.next = tmp
            runner = tmp    
            if output is None:
                output = runner
        if l1 is not None:
            runner.next = l1        
        elif l2 is not None:
            runner.next = l2    
        return output    