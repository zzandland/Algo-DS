class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1]+[0]*(amount)
        for i, coin in enumerate(coins):
            for j in range(coin, amount+1):
                if i == 0:
                    dp[j] = 1 if j % coin == 0 else 0
                else:
                    dp[j] += dp[j-coin]
        return dp[-1]