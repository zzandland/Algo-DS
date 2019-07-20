# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_len = [0]
        self.helper(root, max_len)
        return max_len[0]
    
    def helper(self, node: TreeNode, max_len: List[int]) -> int:
        if not node:
            return 0
        l, r = self.helper(node.left, max_len), self.helper(node.right, max_len)
        max_len[0] = max(max_len[0], l + r)
        return 1 + max(l, r)