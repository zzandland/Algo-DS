from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        def div(a: int, b: int) -> float:
            if b == 0: return 0
            return a / b
        for (u, v), val in zip(equations, values):
            adj[u].append((v, val))
            adj[v].append((u, div(1, val)))
        res = []
        def dfs(n: str, t: str) -> float:
            if n == t: return 1
            if n in seen: return float('inf')
            seen.add(n)
            for nn, v in adj[n]:
                tmp = dfs(nn, t)
                if tmp != float('inf'): return v * tmp
            return float('inf')
        for u, v in queries:
            if u not in adj:
                res.append(-1.0)
            else:
                seen = set()
                val = dfs(u, v)
                if val == float('inf'):
                    res.append(-1)
                else:
                    res. append(val)
                    adj[u].append((v, val))
                    adj[v].append((u, div(1, val)))
        return res