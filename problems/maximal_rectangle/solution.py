class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        N, M = len(matrix), len(matrix[0])
        dp = [[0]*M for _ in range(N+1)]
        for y in range(1, N+1):
            for x in range(M):
                if matrix[y-1][x] == '1': dp[y][x] = dp[y-1][x] + 1
        res = 0
        for y in range(1, N+1):
            row, st = dp[y], []
            left, right = [-1]*M, [M]*M
            for i, n in enumerate(row):
                while st and st[-1][0] > n:
                    right[st.pop()[1]] = i
                if st: left[i] = st[-1][1]
                st.append((n, i))
            for i, n in enumerate(row):
                res = max(res, (right[i]-left[i]-1) * n)
        return res