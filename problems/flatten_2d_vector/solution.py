class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.st = v[::-1]
        self.list = []

    def next(self) -> int:
        if self.hasNext(): return self.list.pop()

    def hasNext(self) -> bool:
        while not self.list:
            if not self.st: return False
            self.list = self.st.pop()[::-1]
        return True

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()