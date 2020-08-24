class Solution:

    def __init__(self, w: List[int]):
        self.run = 0
        self.prefix = []
        for v in w:
            self.run += v
            self.prefix.append(self.run)

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.prefix, random.randint(1, self.run))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()