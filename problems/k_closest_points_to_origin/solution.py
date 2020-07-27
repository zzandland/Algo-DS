from heapq import nsmallest

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return map(lambda x: [x[1], x[2]], nsmallest(K, [(y*y + x*x, y, x) for y, x in points]))