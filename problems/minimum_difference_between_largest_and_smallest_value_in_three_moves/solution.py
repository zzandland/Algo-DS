from collections import Counter

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        c = Counter(nums)
        total = len(nums)
        def dfs(move: int) -> int:
            nonlocal total
            keys = c.keys()
            mn, mx = min(keys), max(keys)
            if move == 3 or total == 1: return mx - mn
            c[mn] -= 1
            if c[mn] == 0: del c[mn]
            total -= 1
            mnd = dfs(move+1)
            c[mn] += 1
            total += 1
            c[mx] -= 1
            if c[mx] == 0: del c[mx]
            total -= 1
            mxd = dfs(move+1)
            c[mx] += 1
            total += 1
            return min(mnd, mxd)
        return dfs(0)