class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.parents = {}
        self.intervals = {}
        
    def find(self, val: int) -> int:
        if val not in self.parents: return -1
        if val != self.parents[val]:
            self.parents[val] = self.find(self.parents[val])
        return self.parents[val]
    
    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == -1 or fy == -1: return
        self.parents[fy] = fx
        xa, xb = self.intervals[fx]
        ya, yb = self.intervals[fy]
        del self.intervals[fy]
        self.intervals[fx] = [min(xa, ya), max(xb, yb)]

    def addNum(self, val: int) -> None:
        if val in self.parents: return
        self.parents[val] = val
        self.intervals[val] = [val, val]
        self.union(val, val-1)
        self.union(val, val+1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.intervals.values())

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()