# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ts = {*to_delete}
        res = []
        def dfs(n: TreeNode, is_root: bool) -> TreeNode:
            if not n: return None
            found = n.val in ts
            if is_root and not found: res.append(n)
            n.left = dfs(n.left, found)
            n.right = dfs(n.right, found)
            return None if found else n
        dfs(root, True)
        return res