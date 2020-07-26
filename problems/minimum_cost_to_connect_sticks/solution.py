from heapq import heappush, heappop, heapify

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # heapify sticks O(sticks) 
        heapify(sticks)
        
        # take out two smallest sticks and stick them O(log sticks)
        cost = 0
        while len(sticks) > 1:
            a, b = heappop(sticks), heappop(sticks)
            cost += a + b
            heappush(sticks, a + b)
        return cost