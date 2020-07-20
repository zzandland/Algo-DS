class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # check conflicts for row, col, diag using set
        row_set, col_set, diag_set, anti_set = set(), set(), set(), set()
        board = [['.']*n for _ in range(n)]
        res = []
        # dfs with backtracking to reach the end on the board O(n!)
        def dfs(y: int, x: int, q: int) -> None:
            if q == n:
                res.append([''.join(row) for row in board])
                return
            for r in range(y, n):
                if q < r: break
                for c in range(x, n):
                    if (r not in row_set and c not in col_set and
                        r-c not in diag_set and r+c not in anti_set):
                        row_set.add(r), col_set.add(c)
                        diag_set.add(r-c), anti_set.add(r+c)
                        board[r][c] = 'Q'
                        dfs(y+1, 0, q+1)
                        row_set.remove(r), col_set.remove(c)
                        diag_set.remove(r-c), anti_set.remove(r+c)
                        board[r][c] = '.'
        dfs(0, 0, 0)
        return res