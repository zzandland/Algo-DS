class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*(N+1) for _ in range(M+1)]
        res = 0
        for y in range(1, M+1):
            for x in range(1, N+1):
                if matrix[y-1][x-1] == '1':
                    dp[y][x] = 1 + min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])
                    res = max(res, dp[y][x]*dp[y][x])
        return res