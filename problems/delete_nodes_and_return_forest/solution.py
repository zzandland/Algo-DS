# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return []
        res, st = [root], set(to_delete)
        if root.val in st: res.pop()
        def dfs(n: TreeNode, p: TreeNode) -> None:
            if not n: return
            l, r = n.left, n.right
            if n.val in st:
                if p:
                    if p.left == n: p.left = None
                    else: p.right = None
                if n.left:
                    if n.left.val not in st: res.append(n.left)
                    n.left = None
                if n.right:
                    if n.right.val not in st: res.append(n.right)
                    n.right = None
            dfs(l, n)
            dfs(r, n)
        dfs(root, None)
        return res