from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mx = max([n for e in edges for n in e])
        V = [i for i in range(mx+1)]
        
        def find(n: int) -> int:
            if V[n] != n:
                V[n] = find(V[n])
            return V[n]
        
        def union(a: int, b: int) -> bool:
            af, bf = find(a), find(b)
            if af == bf:
                return False
            V[af] = bf
            return True
        
        for u, v in edges:
            if not union(u, v):
                return (u, v)