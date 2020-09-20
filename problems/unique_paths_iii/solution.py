class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        N, M = len(grid), len(grid[0])
        dir_ = (-1, 0, 1, 0, -1)
        
        rem = 0
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 0: rem += 1
                elif grid[y][x] == 1: sy, sx = y, x
                elif grid[y][x] == 2: ey, ex = y, x
        
        def dfs(y: int, x: int, seen: {int}) -> int:
            if y == ey and x == ex:
                return 1 if len(seen) == rem+2 else 0
            res = 0
            for ny, nx in ((y+r, x+c) for r, c in zip(dir_, dir_[1:])):
                if 0 <= ny < N and 0 <= nx < M:
                    if grid[ny][nx] != -1 and ny*M+nx not in seen:
                        seen.add(ny*M+nx)
                        res += dfs(ny, nx, seen)
                        seen.remove(ny*M+nx)
            return res
        
        return dfs(sy, sx, {sy*M+sx})