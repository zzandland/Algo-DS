class Solution:
    def numSquares(self, n: int) -> int:
        dp, squares = [float('inf') if i > 0 else 0 for i in range(n+1)], [i**2 for i in range(int(math.sqrt(n))+1)]
        for i in range(n+1):
            for j in squares:
                if i < j: break
                dp[i] = min(dp[i], dp[i-j]+1)    
        return dp[-1]        