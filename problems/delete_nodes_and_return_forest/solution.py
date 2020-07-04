# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return []
        st, res = set(to_delete), set([root])
        def dfs(n: TreeNode, p: TreeNode) -> None:
            nonlocal res
            if not n: return
            l, r = n.left, n.right
            if n.val in st:
                if p:
                    if n == p.left: p.left = None
                    else: p.right = None
                if n in res: res.remove(n)
                if n.left: res.add(l)
                if n.right: res.add(r)
                n.left = n.right = None
            dfs(l, n)
            dfs(r, n)
        dfs(root, None)
        return list(res)