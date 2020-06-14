from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = [(y*y+x*x, y, x) for y, x in points]
        heapify(q)
        return [[y, x] for _, y, x in nsmallest(K, q)]