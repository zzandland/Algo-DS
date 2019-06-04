# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.recurse(root.left, root.right)    
    

    def recurse(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False    
        if left.val != right.val:
            return False
        return self.recurse(left.left, right.right) and self.recurse(left.right, right.left)