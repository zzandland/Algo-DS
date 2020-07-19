class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        V = [-1 for i in range(m*n)]
        
        def find(n: int) -> int:
            if V[n] != n: V[n] = find(V[n])
            return V[n]
        
        def union(n1: int, n2: int) -> bool:
            f1, f2 = find(n1), find(n2)
            if f1 != f2:
                V[f1] = f2
                return True
            return False
        
        dir_ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []
        cnt = 0
        for y, x in positions:
            l = y*n + x
            if V[l] == -1:
                V[l] = l
                cnt += 1
                for ny, nx in ((y+r, x+c) for r, c in dir_):
                    nl = ny*n + nx
                    if 0 <= ny < m and 0 <= nx < n and V[nl] != -1:
                        if union(l, nl): cnt -= 1
            res.append(cnt)
        return res