class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            n = trie
            for c in w:
                if c not in n: n[c] = {}
                n = n[c]
            n['*'] = w
        M, N = len(board), len(board[0])
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(n: dict, y: int, x: int) -> None:
            if '*' in n:
                res.append(n['*'])
                del n['*']
            for ny, nx in [(y+r, x+c) for r, c in dir_]:
                if 0 <= ny < M and 0 <= nx < N and board[ny][nx] in n and (ny, nx) not in seen:
                    seen.add((ny, nx))
                    dfs(n[board[ny][nx]], ny, nx)
                    seen.remove((ny, nx))
        res = []
        for y in range(M):
            for x in range(N):
                if board[y][x] in trie:
                    seen = set([(y, x)])
                    dfs(trie[board[y][x]], y, x)
        return sorted(res)