"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        head = None
        def dfs(n: Node, p: Node, l: bool) -> Node:
            nonlocal head
            if n.left: 
                if not l: 
                    tmp = n.left
                    while tmp.left: tmp = tmp.left
                ln = dfs(n.left, n, True)
                n.left, ln.right = ln, n
                if not l: tmp.left, p.right = p, tmp
            elif not l: n.left = p
            if not head: head = n
            if n.right: return dfs(n.right, n, False)
            return n
        tail = dfs(root, None, True)
        head.left, tail.right = tail, head
        return head