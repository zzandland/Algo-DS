from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj, seen = defaultdict(set), defaultdict(int)
        for u, v in tickets:
            adj[u].add(v)
            seen[u, v] += 1
        found = False
        def dfs(u: int, cnt: int) -> List[str]:
            nonlocal found
            if cnt == 0:
                found = True
                return [u]
            res = []
            for v in sorted(adj[u]):
                if seen[u, v] > 0:
                    seen[u, v] -= 1
                    tmp = [u] + dfs(v, cnt-1)
                    if found: return tmp
                    seen[u, v] += 1
            return []
        return dfs('JFK', len(tickets))