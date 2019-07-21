class DSU:
    def __init__(self, n: int):
        self.parents = [-1] * n
        self.ite = set(range(n))
        
    def find(self, x: int) -> int:
        par = self.parents[x]
        if par < 0:
            return x
        while True:
            prev = par
            par = self.parents[par]
            if par < 0:
                return prev
    
    def union(self, a: int, b: int) -> bool:
        a_par = self.find(a)
        b_par = self.find(b)
        
        if a_par == b_par:
            return False
        if self.parents[a_par] < self.parents[b_par]:
            self.parents[a_par] += self.parents[b_par]
            self.parents[b_par] = a_par
            self.ite.remove(b_par)
        else:
            self.parents[b_par] += self.parents[a_par]
            self.parents[a_par] = b_par
            self.ite.remove(a_par)
        return True    

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        dsu = DSU(N)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    dsu.union(i, j)
        output = 0            
        for parent in dsu.ite:
            output -= (dsu.parents[parent] + 1)
        return output    