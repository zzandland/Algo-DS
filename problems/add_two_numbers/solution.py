# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      x = o = ListNode(0)
      lift = 0
      while l1 or l2 or lift:
        sm = lift
        if l1:
          sm += l1.val
          l1 = l1.next
        if l2:
          sm += l2.val  
          l2 = l2.next
        lift, sm = divmod(sm, 10)  
        x.next = ListNode(sm)
        x = x.next
      return o.next