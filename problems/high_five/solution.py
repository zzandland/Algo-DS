from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for i, score in items:
            heappush(dic[i], score)
            if len(dic[i]) > 5: heappop(dic[i])
        return [[i, sum(scores) // len(scores)] for i, scores in dic.items()]