from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for stid, score in items:
            heappush(scores[stid], score)
            if len(scores[stid]) > 5: heappop(scores[stid])
        return [[stid, sum(scoreList) // len(scoreList)] for stid, scoreList in scores.items()]