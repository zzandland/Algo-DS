import bisect

class MyCalendarThree:

    def __init__(self):
        self.delta = []

    def book(self, start: int, end: int) -> int:
        bisect.insort_left(self.delta, (start, 1))
        bisect.insort_left(self.delta, (end, -1))
        
        curr = mx = 0
        for _, change in self.delta:
            curr += change
            mx = max(mx, curr)
        return mx

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)