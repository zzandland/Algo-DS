class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        for i, (u, v) in enumerate(intervals):
            dic.setdefault(u, (v, i))
            if v < dic[u][0]: dic[u] = (v, i)
        lst = sorted(dic.items())
        res = []
        for _, v in intervals:
            idx = bisect.bisect_left(lst, (v,))
            if idx == len(lst): res.append(-1)
            else: res.append(lst[idx][1][1])
        return res