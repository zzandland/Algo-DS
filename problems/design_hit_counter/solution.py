class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = Counter({0:0})
        self.total = 0
        self.time = [0]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.total += 1
        if timestamp not in self.hits: self.time.append(timestamp)
        self.hits[timestamp] = self.total

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        t = self.time[bisect.bisect(self.time, max(0, timestamp - 300))-1]
        return self.total - self.hits[t]

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)