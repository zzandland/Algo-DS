from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = [(-cnt, num) for (num, cnt) in Counter(nums).items()]
        heapq.heapify(hp)
        return [heapq.heappop(hp)[1] for _ in range(k)]