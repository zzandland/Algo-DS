# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(n: TreeNode) -> List[int]:
            if not n: return []
            return inorder(n.left) + [n] + inorder(n.right)
        arr = inorder(root)
        vals = sorted(map(lambda x: x.val, arr))
        for node, val in zip(arr, vals):
            node.val = val