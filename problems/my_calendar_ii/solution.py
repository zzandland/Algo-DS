(10, 1), (20, -1), (50,)

class MyCalendarTwo:

    def __init__(self):
        self.changes = []
        
    def book(self, start: int, end: int) -> bool:
        tmp = self.changes[:]
        tmp.append((start, 1))
        tmp.append((end, -1))
        tmp.sort()
        curr = 0
        for time, change in tmp:
            curr += change
            if curr > 2: return False
        self.changes = tmp
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)