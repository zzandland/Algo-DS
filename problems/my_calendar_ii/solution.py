class MyCalendarTwo:
    def __init__(self):
        self.single = []
        self.double = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.double:
            if i < end and start < j: return False
        for i, j in self.single:
            if i < end and start < j: self.double.append([max(i, start), min(j, end)])
        self.single.append([start, end])        
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)