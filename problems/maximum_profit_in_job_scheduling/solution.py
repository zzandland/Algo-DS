import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = sorted(zip(startTime, endTime, profit), key=operator.itemgetter(1))
        q = [(0, 0)]
        for st, et, p in arr:
            idx = bisect.bisect_left(q, (st+1,))-1
            if q[idx][1] + p > q[-1][1]: q.append((et, q[idx][1] + p))
        return q[-1][1]