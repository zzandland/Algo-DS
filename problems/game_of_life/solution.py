class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        adj = ((1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0))
        M, N = len(board), len(board[0])
        seen = set((0, 0))
        def dfs(y: int, x: int) -> None:
            alive = board[y][x]
            valid = [(ny, nx) for ny, nx in [(y+r, x+c) for r, c in adj] if 0 <= ny < M and 0 <= nx < N]
            cnt = len(list(filter(lambda x: board[x[0]][x[1]], valid)))
            for ny, nx in valid:
                if (ny, nx) not in seen:
                    seen.add((ny, nx))
                    dfs(ny, nx)
            if alive: board[y][x] = int(2 <= cnt < 4)
            else: board[y][x] = int(cnt == 3)
        dfs(0, 0)