from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s: return None
        q = deque(s)
        def helper() -> TreeNode:
            val = ''
            while q and q[0] not in ('(', ')'):
                val += q.popleft()
            root = TreeNode(int(val))
            if not q or q[0] == ')': return root
            elif q[0] == '(':
                q.popleft()
                root.left = helper()
                q.popleft()
            if not q or q[0] == ')': return root
            elif q[0] == '(':
                q.popleft()
                root.right = helper()
                q.popleft()
            return root
        return helper()