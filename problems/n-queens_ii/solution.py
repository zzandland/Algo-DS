class Solution:
    def totalNQueens(self, n: int) -> int:
        row_set, col_set, diag_set, anti_set = set(), set(), set(), set()
        def dfs(y: int, x: int, q: int) -> int:
            if n == q: return 1
            res = 0
            for r in range(y, n):
                if q < r: break
                for c in range(x, n):
                    if (r not in row_set and c not in col_set and
                        r-c not in diag_set and r+c not in anti_set):
                        row_set.add(r), col_set.add(c)
                        diag_set.add(r-c), anti_set.add(r+c)
                        res += dfs(y+1, 0, q+1)
                        row_set.remove(r), col_set.remove(c)
                        diag_set.remove(r-c), anti_set.remove(r+c)
            return res
        return dfs(0, 0, 0)