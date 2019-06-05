# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_sum = float('-inf')
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.recurse(root)
        return self.max_sum

    def recurse(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_sum = max(0, self.recurse(root.left))
        right_sum = max(0, self.recurse(root.right))
        self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)
        return root.val + max(left_sum, right_sum)