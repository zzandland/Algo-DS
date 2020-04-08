class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        uf, seen, dir_ = [i for i in range(R * C)], [[False for _ in range(C)] for _ in range(R)], [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def find(x: int) -> int:
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x: int, y: int) -> None:
            ux, uy = find(x), find(y)
            if ux != uy:
                uf[ux] = uy
        for y, x in sorted([(r, c) for r in range(R) for c in range(C)], key=lambda x: A[x[0]][x[1]], reverse=True):
            seen[y][x] = True
            for ver, hor in dir_:
                ny, nx = y+ver, x+hor
                if 0 <= ny < R and 0 <= nx < C and seen[ny][nx]:
                    union(ny*C+nx, y*C+x)
                if find(0) == find(R*C-1):
                    return A[y][x]