class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        N, M = len(matrix), len(matrix[0])
        
        dp = [[0]*(M+1) for _ in range(N+1)]
        res = 0
        for y in range(N):
            for x in range(M):
                if matrix[y][x] == 1:
                    dp[y+1][x+1] = min(dp[y+1][x], dp[y][x], dp[y][x+1]) + 1
                    res += dp[y+1][x+1]
        return res