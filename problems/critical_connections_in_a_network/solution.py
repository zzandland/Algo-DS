from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        visit, low, seen, res, t = [None]*n, [None]*n, set(), [], 0
        def dfs(c: int, p: int) -> None:
            if c in seen: return
            nonlocal t
            seen.add(c)
            visit[c] = low[c] = t
            t += 1
            for nn in adj[c]:
                if nn != p:
                    dfs(nn, c)
                    low[c] = min(low[c], low[nn])
                    if visit[c] < low[nn]: res.append([c, nn])
            return low[c]    
        dfs(0, -1)
        return res