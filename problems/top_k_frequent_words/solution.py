from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        hp = [(-c, word) for (word, c) in cnt.items()]
        heapq.heapify(hp)
        return [heapq.heappop(hp)[1] for _ in range(k)]