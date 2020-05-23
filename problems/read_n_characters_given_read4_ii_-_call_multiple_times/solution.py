# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

class Solution:
    def __init__(self):
        self.l = self.r = 0
        self.buf = ['']*4
    
    def read(self, buf: List[str], n: int) -> int:
        if n == 0: return 0
        for i in range(n):
            if self.l >= self.r:
                self.buf = ['']*4
                self.r = read4(self.buf)
                if self.r == 0: return i
                self.l = 0
            buf[i] = self.buf[self.l]    
            self.l += 1
        return i+1