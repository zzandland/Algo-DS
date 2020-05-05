from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.q) == self.size: self.sum -= self.q.popleft()
        self.q.append(val)
        self.sum += val
        return self.sum / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)