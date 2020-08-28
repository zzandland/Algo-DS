# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        idx = {n: i for i, n in enumerate(pre)}
        
        if not post: return None
        
        def helper(i: int) -> TreeNode:
            res = TreeNode(post.pop())
            if post and idx[post[-1]] > i: res.right = helper(idx[post[-1]])
            if post and idx[post[-1]] > i: res.left = helper(idx[post[-1]])
            return res
        return helper(0)