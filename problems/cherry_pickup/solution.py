class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        M, N = len(grid), len(grid[0])
        dp = {}
        
        def dq(y1: int, y2: int, x1: int) -> int:
            x2 = y1 + x1 - y2
            if y1 == M-1 and y2 == M-1 and x1 == N-1 and x2 == N-1: return grid[y1][x1]
            if y1 == M or y2 == M or x1 == N or x2 == N: return float('-inf')
            if grid[y1][x1] == -1 or grid[y2][x2] == -1: return float('-inf')
            if (y1, y2, x1) not in dp:
                res = grid[y1][x1] + grid[y2][x2]
                if res > 0 and y1 == y2: res -= 1
                dp[y1, y2, x1] = res + max(
                    dq(y1 + 1, y2 + 1, x1),
                    dq(y1 + 1, y2, x1),
                    dq(y1, y2 + 1, x1 + 1),
                    dq(y1, y2, x1 + 1)
                )
            return dp[y1, y2, x1]
        
        return max(0, dq(0, 0, 0))