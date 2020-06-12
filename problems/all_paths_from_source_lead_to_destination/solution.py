class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]],
                           source: int, destination: int) -> bool:
        dp, seen, adj = [None]*n, set(), [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
        def dfs(n: int) -> bool:
            if n == destination:
                return not adj[n]
            if dp[n] is None:
                if not adj[n] or n in seen:
                    return False
                seen.add(n)
                dp[n] = all([dfs(nn) for nn in adj[n]])
            return dp[n]
        return dfs(source)