from collections import defaultdict, Counter

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        seen = Counter()
        seen[source] += 1
        def dfs(n: int) -> bool:
            if not adj[n]: return n == destination
            if n == destination: return False
            for nn in adj[n]:
                if seen[nn] > 1: return False
                seen[nn] += 1
                tmp = dfs(nn)
                seen[nn] -= 1
                if not tmp: return False
            return True
        return dfs(source)