from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # stole: just stole. Must rest
        # rest: can rest of steal again
        rest = 0
        stole = float('-inf')
        res = 0
        
        for n in nums:
            ns = max(stole, n + rest)
            nr = max(stole, res)
            stole, rest = ns, nr
            res = max(res, stole, rest)
        return res