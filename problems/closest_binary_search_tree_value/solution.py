# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root: return float('inf')
        return min(root.val, self.closestValue(root.left, target), self.closestValue(root.right, target), key=lambda n: abs(n - target))