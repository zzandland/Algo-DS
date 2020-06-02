from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[set() for _ in range(n)] for _ in range(n)]
        for u, v in prerequisites:
            adj[u][v].add(u)
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    if adj[y][x] and adj[x][z]:
                        adj[y][z] = adj[y][x] | adj[x][z]
        return [u in adj[u][v] for u, v in queries]