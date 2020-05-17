# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return None
        def inorder(n: TreeNode) -> int:
            nonlocal k
            if n.left:
                l = inorder(n.left)
                if l: return l
            k -= 1    
            if k == 0: return n
            if n.right:    
                return inorder(n.right)
        return inorder(root).val