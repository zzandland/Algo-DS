from collections import defaultdict, deque

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        adj, colors = defaultdict(list), [0]*(N+1)
        for a, b in paths:
            adj[a].append(b)
            adj[b].append(a)
        for i in range(1, N+1):
            cs = set([1,2,3,4])
            for ni in adj[i]:
                if colors[ni] in cs:
                    cs.remove(colors[ni])
            colors[i] = next(iter(cs))
        return colors[1:]