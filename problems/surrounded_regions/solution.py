from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        N, M = len(board), len(board[0])
        dir_ = (-1, 0, 1, 0, -1)
        
        oseen = set()
        for y in range(N):
            for x in range(M):
                if board[y][x] == 'O' and (y, x) not in oseen: 
                    seen = {(y, x)}
                    q = deque([(y, x)])
                    capture = True
                    while q:
                        yy, xx = q.popleft()
                        for ny, nx in ((yy+r, xx+c) for r, c in zip(dir_, dir_[1:])):
                            if 0 <= ny < N and 0 <= nx < M:
                                if board[ny][nx] == 'O' and (ny, nx) not in seen:
                                    seen.add((ny, nx))
                                    q.append((ny, nx))
                            else:
                                capture = False
                    if capture:
                        for r, c in seen:
                            board[r][c] = 'X'
                    oseen |= seen