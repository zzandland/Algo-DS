class MyCalendarThree:

    def __init__(self):
        self.changes = []

    def book(self, start: int, end: int) -> int:
        self.changes.append((start, 1))
        self.changes.append((end, -1))
        self.changes.sort()
        curr = res = 0
        for time, change in self.changes:
            curr += change
            res = max(res, curr)
        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)