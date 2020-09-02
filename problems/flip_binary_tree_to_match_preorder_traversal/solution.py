# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        idx = {n: i for i, n in enumerate(voyage)}
        def dfs(n: TreeNode, i: int) -> List[int]:
            if not n or i == -1: return []
            li = idx[n.left.val] if n.left else -1
            ri = idx[n.right.val] if n.right else -1
            if li != -1 and li <= i:  return [-1]
            if ri != -1 and ri <= i: return [-1]
            res = [n.val] if li != -1 and ri != -1 and li > ri else []
            return res + dfs(n.left, li) + dfs(n.right, ri)
        res = dfs(root, 0)
        return [-1] if -1 in res else res