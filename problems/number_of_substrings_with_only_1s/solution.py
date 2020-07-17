class Solution:
    def numSub(self, s: str) -> int:
        arr = list(filter(bool, s.split('0')))
        res = 0
        dp = {}
        def dq(i: int) -> int:
            if i == 1: return 1
            if i not in dp:
                dp[i] = i + dq(i-1)
            return dp[i]
        for ones in arr:
            res += dq(len(ones))
        return res % (10**9 + 7)