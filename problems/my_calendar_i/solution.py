class MyCalendar:

    def __init__(self):
        self.changes = []

    def book(self, start: int, end: int) -> bool:
        tmp = self.changes[:]
        bisect.insort_left(tmp, (start, 1))
        bisect.insort_left(tmp, (end, -1))
        curr = 0
        for time, change in tmp:
            curr += change
            if curr > 1: return False
        self.changes = tmp
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)