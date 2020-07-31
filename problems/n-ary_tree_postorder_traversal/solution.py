"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        st = [root]
        while st:
            n = st.pop()
            res.append(n.val)
            st += n.children
        return res[::-1]