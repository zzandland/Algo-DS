from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            adj[a][b] = v
            if v != 0: adj[b][a] = 1 / v
                
        def dfs(n: str, t: str, seen: set) -> float:
            if t in adj[n]: return adj[n][t]
            for nxt in adj[n]:
                if nxt not in seen:
                    seen.add(nxt)
                    tmp = dfs(nxt, t, seen)
                    if tmp != float('inf'): return adj[n][nxt] * tmp
            return float('inf')
            
        res = []
        for a, b in queries:
            if not adj[b]:
                res.append(-1)
            else:
                tmp = dfs(a, b, {a})
                if tmp != float('inf'):
                    res.append(tmp)
                    adj[a][b] = tmp
                    adj[b][a] = 1 / tmp
                else:
                    res.append(-1)
        return res