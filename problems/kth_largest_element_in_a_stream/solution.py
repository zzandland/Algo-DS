from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for n in nums:
            heappush(self.pq, n)
            if len(self.pq) > k: heappop(self.pq)

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k: heappop(self.pq)
        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)