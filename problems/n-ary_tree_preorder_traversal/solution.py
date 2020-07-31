"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        st = [root]
        res = []
        while st:
            n = st.pop()
            res.append(n.val)
            st += n.children[::-1]
        return res