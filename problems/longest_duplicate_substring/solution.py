class Solution:
    def longestDupSubstring(self, S: str) -> str:
        N = len(S)
        def rh(k: int) -> str:
            b, q, h, seen = 256, 18014398241046527, 0, set()
            for i in range(k):
                h = (b * h + ord(S[i])) % q
            seen.add(h)
            lst = b**(k-1) % q
            for j in range(k, N):
                h = (h - lst * ord(S[j-k])) % q
                h = (b * h + ord(S[j])) % q
                if h in seen:
                    return S[j-k+1:j+1]
                seen.add(h)
            return ''
        l, r, res, dp = 0, N, '', [None]*N
        while l < r:
            m = l + (r-l)//2
            if dp[m] == None:
                dp[m] = rh(m)
            if dp[m] != '':
                res = dp[m]
                l = m+1
            else:
                r = m
        return res