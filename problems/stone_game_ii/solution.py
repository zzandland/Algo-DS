from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        prefix = [0]
        for p in piles:
            prefix.append(prefix[-1] + p)
            
        @lru_cache(maxsize=None)
        def dfs(i: int, x: int, turn: bool) -> int:
            if i >= N: return 0
            if not turn: return min([dfs(i+j, max(x, j), not turn) for j in range(1, 2*x+1)])
            res = 0
            for j in range(1, 2*x+1):
                if i + j > N: break
                res = max(res, prefix[i+j] - prefix[i] + dfs(i+j, max(x, j), not turn))
            return res
        return dfs(0, 1, True)