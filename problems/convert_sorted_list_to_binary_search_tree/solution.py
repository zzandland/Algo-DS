# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        ln = 0
        run = head
        while run:
            ln += 1
            run = run.next
        def dfs(l: int, r: int) -> TreeNode:
            nonlocal head
            if l > r: return None
            m = l + (r-l)//2
            left = dfs(l, m-1)
            root = TreeNode(head.val)
            root.left = left
            head = head.next
            root.right = dfs(m+1, r)
            return root
        return dfs(0, ln-1)