# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        def fn(n: TreeNode, run: List[str]) -> List[str]:
            if not n: return []
            s = str(n.val)
            if not n.left and not n.right: return ['->'.join(run+[s])]
            return fn(n.left, run+[s]) + fn(n.right, run+[s])
        return fn(root, [])