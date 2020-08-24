class Solution:

    def __init__(self, rects: List[List[int]]):
        self.run = 0
        self.pf = []
        self.rects = []
        for x1, y1, x2, y2 in rects:
            self.run += (x2-x1+1) * (y2-y1+1)
            self.pf.append(self.run)
            self.rects.append((x1, y1, x2, y2))
        
    def pick(self) -> List[int]:
        idx = bisect.bisect_left(self.pf, random.randint(1, self.run))
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()