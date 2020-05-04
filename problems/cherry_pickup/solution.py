class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = {}
        def fn(y1: int, x1: int, y2: int) -> int:
            x2 = y1 + x1 - y2
            if (y1 >= N or x1 >= N or y2 >= N or x2 >= N or
                grid[y1][x1] == -1 or grid[y2][x2] == -1): return float('-inf')
            if y1 == x1 == N-1: return grid[y1][x1]
            key = '{}:{}:{}'.format(y1, x1, y2)
            if key not in dp:
                dp[key] = grid[y1][x1] + (x1 != x2) * grid[y2][x2] + max(
                    fn(y1+1, x1, y2+1), fn(y1+1, x1, y2),
                    fn(y1, x1+1, y2+1), fn(y1, x1+1, y2)
                )
            return dp[key]    
        return max(0, fn(0, 0, 0))