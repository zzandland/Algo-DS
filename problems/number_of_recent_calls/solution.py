from collections import deque

class RecentCounter:

    def __init__(self):
        self.l = deque()

    def ping(self, t: int) -> int:
        while self.l and self.l[0] < t - 3000: self.l.popleft()
        self.l.append(t);
        return len(self.l)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)