class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        dp = {}
        def dq(c1: int, c2: int, y: int) -> int:
            if y == R or not (0 <= c1 < C) or not (0 <= c2 < C):
                return 0
            key = '{}:{}:{}'.format(c1, c2, y)
            if key not in dp:
                take = grid[y][c1] + grid[y][c2] if c1 != c2 else grid[y][c1]
                dp[key] = take + max(
                    dq(c1-1, c2-1, y+1), dq(c1, c2-1, y+1), dq(c1+1, c2-1, y+1),
                    dq(c1-1, c2, y+1), dq(c1, c2, y+1), dq(c1+1, c2, y+1),
                    dq(c1-1, c2+1, y+1), dq(c1, c2+1, y+1), dq(c1+1, c2+1, y+1)
                )
            return dp[key]
        return dq(0, C-1, 0)