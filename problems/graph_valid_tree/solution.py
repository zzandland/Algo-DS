class DSU:
    def __init__(self, n: int):
        self.q = [-1] * n
        self.connect = n
        
    def find(self, n: int) -> int:
        par, out = self.q[n], n
        while par >= 0:
            out = par
            par = self.q[par]
        return out    
    
    def union(self, a: int, b: int) -> bool:
        a_par, b_par = self.find(a), self.find(b)
        if a_par == b_par:
            return False
        self.q[b_par] = a_par
        self.connect -= 1
        return True    

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return False
        return dsu.connect == 1