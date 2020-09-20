class Solution:

    def __init__(self, w: List[int]):
        self.pf = []
        run = 0
        for n in w:
            run += n
            self.pf.append(run)

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.pf, random.randint(1, self.pf[-1]))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()