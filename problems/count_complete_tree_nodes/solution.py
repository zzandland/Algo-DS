# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        h, n = 0, root
        while n.left:
            n = n.left
            h += 1
        N = 2**h
        def exists(t: int) -> bool:
            nonlocal h, N
            l, r, d, n = 0, N-1, 0, root
            while d < h:
                m = l + (r-l)//2
                if t <= m:
                    n = n.left
                    r = m
                else:
                    n = n.right
                    l = m+1
                d += 1    
            return bool(n)
        l, r = 0, N-1
        while l < r:
            m = l + (r-l)//2
            if exists(m):
                l = m+1
            else:
                r = m
        if exists(l):        
            l += 1
        return l + sum([2**i for i in range(h)])