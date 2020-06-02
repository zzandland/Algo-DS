from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, True))
            adj[v].append((u, False))
        def dfs(i: int, p: int) -> None:
            res = 0
            for ni, d in adj[i]:
                if ni != p:
                    if d: res += 1
                    res += dfs(ni, i)
            return res        
        return dfs(0, -1)            