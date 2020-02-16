# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.helper(root1, root2)
    
    def helper(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        if not self.helper(root1.left, root2.right) and not self.helper(root1.left, root2.left):
            return False     
        if not self.helper(root1.right, root2.left) and not self.helper(root1.right, root2.right):
            return False
        return True