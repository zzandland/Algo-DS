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
        run, dic = head, {None: None}
        while run:
            dic[run] = Node(run.val)
            run = run.next
        run = head    
        while run:
            dic[run].next = dic[run.next]
            dic[run].random = dic[run.random]
            run = run.next
        return dic[head]    