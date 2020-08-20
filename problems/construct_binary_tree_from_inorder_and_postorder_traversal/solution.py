# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx = {v: i for i, v in enumerate(inorder)}
        def dfs(l: int, r: int) -> TreeNode:
            if l > r: return None
            val = postorder.pop()
            root = TreeNode(val)
            root.right = dfs(idx[val]+1, r)
            root.left = dfs(l, idx[val]-1)
            return root
        return dfs(0, len(inorder)-1)