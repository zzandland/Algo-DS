# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf = ['']*4
        self.i = self.j = 0
    
    def read(self, buf: List[str], n: int) -> int:
        if n == 0: return 0
        for i in range(n):
            if self.i == self.j:
                self.j, self.i = read4(self.buf), 0
                if self.j == 0: return i
            buf[i] = self.buf[self.i]
            i += 1
            self.i += 1
        return i