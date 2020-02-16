# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
      evenHead = evenIter = ListNode(0)
      oddIter = ListNode(0)
      isOdd, i = True, head
      while i:
        if isOdd:
          oddIter.next = i
          oddIter = i
        else:
          evenIter.next = i  
          evenIter = i
        isOdd = not isOdd  
        i = i.next
      evenIter.next = None  
      oddIter.next = evenHead.next
      return head