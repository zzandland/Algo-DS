class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.mins = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        min_ = x if not self.mins else min(x, self.mins[-1])
        self.mins.append(min_)

    def pop(self) -> None:
        if not self.nums: return
        self.nums.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()