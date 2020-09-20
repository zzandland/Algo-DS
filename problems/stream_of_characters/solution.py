from collections import deque

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.buf = deque()
        for w in words:
            n = self.root
            for c in w[::-1]:
                n.setdefault(c, {})
                n = n[c]
            n['*'] = w

    def query(self, letter: str) -> bool:
        self.buf.appendleft(letter)
        n = self.root
        for c in self.buf:
            if '*' in n: return True
            if c not in n: return False
            n = n[c]
        return '*' in n


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)