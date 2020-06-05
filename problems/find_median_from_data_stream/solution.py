from heapq import *

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hp = [], []

    def addNum(self, num: int) -> None:
        l, h = self.hp
        heappush(l, -heappushpop(h, num))
        if len(l) > len(h):
            heappush(h, -heappop(l))

    def findMedian(self) -> float:
        l, h = self.hp
        if len(h) > len(l):
            return float(h[0])
        else:
            return (-l[0]+h[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()