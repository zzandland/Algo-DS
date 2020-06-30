# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        H, n = 0, root
        while n.left:
            n = n.left
            H += 1
        N = 2**H
        def exist(n: TreeNode, l: int, r: int, t: int) -> bool:
            h = 0
            while h < H:
                m = l + (r-l)//2
                h += 1
                if t < m:
                    r = m
                    n = n.left
                else:
                    l = m+1
                    n = n.right
            return n
        L, R = 0, N
        while L < R:
            M = L + (R-L)//2
            if exist(root, 0, N, M):
                L = M+1
            else:
                R = M
        return 2**H - 1 + L