from typing import Dict, Any

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = []
        if not board or not words:
            return output
        
        root = {}
        for word in words:
            trie = root
            for c in word:
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]    
            trie['#'] = word    
            
        def recurse(row: int, col: int, trie) -> None:
            nonlocal board
            if '#' in trie:
                word = trie['#']
                if word not in found_word:
                    found_word.add(word)
                    output.append(word)
            tmp, board[row][col] = board[row][col], ''
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if board[r][c] in trie:
                        recurse(r, c, trie[board[r][c]])
            board[row][col] = tmp
    
        found_word = set()
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] in root:
                    recurse(i, j, root[board[i][j]])
        return sorted(output)
    
