class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        dp = {}
        def dfs(i: int) -> int:
            if i == len(s): return 1
            if i not in dp:
                res = 0
                if i + 1 < len(s) and int(s[i:i+2]) <= 26: res += dfs(i+2)
                dp[i] = res + dfs(i+1) if s[i] != '0' else 0
            return dp[i]
        return dfs(0)