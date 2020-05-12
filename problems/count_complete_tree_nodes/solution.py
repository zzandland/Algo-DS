# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        h, n, res = 0, root, 0
        while n and n.left:
            res += 2**h
            h, n = h+1, n.left
        d = 2**h    
        def down(t: int) -> TreeNode:
            n, l, r = root, 0, d-1
            while l < r:
                m = l + (r-l)//2
                if m >= t: r, n = m, n.left
                else: l, n = m+1, n.right
            return n        
        l, r = 0, d-1
        while l <= r:
            m = l + (r-l)//2
            n = down(m)
            if n and r == l: break
            if n: l = m+1
            else: r = m-1 
        return d + min(l, r)        