class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]],
                m: int, n: int, target: int) -> int:
        dp = {(0, 0): 0}
        for i, ch in enumerate(houses):
            ndp = {}
            for cj in range(1, n+1) if ch == 0 else [ch]:
                for ci, b in dp:
                    b2 = b + (cj != ci)
                    if b2 <= target:
                        ndp[cj, b2] = min(
                            ndp.get((cj, b2), float('inf')),
                            dp[ci, b] + (cost[i][cj-1] if cj != ch else 0)
                        )
            dp = ndp
        return min([dp[(c, b)] for c, b in dp if b == target] or [-1])