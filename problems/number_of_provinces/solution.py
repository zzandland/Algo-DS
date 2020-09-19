class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        N = len(M)
        
        parent = [*range(N)]
        size = [1]*N
        
        def find(u: int) -> int:
            if parent[u] != u: parent[u] = find(parent[u])
            return parent[u]
            
        def union(u: int, v: int) -> None:
            uf, vf = find(u), find(v)
            if size[uf] > size[vf]: uf, vf = vf, uf
            parent[uf] = vf
            size[vf] += size[uf]
            
        for y in range(N):
            for x in range(y+1, N):
                if M[y][x] == 1: union(y, x)                    
                    
        return len([1 for i in range(N) if find(i) == i])