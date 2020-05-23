# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def fn(n: TreeNode, h: int) -> None:
            if not n: return
            if h == len(res): res.append(n.val)
            fn(n.right, h+1)
            fn(n.left, h+1)
        fn(root, 0)
        return res