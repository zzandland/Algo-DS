class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        M, N = len(grid), len(grid[0])
        dp = [[0]*(N+2) for _ in range(N+2)]
        
        for y in range(M-1, -1, -1):
            ndp = [[0]*(N+2) for _ in range(N+2)]
            for x1 in range(1, N+1):
                for x2 in range(x1+1, N+1):
                    prev = max(dp[px1][px2] for px1, px2 in [(x1+c1, x2+c2) for c1 in (-1, 0, 1) for c2 in (-1, 0, 1)])
                    ndp[x1][x2] = grid[y][x1-1] + grid[y][x2-1] + prev
            dp = ndp
            
        return dp[1][N]