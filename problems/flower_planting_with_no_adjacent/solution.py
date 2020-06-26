from collections import defaultdict

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        adj, seen, V = defaultdict(list), set(), [0]*(N+1)
        for u, v in paths:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(n: int) -> None:
            colors = {1, 2, 3, 4}
            for nei in adj[n]:
                if V[nei] in colors: colors.remove(V[nei])
            V[n] = next(iter(colors))
            for nei in adj[n]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        for i in range(1, N+1):
            if i not in seen:
                seen.add(i)
                dfs(i)
        return V[1:]