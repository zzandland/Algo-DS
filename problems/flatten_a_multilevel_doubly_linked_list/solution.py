"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(n: Node) -> Node:
            if not n: return None
            while n.next:
                if n.child:
                    nxt = n.next
                    n.next, n.child.prev, n.child = n.child, n, None
                    n = dfs(n.next)
                    n.next, nxt.prev = nxt, n    
                n = n.next    
            if n.child: n.next, n.child.prev, n.child = dfs(n.child), n, None
            return n        
        dfs(head)
        return head