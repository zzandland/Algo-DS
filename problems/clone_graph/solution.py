"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic, visited = {}, set()
        if not node: return None
        def dfs(n: Node) -> Node:
            dic.setdefault(node, Node(node.val))
            if n in visited: return dic[n]
            visited.add(n)
            for nxt in n.neighbors:
                dic.setdefault(nxt, Node(nxt.val))
                dic[n].neighbors.append(dic[nxt])
                dfs(nxt)
            return dic[n]
        return dfs(node)