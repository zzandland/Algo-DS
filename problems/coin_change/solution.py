class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        coins.sort()
        N = len(coins)
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]