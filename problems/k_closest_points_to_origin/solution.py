class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def compare(a):
            return math.sqrt(a[0]*a[0] + a[1]*a[1])
        points.sort(key=lambda x: compare(x))
        return points[:K]