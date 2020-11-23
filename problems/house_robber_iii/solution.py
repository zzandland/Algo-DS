# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @functools.lru_cache(None)
    def helper(self, root: TreeNode, visited: bool) -> int:
        if not root: return 0    
        pss = self.helper(root.left, False) + self.helper(root.right, False)
        if visited: return pss
        return max(pss, root.val + self.helper(root.left, True) + self.helper(root.right, True))

    def rob(self, root: TreeNode) -> int:
        return self.helper(root, False)