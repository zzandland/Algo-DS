class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        N = len(grid)
        dp = [[[None]*N for _ in range(N)] for _ in range(N)]
        def fn(y1: int, x1: int, y2: int) -> int:
            x2 = y1 + x1 - y2
            if (y1 == N or x1 == N or y2 == N or x2 == N or
                grid[y1][x1] == -1 or grid[y2][x2] == -1):
                return float('-inf')
            if y1 == y2 == x1 == x2 == N-1:
                return grid[y1][x1]
            if dp[y1][x1][y2] is None:
                collect = grid[y1][x1] + grid[y2][x2]
                if y1 == y2 and x1 == x2:
                    collect -= grid[y2][x2]
                dp[y1][x1][y2] = (collect + max(
                    fn(y1+1, x1, y2+1), fn(y1+1, x1, y2),
                    fn(y1, x1+1, y2+1), fn(y1, x1+1, y2)
                ))
            return dp[y1][x1][y2]    
        return max(0, fn(0, 0, 0))            