# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.recurse(root, None, None)
    
    def recurse(self, root: TreeNode, lower: int, upper: int) -> bool:
        if root is None:
            return True
        if lower is not None and root.val <= lower:
            return False
        if upper is not None and root.val >= upper:
            return False
        if root.left is not None and root.val <= root.left.val:
            return False
        if root.right is not None and root.val >= root.right.val:
            return False    
        left_sub = self.recurse(root.left, lower, root.val) 
        right_sub = self.recurse(root.right, root.val, upper)
        return left_sub and right_sub