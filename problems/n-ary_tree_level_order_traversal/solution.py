"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []
        q = [root]
        while q:
            nq = []
            level = []
            for n in q:
                level.append(n.val)
                nq += n.children
            q = nq
            res.append(level)
        return res