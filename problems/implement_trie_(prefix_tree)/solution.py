class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = self.trie
        for c in word:
          if c not in n:
            n[c] = {}
          n = n[c]
        n['*'] = 1  
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self.trie
        for c in word:
          if c not in n:
            return False
          n = n[c]
        return '*' in n
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = self.trie
        for c in prefix:
          if c not in n:
            return False
          n = n[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)