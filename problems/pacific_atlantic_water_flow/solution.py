class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        if not matrix: return res
        M, N = len(matrix), len(matrix[0])
        p_seen, a_seen = [[False]*N for _ in range(M)], [[False]*N for _ in range(M)]
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(y: int, x: int, seen: set) -> None:
            if seen[y][x]: return
            seen[y][x] = True
            for ny, nx in ((y+r, x+c) for r, c in dir_):
                if 0 <= ny < M and 0 <= nx < N and matrix[ny][nx] >= matrix[y][x]:
                    dfs(ny, nx, seen)
        for i in range(M):
            dfs(i, 0, p_seen)
            dfs(i, N-1, a_seen)
            
        for j in range(N):
            dfs(0, j, p_seen)
            dfs(M-1, j, a_seen)
            
        return [(y, x) for y in range(M) for x in range(N) if p_seen[y][x] and a_seen[y][x]]