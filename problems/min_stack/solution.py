class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.mn = []

    def push(self, x: int) -> None:
        self.st.append(x)
        mnval = x if not self.mn else min(self.mn[-1], x)
        self.mn.append(mnval)

    def pop(self) -> None:
        self.st.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()