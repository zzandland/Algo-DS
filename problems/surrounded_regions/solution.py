class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        R, C = len(board), len(board[0])
        seen = [[False]*C for _ in range(R)]
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(y: int, x: int, tick: bool) -> None:
            if seen[y][x]:
                return
            seen[y][x] = True
            if tick:
                board[y][x] = 'X'
            for ny, nx in [[y+r, x+c] for r, c in dir_]:
                if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == 'O':
                    dfs(ny, nx, tick)
        for y, x in [(y, x) for x in (0, C-1) for y in range(R)] + [(y, x) for y in (0, R-1) for x in range(C)]:
            if board[y][x] == 'O':
                dfs(y, x, False)
        for y, x in [(y, x) for y in range(1, R-1) for x in range(1, C-1)]:
            if board[y][x] == 'O':
                dfs(y, x, True)