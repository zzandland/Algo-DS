class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if abs(S) > 1000:
            return 0
        dp, q = [0]*2001, set([1000])
        dp[1000] = 1
        for n in nums:
            nq = set()
            ndp = [0]*2001
            for p in q:
                ndp[p+n] += dp[p]
                ndp[p-n] += dp[p]
                nq.add(p+n)
                nq.add(p-n)
            q, dp = nq, ndp
        return dp[S+1000]