class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        if not A: return 0
        M, N = len(A), len(A[0])
        
        dp = [[0]*(N+1) for _ in range(M+1)]
        dp[0][1] = 1
        
        for y in range(M):
            for x in range(N):
                if A[y][x] == 0:
                    dp[y+1][x+1] = dp[y][x+1] + dp[y+1][x]
                    
        return dp[-1][-1]