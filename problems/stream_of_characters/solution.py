from collections import deque

class Trie:
    def __init__(self):
        self.next = {}
        self.end = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = Trie()
        self.buffer = ''
        self.maxlen = 0
        for w in map(lambda w: w[::-1], words):
            n = self.root
            self.maxlen = max(self.maxlen, len(w))
            for c in w:
                n.next.setdefault(c, Trie())
                n = n.next[c]
            n.end = True

    def query(self, letter: str) -> bool:
        self.buffer = (letter + self.buffer)[:self.maxlen]
        n = self.root
        for c in self.buffer:
            if c in n.next:
                n = n.next[c]
                if n.end: return True
            else: break
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)