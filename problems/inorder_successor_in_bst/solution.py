# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        found = False
        st = []
        n = root
        while n or st:
            while n:
                st.append(n)
                n = n.left
            n = st.pop()
            if found: return n
            elif n == p: found = True
            n = n.right
        return None