# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(n: TreeNode, left: bool) -> int:
            if not n: return 0
            if left and not n.left and not n.right: return n.val
            return helper(n.left, True) + helper(n.right, False)
        return helper(root, False)