class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        rows, cols = [0]*M, [0]*N
        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1:
                    rows[y] += 1
                    cols[x] += 1
        return sum([rows[y] + cols[x] > 2 for y in range(M) for x in range(N) if grid[y][x] == 1])