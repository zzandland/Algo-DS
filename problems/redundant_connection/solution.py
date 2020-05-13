from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        def find(n: int) -> int:
            if n not in parents: parents[n] = n
            if n != parents[n]: parents[n] = find(parents[n])
            return parents[n]    
        def union(a: int, b: int) -> None:
            fa, fb = find(a), find(b)
            parents[parents[a]] = b
        for u, v in edges:
            fu, fv = find(u), find(v)
            if fu == fv: return u, v
            union(u, v)