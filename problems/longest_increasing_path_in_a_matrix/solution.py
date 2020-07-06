class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*N for _ in range(M)]
        def dfs(y: int, x: int) -> int:
            if not dp[y][x]:
                res = 0
                for ny, nx in [(y + r, x + c) for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1))]:
                    if 0 <= ny < M and 0 <= nx < N and matrix[ny][nx] > matrix[y][x]:
                        res = max(res, dfs(ny, nx))
                dp[y][x] = res + 1
            return dp[y][x]
        return max([dfs(y, x) for y, x in [(y, x) for y in range(M) for x in range(N)]])