class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        idx = {n: i for i, n in enumerate(row)}
        parent = [i for i in range(N//2)]
        size = [1] * (N//2)
        
        def find(n: int) -> int:
            if parent[n] != n: parent[n] = find(parent[n])
            return parent[n]
        
        def union(a: int, b: int) -> bool:
            pa, pb = find(a), find(b)
            if pa == pb: return False
            if size[pa] > size[pb]: pa, pb = pb, pa
            parent[pa] = pb
            size[pb] += size[pb]
            return True
        
        res = 0
        for i in range(0, N, 2):
            a, c = row[i], row[i+1]
            bi = idx[a+1] if a & 1 == 0 else idx[a-1]
            di = idx[c+1] if c & 1 == 0 else idx[c-1]
            if union(i//2, bi//2): res += 1
            if union(i//2, di//2): res += 1
                
        return res