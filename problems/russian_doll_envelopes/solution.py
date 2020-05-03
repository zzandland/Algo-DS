class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        N, mx = len(envelopes), 1
        envelopes.sort()
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                iw, ih = envelopes[i]
                jw, jh = envelopes[j]
                if iw > jw and ih > jh and dp[i] <= dp[j]: dp[i] += 1
            mx = max(mx, dp[i])        
        return mx    