# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_d = [0]
        self.recurse(root, max_d)
        return max_d[0] - 1
    
    def recurse(self, root: TreeNode, max_d: List[int]) -> int:
        if root is None:
            return 0
        left_len = self.recurse(root.left, max_d)
        right_len = self.recurse(root.right, max_d)
        diameter = left_len + right_len + 1
        if diameter > max_d[0]:
            max_d[0] = diameter
        return max(left_len, right_len) + 1    