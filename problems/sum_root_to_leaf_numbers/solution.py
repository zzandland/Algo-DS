# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        run, res = [], []
        def fn(n: TreeNode) -> None:
            run.append(str(n.val))
            if not n.left and not n.right:
                res.append(int(''.join(run)))
            else:
                if n.left: fn(n.left)
                if n.right: fn(n.right)
            run.pop()
        fn(root)
        return sum(res)