from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        def calDist(frm: int, to: int) -> int:
            if frm == -1: return 0
            return abs(frm // 6 - to // 6) + abs(frm % 6 - to % 6)
        
        dp = {(-1, -1): 0}
        for n in word:
            nxt = ord(n) - ord('A')
            ndp = {}
            for a, b in dp:
                ndp[nxt, b] = min(ndp.get((nxt, b), float('inf')), dp[a, b] + calDist(a, nxt))
                ndp[a, nxt] = min(ndp.get((a, nxt), float('inf')), dp[a, b] + calDist(b, nxt))
            dp = ndp
        return min(ndp.values())