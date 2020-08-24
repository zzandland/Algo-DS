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
            n['*'] = {}

    def query(self, letter: str) -> bool:
        self.buf.appendleft(letter)
        run = self.root
        for c in self.buf:
            if c not in run: return False
            run = run[c]
            if '*' in run: return True

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)