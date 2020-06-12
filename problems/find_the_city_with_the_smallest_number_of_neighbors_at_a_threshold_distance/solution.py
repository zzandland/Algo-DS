class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[0 if r == c else float('inf') for c in range(n)] for r in range(n)]
        for u, v, w in edges:
            adj[u][v] = w
            adj[v][u] = w
        for c in range(n):
            for y in range(n):
                for x in range(n):
                    adj[y][x] = min(adj[y][x], adj[y][c] + adj[c][x])
        cnt = [0]*n
        for y, r in enumerate(adj):
            for x, c in enumerate(r):
                if y != x and c <= distanceThreshold:
                    cnt[y] += 1
        mx, mxi = float('inf'), -1
        for i, n in enumerate(cnt):
            if n <= mx:
                mx, mxi = n, i
        return mxi