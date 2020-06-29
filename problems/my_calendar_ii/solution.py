class MyCalendarTwo:

    def __init__(self):
        self.s = set()
        self.d = set()

    def book(self, start: int, end: int) -> bool:
        for ds, de in self.d:
            if start >= de or end <= ds: continue
            else: return False
        for ss, se in self.s:
            if start >= se or end <= ss: continue
            else: self.d.add((max(start, ss), min(end, se)))
        self.s.add((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)