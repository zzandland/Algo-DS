class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.lru_cache(None)
        def dfs(l: int, r: int, turn: bool) -> int:
            if l > r: return 0
            if not turn: return min(dfs(l+1, r, not turn), dfs(l, r-1, not turn))
            return max(piles[l] + dfs(l+1, r, not turn), piles[r] + dfs(l, r-1, not turn))
        return dfs(0, len(piles)-1, True) > (sum(piles) / 2)