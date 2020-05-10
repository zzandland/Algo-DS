# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf = [None]*4
        self.i = 0
        self.n = read4(self.buf)

    def read(self, buf: List[str], n: int) -> int:
        if self.n == 0: return 0
        for i in range(n):
            if self.i == self.n:
                self.buf, self.i = [None]*4, 0
                self.n = read4(self.buf)
                if self.n == 0: return i
            buf[i] = self.buf[self.i]
            self.i += 1
        return n    