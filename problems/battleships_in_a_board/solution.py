class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: return 0
        N, M = len(board), len(board[0])
        
        res = 0
        for y in range(N):
            for x in range(M):
                if board[y][x] == 'X':
                    res += 1
                    board[y][x] = '.'
                    for r, c in ((1, 0), (0, 1)):
                        ny, nx = y+r, x+c
                        while 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 'X':
                            dy, dx = ny, nx
                            board[dy][dx] = '.'
                            ny, nx = dy+r, dx+c
        return res