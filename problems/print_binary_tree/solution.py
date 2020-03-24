# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHt(n: TreeNode) -> int:
            if not n: return 0
            return max(getHt(n.left), getHt(n.right)) + 1
        ht = getHt(root)
        wd = 1
        for i in range(ht-1):
            wd= wd * 2 + 1
        ans = [["" for i in range(wd)] for j in range(ht)]    
        def place(n: TreeNode, h: int, l:int, r: int) -> None:
            if not n: return
            m = (l + r) // 2
            ans[h-1][m] = str(n.val)
            place(n.left, h+1, l, m-1)
            place(n.right, h+1, m+1, r)
        place(root, 1, 0, wd)
        return ans