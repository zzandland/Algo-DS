from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        n = self.root
        for c in word:
            n.setdefault(c, {})
            n = n[c]
        n['*'] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        N = len(word)
        def dfs(i: int, n: dict) -> bool:
            if i == N: return '*' in n
            c = word[i]
            if c == '.':
                for nxt in n:
                    if nxt != '*' and dfs(i+1, n[nxt]): return True
            elif c in n and dfs(i+1, n[c]):
                return True
            return False
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)