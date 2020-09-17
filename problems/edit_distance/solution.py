class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        A, B = len(word1), len(word2)
        dp = [[0]*(B+1) for _ in range(A+1)] 
        for a in range(A+1): dp[a][0] = a
        for b in range(B+1): dp[0][b] = b
        for a in range(A):
            for b in range(B):
                if word1[a] == word2[b]: dp[a+1][b+1] = dp[a][b]
                else: dp[a+1][b+1] = 1 + min(dp[a+1][b], dp[a][b], dp[a][b+1])
        return dp[A][B]