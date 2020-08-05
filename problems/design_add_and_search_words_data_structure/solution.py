class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        n = self.trie
        for c in word:
            n.setdefault(c, {})
            n = n[c]
        n['*'] = word;

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        N = len(word)
        def dfs(i: int, n: dict) -> bool:
            if isinstance(n, str): return False
            if i == N: return '*' in n
            if word[i] == '.': return any([dfs(i+1, nc) for nc in n.values()])
            if word[i] not in n: return False
            return dfs(i+1, n[word[i]])
        return dfs(0, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)