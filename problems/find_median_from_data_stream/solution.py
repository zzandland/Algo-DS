from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hp = [], []

    def addNum(self, num: int) -> None:
        l, r = self.hp
        heappush(l, -num)
        heappush(r, -heappop(l))
        if len(l) < len(r): heappush(l, -heappop(r))

    def findMedian(self) -> float:
        l, r = self.hp
        if len(l) == len(r): return (-l[0] + r[0]) / 2
        return -l[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()