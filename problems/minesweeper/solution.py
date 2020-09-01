class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board: return None
        M, N = len(board), len(board[0])
        dir_ = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        
        def dfs(y: int, x: int) -> None:
            if board[y][x] == 'M':
                board[y][x] = 'X'
                return
            
            mines = 0
            for ny, nx in ((y+r, x+c) for r, c in dir_):
                if 0 <= ny < M and 0 <= nx < N and board[ny][nx] == 'M': mines += 1
            
            board[y][x] = str(mines) if mines > 0 else 'B'
            if mines == 0:
                for ny, nx in ((y+r, x+c) for r, c in dir_):
                    if 0 <= ny < M and 0 <= nx < N and board[ny][nx] == 'E': dfs(ny, nx)
                        
        dfs(*click)
        return board