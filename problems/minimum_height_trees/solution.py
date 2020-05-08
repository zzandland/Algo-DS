from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = [n for n, lst in enumerate(graph) if len(lst) == 1]
        while n > 2:
            n -= len(leaves)
            tmp = []
            for leaf in leaves:
                to = graph[leaf].pop()
                graph[to].remove(leaf)
                if len(graph[to]) == 1: tmp.append(to)
            leaves = tmp        
        return leaves    