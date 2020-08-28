from collections import Counter

class MyCalendarTwo:

    def __init__(self):
        self.delta = Counter()

    def book(self, start: int, end: int) -> bool:
        self.delta[start] += 1
        self.delta[end] -= 1
        curr = 0
        for time in sorted(self.delta.keys()):
            curr += self.delta[time]
            if curr > 2:
                self.delta[start] -= 1
                self.delta[end] += 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)