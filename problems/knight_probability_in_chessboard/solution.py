class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        moves = ((1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1))
        dp = [[0]*N for _ in range(N)]
        dp[r][c] = 1
        for i in range(K):
            ndp = [[0]*N for i in range(N)]
            for y in range(N):
                for x in range(N):
                    for ny, nx in [(y+r, x+c) for r, c in moves]:
                        if 0 <= ny < N and 0 <= nx < N:
                            ndp[ny][nx] += dp[y][x]
            dp = ndp                
        return sum(map(sum, dp)) / 8**K