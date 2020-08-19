class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.r = []
        self.ln = 0
        
    def addNum(self, num: int) -> None:
        heappush(self.l, -num)
        heappush(self.r, -heappop(self.l))
        if self.ln & 1 == 0: heappush(self.l, -heappop(self.r))
        self.ln += 1

    def findMedian(self) -> float:
        if not self.ln: return 0
        if self.ln & 1 == 1: return -self.l[0]
        return (-self.l[0] + self.r[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()