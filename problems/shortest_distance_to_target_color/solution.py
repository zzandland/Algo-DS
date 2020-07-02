from collections import defaultdict
import bisect

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i, c in enumerate(colors):
            dic[c].append(i)
        res = []
        for i, c in queries:
            if not dic[c]:
                res.append(-1)
            else:
                idx = bisect.bisect_left(dic[c], i)
                if idx == len(dic[c]): target = dic[c][idx-1]
                elif abs(dic[c][idx-1] - i) < abs(dic[c][idx] - i): target = dic[c][idx-1]
                else: target = dic[c][idx]
                if idx == len(dic[c]): res.append(abs(target-i))
                else: res.append(abs(target-i))
        return res