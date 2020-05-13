from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            graph[a][b] = values[i]
            graph[b][a] = 1/values[i] if values[i] != 0 else -1
        visited = set()    
        output = []
        def dfs(n: int, t: int) -> float:
            if n == t: return 1
            if n in visited: return -1
            visited.add(n)
            for nxt in graph[n]:
                if graph[n][nxt] != -1:
                    f = dfs(nxt, t)
                    if f != -1: return f * graph[n][nxt]
            return -1    
        for a, b in queries:
            if a in graph:
                if b not in graph[a]:
                    visited = set()
                    graph[a][b] = dfs(a, b)
                output.append(graph[a][b])    
            else: output.append(-1)    
        return output    