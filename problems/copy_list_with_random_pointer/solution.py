"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        save = { None: None }
        def fn(n: Node) -> Node:
            if not n: return
            if not n in save: 
                cpy = Node(n.val)
                save[n] = cpy
            if n.random and not n.random in save:    
                randCpy = Node(n.random.val)
                save[n.random] = randCpy
            save[n].random = save[n.random]
            save[n].next = fn(n.next)    
            return save[n]
        return fn(head)