from collections import defaultdict
from heapq import *

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        dic = defaultdict(list)
        for v, l in zip(values, labels):
            dic[l].append(v)
        for l in dic:
            dic[l] = sorted(dic[l], reverse=True)[:use_limit][::-1]
        q = []
        for l in dic:
            heappush(q, (-dic[l].pop(), l))
        res = 0
        for i in range(num_wanted):
            if not q: return -res
            v, l = heappop(q)
            res += v
            if dic[l]: heappush(q, (-dic[l].pop(), l))
        return -res