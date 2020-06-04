# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def fn(n: TreeNode) -> TreeNode:
            if not n: return None
            n.left, n.right = fn(n.right), fn(n.left)
            return n
        return fn(root)    