class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = [[False for j in range(n)] for i in range(m)]
        
        def dfs(y: int, x: int, i: int) -> None:
            nonlocal seen
            if word[i] != board[y][x]: return False
            if i == len(word) - 1: return True
            for r, c in zip((1, 0, -1, 0, 1), (0, -1, 0, 1)):
                ny, nx = y + r, x + c
                if 0 <= ny < m and 0 <= nx < n and not seen[ny][nx]:
                    seen[ny][nx] = True
                    if dfs(ny, nx, i+1): return True
                    seen[ny][nx] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    seen[i][j] = True
                    if dfs(i, j, 0): return True
                    seen[i][j] = False
        return False