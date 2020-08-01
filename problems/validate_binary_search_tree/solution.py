# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(n: TreeNode, l: int, r: int) -> bool:
            if not n: return True
            return l < n.val < r and helper(n.left, l, n.val) and helper(n.right, n.val, r)
        return helper(root, float('-inf'), float('inf'))