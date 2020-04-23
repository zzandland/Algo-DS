# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        output = 0
        def fn(n: TreeNode) -> int:
            nonlocal output
            if not n: return 0
            left, right = fn(n.left), fn(n.right)
            output = max(output, left+right)
            return 1 + max(left, right)
        fn(root)
        return output