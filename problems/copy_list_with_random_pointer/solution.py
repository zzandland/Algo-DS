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
        dic = defaultdict(lambda: Node(0))
        dic[None] = None
        run = head
        while run:
            dic[run].val = run.val
            dic[run].next = dic[run.next]
            dic[run].random = dic[run.random]
            run = run.next
        return dic[head]