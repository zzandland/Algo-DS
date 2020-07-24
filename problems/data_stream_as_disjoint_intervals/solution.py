import bisect

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        N = len(self.intervals)
        idx = bisect.bisect_left([i for _, i in self.intervals], val)
        if not self.intervals:
            self.intervals.append([val, val])
        elif (0 < idx < N and self.intervals[idx-1][1] < val and
            val < self.intervals[idx][0]):
            self.intervals.insert(idx, [val, val])
        elif idx == 0 and val < self.intervals[idx][0]:
            self.intervals.insert(0, [val, val])
        elif idx == N and self.intervals[idx-1][1] < val:
            self.intervals.append([val, val])
        while 0 < idx < len(self.intervals) and self.intervals[idx-1][1] + 1 == self.intervals[idx][0]:
            self.intervals[idx-1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        while 0 <= idx < len(self.intervals)-1 and self.intervals[idx][1] + 1 == self.intervals[idx+1][0]:
            self.intervals[idx][1] = self.intervals[idx+1][1]
            self.intervals.pop(idx+1)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()