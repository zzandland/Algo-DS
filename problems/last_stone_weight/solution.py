import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-stone for stone in stones]
        heapq.heapify(hp)
        while len(hp) > 1:
            broken = abs(heapq.heappop(hp) - heapq.heappop(hp))
            if broken > 0: heapq.heappush(hp, -broken)
        return 0 if not hp else -hp[0]