from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)
        for y, x in stones:
            rows[y].append(x)
            cols[x].append(y)
        def dfs(y: int, x: int) -> int:
            if (y, x) in seen: return 0
            seen.add((y, x))
            res = 1
            for nx in rows[y]:
                res += dfs(y, nx)
            for ny in cols[x]:
                res += dfs(ny, x)
            return res
        seen = set()
        res = 0
        for y, x in stones:
            if (y, x) not in seen:
                res += dfs(y, x) - 1
        return res