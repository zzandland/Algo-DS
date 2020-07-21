class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N, L = len(board), len(board[0]), len(word)
        seen = set()
        # dfs and matching chars on board with the word
        # set dynamically grows and shrinks to handle visiting agian
        def dfs(y: int, x: int, i: int) -> bool:
            if (y, x) in seen or board[y][x] != word[i]: return False
            if i == L-1: return True
            seen.add((y, x))
            for ny, nx in ((y+r, x+c) for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                if 0 <= ny < M and 0 <= nx < N and dfs(ny, nx, i+1): return True
            seen.remove((y, x))
            return False
        
        for y, x in ((y, x) for y in range(M) for x in range(N)):
            if dfs(y, x, 0): return True
        return False