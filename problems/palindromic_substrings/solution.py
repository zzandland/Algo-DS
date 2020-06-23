class Solution:
    def countSubstrings(self, s: str) -> int:
        N, dp = len(s), {}
        def cal(l: int, r: int) -> int:
            if l >= r:
                return 1
            if s[l] != s[r]:
                return 0
            if (l, r) not in dp:
                dp[l, r] = cal(l+1, r-1)
            return dp[l, r]
        return sum([cal(i, j) for i in range(N) for j in range(i, N)])