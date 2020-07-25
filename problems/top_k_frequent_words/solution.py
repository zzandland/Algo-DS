from collections import Counter, defaultdict
from heapq import heapify, nlargest

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # cnt all words O(n)
        c = Counter(words)
        
        # heapify the words in max heap by count O(n log n)
        h = [(-cnt, word) for word, cnt in c.items()]
        heapify(h)
            
        # take out from heap one at a time until k words are out O(k log n)
        return [heappop(h)[1] for _ in range(k)]