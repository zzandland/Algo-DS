from heapq import nlargest, heapify
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        d = [(f, n) for n, f in c.items()]
        heapify(d)
        return map(lambda x: x[1], nlargest(k, d))