"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dic, st, seen = {}, [node], set()
        while st:
            n = st.pop()
            seen.add(n)
            dic.setdefault(n, Node(n.val))
            if n.neighbors:
                dic[n].neighbors = set()
                for nn in n.neighbors:
                    dic.setdefault(nn, Node(nn.val))
                    dic[n].neighbors.add(dic[nn])
                    if nn not in seen:
                        st.append(nn)
        return dic[node]                