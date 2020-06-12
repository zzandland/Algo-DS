class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {}
        def dfs(n: int) -> int:
            if n == 1:
                return 0
            if n not in dp:
                if n % 2 == 0:
                    dp[n] = dfs(n//2) + 1
                else:
                    dp[n] = dfs(n*3+1) + 1
            return dp[n]
        res = []
        for i in range(lo, hi+1):
            res.append((i, dfs(i)))
        return sorted(res, key=lambda x: x[1])[k-1][0]