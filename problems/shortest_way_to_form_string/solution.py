from collections import defaultdict
import bisect

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        dic = defaultdict(list)
        for i, c in enumerate(source):
            dic[c].append(i)
        res, s = 1, -1
        for t in target:
            if t not in dic: return -1
            j = bisect.bisect_left(dic[t], s+1)
            if j == len(dic[t]) or dic[t][j] < s:
                s = dic[t][0]
                res += 1
            else:
                s = dic[t][j]
        return res