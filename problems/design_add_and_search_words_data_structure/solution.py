from collections import defaultdict

class Trie:
    
    def __init__(self):
        self.next = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        n = self.root
        for c in word:
            n.next.setdefault(c, Trie())
            n = n.next[c]
        n.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(i: int, n: Trie) -> bool:
            if i == len(word): return n.end
            if word[i] == '.':
                for c in n.next:
                    if dfs(i+1, n.next[c]): return True
            elif word[i] in n.next: return dfs(i+1, n.next[word[i]])
            return False
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)