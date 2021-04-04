# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        n, st = head, []
        while n:
            st.append(n)
            n = n.next
        while head:
            if head.val != st.pop().val: return False
            head = head.next
        return True