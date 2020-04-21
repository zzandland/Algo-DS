# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def fn(l: int, r: int) -> TreeNode:
            if l > r: return None
            if l == r: return TreeNode(preorder[l])
            n, m = TreeNode(preorder[l]), l+1
            while m < r and preorder[m] < n.val:
                m += 1 
            if preorder[m] < n.val: m += 1
            n.left = fn(l+1, m-1)
            n.right = fn(m, r)
            return n
        return fn(0, len(preorder)-1)