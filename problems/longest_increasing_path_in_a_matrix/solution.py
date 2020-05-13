class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        R, C = len(matrix), len(matrix[0])
        lst = sorted([(y, x) for y in range(R) for x in range(C)], key=lambda x: -matrix[x[0]][x[1]])
        dp, mx = [[1]*C for _ in range(R)], 1
        for i, j in lst:
            for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i+r, j+c
                if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[ni][nj]+1)
                mx = max(mx, dp[i][j])
        return mx            