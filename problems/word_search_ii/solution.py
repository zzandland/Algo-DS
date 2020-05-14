from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        dic, n = {}, None
        for w in words:
            n = dic
            for i in range(len(w)):
                n.setdefault(w[i], {})
                n = n[w[i]]
            n['*'] = 1    
        output = []
        def dfs(y: int, x: int, s: str, n: object) -> None:
            if s == 'bend': print(n)
            if '*' in n: 
                del n['*']
                output.append(s)
            for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y+r, x+c    
                if 0 <= ny < R and 0 <= nx < C and (ny, nx) not in visited:
                    ch = board[ny][nx]
                    if ch in n: 
                        visited.add((ny, nx))
                        dfs(ny, nx, s+ch, n[ch])
                        visited.remove((ny, nx))
        for y in range(R):
            for x in range(C):
                ch = board[y][x]
                if ch in dic:
                    visited = set([(y, x)])
                    dfs(y, x, ch, dic[ch])
        return output