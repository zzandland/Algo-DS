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
        if not head: return head
        obj = {None: None}
        run = head
        while run:
            obj[run] = Node(run.val)
            run = run.next
            
        run = head
        while run:
            obj[run].next = obj[run.next]
            obj[run].random = obj[run.random]
            run = run.next
            
        return obj[head]