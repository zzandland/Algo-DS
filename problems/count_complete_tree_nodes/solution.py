# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        # get lowest level
        lv = 0
        run = root
        while run.left:
            lv += 1
            run = run.left
        l, r = 0, (1 << lv) - 1
        def check(m: int) -> bool:
            run = root
            a, b = 0, (1 << lv) - 1
            while a < b:
                c = a + (b-a)//2
                if c >= m:
                    run = run.left
                    b = c
                else:
                    run = run.right
                    a = c+1
            return run
                    
        while l < r:
            m = l + (r-l)//2
            if check(m): l = m+1
            else: r = m
        if check(l): l += 1
        res = 0
        for i in range(lv):
            res += (1 << i)
        return res + l