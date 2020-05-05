class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        t = timestamp // 60
        if t not in self.q: self.q[t] = [0]*61
        self.q[t][timestamp%60] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        t, output = timestamp // 60, 0
        j = t - 5
        for i in range(j, t+1):
            if i in self.q and i >= 0:
                if i == j:  output += sum(self.q[i][timestamp%60+1:])
                else: output += sum(self.q[i])    
        return output            

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)