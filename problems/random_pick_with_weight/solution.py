class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        self.size = 0
        for n in w:
            self.arr.append(self.size)
            self.size += n
        self.arr.append(self.size)    

    def pickIndex(self) -> int:
        t = random.randrange(self.size)
        l, r = 0, len(self.arr)
        while l < r:
            m = l + (r-l)//2
            if t >= self.arr[m] and t < self.arr[m+1]:
                return m
            if t > self.arr[m]:
                l = m+1
            else:
                r = m    
        return l        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()