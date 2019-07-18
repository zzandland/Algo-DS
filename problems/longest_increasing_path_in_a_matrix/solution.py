class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        w, l = len(matrix), len(matrix[0])
        dp = [[0] * l for _ in range(w)]
        def helper(r: int, c: int) -> int:
            if not dp[r][c]:
                max_len, curr = 1, matrix[r][c]
                for y, x in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if 0 <= y < w and 0 <= x < l and matrix[y][x] > curr:
                        max_len = max(max_len, 1 + helper(y, x))
                dp[r][c] = max_len            
            return dp[r][c]    
        output = 1
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                output = max(output, helper(i, j))
        return output        