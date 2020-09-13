class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        tmp = [(newInterval[0], 1), (newInterval[1], -1)]
        for s, e in intervals:
            tmp.append((s, 1))
            tmp.append((e, -1))
        tmp.sort(key=lambda x: (x[0], -x[1]))
        res = []
        cur = 0
        for t, c in tmp:
            cur += c
            if c == 1 and cur == 1: s = t
            if cur == 0: res.append([s, t])
        return res