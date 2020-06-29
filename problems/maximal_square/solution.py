class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        M, N, res = len(matrix), len(matrix[0]), 0
        dp = [[0]*N for _ in range(M)]
        for y in range(M):
            for x in range(N):
                if matrix[y][x] == '1':
                    dp[y][x] = min(dp[y-1][x], dp[y-1][x-1], dp[y][x-1]) + 1
                    res = max(res, dp[y][x])
        return res * res