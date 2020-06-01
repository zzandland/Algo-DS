class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for _, h in envelopes:
            l, r = 0, len(dp)
            while l < r:
                m = l + (r-l)//2
                if dp[m] == h:
                    l = r = m
                elif dp[m] > h:
                    r = m
                else:
                    l = m+1
            if l == len(dp):
                dp.append(h)
            else:
                dp[l] = h
        return len(dp)