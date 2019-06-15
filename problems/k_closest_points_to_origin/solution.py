class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        hp = []
        for y, x in points:
            dist = math.sqrt(x * x + y * y)
            heapq.heappush(hp, (dist, [y, x]))
        output = []    
        for i in range(K):
            output.append(heapq.heappop(hp)[1])
        return output    