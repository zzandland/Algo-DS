# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        copy_list = []
        self.recurse(head, copy_list)
        return copy_list[0]
    
    def recurse(self, head: ListNode, lst: List) -> ListNode:
        copy = ListNode(head.val)
        if head.next is None:
            lst.append(copy)    
            return copy
        prev = self.recurse(head.next, lst)
        prev.next = copy
        return copy