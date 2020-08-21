# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        st = [root, root]
        while st:
            n = st.pop()
            if st and st[-1] == n:
                if n.right: st += [n.right, n.right]
                if n.left: st += [n.left, n.left]
            else:
                res.append(n.val)
        return res