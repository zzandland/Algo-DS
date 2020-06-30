class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M: return 0
        m, n = len(M), len(M[0])
        dp = [[(0,0,0,0) for _1 in range(n+2)] for _2 in range(m+1)]
        res = 0
        for y in range(1, m+1):
            for x in range(1, n+1):
                if M[y-1][x-1] == 1:
                    hor = dp[y][x-1][0] + 1
                    ver = dp[y-1][x][1] + 1
                    diag = dp[y-1][x-1][2] + 1
                    anti = dp[y-1][x+1][3] + 1
                    dp[y][x] = (hor, ver, diag, anti)
                    res = max(res, *dp[y][x])
        return res