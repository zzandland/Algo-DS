class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        M, N = len(board), len(board[0])
        dir_ = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        nb = [[0]*N for _ in range(M)]
        for y in range(M):
            for x in range(N):
                cnt = 0
                for ny, nx in ((y+r, x+c) for r, c in dir_):
                    if 0 <= ny < M and 0 <= nx < N and board[ny][nx] == 1: cnt += 1
                if board[y][x] == 1: nb[y][x] = int(2 <= cnt <= 3)
                else: nb[y][x] = int(cnt == 3)
        for y in range(M):
            for x in range(N):
                board[y][x] = nb[y][x]