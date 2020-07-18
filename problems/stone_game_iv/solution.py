class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares, i = [], 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        dp = [False] + [None]*n
        for i in range(1, n+1):
            valids = filter(lambda x: x <= i, squares)
            dp[i] = any([not dp[i-valid] for valid in valids])
        return dp[i]