class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return 0
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        if dp[-1] > amount:
            return -1        
        else:
            return dp[-1]