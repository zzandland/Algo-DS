class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [1] + [0]*(amount)
                
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
        return dp[-1]