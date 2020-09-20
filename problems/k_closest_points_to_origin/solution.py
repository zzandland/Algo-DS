from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        tmp = [(y*y + x*x, y, x) for y, x in points]
        heapify(tmp)
        res = []
        for _ in range(K):
            res.append(heappop(tmp)[1:])
        return res